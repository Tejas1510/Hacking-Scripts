//Getting the DOM elements

const time = document.getElementById("time"),
 greeting=document.getElementById('wish'),
 name=document.getElementById('name'),
 focus=document.getElementById('focus');


 // optional : showing ampm

 const showAmPm= true;
//Making a time function to show time

function showTime(){
 let today = new Date(),

    hour= today.getHours(),
    min = today.getMinutes(),
    sec = today.getSeconds();

//Setting AM and PM
    const amPm = hour>=12 ? 'PM' : 'AM' ;

// 12 hour time (clock)

hour = hour%12 || 12 ;

//Time output

time.innerHTML = `${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(sec)} ${showAmPm ? amPm : '' }`;

setTimeout(showTime, 1000);

}

//adding zeros

function addZero(n) {
    return(parseInt(n, 10) < 10 ? '0' : '') + n ;

}

//setting background and greeting

function settingBgGreeting(){
       let today = new Date(),
        hour = today.getHours();

    if ( hour < 12){
        //morning
        document.body.style.backgroundImage = "url('images/morning.jpg')" ;
        document.body.style.backgroundSize = "100vw 100vh";
        greeting.textContent = "Good Morning";
    } else if( hour < 18){
        //afternoon
        document.body.style.backgroundImage = "url('images/afternoon.jpg')";
        document.body.style.backgroundSize = "100vw 100vh";
        greeting.textContent = "Good Afternoon";
    }else{
        //night
        document.body.style.backgroundImage = "url('images/night.jpg')";
        greeting.textContent = "Good Night";
        document.body.style.backgroundSize = "100vw 100vh";
        document.body.style.color = 'white';
    }

}
//get name 

function getName(){
    if (localStorage.getItem('name') === null){
        name.textContent = "[Enter Your Name]";
    }else{
        name.textContent = localStorage.getItem('name');
    }
}
//get focus
function getFocus(){
    if(localStorage.getItem('focus') === null){
        focus.textContent = "[Enter Focus]";
    }else{
        focus.textContent = localStorage.getItem('focus');
    }
}

//set Name

function setName(e){
    if(e.type === 'keypress'){
        //ensuring that 'enter is pressed'
        if(e.which == 13 || e.keycode == 13){
            localStorage.setItem('name', e.target.innerText);
            name.blur();

        }else{
            localStorage.setItem('name', e.target.innerText)
        }
    }
}
//set focus

function setFocus(e){
    if(e.type === 'keypress'){
        //ensuring that 'enter is pressed'
        if(e.which == 13 || e.keycode == 13){
            localStorage.setItem('focus', e.target.innerText);
            focus.blur();

        }else{
            localStorage.setItem('focus', e.target.innerText)
        }
    }
}
//adding eventlistener

name.addEventListener('keypress', setName);
name.addEventListener('blur', setName);
focus.addEventListener('keypress', setFocus);
focus.addEventListener('blur', setFocus);

//Run time function

showTime();
settingBgGreeting();
getName();
getFocus();
