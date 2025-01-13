<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useListsStore } from '@/stores/lists';
import TodoItem from './TodoItem.vue';

// props and actions
const props = defineProps(['selectedList'])
const emit = defineEmits(['deselectList', 'renameList'])

// state
const newTodolistName = ref("")
const newItemName = ref("")

// stores
const listsStore = useListsStore()

function deleteTodolist() {
    listsStore.deleteTodolist(props.selectedList._id)
    emit('deselectList')
}

async function renameTodolist() {
    await listsStore.renameTodolist(props.selectedList._id, newTodolistName.value)
    emit('renameList', newTodolistName.value)
}

async function submitNewItem() {
    await listsStore.addTodoItem(props.selectedList._id, newItemName.value)
    newItemName.value = ""
}

watchEffect(() => {
    newTodolistName.value = props.selectedList?.name
})

</script>


<template>
<div>

    <div v-if="props.selectedList!=null">
        <div class="" :style="{display:'flex', gap: '1em', alignItems: 'center'}">
            <h3 style="flex-grow: 4;">
                <input 
                    type="text"
                    v-model="newTodolistName"
                    class="custom-input"
                    @keypress.enter="renameTodolist"
                    @focusout="renameTodolist"
                />
            </h3>
            <!-- <label for="modal_add_todoitem" class="pseudo button">➕</label> -->
            <button class="pseudo button" @click="deleteTodolist">🗑️</button>
        </div>
        <div :style="{display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '0.3em'}">
            <input 
            type="text"
            v-model="newItemName"
            placeholder="New Item Name"
            @keypress.enter="submitNewItem"
            />
            <button @click="submitNewItem" class="pseudo button">➕</button>
        </div>

        <div v-for="item in props.selectedList.todoItems.toReversed()">
            <TodoItem :listID="props.selectedList._id" :item="item"/>
        </div>
    </div>
</div>

</template>

<style scoped>

.custom-input {
    transition: all;
    border: none;
}

.custom-input:hover {
    background-color: rgba(0,0,0,0.06);
}

</style>