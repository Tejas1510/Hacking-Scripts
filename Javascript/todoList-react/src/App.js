import React,{useState, useEffect} from 'react';
import './App.css';
/// importingcomponents
import Form from './components/Form';
import TodoList from './components/Todolist';


function App() {


  /// state
  const [inputText,  setInputText] =useState("");
  const [todos, setTodos] = useState([]) ;
  const [status, setStatus] = useState('all');
  const [filteredTodos, setFilteredTodos] = useState([]);

   /// run once when the app start
   useEffect(() => {
     getLocalTodos();
   },[]);
   /// use Effect
   useEffect(() => {
    filterHandeler()
  }, [todos, status]);


///function
  const filterHandeler = () =>{
    switch(status){
      case 'completed':
        setFilteredTodos(todos.filter(todo => todo.completed === true));
        break;

      case 'uncompleted':
        setFilteredTodos(todos.filter(todo => todo.completed === false));
        break;

      default:
        setFilteredTodos(todos);
        break;
    }

  };

  // save to local
  const saveLocalTodos = () => {
      localStorage.setItem("todos", JSON.stringify([]));

  };

  const getLocalTodos = () => {

    if(localStorage.getItem("todos") === null){
      localStorage.setItem("todos", JSON.stringify([]));

    }else{
    let todoLocal =  JSON.parse(localStorage.getItem("todos"));
    setTodos(todoLocal);
    }

  };

  return (
    <div className="App">
    <header>
      <h1> Todolist </h1>
      </header>
      <Form  setStatus={setStatus} inputText={inputText} todos ={todos} setTodos={setTodos} setInputText={setInputText}/>
      <TodoList filteredTodos = {filteredTodos} setTodos={setTodos} todos={todos}/>
    </div> 
  );
} 

export default App;
 