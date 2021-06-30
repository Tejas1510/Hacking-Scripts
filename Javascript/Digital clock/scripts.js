const month = {
    0: 'Jan',
    1: 'Feb',
    2: 'Mar',
    3: 'Apr',
    4: 'May',
    5: 'Jun',
    6: 'Jul',
    7: 'Aug',
    8: 'Sept',
    9: 'Oct',
    10: 'Nov',
    11: 'Dec'
};

let dc = document.createElement('h1');
dc.className = 'heading';
dc.textContent = 'DIGITAL-CLOCK';
dc.setAttribute("style", "color: rgb(121, 62, 111); font-family: Itim; text-align: center; position: relative; top: -100px;");
let body = document.querySelector('body');
body.insertBefore(dc, body.firstElementChild);

setInterval(function() {
    let date = new Date();
    let y = date.getFullYear(), mo = date.getMonth(), d =date.getDate(), h = date.getHours(), m = date.getMinutes(), s = date.getSeconds();
    let sh = date.getHours(), sm = date.getMinutes(), ss = date.getSeconds();
    if (parseInt(h / 10) == 0) {
        sh = `0${h}`;
    }
    if (parseInt(m / 10) == 0) {
        sm = `0${m}`;
    }
    if (parseInt(s / 10) == 0) {
        ss = `0${s}`;
    }
    document.getElementById('root').innerHTML = `<div>${sh} ${sm} ${ss}</div>`;
    let parent = document.getElementById('root');
    let txt = document.createElement('p');
    txt.innerHTML = `${d} ${month[mo]} ${y}`;
    parent.appendChild(txt);
}, 1000)
