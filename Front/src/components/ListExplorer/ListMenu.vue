<script setup lang="ts">
const props = defineProps({
    lists: {type:Array, required:true},
    selectedList: {type:String, required:true}
})

const emit = defineEmits(["updateSelected"])

function logueador(id:string) {
    emit('updateSelected', id)
    
}
</script>

<template>
<div>
    <div v-for="list in lists" role="button" :style="{padding: '4px', marginBottom: '4px'}" @click="()=>{logueador(list as string)}">{{ list }}</div>
</div>
</template>