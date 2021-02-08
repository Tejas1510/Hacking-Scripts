function updateText() {

    let texts = document.getElementById('text-input').value
    document.getElementById('text-output').innerText = texts
}

function makeBold(elem) {

    elem.classList.toggle('active')
    document.getElementById('text-output').classList.toggle('bold')
}


function makeItalic(elem) {
    elem.classList.toggle('active')
    document.getElementById('text-output').classList.toggle('italic')
}

function makeUnderline(elem) {

    elem.classList.toggle('active')

    let formattext = document.getElementById('text-output')
    if (formattext.classList.contains('underline')) {
        formattext.classList.remove('underline')
    } else {
        formattext.classList.add('underline')
    }
}


function alignText(elem, alignType) {

    elem.classList.toggle('active')
    document.getElementById('text-output').style.textAlign = alignType
}