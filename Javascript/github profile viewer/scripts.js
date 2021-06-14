const api_url = 'https://api.github.com/users/';

$(document).ready(function () {
    $('#sbmt').click(function (e) {
        e.preventDefault();
        $('#result').html('');
        if ($('#inputUname').val() != '') {
            fetchuser($('#inputUname').val()).then(user => displayTemplate(user));
        }
        else {
            $('#result').html('<p class="text-danger text-center">Please Enter username</p>');
        }
    });
});

let fetchuser = async (data) => {
    const res = await fetch(api_url + data);
    const user = await res.json();
    if (user.login == undefined) {
        $('#result').html('<p class="text-danger text-center">No such user found</p>');
    }
    else {
        return user;
    }
};

let displayTemplate = (user) => {
    $('#result').html(`
    <div class="container mt-5 d-flex justify-content-center">
    <div class="card p-3">
        <div class="d-flex align-items-center">
            <div class="image"> <img src="${user.avatar_url}" class="rounded" width="155"> </div>
            <div class="ml-3 w-100">
                <h4 class="mb-0 mt-0">${user.name}</h4> <span>${user.login}</span>
                <div class="p-2 mt-2 bg-primary d-flex justify-content-between rounded text-white stats">
                    <div class="d-flex flex-column"> <span class="articles">Followers</span> <span class="number1">${user.followers}</span> </div>
                    <div class="d-flex flex-column"> <span class="followers">Following</span> <span class="number2">${user.following}</span> </div>
                    <div class="d-flex flex-column"> <span class="rating">Repos</span> <span class="number3">${user.public_repos}</span> </div>
                </div>
                <div class="button mt-2 d-flex flex-row align-items-center"> 
                <button class="btn btn-sm btn-outline-primary w-100" onclick="location.href = 'https://github.com/${user.login}'" >View</button>  
                </div>
            </div>
        </div>
    </div>
    </div>
        `);
    $('#inputUname').val('');
};