var gamePattern = [];
var userClickedPattern = [];
var buttonColours = ["red","blue","green","yellow"];
var level = 0;
var ok = false;

// To check wheter firstime key is pressed
$(document).keypress(function(){
    if(!ok){
        $("#level-title").text("Level "+ level);
        nextSequence();
        ok=true;
    }
});

//Creating the array the way user click buttons
$(".btn").click(function(){
    var userChosenColour = $(this).attr('id');
    userClickedPattern.push(userChosenColour);
    checkAnswer(userClickedPattern.length-1);
    playSound(userChosenColour);
    animatePress(userChosenColour);
});

// Select randomly a color to be chosen
function nextSequence(){
    userClickedPattern=[];
    level++;
    $("#level-title").text("Level "+level);
    var randomNumber = Math.floor(Math.random()*4);
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);
    $("#"+randomChosenColour).fadeOut(100).fadeIn(100);
    playSound(randomChosenColour);
}

// As the name suggests play sound
function playSound(name){
    var p = "sounds/"+name+".mp3";
    var au = new Audio(p);
    au.play();
}

//Animation when you click 
function animatePress(currentColour){
    $("#"+currentColour).addClass("pressed");
    setTimeout(() => {
        $("#"+currentColour).removeClass("pressed");
    }, 100);
}

function checkAnswer(currentLevel) {
    if(userClickedPattern[currentLevel]===gamePattern[currentLevel]){
        console.log("success");
        if(userClickedPattern.length===gamePattern.length){
            setTimeout(() => {
                nextSequence();
            }, 1000);
        }
    }
    else{
        $("h1").text("Game Over");
        playSound("wrong");
        $("body").addClass("game-over");
        setTimeout(() => {
            $("body").removeClass("game-over")
        }, 200);
        startOver();        
        ok = false;
    }
}

function startOver(){
    level = 0;
    gamePattern = [];
    userClickedPattern = [];
}
