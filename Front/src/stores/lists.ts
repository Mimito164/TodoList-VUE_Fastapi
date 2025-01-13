import { ref, watchEffect } from 'vue'
import { defineStore } from 'pinia'

import { useUserStore } from './users'
import { fetchLists, createList, deleteList, renameList, addItem, removeItem, toggleItemDone, renameItem, addSubItem, toggleSubItemDone, deleteSubitem, renameSubitem } from '@/requests/back'

export const useListsStore = defineStore('lists', () => {
    const userStore = useUserStore()

    const lists = ref<any[]>([])

    watchEffect(async () => {
        if(userStore.loggedUser != null) {
            lists.value = await fetchLists( userStore.loggedUser._id )
        }
        else {
            clearState()
        }
    })


    async function createTodolist(listName:string) {
        
        const createdList: any =  await createList(userStore.loggedUser._id, listName)
        lists.value.push(createdList)
    }
    
    async function deleteTodolist(listID:string) {
        lists.value = lists.value.filter(list => list._id != listID)
        await deleteList(userStore.loggedUser._id, listID)
    }

    async function renameTodolist(listID:string, newName:string) {
        let founded = lists.value.find((todolist) => {
            return todolist._id == listID
        })
        
        founded.name = newName

        await renameList(userStore.loggedUser._id, listID, newName)
    }

    async function addTodoItem(listID:string, todoItemName:string) {
        const created_item = await addItem(userStore.loggedUser._id, listID, todoItemName)
        const listIndex =lists.value.findIndex(list => list._id == listID)
        lists.value[listIndex].todoItems.push(created_item)
        return created_item
    }

    async function removeTodoItem(listID:string, itemID:string) {
        const listIndex = lists.value.findIndex(list => list._id===listID)
        const itemIndex = lists.value[listIndex].todoItems.findIndex((item:any) => item._id===itemID)
        if (itemIndex!=-1) {
            
            lists.value[listIndex].todoItems.splice(itemIndex,1)
            await removeItem(userStore.loggedUser._id,listID,itemID)
        }
    }

    async function toggleTodoItemDone(todolistID:string, todoitemID:string) {
        await toggleItemDone(todolistID, todoitemID)
        
    }

    async function renameTodoItem(todolistID:string, todoitemID:string, newName:string) {
        await renameItem(todolistID, todoitemID, newName)
        
    }

// -----------------------------------------------------------------------------------------


async function addTodoSubItem(listID:string, itemID:string, todoSubItemName:string) {
    try {
        const listIndex = lists.value.findIndex(list => list._id == listID) // found the list
        const todoItemindex = lists.value[listIndex].todoItems.findIndex((item:any) => item._id == itemID) // found the item
        const created_item = await addSubItem(listID, itemID, todoSubItemName)
        lists.value[listIndex].todoItems[todoItemindex].subTodoItems.push(created_item)
        return created_item
    } catch (error) {
        console.error(error);
    }
}

async function removeTodoSubItem(listID:string, itemID:string, subitemID: string) {
    const listIndex = lists.value.findIndex(list => list._id===listID)
    const itemIndex = lists.value[listIndex].todoItems.findIndex((item:any) => item._id===itemID)
    const subItemIndex = lists.value[listIndex].todoItems[itemIndex].subTodoItems.findIndex((subitem:any) => subitem._id===subitemID)
    if ( itemIndex!=-1 && subItemIndex!=-1 ) {
        lists.value[listIndex].todoItems[itemIndex].subTodoItems.splice(subItemIndex,1)
        await deleteSubitem(listID,itemID,subitemID)
    }
}

async function toggleTodoSubItemDone(  todoItemID:string, todoSubItemID:string) {
    await toggleSubItemDone( todoItemID, todoSubItemID)

}

async function renameTodoSubItem(todoitemID:string, todosubitemID:string, newName:string) {
    await renameSubitem(todoitemID, todosubitemID, newName)
    
}
    

    function clearState() {
        lists.value = []
    }

    return {
        lists,
        createTodolist,
        deleteTodolist,
        renameTodolist,
        addTodoItem,
        removeTodoItem,
        toggleTodoItemDone,
        renameTodoItem,
        addTodoSubItem,
        toggleTodoSubItemDone,
        removeTodoSubItem,
        renameTodoSubItem
    }
})

