//import React from 'react';
import React, { useState } from 'react';
import TodoList from './components/TodoList';
import TodoForm from './components/TodoForm';
import './App.css';

function App() {
      const [todos, setTodos] = useState([
        { complete: false, task: "Aprendendo sobre MongoDb"},
        { complete: false, task: "Criando um React para fazer App"},
        { complete: false, task: "Encontra minha chave"}
      ]);
      return (
        <div className="App">
          <TodoForm addTodo={(todo) => {
            if (todo.task.trim().length > 0) {
              setTodos([...todos, todo]);
            }
          }} />
          <TodoList todos={todos} updateTodos={(list) => { setTodos(list) }}></TodoList>
        </div>
  );
}

export default App;