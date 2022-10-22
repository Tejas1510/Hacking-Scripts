import React from 'react'
import CharactersList from './components/CharactersList'
import HerosList from './components/HerosList'
import Stats from './components/Stats'
const App = () => {
    return (
        <div>
            <h3>Supersquad</h3>
            <CharactersList />
            <HerosList />
            <Stats />
        </div>
    )
}

export default App