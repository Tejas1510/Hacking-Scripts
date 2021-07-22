const score = document.querySelector('.score');
var Intscore = parseInt((score.innerHTML));
const w = 4;
var squares = [];
const box = document.querySelector("#box");
const game = document.querySelector(".game-ow");
var o = document.createElement('p');


// making squares inside box
function boxMaker() {
    for (let i = 0; i < w * w; i++) {
        var square = document.createElement('div');
        square.innerHTML = 0;
        box.appendChild(square);
        squares.push(square);
    }
    generator();
    generator();
}
boxMaker();

//generating random 2 on the square 
function generator() {
    let randomNumber = Math.floor(Math.random() * squares.length);
    if (squares[randomNumber].innerHTML == 0) {
        squares[randomNumber].innerHTML = 2;
    } else { generator(); }
    colorchanger();
    gameWin();
    gameOver();
}

//change color of boxes according to the number contained in them
function colorchanger() {
    for (let i = 0; i < squares.length; i++) {
        if (squares[i].innerHTML == 0) {
            squares[i].style.color = "rgb(187, 171, 171, 0.7)";
            squares[i].style.backgroundColor = "rgb(187, 171, 171, 0.7)";
        } else if (squares[i].innerHTML == 2) {
            squares[i].style.backgroundColor = "#EEE4DB";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 4) {
            squares[i].style.backgroundColor = "#EEDFC8";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 8) {
            squares[i].style.backgroundColor = "#F2B179";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 16) {
            squares[i].style.backgroundColor = "#EC8D55";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 32) {
            squares[i].style.backgroundColor = "#F77B5F";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 64) {
            squares[i].style.backgroundColor = "#EA5A38";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 128) {
            squares[i].style.backgroundColor = "#EDCF72";
            squares[i].style.color = "black";
        } else if (squares[i].innerHTML == 256) {
            squares[i].style.backgroundColor = "#F2D04B";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 512) {
            squares[i].style.backgroundColor = "#EDC850";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 1024) {
            squares[i].style.backgroundColor = "#E3BA14";
            squares[i].style.color = "black";

        } else if (squares[i].innerHTML == 2048) {
            squares[i].style.backgroundColor = "#ECC402";
            squares[i].style.color = "black";

        }
    }
}

function moveRight() {
    for (let i = 0; i < 16; i++) {
        if (i % 4 == 0) {
            let ArrayOne = [];
            ArrayOne[0] = squares[i].innerHTML;
            ArrayOne[1] = squares[i + 1].innerHTML;
            ArrayOne[2] = squares[i + 2].innerHTML;
            ArrayOne[3] = squares[i + 3].innerHTML;
            let row = [parseInt(ArrayOne[0]), parseInt(ArrayOne[1]), parseInt(ArrayOne[2]), parseInt(ArrayOne[3])];

            let array = row.filter(num => num);
            let remaining = 4 - array.length;
            let array2 = Array(remaining).fill(0);
            let array3 = array2.concat(array);
            squares[i].innerHTML = array3[0];
            squares[i + 1].innerHTML = array3[1];
            squares[i + 2].innerHTML = array3[2];
            squares[i + 3].innerHTML = array3[3];
        }
    }
}

function moveLeft() {
    for (let i = 0; i < 16; i++) {
        if (i % 4 == 0) {
            let ArrayOne = [];
            ArrayOne[0] = squares[i].innerHTML;
            ArrayOne[1] = squares[i + 1].innerHTML;
            ArrayOne[2] = squares[i + 2].innerHTML;
            ArrayOne[3] = squares[i + 3].innerHTML;
            let row = [parseInt(ArrayOne[0]), parseInt(ArrayOne[1]), parseInt(ArrayOne[2]), parseInt(ArrayOne[3])];

            let array = row.filter(num => num);
            let remaining = 4 - array.length;
            let array2 = Array(remaining).fill(0);
            let array3 = array.concat(array2);
            squares[i].innerHTML = array3[0];
            squares[i + 1].innerHTML = array3[1];
            squares[i + 2].innerHTML = array3[2];
            squares[i + 3].innerHTML = array3[3];
        }
    }
}

