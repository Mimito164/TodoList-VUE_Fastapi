<script setup lang="ts">
import ListEditor from './ListEditor.vue';
import ListMenu from './ListMenu.vue';
import { ref, watch } from 'vue';
import { useUserStore } from '@/stores/users';
import { createList, fetchList, fetchLists } from '@/requests/back';


const userStore = useUserStore()
const lists = ref<any[]>([])
const selectedList= ref("")

function updateSelected(newList: string) {
    selectedList.value = newList
}


watch(()=>{return userStore.loggedUser}, async () => {
    
    if(userStore.loggedUser != null && Array.isArray(userStore.loggedUser.todolistIDs) ) {
            const element = await fetchLists(userStore.loggedUser._id) ;
            lists.value = element

    }
    else {
        lists.value = []
        selectedList.value = ""
    }
})



</script>


<template>
<div>
    <form  @submit="(e:Event)=>{
        e.preventDefault()
        const todolisName = (e.target as HTMLFormElement).elements.namedItem('todolistname') as HTMLInputElement;
        const userID = userStore.loggedUser._id;
        createList(userID, todolisName.value.toString())
    }">
        <fieldset role="group">
            <input name="todolistname" type="text" placeholder="Enter todolist name" />
            <input type="submit" value="add list" />
        </fieldset>
    </form>
    <div class="grid" :style="{gridTemplateColumns:'1fr 3fr'}">
        <ListMenu @updateSelected="updateSelected"  :lists="lists" :selectedList="selectedList"/>
    
        <ListEditor :selectedList="selectedList"/>
    </div>
</div>

    
</template>