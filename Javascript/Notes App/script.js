const addBtn = document.getElementById('add')

const notes = JSON.parse(localStorage.getItem('notes'))

if(notes) {
    notes.forEach(note => addNewNote(note))
}

addBtn.addEventListener('click', () => addNewNote())
var originalDate ,originalMonth,originalYear ,dt ,giveDate;
function noteDate() {
    dt = new Date();
    originalDate = dt.getDate();
    originalMonth = dt.getMonth() + 1;
    originalYear = dt.getFullYear();
    
    
    if (originalDate <= 9) {
        originalDate = '0' + originalDate;
    }
    if (originalMonth <= 9) {
        originalMonth = '0' + originalMonth;
    }
    if (originalYear <= 9) {
        originalYear = '0' + originalYear;
    }

    return (giveDate = originalDate + `<span class= "slash">/</span>` + originalMonth + `<span class= "slash">/</span>` + originalYear);
    
}
var dy, hr, min, sec, clock;

function clocky() {
    dy = new Date();
    hr = dy.getHours();
    min = dy.getMinutes();
    sec = dy.getSeconds();
    
    
    if (hr <= 9) {
        hr = '0' + hr;
    }
    if (min <= 9) {
        min = '0' + min;
    }
    if (hr >= 12) {
        return (clock = hr + `<span class= "colon">:</span>` + min + `<span class= "colon">:</span>` + "pm");
        
    } else {
        return (clock = hr + `<span class= "colon">:</span>` + min + `<span class= "colon">:</span>` + "am");
        
    }

    
}
function addNewNote(text = '') {
    const note = document.createElement('div')
    note.classList.add('note')
    var NoteDATE = noteDate();
    var NoteTIME = clocky();

    note.innerHTML = `
    <div class="tools">
        <button class="edit"><i class="fas fa-edit"></i></button>
        <button class="delete"><i class="fas fa-trash-alt"></i></button>
    </div>
    <h5 class="center">Date- ${NoteDATE}</h5>
    <h6 class="center">Time- ${NoteTIME}</h6>

    <div class="main ${text ? "" : "hidden"}"></div>
    <textarea class="${text ? "hidden" : ""}"></textarea>
    `

    const editBtn = note.querySelector('.edit')
    const deleteBtn = note.querySelector('.delete')
    const main = note.querySelector('.main')
    const textArea = note.querySelector('textarea')

    textArea.value = text
    main.innerHTML = marked(text)

    deleteBtn.addEventListener('click', () => {
        note.remove()

        updateLS()
    })

    editBtn.addEventListener('click', () => {
        main.classList.toggle('hidden')
        textArea.classList.toggle('hidden')
    })

    textArea.addEventListener('input', (e) => {
        const { value } = e.target

        main.innerHTML = marked(value)

        updateLS()
    })

    document.body.appendChild(note)
}

function updateLS() {
    const notesText = document.querySelectorAll('textarea')

    const notes = []

    notesText.forEach(note => notes.push(note.value))

    localStorage.setItem('notes', JSON.stringify(notes))
}