function moveUp() {
    for (let i = 0; i < 4; i++) {
        let ArrayOne = [];
        ArrayOne[0] = squares[i].innerHTML;
        ArrayOne[1] = squares[i + w].innerHTML;
        ArrayOne[2] = squares[i + (w * 2)].innerHTML;
        ArrayOne[3] = squares[i + (w * 3)].innerHTML;
        let column = [parseInt(ArrayOne[0]), parseInt(ArrayOne[1]), parseInt(ArrayOne[2]), parseInt(ArrayOne[3])];

        let array = column.filter(num => num);
        let remaining = 4 - array.length;
        let array2 = Array(remaining).fill(0);
        let array3 = array.concat(array2);
        squares[i].innerHTML = array3[0];
        squares[i + w].innerHTML = array3[1];
        squares[i + (w * 2)].innerHTML = array3[2];
        squares[i + (w * 3)].innerHTML = array3[3];
    }
}

function moveDown() {
    for (let i = 0; i < 4; i++) {
        let ArrayOne = [];
        ArrayOne[0] = squares[i].innerHTML;
        ArrayOne[1] = squares[i + w].innerHTML;
        ArrayOne[2] = squares[i + (w * 2)].innerHTML;
        ArrayOne[3] = squares[i + (w * 3)].innerHTML;
        let column = [parseInt(ArrayOne[0]), parseInt(ArrayOne[1]), parseInt(ArrayOne[2]), parseInt(ArrayOne[3])];

        let array = column.filter(num => num);
        let remaining = 4 - array.length;
        let array2 = Array(remaining).fill(0);
        let array3 = array2.concat(array);
        squares[i].innerHTML = array3[0];
        squares[i + w].innerHTML = array3[1];
        squares[i + (w * 2)].innerHTML = array3[2];
        squares[i + (w * 3)].innerHTML = array3[3];
    }
}

function combinedColumn() {
    let flag1 = false;
    let flag2 = false;
    let flag3 = false;
    let flag4 = false;
    for (let i = 0; i < 12; i++) {
        if ((i % 4 == 0) && flag4 == false) {
            if (squares[i + w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i + w].innerHTML);
                squares[i + w].innerHTML = 0;
                squares[i].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                //console.log(typeof(score.innerHTML))=>returns String.Although intscore is number but score.innerHtml is always string.
                if (i == 1 || i == 5 || i == 9) flag1 = true;
                else if (i == 2 || i == 6 || i == 10) flag2 = true;
                else if (i == 3 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i == 1 || i == 5 || i == 9) && flag1 == false) {
            if (squares[i + w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i + w].innerHTML);
                squares[i + w].innerHTML = 0;
                squares[i].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                //console.log(typeof(score.innerHTML))=>returns String.Although intscore is number but score.innerHtml is always string.
                if (i == 1 || i == 5 || i == 9) flag1 = true;
                else if (i == 2 || i == 6 || i == 10) flag2 = true;
                else if (i == 3 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i == 2 || i == 6 || i == 10) && flag2 == false) {
            if (squares[i + w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i + w].innerHTML);
                squares[i + w].innerHTML = 0;
                squares[i].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                //console.log(typeof(score.innerHTML))=>returns String.Although intscore is number but score.innerHtml is always string.
                if (i == 1 || i == 5 || i == 9) flag1 = true;
                else if (i == 2 || i == 6 || i == 10) flag2 = true;
                else if (i == 3 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i == 3 || i == 7 || i == 11) && flag3 == false) {
            if (squares[i + w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i + w].innerHTML);
                squares[i + w].innerHTML = 0;
                squares[i].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                //console.log(typeof(score.innerHTML))=>returns String.Although intscore is number but score.innerHtml is always string.
                if (i == 1 || i == 5 || i == 9) flag1 = true;
                else if (i == 2 || i == 6 || i == 10) flag2 = true;
                else if (i == 3 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        }
    }
}


function combinedColumnDown() {
    let flag1 = false;
    let flag2 = false;
    let flag3 = false;
    let flag4 = false;
    for (let i = 15; i > 3; i--) {
        if ((i == 13 || i == 5 || i == 9) && flag1 == false) {
            if (squares[i - w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i - w].innerHTML);
                squares[i].innerHTML = 0;
                squares[i - w].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i == 13 || i == 5 || i == 9) flag1 = true;
                else if (i == 14 || i == 6 || i == 10) flag2 = true;
                else if (i == 15 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i == 14 || i == 6 || i == 10) && flag2 == false) {
            if (squares[i - w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i - w].innerHTML);
                squares[i].innerHTML = 0;
                squares[i - w].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i == 13 || i == 5 || i == 9) flag1 = true;
                else if (i == 14 || i == 6 || i == 10) flag2 = true;
                else if (i == 15 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i == 15 || i == 7 || i == 11) && flag3 == false) {
            if (squares[i - w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i - w].innerHTML);
                squares[i].innerHTML = 0;
                squares[i - w].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i == 13 || i == 5 || i == 9) flag1 = true;
                else if (i == 14 || i == 6 || i == 10) flag2 = true;
                else if (i == 15 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        } else if ((i % 4 == 0) && flag4 == false) {
            if (squares[i - w].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i - w].innerHTML);
                squares[i].innerHTML = 0;
                squares[i - w].innerHTML = combinedTotal;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i == 13 || i == 5 || i == 9) flag1 = true;
                else if (i == 14 || i == 6 || i == 10) flag2 = true;
                else if (i == 15 || i == 7 || i == 11) flag3 = true;
                else if (i % 4 == 0) flag4 = true;
            }
        }
    }
}


