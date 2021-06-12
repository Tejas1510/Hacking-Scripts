import React, {createContext, useReducer} from 'react';
import AppReducer from './AppReducer'

const initialState = {
  transactions : [
    // {id: 1, text: 'Books', amount: -500},
    // {id: 2, text: 'Salary', amount: 1000},
    // {id: 3, text: 'Chocolates', amount: -100},
    // {id: 4, text: 'Income', amount: 500}
  ]
}

export const GlobalContext = createContext(initialState);

export const GlobalProvider = ({children}) => {
  const[state, dispatch] = useReducer(AppReducer, initialState);

  function deleteTransaction(id){
    dispatch({
      type : 'DELETE_TRANSACTION',
      payload: id
    });
  }
  function addTransaction(transaction){
    dispatch({
      type : 'ADD_TRANSACTION',
      payload: transaction
    });
  }
  return <GlobalContext.Provider value={{
    transactions : state.transactions,
    deleteTransaction,
    addTransaction
  }}>
    {children}
  </GlobalContext.Provider>
}