<script>
export default {
    methods: {
        async deleteTask(taskId) {
            try {
                    const response = await fetch(`http://localhost:8000/task/${taskId}`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    }
                })

                if(!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`)
                }
                
                const removedTask = await response.json()

                this.$emit('deletingTask', removedTask)

            }
            catch (error){
                console.error('found and error: ', error)
            }
        }
    },
    emits: ['deletingTask']
}
</script>

<template>
    <button @click="deleteTask">Delete</button>
</template>