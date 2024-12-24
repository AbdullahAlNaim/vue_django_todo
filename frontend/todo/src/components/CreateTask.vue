<script>
export default {
    data () {
        return {
            formData: {
                task_name: '',
                description: '',
                completed: false,
            }
        }
    },
    methods: {
        async submitForm () {
            try {
                const response = await fetch('http://localhost:8000', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    },
                    body: JSON.stringify(this.formData)
                })

                if(!response.ok) {
                    throw new Error(`HTTP error! status ${response.status}`)
                }

                const newTask = await response.json()

                this.$emit('newTaskCreated', newTask)
                this.formData.task_name = ''
                this.formData.description = ''

            } catch (error) {
                console.error('Found error: ', error)
            }
        }
    },
    emits: ['newTaskCreated']
}
</script>

<template>
    <form @submit.prevent="submitForm">
        <input type="text" 
        v-model="formData.task_name" 
        placeholder="task name">

        <input type="text"
        v-model="formData.description"
        placeholder="description">
        <button type="submit">Add</button>
    </form>
</template>