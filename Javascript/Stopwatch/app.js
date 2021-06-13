const watch = document.querySelector('#watch');//call id watch
let milliseconds = 0;
let timer;
//making each function 

//on hitting start
const startWatch = () => {
  watch.classList.remove('paused');
  clearInterval(timer);
  timer = setInterval(()=>{ 
    milliseconds += 10;
    let dateTimer = new Date(milliseconds);
    //STOP WATCH TIMER ACCORDING TO UNIVERSAL COORDINATED TIME
    watch.innerHTML = 
      ('0'+dateTimer.getUTCHours()).slice(-2) + ':' +
      ('0'+dateTimer.getUTCMinutes()).slice(-2) + ':' +
      ('0'+dateTimer.getUTCSeconds()).slice(-2) + ':' +
      ('0'+dateTimer.getUTCMilliseconds()).slice(-3,-1);
  },10);
};
//on hitting pause

const pauseWatch = () => {
  watch.classList.add('paused');
  clearInterval(timer);
};
//Reseting the stop watch
const resetWatch = () => {
  watch.classList.remove('paused');
  clearInterval(timer);
  milliseconds = 0;
  watch.innerHTML= '00:00:00:00';
};

//onclicking
document.addEventListener('click', (e) =>{
  const element = e.target;
  if (element.id === 'start') startWatch(); //startwatch function
  if (element.id === 'pause') pauseWatch();
  if (element.id === 'reset') resetWatch();
});