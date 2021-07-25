import React, { useContext} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import './Home.css';
import { Context } from '../../context/Context';

const Home=()=>{
    const {user,dispatch}=useContext(Context);

    const handleLogout=()=>{
        dispatch({type:"LOGOUT"});
    }
    return(
        <div className="home">
        <h1>{`Welcome,${user.username} you are succesfully logged in 👍`}</h1>
        <small className="loo">{'Click below to logout ⬇️'}</small>
        <form onSubmit={handleLogout}>
           <button className="btn-danger">{user && "LOGOUT"}</button>
        </form>
        </div>
    )
}

export default Home;