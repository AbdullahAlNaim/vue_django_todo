<script>
export default {
    methods: {
        async getTask() {
            try {
                const response = await fetch(`http://localhost:8000/task/${this.taskId}/`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    }
                })

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`)
                }

                const removingTask = await response.json();
                this.$emit('deletingTask', removingTask)
                console.log('deleted', removingTask)

            } catch (error) {
                console.error('found and error: ', error);   
            }
        },
        async deleteTask() {
            
            this.getTask();

            try {
                    const response = await fetch(`http://localhost:8000/task/${this.taskId}/`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    }
                })

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`)
                }

            }
            catch (error){
                console.error('found and error: ', error)
            }
        },
        speak() {
            console.log(this.taskId);
        }
    },
    emits: ['deletingTask'],
    props: {
        taskId: Number,
    },
}
</script>

<template>
    <button @click="deleteTask">Delete</button>
</template>