const express = require("express");
const bodyParser = require("body-parser");
const fetch = require("node-fetch");

const ejs = require("ejs");
const base_url = "https://api.jikan.moe/v3";



const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/" ,  async function(req, res) {

  const obj1 = await fetch("https://api.jikan.moe/v3/top/anime")
      .then(res => res.json())
      .catch((err) => console.log(err));

const animeGenre = obj1.top;


    res.render("index", { animeGenre });

})




app.post("/genre" , async function(req , res)  {



let genre_id = (req.body.anime);

const obj1 = await fetch(`${base_url}/genre/anime/${genre_id}/1`)
    .then(res => res.json())
    .catch((err) => console.log(err));
const animeGenre = obj1.anime;

  res.render("index", {animeGenre });





})

app.get("/genre" , function(req, res) {

  res.redirect("/");

})




app.post("/" , async function(req , res) {

  let name = req.body.animeTaken;


  const object =  await fetch(`${base_url}/search/anime?q=${name}`)
      .then(res => res.json())
      .catch((err) => console.log(err));

      const results = object.results;


      if(results)
      {
        res.render("search" , {results});
      }
      else {
        res.redirect("/");
      }





})
app.listen(3000 , function (req , res) {

	console.log("Server is Running");

})
