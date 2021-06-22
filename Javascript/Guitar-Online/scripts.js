let notes = (e, note) => {
    console.log(e);
    let audio = new Audio(note);
    audio.play();
}