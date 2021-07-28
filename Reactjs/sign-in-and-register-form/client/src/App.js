import React, { useContext } from 'react';
import {BrowserRouter as Router,Switch,Route} from "react-router-dom";
import Signup from './component/Sign up/Signup';
import Signin from './component/Signin/Signin';
import Home from './component/Home/Home';
import Particles from 'react-particles-js';
import { Context } from './context/Context';
import './App.css';

const particleOptions = {
  particles:{
    number: {
      value:80,
      density:{
        enable:true,
        value_area:800
      }
    }
  }
}

const App=()=>{
  const { user } = useContext(Context);
  return(
    <>
      <Router>
      <Particles className='particles' params={particleOptions}/>
       <Switch>
       <Route exact path="/">
         <Signup/>
       </Route>
       <Route path="/register">{user ? <Home/> : <Signup/>}</Route>
      <Route path="/signin">{user ? <Home/>:<Signin/>}</Route>
        </Switch>
      </Router>
    </>
  )
}

export default App;