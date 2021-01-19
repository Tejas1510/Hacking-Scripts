
function rpsGame(yourChoice) {
    var humanChoice, botChoice;
    humanChoice = yourChoice.id;
    botChoice = numberToChoice(randToRpsInt());
    results = decideWinner(humanChoice, botChoice);
    message = finalMessage(results);
    rpsFrontEnd(yourChoice.id, botChoice, message);

}
function randToRpsInt() {
    return Math.floor(Math.random() * 3);
}
function numberToChoice(number) {
    return ['rock', 'paper', 'scissor'][number];
}
function decideWinner(yourChoice, botChoice) {
    var rpsDatabase = {
        'rock': { "scissor": 1, "rock": 0.5, "paper": 0 },
        'paper': { "rock": 1, "paper": 0.5, "scissor": 0 },
        'scissor': { "rock": 0, "paper": 1, "scissor": 0.5 }
    }

    var yourScore = rpsDatabase[yourChoice][botChoice];
    var botScore = rpsDatabase[botChoice][yourChoice];

    return [yourScore, botScore];
}

function finalMessage([yourScore, botScore]) {
    if (yourScore === 0) {
        return { 'message': "You Lost!", 'color': 'red' };

    } else if (yourScore === 1) {
        return { 'message': "You Win!", 'color': 'green' };
    } else {
        return { 'message': "Drawn!", 'color': 'yellow' }
    }
}

function rpsFrontEnd(humanImageChoice, botImageChoice, finalMessage) {
    var imageDatabase = {
        'rock': document.getElementById('rock').src,
        'paper': document.getElementById('paper').src,
        'scissor': document.getElementById('scissor').src,

    }

    document.getElementById('rock').remove();
    document.getElementById('paper').remove();
    document.getElementById('scissor').remove();

    var humanDiv = document.createElement('div');
    var botDiv = document.createElement('div');
    var messageDiv = document.createElement('div');

    humanDiv.innerHTML = "<img src='" + imageDatabase[humanImageChoice] + "' height=150 width=150 style='box-shadow: 0px 10px 30px rgba(0,233,0,0.7) ;'>";
    botDiv.innerHTML = "<img src='" + imageDatabase[botImageChoice] + "' height=150 width=150 style='box-shadow: 0px 10px 30px rgba(233,0,0,0.8);'>";
    messageDiv.innerHTML = "<h1 style='color:" + finalMessage['color'] + " ; font-size: 60px ; padding: 30px; '>" + finalMessage['message'] + "</h1>";

    document.getElementById('flex-box-rps-div').appendChild(humanDiv);
    document.getElementById('flex-box-rps-div').appendChild(messageDiv);
    document.getElementById('flex-box-rps-div').appendChild(botDiv);
}    
