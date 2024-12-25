<script>
export default {
    methods: {
        async deleteTask() {
            console.log(this.taskId)
            try {
                    const response = await fetch(`http://localhost:8000/task/${this.taskId}/`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    }

                })

                console.log('deleted', this.taskId)

                if(!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`)
                }
                
                // const removedTask = await response.json()
                // console.log(removedTask)
                // this.$emit('deletingTask', removedTask)

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