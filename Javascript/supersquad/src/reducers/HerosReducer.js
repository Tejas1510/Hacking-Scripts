import { ADD_CHARACTER, REMOVE_CHARACTER } from '../Types'
import data from '../data/data.json'

const HerosReducer = (state = [], action) => {
    switch (action.type) {
        case ADD_CHARACTER:
            const hero = [...state, findCharacter(action.id)]
            return hero

        case REMOVE_CHARACTER:
            const heros = state.filter(item => item.id !== action.id)
            return heros

        default: return state
    }
}

const findCharacter = id => {
    const hero = data.find(item => item.id === id)
    return hero
}

export default HerosReducer