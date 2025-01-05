<script setup lang="ts">

import { ref, toValue } from 'vue';
const contador = ref(0);
const contadorRancio = {
    nombre:contador
}

function incrementar() {
    contador.value++
}

function decrementar() {
    contador.value--
}

</script>

<template>

<div :id="String(contador)"  v-if="contador>3">contador1: {{ contador }}</div>
<div v-else>pucha</div>
<button @click="incrementar">+</button>
<button @click="decrementar">-</button>

<button @click="()=>{contadorRancio.nombre.value++}">+</button>
<div>{{ contadorRancio.nombre }}</div>
</template>