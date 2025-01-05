<script setup lang="ts">
import { useCounterStore } from '@/stores/counter';
import { storeToRefs } from 'pinia'


const store = useCounterStore()
const {count} = storeToRefs(store)
const {increment} = store

</script>

<template>
    <div>
        La puta: {{ count }}
    </div>
    <div>
        <button @click="increment">+</button>
    </div>
</template>