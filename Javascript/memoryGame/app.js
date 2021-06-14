document.addEventListener('DOMContentLoaded', () => {

  const cardArray = [
    {
      name: 'card1',
      img: 'images/card1.png'
    },
    {
      name: 'card1',
      img: 'images/card1.png'
    },
    {
      name: 'card2',
      img: 'images/card2.png'
    },
    {
      name: 'card2',
      img: 'images/card2.png'
    },
    {
      name: 'card3',
      img: 'images/card3.png'
    },
    {
      name: 'card3',
      img: 'images/card3.png'
    },
    {
      name: 'card4',
      img: 'images/card4.png'
    },
    {
      name: 'card4',
      img: 'images/card4.png'
    },
    {
      name: 'card5',
      img: 'images/card5.png'
    },
    {
      name: 'card5',
      img: 'images/card5.png'
    },
    {
      name: 'card6',
      img: 'images/card6.png'
    },
    {
      name: 'card6',
      img: 'images/card6.png'
    }
  ]
  cardArray.sort(() => 0.5 - Math.random())

  const grid = document.querySelector('.grid')
  const resultDisplay = document.querySelector('#result')
  let cardsChosen = []
  let cardsChosenId = []
  let cardsWon = []

  function createBoard() {
    for (let i = 0; i < cardArray.length; i++) {
      const card = document.createElement('img')
      card.setAttribute('src', 'images/cover.png')
      card.setAttribute('data-id', i)
      card.addEventListener('click', flipcard)
      grid.appendChild(card)
    }
  }

  function checkForMatch() {
    const cards = document.querySelectorAll('img')
    const optionOneId = cardsChosenId[0]
    const optionTwoId = cardsChosenId[1]


    if (optionOneId == optionTwoId) {
      cards[optionOneId].setAttribute('src', 'images/cover.png')
      cards[optionTwoId].setAttribute('src', 'images/cover.png')
    }
    else if (cardsChosen[0] === cardsChosen[1]) {
      cards[optionOneId].setAttribute('src', 'images/blank.JPG')
      cards[optionTwoId].setAttribute('src', 'images/blank.JPG')
      cards[optionOneId].removeEventListener('click', flipcard)
      cards[optionTwoId].removeEventListener('click', flipcard)
      cardsWon.push(cardsChosen)
    } else {
      cards[optionOneId].setAttribute('src', 'images/cover.png')
      cards[optionTwoId].setAttribute('src', 'images/cover.png')
    }
    cardsChosen = []
    cardsChosenId = []
    resultDisplay.textContent = cardsWon.length
    if (cardsWon.length === cardArray.length / 2) {
      resultDisplay.textContent = 'Congratulations! You Won!'
    }
  }

  function flipcard() {
    let cardId = this.getAttribute('data-id')
    cardsChosen.push(cardArray[cardId].name)
    cardsChosenId.push(cardId)
    this.setAttribute('src', cardArray[cardId].img)
    if (cardsChosen.length === 2) {
      setTimeout(checkForMatch, 500)
    }
  }

  createBoard()

})