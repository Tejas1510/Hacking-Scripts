import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

import { createStore } from 'redux'
import { Provider } from 'react-redux'

import rootReducer from './reducers/index'

const store = createStore(rootReducer)
console.log(store.getState())

store.subscribe(() => console.log('Store subscribe ', store.getState()))
// store.dispatch(addCharacterById(2))

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
)