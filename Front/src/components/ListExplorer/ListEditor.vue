<script setup lang="ts">

const props = defineProps({
    selectedList: {type:String, required:true}
})
</script>


<template>
<div>
{{ props.selectedList }}
</div>
</template>