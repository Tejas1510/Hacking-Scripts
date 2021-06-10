var x = document.querySelector(".city-name");
var date = new Date();
var hour = date.getHours();


// Event handling for buttons "Check" 
document.getElementById("btn-location").addEventListener("click", function () {
    getLocation();
});

document.getElementById("btn-choice").addEventListener("click", function () {
    getWheater($("#city-input").val());
});

// Event handling for press Enter 
document.getElementById("city-input").addEventListener("keypress", function (event) {
    if (event.keyCode == 13) {
        getWheater($("#city-input").val());
        console.log("asd");
        $("#city-input").val("");
    }
}, false);


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    displayLocation(lat, lon);
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

function displayLocation(latitude, longitude) {
    var geocoder;
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(latitude, longitude);

    geocoder.geocode({
            'latLng': latlng
        },
        function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[0]) {
                    var add = results[0].formatted_address;
                    var value = add.split(",");

                    count = value.length;
                    country = value[count - 1];
                    city = value[count - 2];
                    adress = value[count - 3];
                    correct = true;
                    x.innerHTML = city;
                    getWheater(city);
                } else {
                    x.innerHTML = "address not found";
                }
            } else {
                x.innerHTML = "Geocoder failed due to: " + status;
            }
        }
    );
}

function getWheater(city) {
    $.getJSON("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=3a04b53f7b6d2edbaad0c1e9b9d783f1",
        function (response) {
            console.log(response);
            var city2 = city;
            var country = response.sys.country;
            var wheater = response.weather[0].main;
            var temp = response.main.temp;
            var pressure = response.main.pressure;
            var windSpeed = response.wind.speed;
            console.log(city2 + " " + country + " " + wheater + " " + temp + " " + pressure + " " + windSpeed);
            wheaterSet(city2, country, wheater, temp, pressure, windSpeed);
        });
}

function wheaterSet(city, country, wheater, temp, pressure, windSpeed) {
    console.log(wheater);
    if (wheater == "Clear") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/clearNight.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Clear" && (hour <= 20 && hour >= 6)) {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/clearDay.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Rain") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/rain.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Clouds") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/cloudsNight.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Clouds" && (hour <= 20 && hour >= 6)) {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/clouds.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Snow") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/snow.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Mist") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/mist.mp4" type="video/mp4"></video>');
    }
    if (wheater == "Thunderstorm") {
        $("#wheater-video").html("<video autoplay muted loop " + 'id="myVideo"><source  src="videos/thunderstorm.mp4" type="video/mp4"></video>');
    }
    //    $(".container-fluid").css("background", "rgba(0, 0, 0, 0.4)");    
    $("#city-info").html(city + " " + country);
    $("#wheat-info").html(wheater);
    $("#temp-info").html(temp + " &deg;C");
    $("#pressure-info").html(pressure + " hPa");
    $("#windSpeed-info").html(windSpeed + " m/s");
    $("#wheater-info").show();
    thunderstorm
}
