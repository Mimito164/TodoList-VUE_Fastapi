<script setup lang="ts">
import { useListsStore } from '@/stores/lists';
import { ref } from 'vue';

const props = defineProps({
  item: {
    type: Object,
    required: true
  },
  listID: {
    type: String,
    required: true
  },
  parentID: {
      type: String,
      default: ''
    }
})

const listsStore = useListsStore()

const itemDescription = ref(props.item.description)

function wrapperDelete() {
    if (!props.parentID) {
        listsStore.removeTodoItem(props.listID, props.item._id)
    }
    else {
        listsStore.removeTodoSubItem(props.listID, props.parentID, props.item._id)
    }
}

function wrapperEdit() {
    if (!props.parentID) {
        listsStore.renameTodoItem(props.listID, props.item._id, itemDescription.value)
    }
    else {
        listsStore.renameTodoSubItem(props.parentID, props.item._id, itemDescription.value)
        // listsStore.renameSubTodoItem(props.listID, props.parentID, props.item._id, props.item.description)
    }
}

function wrapperCheckbox() {
    if (!props.parentID) {
        listsStore.toggleTodoItemDone(props.listID, props.item._id)
    }
    else {
        listsStore.toggleTodoSubItemDone(props.parentID, props.item._id)
    }
}

const newSubItemDescription = ref("")

function closeModal(modalId: string) {
    const modal = document.getElementById(modalId) as HTMLInputElement
    if (!modal) return
    modal.checked = false;
}

function openModal(modalId: string) {
    const modal = document.getElementById(modalId) as HTMLInputElement
    if (!modal) return
    modal.checked = true;
}

</script>

<template >
<div>
    <div style="display: flex; align-items: center;">
        <label class="stack" style="flex: 1;">
            <template v-if="props.item.done">
                <input type="checkbox" checked @click="wrapperCheckbox" >
            </template>
            <template v-else >
                <input type="checkbox" @click="wrapperCheckbox" >
            </template>
            <span class="checkable" ></span>
            <!-- <span class="checkable" >{{props.item.description }}</span> -->
        </label>
        <input
            class="custom-input"
            type="text"
            v-model="itemDescription"
            @keypress.enter="wrapperEdit"
            @focusout="wrapperEdit"
        />

        <button v-if="props.parentID==''"  class="pseudo button" @click="openModal('modal_todoitem'+props.item._id)">➕</button>
        <button class="pseudo button" @click="wrapperDelete">❌</button>
    </div>
    <div style="margin-left: 5%;">
        <div v-for="subitem in item.subTodoItems.toReversed()" :key="subitem._id">
            <TodoItem :listID="props.listID" :item="subitem" :parentID="props.item._id"/>
        </div>
    </div>

    <div class="modal">
        <input :id="'modal_todoitem'+props.item._id" type="checkbox" />
        <label :for="'modal_todoitem'+props.item._id" class="overlay"></label>
        <article>
            <header>
                Enter description for Sub todo-item
            </header>
            <section class="content">
                <input
                    autofocus
                    placeholder="New Sub Item Description" 
                    v-model="newSubItemDescription"
                    @keypress.enter="async()=>{
                        await listsStore.addTodoSubItem(props.listID, props.item._id, newSubItemDescription)                  
                        newSubItemDescription=''
                        closeModal('modal_todoitem'+props.item._id)
                    }"
                />
                
                <button
                    class="button success" 
                    @click="async()=>{
                        await listsStore.addTodoSubItem(props.listID, props.item._id, newSubItemDescription)                  
                        newSubItemDescription=''
                        closeModal('modal_todoitem'+props.item._id)
                    }">
                    Add
                </button>

                    <button 
                        class="button dangerous"
                        @click="closeModal('modal_todoitem'+props.item._id)"    
                    >
                        Cancel
                    </button>
                
            </section>
        </article>    
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