const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const fetch = require('node-fetch');
const http = require('http');
const socketIO = require('socket.io');

require('dotenv').config();

const STATS_URL = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCLNgu_OupwoeESgtab33CCw&key=' + process.env.API_KEY;

const app = express();
const server = http.Server(app);
const io = socketIO(server);

let latestStats;

app.use(morgan('dev'));
app.use(cors());

app.get('/', (req, res) => {
  res.json({
    message: '🦄🌈✨Hello World! 🌈✨🦄'
  });
});

function getLatestStats() {
  return fetch(STATS_URL)
    .then(async res => {
      const json = await res.json();
      if (!res.ok) {
        console.log('Error calling Youtube API');
        console.log(JSON.stringify(json, null, 2));
      }
      return json;
    }).then(result => {
      if (result.items) {
        latestStats = result.items[0].statistics; 
        io.emit('stats', latestStats); 
      }
      setTimeout(() => {
        getLatestStats();
      }, 1000);
    });
}

getLatestStats();

app.get('/stats', (req, res) => {
  res.json(latestStats);
});

function notFound(req, res, next) {
  res.status(404);
  const error = new Error('Not Found - ' + req.originalUrl);
  next(error);
}

function errorHandler(err, req, res, next) {
  res.status(res.statusCode || 500);
  res.json({
    message: err.message,
    stack: err.stack
  });
}

app.use(notFound);
app.use(errorHandler);

const port = process.env.PORT || 5000;
server.listen(port, () => {
  console.log('Listening on port', port);
});