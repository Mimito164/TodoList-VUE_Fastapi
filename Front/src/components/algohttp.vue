<script setup lang="ts">
// import { useCounterStore } from '@/stores/counter';
// import { storeToRefs } from 'pinia'
import axios, { type AxiosResponse } from 'axios';
import { ref } from 'vue';

const res = ref()

const back_url = import.meta.env.BACK_URL
// const store = useCounterStore()
// const {count} = storeToRefs(store)
// const {increment} = store


async function fetchear() {
    const response = await axios.get(back_url+"/api/")
    res.value = response
}

fetchear()

</script>

<template>
    <div><button @click="fetchear">fetchear</button></div>
    <div v-if="res!=null">
        {{ res }}
    </div>
</template>