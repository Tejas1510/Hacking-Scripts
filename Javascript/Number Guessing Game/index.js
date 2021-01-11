let turn = 0;
let flag = false;
let random = -1;
let guess = -1;
$("#start").click(function () {
  if (turn % 2 == 0) {
    $("#start").text("Stop");
    $("#start").removeClass("btn-success");
    $("#start").addClass("btn-danger");
    flag = true;
    random = generateRandom();
    guess = 0;
    turn++;
  } else {
    $("#start").text("Start");
    $("#start").removeClass("btn-danger");
    $("#start").addClass("btn-success");
    flag = false;
    turn++;
  }
});
$("#check").click(function () {
  if (!flag) {
    $("#result").text("Please press the start button so as to start the game.");
  } else {
    ++guess;
    let user = $("#user").val();
    let comp = Math.floor(Math.random() * 10);
    if (comp == random) {
      $("#result").text("Oops you lost the game as computer guessed it correct. The correct number was " + random);
      reset();
    } else {
      if (user < random) {
        $("#result").text("Ohhh you guessed less than the required value. \nNo. of guesses = " + guess);
      } else if (user > random) {
        $("#result").text("Ohhh you guessed more than the required value. \nNo. of guesses = " + guess);
      } else {
        $("#result").text("Congragulation you won after " + guess + " guesses.");
        reset();
      }
    }
    console.log(user);
    console.log(random);
    console.log(comp);
  }
});

$("#re").click(function () {
  $("#start").text("Start");
  $("#start").removeClass("btn-danger");
  $("#start").addClass("btn-success");
  turn = 0;
  flag = false;
});

function generateRandom() {
  return Math.floor(Math.random() * 10);
}

function reset() {
  $("#start").text("Start");
  $("#start").removeClass("btn-danger");
  $("#start").addClass("btn-success");
  flag = false;
  turn = 0;
}
