import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js'
import './Signup.css';

const Register=()=>{
    const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(false);

  const handleSubmit = async (e)  =>{
      e.preventDefault();
      setError(false);
      try{
          const res = await axios.post("/auth/register",{
              username,
              email,
              password,
          });
          res.data && window.location.replace("/signin");
      }catch(err){
          setError(true);
      }
  };
  return (
    <div className="container">
    <span className="loginTitle">Register</span>
   <form onSubmit={handleSubmit}>
   <div className="form-group">
     <label htmlFor="exampleInputEmail1" className="p-2">Username</label>
     <input type="text" className="form-control" id="exampleInputEmail1" 
     aria-describedby="emailHelp" 
     placeholder="Enter your username"
     onChange={(e)=>setUsername(e.target.value)}
     />
   </div>
   <div className="form-group p-2">
     <label htmlFor="exampleInputPassword1" className="p-2">Email</label>
     <input type="email" className="form-control " id="exampleInputPassword1"
      placeholder="Enter your Password"
       onChange={(e)=>setEmail(e.target.value)}
      />
      <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
   </div>
   <div className="form-group p-2">
     <label htmlFor="exampleInputPassword1" className="p-2">Password</label>
     <input type="password" className="form-control "
      placeholder="Enter your Password"
       onChange={(e)=>setPassword(e.target.value)}
      />
       <small id="emailHelp" className="form-text text-muted">We'll never share your password with anyone else.</small>
   </div>
   <button type="submit" className="btn btn-primary">Register</button>
 </form>
 <button className="registerLoginButton">
       <Link className="link" to="/signin">
         Login
       </Link>
 </button>
  {error && <span style={{color:"red",marginTop:"10px"}}>Something went wrong!!</span>}
 </div>
  )
}

export default Register;