<script setup lang="ts">

import { RouterView } from 'vue-router'
import NavBar from './components/Navbar.vue'
import { useUsersStore } from './stores/users';


// provisorio
const user = useUsersStore()

</script>

<template>
  <div class="container">
    <NavBar />
    <RouterView />
  </div>
  </template>
