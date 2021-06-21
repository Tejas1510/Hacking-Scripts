import React from "react";
import UseAnimations from "react-useanimations";
import trash2 from "react-useanimations/lib/trash2";
import checkBox from "react-useanimations/lib/checkBox";

const Todo =({text,todo,todos,setTodos}) => {
    /// Events

    const deleteHandler = () => {
        setTodos(todos.filter((e1) => e1.id !== todo.id));

    }

    const completeHandler =() => {
        setTodos(todos.map(item =>{
            if(item.id === todo.id){
                return{
                    ...item, completed:!item.completed
                }
            }
            return item;
        }) )
    }
            
    return (
      <div className="todo">
        <li className={`todo-item ${todo.completed ? "completed" : ""}`}>
          {text}
        </li>
        <button onClick={completeHandler} className="complete-btn">
          <UseAnimations
            animation={checkBox}
            size={26}
            speed={1}
          />
        </button>

        <div className="trash-btn">
          <UseAnimations
            animation={trash2}
            onClick={deleteHandler}
            size={26}
            speed={0.8}
          />
        </div>
      </div>
    );

}

export default Todo; 