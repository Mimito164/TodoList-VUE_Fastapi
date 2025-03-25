<script setup lang="ts">
import ListEditor from './ListEditor.vue';
import ListMenu from './ListMenu.vue';
import { useUserStore } from '@/stores/users';
import { useListsStore } from '@/stores/lists';
import { ref, watchEffect } from 'vue';
// import { toast, type ToastOptions } from 'vue3-toastify';

const userStore = useUserStore()
const listsStore = useListsStore()

const selectedList = ref() 

watchEffect(() => {
    if (userStore.loggedUser == null) selectedList.value = null 
})

function selectList( list:any ) {   
    selectedList.value = list
}

function deselectList( ) {
  selectedList.value = null
}

function renameList(newName:string) {
  selectedList.value.name = newName
}
</script>


<template>
  <div :style="{padding: '1em'}">

    <div class="explorer-container" >
      <ListMenu   :lists="listsStore.lists" @selectList="selectList"  />
      <ListEditor class="list-editor"  :selectedList="selectedList" @deselectList="deselectList" @renameList="renameList"/>
    </div>
  </div>

</template>

<style scoped>
/* Fieldset styling */
.form-group {
  display: flex;
  align-items: center; /* Align items vertically in the center */
  gap: 8px; /* Add space between elements */
}

/* Input field styling */
.input-field {
  flex: 1; /* Allow input to take up remaining space */
  padding: 8px;
  border-radius: 4px;
}

/* Plus icon styling */
.pseudo.button.icon-plus {
  cursor: pointer;
  padding: 8px;
  font-size: 16px;
  text-align: center;
}

.list-editor {
  flex: 1;
}

.explorer-container  {
  display: flex;
  gap: 1em;
}
</style>