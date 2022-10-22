import { combineReducers } from 'redux'

import CharactersReducer from './CharactersReducer'
import HerosReducer from './HerosReducer'

const rootReducer = combineReducers({
    Characters: CharactersReducer,
    Heros: HerosReducer
})

export default rootReducer