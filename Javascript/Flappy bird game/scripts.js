var block = document.getElementById('block');
var hole = document.getElementById('hole');
var character = document.getElementById('character');
let jumping = 0, counter = 1,f = 0;

function refresh() {
    $('h3').show(200);
    setTimeout(function() {
        $('h3').hide(400);
    }, 1000);
}

hole.addEventListener('animationiteration', () => {
    if(f) {
        let random = -(Math.random()*350+150);
        hole.style.top = random + 'px';
    }
    console.log(f);
    f=1;
    counter++;
});

setInterval(function() {
    let charTop = parseInt(window.getComputedStyle(character).getPropertyValue('top'));
    if(jumping == 0) {
        character.style.top = (charTop+3) + 'px';
    }
    let bl = parseInt(window.getComputedStyle(block).getPropertyValue('left'));
    let ht = parseInt(window.getComputedStyle(hole).getPropertyValue('top'));
    let ct = -(550 - charTop);
    if(charTop<0||charTop>520||((bl<88)&&(bl>36)&&((ct<ht)||(ct>ht+120)))) {
        if(counter > 0) {
            counter--;
            alert('Game over, Your Score: ' + (counter));
        }
        else {
            counter = 0;
            alert('Game over, Your Score: 0');
        }
        let hs = parseInt(document.querySelector('strong').textContent);
        if(counter > hs) {
            document.querySelector('strong').innerHTML = counter;
        }
        counter = 1;f = 0;
        hole.style.top = -350 + 'px';
        hole.style.animation = 'none';
        block.style.animation = 'none';
        setTimeout(function() {
            hole.style.animation = '';
            block.style.animation = '';
        }, 10);
        character.style.top = 150 + 'px';
    }
}, 10);

function jump() {
    jumping = 1;
    let jumpCount=0;
    let jumpi = setInterval(function() {
        let charTop = parseInt(window.getComputedStyle(character).getPropertyValue('top'));
        character.style.top = (charTop-5) + 'px';
        if(jumpCount>20) {
            clearInterval(jumpi);
            jumping = 0;
            jumpCount = 0;
        }
        jumpCount++;
    },10);
}