const api_url = 'https://codeforces.com/api/user.info?handles=';

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
    if (user.result == undefined) {
        $('#result').html('<p class="text-danger text-center">No such user found</p>');
    }
    else {
        return user.result;
    }
};

let displayTemplate = (user) => {
    $('#result').html(`
    <div class="container mt-5 d-flex justify-content-center">
    <div class="card p-3">
        <div class="d-flex align-items-center">
            <div class="image"> <img src="${user[0]['avatar']}" class="rounded" width="155"> </div>
            <div class="ml-3 w-100">
                <h4 class="mb-0 mt-0">${user[0]['firstName']} ${user[0]['lastName']}</h4> <span>${user[0].handle}</span>
                <div class="p-2 mt-2 bg-primary d-flex justify-content-between rounded text-white stats">
                    <div class="d-flex flex-column"> <span class="articles">Friends Of</span> <span class="number1">${user[0]['friendOfCount']}</span> </div>
                    <div class="d-flex flex-column"> <span class="followers">Rating</span> <span class="number2">${user[0].rating}</span> </div>
                    <div class="d-flex flex-column"> <span class="rating">Rank</span> <span class="number3">${user[0].rank}</span> </div>
                </div>
                <div class="button mt-2 d-flex flex-row align-items-center"> 
                <button class="btn btn-sm btn-outline-primary w-100" onclick="location.href = 'https://codeforces.com/profile/${user[0].handle}'" >View</button>  
                </div>
            </div>
        </div>
    </div>
    </div>
        `);
    $('#inputUname').val('');
};