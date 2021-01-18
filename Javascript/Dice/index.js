var randomNumber1 = Math.floor(Math.random() * 6)+1;

var randomDiceImage = "dice" + randomNumber1 + ".png"

var randomImageSource = "images/" + randomDiceImage;

var image1 = document.querySelectorAll("img")[0];
image1.setAttribute("src", randomImageSource);

var button = document.querySelector(".noselect")

function refreshPage(){
    window.location.reload();
} 