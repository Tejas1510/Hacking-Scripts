// console.log("Calculator");

let screen = document.getElementById('screen');
let buttons = document.getElementsByClassName('btn');
//Intial 
let user_screen = '';
for (items of buttons) {
    items.addEventListener('click', (opt) => {
        buttonText = opt.target.innerText;
        if (buttonText == 'X') {
            buttonText = '*';
            user_screen += buttonText;
            screen.value = user_screen;
        }
        else if (buttonText == 'C') {
            user_screen = '';
            screen.value = user_screen;
        }
        else if (buttonText == '=') {
            screen.value = eval(user_screen);
        }

        else {
            user_screen += buttonText;
            screen.value = user_screen;
        }
    });
}