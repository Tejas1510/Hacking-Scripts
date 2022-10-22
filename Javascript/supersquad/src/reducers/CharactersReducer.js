import { ADD_CHARACTER, REMOVE_CHARACTER } from '../Types'
import data from '../data/data.json'

const CharactersReducer = (state = data, action) => {
    switch (action.type) {
        case ADD_CHARACTER:
            // Remove character from the character list and add it to the heros list 
            let characters = state.filter(item => item.id !== action.id)
            return characters
        case REMOVE_CHARACTER:
            // Add character to the character list 
            let character = [...state, addCharacterById(action.id)]
            return character
        default: return state
    }
}
const addCharacterById = id => {
    const character = data.find(item => item.id === id)
    return character
}

export default CharactersReducer