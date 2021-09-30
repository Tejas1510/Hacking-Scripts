import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

const firebase = require('firebase');
require('firebase/firestore');

firebase.initializeApp({
  apiKey: "AIzaSyB_Pq5AHrbKM2te-Ky1Zm45BqIodKLLNX0",
  authDomain: "evernote-clone-44896.firebaseapp.com",
  databaseURL: "https://evernote-clone-44896.firebaseio.com",
  projectId: "evernote-clone-44896",
  storageBucket: "evernote-clone-44896.appspot.com",
  messagingSenderId: "915706065297",
  appId: "1:915706065297:web:103bb9bcb967aef5"
});

ReactDOM.render(<App />, document.getElementById('evernote-container'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
