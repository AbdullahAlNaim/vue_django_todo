<script>
export default {
    methods: {
        async completeTask(taskId) {
            try {
                const response = await fetch(`http://localhost:8000/task/${this.taskId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
                },
                body: JSON.stringify({
                    completed: true,
                })
            });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                console.log('completed task: ', this.taskId);

            } catch (error) {
                console.error('found an error: ', error)
            }
        }
    },
    props: {
        taskId: Number,
    }
}
</script>

<template>
    <button @click="completeTask">COMPLETE</button>
</template>