import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import Recipe from './Recipe';
import './App.css';

const App = () => {
  const App_ID="your api id";
  const App_KEY="your api key";

  const[recipes,setrecipes] = useState([]);
  const[search,setSearch] =useState('');
  const[query,setQuery]=useState('chicken');

  useEffect(() =>{
    getRecipes();
  }, [query]);

  const getRecipes = async ()=>{
    const response=await fetch(`https://api.edamam.com/search?q=${query}&app_id=${App_ID}&app_key=${App_KEY}`);
    const data= await response.json();
    console.log(data);
    setrecipes(data.hits);
    console.log(data.hits)
  }

  const updateSearch=e =>{
    setSearch(e.target.value);
  }

  const getSearch=e =>{
    e.preventDefault();
    setQuery(search);
    setSearch('')
  }

  return (
    <div className="App">
      <center><h1>Craving for something ? Just Search!!</h1></center>
      <form onSubmit={getSearch} className="search-form">
        <input type="text" className="search-bar" value={search} onChange={updateSearch}></input>
        <button className="search-button" type="submit">
          search
        </button>
      </form>
      <div className="recipe">
        {recipes.map(recipe =>(
          <Recipe 
          key={recipe.recipe.label}
          title={recipe.recipe.label}
          calories={recipe.recipe.calories}
          image={recipe.recipe.image}
          ingredients={recipe.recipe.ingredients}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
