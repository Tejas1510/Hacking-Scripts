const light = document.querySelector('#bulb');

//Toggling will keep on adding and removing "bulb-on" class there by toggling between on and off states of the bulb
light.addEventListener('click', function (e) {

    e.target.classList.toggle('bulb-on');

})