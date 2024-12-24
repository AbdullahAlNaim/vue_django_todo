import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
// import router from './router/index.js'
import Tasks from './components/Tasks.vue'
import CreateTask from './components/CreateTask.vue'
import DeleteTask from './components/DeleteTask.vue'

const app = createApp(App);
app.component('tasks', Tasks);
app.component('create-task', CreateTask);
app.component('delete-task', DeleteTask);
// app.use(router);

app.mount('#app');
