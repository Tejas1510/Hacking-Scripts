//https://api.github.com/users/user_name/repos

const user_img = document.querySelector(".user_img");
const userName = document.querySelector(".user_name h1");
const followers_ = document.querySelector(".followers_ span");
const repo_details = document.querySelector(".repo_details");
const btn_submit = document.querySelector(".btn_submit");
const followe = document.querySelector(".followe span");

let user_name = '';

//when user enters username in text box
function inputFunction() {
    //trim removes leading and trailing white space from user input
    let input_user = document.querySelector(".input_user").value.trim();

    //if invalid username
    if (input_user.length <= 0) {
        alert("Please enter github user name");
        document.querySelector(".input_user").value = "";
        document.querySelector(".input_user").focus();
        return false;
    } 
    //if username is valid, call fetchUser()
    else {
        user_name = input_user.split("").join("");
        fetchUser();

        //clear the input box and refocus it
        document.querySelector(".input_user").value = "";
        document.querySelector(".input_user").focus();
    }
};

btn_submit.addEventListener("click", function () {
    inputFunction()
});

//if user presses enter it should submit 
document.querySelector(".input_user").addEventListener("keyup", function (e) {
    if (e.keyCode === 13) {
        //alert("you have pressed enter key");
        inputFunction()
    }
})

//fetch user info from github api
function fetchUser() {
    fetch(`https://api.github.com/users/${user_name}`).then(response => response.json()).then(function (data) {
        console.log(data);
        if (data.message === "Not Found") {
            alert("user not found");
            return false;
        } 
        else {
            user_img.innerHTML = `<img src="${data.avatar_url}">`;
            userName.innerHTML = data.login;
            followers_.innerHTML = data.bio;
            followe.innerHTML = data.login+",";
        }
    })
}

// downloads screenshot to local computer
document.querySelector(".download_button").addEventListener("click",function() {
    html2canvas(document.querySelector(".row"),{useCORS:true}).then(function(canvas) {
        console.log(canvas);
        saveAs(canvas.toDataURL(),'Badge.png');
    });
});

function saveAs(uri, filename) {
    var link = document.createElement('a');

    if (typeof link.download === 'string') {
        link.href = uri;
        link.download = filename;

        //Firefox requires the link to be in the body
        document.body.appendChild(link);

        //simulate click
        link.click();

        //remove the link when done
        document.body.removeChild(link);

    } else {
        window.open(uri);
    }
}
