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
                const response = await fetch('http://localhost:8000/tasks/')
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
}
</script>

<template>
    <hr>
    <h1>Create Task</h1>
    <create-task @newTaskCreated="handleNewTask"/>
    <hr>
    <h1>Current Tasks</h1>
    <ul>
        <div v-for="task in tasks">
            <li class="single-task" 
                v-if="!task.completed">
                Task: {{ task.task_name }}
                <br>
                Description: {{ task.description }}

                <complete-task 
                :taskId="task.id"
                :taskName="task.task_name"
                :description="task.description" 
                @updatingTask="retrieve"/>

                <delete-task :taskId="task.id" @deletingTask="removeTask"/>
                <hr>
            </li>
        </div>
    </ul>
    <hr>
    <h1>Completed Tasks</h1>
    <hr>
    <ul>
        <div v-for="task in tasks">
            <li class="single-task" 
                v-if="task.completed">
                Task: {{ task.task_name }}
                <br>
                Description: {{ task.description }} 
                <br>
                Completed on: {{ task.updated_at }}
                <hr>
            </li>
        </div>
    </ul>
</template>

<style scoped>
h1, h2 {
    text-align: center;
}

.single-task:hover {
    background-color: aliceblue;
}

li {
    list-style-type: none;
}
</style>