document.addEventListener('keyup', control);

function combinedRow() {
    for (let i = 0; i < 15; i++) {
        if (i != 3 && i != 7 && i != 11 && i != 15) {
            if (squares[i].innerHTML === squares[i + 1].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i + 1].innerHTML);
                squares[i].innerHTML = combinedTotal;
                squares[i + 1].innerHTML = 0;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i % 4 == 0) i = i + 3;
                if (i == 1 || i == 5 || i == 9 || i == 13) i = i + 2;
                else if (i == 2 || i == 6 || i == 10 || i == 14) i = i + 1;
            }
        }
    }
}

function combinedRowRight() {
    for (let i = 15; i > 0; i--) {
        if ((i % 4) != 0) {
            if (squares[i - 1].innerHTML === squares[i].innerHTML) {
                let combinedTotal = parseInt(squares[i].innerHTML) + parseInt(squares[i - 1].innerHTML);
                squares[i].innerHTML = combinedTotal;
                squares[i - 1].innerHTML = 0;
                Intscore += combinedTotal;
                score.innerHTML = Intscore;
                if (i == 1 || i == 5 || i == 9 || i == 13) i = i - 1;
                else if (i == 2 || i == 6 || i == 10 || i == 14) i = i - 2;
                else if (i == 3 || i == 7 || i == 11 || i == 15) i = i - 3;
            }
        }
    }
}

//assign keycodes
function control(e) {
    if (e.keyCode === 39) {
        keyRight();
    } else if (e.keyCode === 37) {
        keyLeft();
    } else if (e.keyCode === 38) {
        keyUp();
    } else if (e.keyCode === 40) {
        keyDown();
    }
}


function keyRight() {
    moveRight();
    combinedRowRight();
    moveRight();
    generator();
}

function keyLeft() {
    moveLeft();
    combinedRow();
    moveLeft();
    generator();
}

function keyUp() {
    moveUp();
    combinedColumn();
    moveUp();
    generator();
}

function keyDown() {
    moveDown();
    combinedColumnDown();
    moveDown();
    generator();
}


function checkforWin() {
    for (let i = 0; i < squares.length; i++) {
        if ((squares[i].innerHTML) == 2048) return true;
    }
    return false;
}

// check for gameOver function to check wheather two blocks aligned side by side have same number or not when fully filled.
function squaresCheck() {
    for (let i = 0; i < squares.length; i++) {
        if ((i > 3) && ((squares[i].innerHTML) == (squares[i - w].innerHTML))) {
            return false;
        }
        if ((i < 12) && ((squares[i].innerHTML) == (squares[i + w].innerHTML))) {
            return false;
        }
        if (((i != 3 && i != 7 && i != 11 && i != 15)) && ((squares[i].innerHTML) == (squares[i + 1].innerHTML))) {
            return false;
        }
        if ((i % 4 != 0) && ((squares[i].innerHTML) == (squares[i - 1].innerHTML))) {
            return false;
        }
    }
    return true;
}

function gameOver() {
    let count = 0;
    for (let i = 0; i < squares.length; i++) {
        if ((squares[i].innerHTML) == 0) ++count;
    }
    let some = squaresCheck();
    if (count == 0 && some) {
        o.innerHTML = "GAME OVER";
        game.appendChild(o);
        game.style.visibility = "visible";
        document.removeEventListener('keyup', control);
    }
}

function gameWin() {
    let some = checkforWin();
    if (some) {
        o.innerHTML = "CONGRATULATIONS!<br>YOU WIN";
        game.appendChild(o);
        game.style.visibility = "visible";
        document.removeEventListener('keyup', control);
    }
}