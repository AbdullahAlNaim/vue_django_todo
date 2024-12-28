<script>
</script>

<template>
    <ul>
        <router-link to="/">
            <li>Home</li>
        </router-link>
        <router-link to="/tasks">
            <li>Tasks</li>
        </router-link>
        <router-link to="/settings">
            <li>Profile</li>
        </router-link>
    </ul>
</template>

<style scoped>
body {
    background-color: blueviolet
}

ul {
    list-style-type: none;
}

li:hover {
    background-color: aquamarine;
    color: black;
}

li {
    display: inline-block;
    margin-right: 10px;
    padding: 10px;
}
</style>