<script setup lang="ts">
import { useUserStore } from '@/stores/users'
import { useListsStore } from '@/stores/lists'

const props = defineProps(['lists'])

const emit = defineEmits(["selectList"])

const userStore = useUserStore()
const listsStore = useListsStore()


function submitNewList(e:Event){
    e.preventDefault()
    const todolisName = (e.target as HTMLFormElement).elements.namedItem('todolistname') as HTMLInputElement;
    if ( todolisName.value.toString() === "" ) {
      alert("Missing name for todolsit")
      return
    }
    if ( userStore.loggedUser == null ) {
      alert("Missing user")
      return
    }

    listsStore.createTodolist( todolisName.value.toString())
    todolisName.value = ""
}

</script>

<template>
<div :style="{display: 'flex', flexDirection: 'column'}">
    <h3 :style="{padding: '1em 0 1em 0'}">My Todolists</h3>

    <form @submit="submitNewList" class="" :style="{width: '25ch', marginBottom: '1em', paddingTop:'0.1em'}">
        <input
          name="todolistname" 
          type="text" 
          placeholder="New Todo-list name" 
          class="stack"
          autocomplete="off"
        />
    </form>


    <template v-for="list in props.lists">
        <label class="stack">
            <input name="stack" @click="emit('selectList', list)" type="radio">
            <div class="button toggle" :style="{overflow: 'hidden', textOverflow: 'ellipsis', width: '25ch', display: 'block'}">
                {{list.name}}
            </div>
        </label>
    </template>

</div>
</template>