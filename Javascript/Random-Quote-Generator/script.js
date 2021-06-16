const quote=document.querySelector("#quote");
const author=document.querySelector("#author");
const btn=document.querySelector("#btn");

btn.addEventListener("click", getQuote);


function getQuote() {
    fetch('https://api.quotable.io/random')
    .then((res) => res.json())
    .then((data) => {
    quote.innerHTML = `"${data.content}"`;
    author.innerHTML = `${data.author}`;
  });
       
  }