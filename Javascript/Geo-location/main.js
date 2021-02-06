var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;


    var latlon = position.coords.latitude + "," + position.coords.longitude;
    var img_url = `https://maps.googleapis.com/maps/api/staticmap?center=${latlon} & zoom=14 & size=400x300 & sensor=false & key=a9d8b788-9b49-4bb7-8f11-9e21e4eabb12`;

    document.getElementById("mapholder").innerHTML = "<img src='" + img_url + "'>";
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation."
            break;
        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable."
            break;
        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out."
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred."
            break;
    }
}