import React, { useState, useEffect } from "react";
import "./App.css";
// importing components
import Form from "./components/Form";
import TodoList from "./components/Todolist";
import styled, { ThemeProvider } from "styled-components";
import { lightTheme, darkTheme, GlobalStyles } from "./themes.js";
import { Switch as DarkModeToggle } from "antd";

const StyledApp = styled.div``;

function App() {
  // state
  const [inputText, setInputText] = useState("");
  const [todos, setTodos] = useState([]);
  const [status, setStatus] = useState("all");
  const [filteredTodos, setFilteredTodos] = useState([]);

  const filterHandeler = () => {
    switch (status) {
      case "completed":
        setFilteredTodos(todos.filter((todo) => todo.completed === true));
        break;

      case "uncompleted":
        setFilteredTodos(todos.filter((todo) => todo.completed === false));
        break;

      default:
        setFilteredTodos(todos);
        break;
    }
  };
  useEffect(() => {
    filterHandeler();
  }, [todos, status]);

  // Save Todo data to local Storage.Used to retain the todo list even after browser reload
  useEffect(() => {
    const savedData = JSON.parse(localStorage.getItem("MyKeytoGetData"));
    if (savedData) {
      setTodos(savedData);
    }
  }, []);

  //Save "todos" in json string format to local storage with key of "MyKeytoGetData"
  useEffect(() => {
    localStorage.setItem("MyKeytoGetData", JSON.stringify(todos));
  }, [todos]);

  //Dark mode logic
  const [theme, settheme] = useState("light");
  const themeToggler = () => {
    theme === "light" ? settheme("dark") : settheme("light");
  };

  return (
    <ThemeProvider theme={theme === "light" ? lightTheme : darkTheme}>
      <GlobalStyles />
      <StyledApp className="App">
        {/* Toggle Switch */}
        <div className="toggleSwitch">
          <DarkModeToggle
            checkedChildren="Dark"
            unCheckedChildren="Light"
            onChange={() => themeToggler()}
          />
        </div>
        {/* Content of ToDo List goes here 👇 */}
        <header>
          <h1> Todolist </h1>
        </header>
        <Form
          setStatus={setStatus}
          inputText={inputText}
          todos={todos}
          setTodos={setTodos}
          setInputText={setInputText}
        />
        <TodoList
          filteredTodos={filteredTodos}
          setTodos={setTodos}
          todos={todos}
        />
      </StyledApp>
    </ThemeProvider>
  );
}

export default App;
