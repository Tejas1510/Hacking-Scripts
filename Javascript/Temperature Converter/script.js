//celcius to farenheit
const go = () => {
    let celTemp = document.getElementById('string').value;
    let conversion = (celTemp * 9 / 5) + 32;

    document.getElementById('stringLength').value = `${conversion}°F`;
    h3.style.visibility = "hidden";
}

//farenheit to celcius
const go2 = () => {

    let celFar = document.getElementById('string2').value;
    let conversion = (celFar - 32) * 5 / 9;

    document.getElementById('stringLength2').value = `${conversion}°C`;
    h3.style.visibility = "hidden";
}