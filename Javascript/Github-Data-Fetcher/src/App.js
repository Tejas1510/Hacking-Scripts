import {  React, Component,useEffect, useState} from "react";
import { Card, Form, Icon, Image } from "semantic-ui-react";
import './App.css';
import ParticlesBg from 'particles-bg'


function App() {
  const [name, setName] = useState('');
  const [userName, setUserName] = useState('');
  const [followers, setFollowers] = useState('');
  const [following, setFollowing] = useState('');
  const [repos, setRepos] = useState('')
  const [avatar, setAvatar] = useState('')
  const [userInput, setUserInput] = useState('');
  const [bio, setBio] = useState('')
  const [organizations, setOrganizations] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    fetch("https://api.github.com/users/pritamp17")
    .then(res=>res.json())
    .then(data=>{
      // console.log(data);
      setData(data)
    })
    
  }, []);

  const setData = ({name,login, followers, following,public_repos,avatar_url,bio}) => {

    setName(name)
    setUserName(login)
    setFollowers(followers)
    setFollowing(following)
    setRepos(public_repos)
    setAvatar(avatar_url)
    setBio(bio)
    
  }

  const handleSearch = (e) => {
    console.log(e.target.value);
    setUserInput(e.target.value);
    
  }

  
  const handleSubmit = () => {
    fetch(`https://api.github.com/users/${userInput}`)
    .then(res=>res.json())
    .then((data)=>{
      if(data.message){
        setError(data.message)
      }
      else{
        setData(data);
        setError(null);
        // console.log(data);
      }
      
    })
  }

  let config = {
    position: {height:120}
  }

  return (
    
    <div className="App">
     <div className="navbar">
     <h2>Github search</h2></div>

    <div className="search">

    
        <Form onSubmit={handleSubmit} autoComplete="off">
              <Form.Group>
                <Form.Input placeholder='Github user' name='Github user' onChange={handleSearch}/>
    
                <Form.Button content='Search' class="ui primary button"/>
              </Form.Group>
            </Form>
    </div>
    
    {error ? (<h2 className="result">{error}</h2>) :
    (<div className="card">  


     <Card>
     <Image
      src={avatar}  
     wrapped
       ui={false} />
 
     <Card.Content>
     <Card.Header>{name}</Card.Header> 
       {/* <Card.Header>{userName}</Card.Header> */}
     </Card.Content>

     <Card.Content extra>
    
       <span className="spn">
         <Icon name='github' />
         {bio} 
       </span>
     </Card.Content>


     <Card.Content extra>
     
       <span className="spn">
         <Icon name='github' />
         {repos} repos
       </span>
     </Card.Content>

     

     <Card.Content extra>
    
       <span className="spn">
         <Icon name='github' />
         {followers} followers
       </span>
     </Card.Content>

     <Card.Content extra>
     
       <span  className="spn">
         <Icon name='github' />
         {following} following
       </span>
     </Card.Content>
    
   </Card>
  
 </div>
 ) }   
      
  
 <ParticlesBg type="ball"  config={config} bg={true} />
 
  </div>
  
  );
}

export default App;
