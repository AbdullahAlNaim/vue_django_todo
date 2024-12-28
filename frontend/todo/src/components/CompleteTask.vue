<script>
export default {
    methods: {
        async completeTask(taskId) {
            try {
                const response = await fetch(`http://localhost:8000/tasks/${this.taskId}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                    },
                    body: JSON.stringify({
                        task_name: this.taskName,
                        description: this.description,
                        completed: true,
                    })
                });

                const updateTask = await response.json();
                this.$emit('updatingTask', updateTask);
                console.log('updated ', updateTask);


                if (!response.ok) {
                    if (response.status === 404) {
                        console.error('Task not found');
                    } else {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return ;
                }

                console.log('completed task: ', this.taskId);

            } catch (error) {
                console.error('found an error: ', error)
            }
        }
    },
    props: {
        taskId: Number,
        taskName: String,
        description: String,
    },
    emits: ['updatingTask']
}
</script>

<template>
    <button @click="completeTask">COMPLETE</button>
</template>