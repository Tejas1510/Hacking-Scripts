import React from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import './Signin.css'
import { useContext,useRef,useState } from 'react';
import {Link} from 'react-router-dom';
import {Context} from '../../context/Context';

const Signin = ()=>{
  const userRef = useRef();
  const passwordRef = useRef();
  const [error, setError] = useState(false);
  const {dispatch,isfetching} = useContext(Context);

  const handleSubmit  =async(e)=>{
      e.preventDefault();
      setError(false);
      dispatch({type:"LOGIN_START"});
      try{
          const res = await axios.post("auth/signin",{
              username:userRef.current.value,
              password:passwordRef.current.value,
          });
          dispatch({type:"LOGIN_SUCCESS",payload:res.data})
      }catch(err){
          dispatch({type:"LOGIN_FAILURE"});
          setError(true);
      }
  }
  return(
    <div className="container">
     <span className="loginTitle">Sign in</span>
     <small id="emailHelp" className="form-text text-muted">We'll never share your password with anyone else.</small>
    <form onSubmit={handleSubmit}>
    <div className="form-group p-2">
      <label htmlFor="exampleInputEmail1" className="p-2">Username</label>
      <input type="text" className="form-control" id="exampleInputEmail1" 
      aria-describedby="emailHelp" 
      placeholder="Enter your username"
       ref={userRef}
      />
    </div>
    <div className="form-group p-2 m-lg-2">
      <label htmlFor="exampleInputPassword1" className="p-2">Password</label>
      <input type="password" className="form-control " id="exampleInputPassword1"
       placeholder="Password"
        ref={passwordRef}
       />
    </div>
    <button type="submit" className="btn btn-primary" disabled={isfetching}>Submit</button>
  </form>
  <button className="loginRegisterButton">
        <Link className="link" to="/register">
          Register
        </Link>
  </button>
  {error && <span style={{color:"red",marginTop:"10px"}}>Something went wrong!!</span>}
  </div>
  )
}

export default Signin;