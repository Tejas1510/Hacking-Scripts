score = 0;
cross = true;

audio = new Audio('music.mp3');
audiogo = new Audio('gameover.mp3');
setTimeout(() => {
    audio.play()
}, 500);

//key jb press ho toh
document.onkeydown = function (e) {
    console.log("Key code is: ", e.keyCode)
    if (e.keyCode == 38) {
        dino = document.querySelector('.dino');//call dino class
        dino.classList.add('animateDinoup');//adding animatedinoup class
        setTimeout(() => {
            dino.classList.remove('animateDinoup')
        }, 700);
    }
    // front key


    if (e.keyCode == 39) {
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
        dino.style.left = dinoX + 112 + "px";
    }
    //back key
    if (e.keyCode == 37) {
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
        dino.style.left = (dinoX - 112) + "px";
    }
}

// iss kam ko krte rhe check krte rhe ki taakkar ho rhi h y nhi 
setInterval(() => {
    dino = document.querySelector('.dino');
    gameOver = document.querySelector('.gameOver');
    obstacle = document.querySelector('.obstacle');


    // detection collosion of dino
    // getComputedStyle y value deta h 
    dx = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(dino, null).getPropertyValue('top'));


     // detection collosion of obstacle
    // getComputedStyle y value deta h 
    ox = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('top'));

    offsetX = Math.abs(dx - ox);
    offsetY = Math.abs(dy - oy);

    // agr takra gye 
    if (offsetX<93 && offsetY<52) {
        gameOver.innerHTML='Game Over - Play Again! ';
        obstacle.classList.remove('disturbance');
        audiogo.play();
        setTimeout(() => {
            audiogo.pause();
            audio.pause();
        }, 1000);
    } 

    //checking x-axis m kitta dur h aur cross true rhe
else if(offsetX<145 && cross) {
    score+=1;
    updatescore(score);
    // score bdh gya h 
    cross =false;

    // cross ko true kr rhe h 1 sec k bdd kuki ab tk vo dur ja vhuka h 
    setTimeout(() => {
        cross=true;
    }, 1000);

    // hmara disturbance ki speed bdha rhe h dheere dheere

    setTimeout(() => {
        
        disDura=parseFloat(window.getComputedStyle(obstacle, null).getPropertyValue('animation-duration'));
        newDura =disDura -0.1;
        obstacle.style.animationDuration = newDura +'s';
        console.log(newDura);
    }, 500);
}
},100);

function updatescore(score) {
    scoreCont.innerHTML ="Your Score : "+score;
}