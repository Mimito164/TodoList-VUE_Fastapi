<script setup lang="ts">

import { RouterView } from 'vue-router'
import NavBar from './components/Navbar.vue'
import { useUserStore } from './stores/users';


// provisorio
const user = useUserStore()

</script>

<template>
  <div class="container">
    <NavBar />
    <RouterView />
  </div>
  </template>
