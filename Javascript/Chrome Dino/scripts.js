var character = document.getElementById('character');
var block = document.getElementById('block');
let jumping = 1, b3 = 1, score = 0;

document.addEventListener('animationiteration', function () {
    b3 = Math.floor(Math.random()*3) + 1;
    block.style.width = 20 * b3 + 'px';
    score++;
    // console.log(score);
});

setInterval(function gravity() {
    if(!jumping) {
        let charp = parseInt(window.getComputedStyle(character).getPropertyValue('top'));
        if(charp == 295) {
            jumping = 1;
            document.querySelector('body').style.pointerEvents = 'auto';
        }        
        character.style.top = (charp + 5) + 'px';
    }
    let bl = parseInt(window.getComputedStyle(block).getPropertyValue('left'));
    let ct = parseInt(window.getComputedStyle(character).getPropertyValue('top'));
    if((bl<118&&bl>(120-20*b3))&&ct>255) {
        if(score < 0) {
            score = 0;
        }
        alert('Game Over, Score: ' + score);
        let hs = parseInt(document.querySelector('strong').textContent);
        if(score > hs) {
            document.querySelector('strong').textContent = score;
        }
        block.style.animation = 'none';
        setTimeout(function() {
            block.style.animation = '';
        }, 10);
        score = 0;
    }
}, 10);

function jump() {
    if (jumping) {
        let jc = 0;
        document.querySelector('body').style.pointerEvents = 'none';
        let j = setInterval(function () {
            let charp = parseInt(window.getComputedStyle(character).getPropertyValue('top'));
            character.style.top = (charp - 5) + 'px';
            jc++;
            if (jc > 25) {
                jumping = 0;
                clearInterval(j);
            }
        }, 10);
    }
}

