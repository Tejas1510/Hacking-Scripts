const express = require("express");
const app = express();
const dotenv = require("dotenv");
const cors = require('cors');
const connectDB = require('./db/conn');
const authRoute = require('./route/auth');
dotenv.config({path:'./config.env'});
connectDB();

app.use(express.json());
app.use(cors());
const PORT= process.env.PORT;
app.use('/api/auth',authRoute);
app.listen(PORT,()=>{
    console.log("backend is running");
})