<script setup lang="ts">
import ListExplorer from '@/components/ListExplorer/ListExplorer.vue';


/////////////////////
// Begin Test Area //
/////////////////////

// class input_action {
//     displayText
//     callback
//     constructor(displayText:string, callback: () => void) {
//         this.displayText = displayText;
//         this.callback =  callback;
//     }
// }
// const input_actions = [
//     new input_action("a", ()=>{console.log("hola1")}),
//     new input_action("b", ()=>{console.log("hola2")}),

// ]
// function uncb (){
//     alert('esto funko!')
// }
// let texto = ref("")

///////////////////
// End Test Area //
///////////////////

</script>

<template>

<!-- <TextInputBar :actions="input_actions" :customPlaceholder="'asd'" @submitCallback="uncb"/> -->
<ListExplorer/>
</template>