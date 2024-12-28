import { createRouter, createWebHistory } from 'vue-router'
import.meta.env.BASE_UR

import Home from '../views/Home.vue'
import TodoTasks from '../views/TasksTodo.vue'
import Profile from '../views/ProfileSettings.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/tasks',
        name: 'TodoTasks',
        component: TodoTasks
    },
    {
        path: '/settings',
        name: 'ProfileSettings',
        component: Profile
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URO), 
    routes
})

export default router;