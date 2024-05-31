<script setup>
import axios from 'axios'
</script>

<template>
  <div class="rectangle">
    <h1>Todo List</h1>
    <form @submit.prevent="addTodo">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="newTodo.title" required />
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" v-model="newTodo.description" required></textarea>
      </div>
      <div class="form-group">
        <label for="is_complete">Completed:</label>
        <input type="checkbox" id="is_complete" v-model="newTodo.is_complete" />
      </div>
      <button type="submit">Add Todo</button>
    </form>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <h2>{{ todo.title }}</h2>
        <p>{{ todo.description }}</p>
        <p><strong>Completed:</strong> {{ todo.is_complete ? 'Yes' : 'No' }}</p>
        <button @click="removeTodo(todo.id)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
      newTodo: {
        title: '',
        description: '',
        is_complete: false,
      }
    };
  },
  mounted() {
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/todo/');
        this.todos = response.data;
      } catch (error) {
        console.error('Error fetching todos:', error);
      }
    },
   async addTodo() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/todo/', this.newTodo);
    if (response.status === 201) { // Check if the response status is created
      this.todos.push(response.data);
      this.resetNewTodo();
    } else {
      console.error('Error adding todo: Unexpected response status', response.status);
    }
  } catch (error) {
    console.error('Error adding todo:', error);
  }
},


    async removeTodo(id) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`);
        this.todos = this.todos.filter(todo => todo.id !== id);
      } catch (error) {
        console.error('Error removing todo:', error);
      }
    },
    resetNewTodo() {
      this.newTodo = {
        title: '',
        description: '',
        is_complete: false,
        user: ''
      };
    }
  }
};
</script>

<style scoped>
.rectangle {
  width: 400px;
  min-height: 500px;
  background-color: #dceaf7; /* Light blue background */
  padding: 20px;
  border: 2px solid #3498db; /* Dark blue border */
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  width: 100%;
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: calc(100% - 20px); /* Adjusted width with padding */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button[type="submit"] {
  width: 100%;
  padding: 10px 20px;
  background-color: #3498db; /* Dark blue button color */
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

ul {
  width: 100%;
  margin-top: 20px;
  padding: 0;
}

li {
  width: 100%;
  list-style: none;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
}

</style>
