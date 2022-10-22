import { ADD_CHARACTER, REMOVE_CHARACTER } from '../Types'

export const addCharacterById = id => {
    const action = {
        type: ADD_CHARACTER,
        id
    }
    return action
}

export const removeCharacterById = id => {
    const action = {
        type: REMOVE_CHARACTER,
        id
    }
    return action
}
