<script>
export default {
    data () {
        return {
            tasks: [],
        }
    },
    methods: {
        async retrieve () {
            try {
                const response = await fetch('http://localhost:8000/')
                const data = await response.json()
                this.tasks = data
            } catch (error) {
                console.error('Error found: ', error)
            }
            
        },
        handleNewTask(newTask) {
            this.tasks.push(newTask);
        },
        removeTask(removingTask) {
            // bad performance for larger arrays 
            // this.tasks = this.tasks.filter(task => task.id !== removingTask.id)

            // better for performance
            const index = this.tasks.findIndex(task => task.id === removingTask.id);
            if (index > -1) {
                const newTaskList = [...this.tasks];
                newTaskList.splice(index, 1);
                this.tasks = newTaskList;
            } else {
                console.warn('Task ID ', removingTask.id, ' not found');
            }
            
        }
    },
    mounted () {
        this.retrieve();
    },
    emit: ['taskIdentifier']
}
</script>


<template>
    <h1>Tasks</h1>
    <create-task @newTaskCreated="handleNewTask"/>
    <hr>
    <ul>
        <div v-for="task in tasks">
            <li v-if="!task.completed">
                Task: {{ task.task_name }}
                <br>
                Description: {{ task.description }}
                <delete-task :taskId="task.id" @deletingTask="removeTask"/>
                <hr>
            </li>
        </div>
    </ul>
</template>

