var randomNumber1 = Math.floor(Math.random() * 6) + 1;
var randomNumber2 = Math.floor(Math.random() * 6) + 1;

var randomDiceImage1 = "dice" + randomNumber1 + ".png";
var randomDiceImage2 = "dice" + randomNumber2 + ".png";

var randomImageSource1 = "images/" + randomDiceImage1;
var randomImageSource2 = "images/" + randomDiceImage2;

var image1 = document.getElementById("img1");
image1.setAttribute("src", "images/dice6.png");

var image2 = document.getElementById("img2");
image2.setAttribute("src", "images/dice6.png");

function decider() {
  var image1 = document.getElementById("img1");
  image1.setAttribute("src", randomImageSource1);

  var image2 = document.getElementById("img2");
  image2.setAttribute("src", randomImageSource2);

  if (randomNumber1 > randomNumber2) {
    var winner = document.getElementById("result");
    winner.innerHTML = "Player 1 Wins!";
    setInterval(function () {
      location.reload();
    }, 3000);
  } else if (randomNumber1 < randomNumber2) {
    var winner = document.getElementById("result");
    winner.innerHTML = "Player 2 Wins!";
    setInterval(function () {
      location.reload();
    }, 3000);
  } else {
    var winner = document.getElementById("result");
    winner.innerHTML = "Draw";
    setInterval(function () {
      location.reload();
    }, 3000);
  }
}
