import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index.js'
import Navbar from './components/Navbar.vue'
import Tasks from './components/Tasks.vue'
import CreateTask from './components/CreateTask.vue'
import DeleteTask from './components/DeleteTask.vue'
import CompleteTask from './components/CompleteTask.vue'

const app = createApp(App);

app.component('Navbar', Navbar);
app.component('tasks', Tasks);
app.component('create-task', CreateTask);
app.component('delete-task', DeleteTask);
app.component('complete-task', CompleteTask);

app.use(router);

app.mount('#app');
