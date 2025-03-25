import axios from "axios"

const BACK_URL = import.meta.env.VITE_BACK_URL

export async function fetchUser(): Promise<{id:string, wallet:string}[]> {
    try {
        const response = await axios.get("/api/users/")
        return response.data
    } catch(e) {
        console.error(e)
        return []
    }
}

export async function fetchOrCreateUser(wallet:string): Promise<{id:string, todolistIDs:Array<string>,wallet:string}> {
    const res = await axios.post("/api/user/", { wallet,  todolistIDs:[] } )
    
    return res.data
}

export async function fetchLists(userID:String) {
    const res = await axios.get("/api/todolists/"+userID+"/")
    return res.data
}


export async function fetchList(userID:String,listID:string) {
    const res = await axios.get("/api/todolists/"+userID+"/"+listID+"/")
    return res.data
}

export async function createList(user_id:string, todolist_name:string) {
    
    const res = await axios.post("/api/todolists/", { user_id, todolist_name })
    return res.data
}

export async function deleteList(user_id:string, todolist_id:string) {
    const res = await axios.delete("/api/todolists/"+user_id+"/"+todolist_id+"/")
    return res.data
}

export async function renameList(user_id:string, todolist_id:string, todolist_name:string) {
    const res = await axios.put("/api/todolists/",{user_id, todolist_id, todolist_name})
    return res.data
}

export async function addItem(user_id:string, todolist_id:string, todoItemDescription:string) {
    
    const todoItemObject = {
        description:todoItemDescription,
        subTodoItems:[],
        done:false
    }
    const res = await axios.put("/api/todolists/", {user_id, todolist_id, "todo_item":todoItemObject})
    
    return res.data
}

export async function removeItem(user_id:string, todolist_id:string, todo_item_id:string) {
    const queryparams = [user_id,todolist_id,todo_item_id].join("/")
    
    try {
        const res = await axios.delete("/api/todolists/todoitems/"+queryparams+"/")
    }
    catch (e) {
        console.error("error",e)
    }
    
    // return res.data
}

export async function toggleItemDone(listID:string, itemID:string) {
    try {
        const body = {
            "list_id":listID,
            "item_id": itemID
          }
        const res = await axios.put("/api/todolists/todoitems/done/",body)
    } catch (error) {
       console.error("errrror", error) 
    }
}


export async function renameItem(listID:string, itemID:string, itemNewName:string) {
    try {
        const body = {
            "list_id":listID,
            "item_id": itemID,
            "description":itemNewName
        }
        const res = await axios.put("/api/todolists/todoitems/rename/",body)
    } catch (error) {
        console.error(error);
    }
}

// ------------------------------------------------------------------------------------------

export async function addSubItem(listID:string, itemID:string, todoSubItemName:string) {
    const body = {
        "list_id":listID,
        "item_id": itemID,
        "description":todoSubItemName
    }
    
    try {
        const res = await axios.post("/api/todolists/todoitems/subtodoitems/", body)
        return res.data
    } catch (error) {
        console.error(error);
        
    }
}

export async function toggleSubItemDone(item_id:string, subitem_id:string) {
    const body = {
        item_id,
        subitem_id
    }
    try {
        const res = await axios.put("/api/todolists/todoitems/subtodoitems/done/", body)

    }
    catch (error){
        console.error(error)
    }
}
// item_id:str
// subitem_id:str
// description: Optional[str] = Field(default="")

export async function renameSubitem(item_id:string, subitem_id:string, description:string) {
    const body = {
        item_id,
        subitem_id,
        description
    }
    try {
        await axios.put("/api/todolists/todoitems/subtodoitems/rename/", body)
    } catch (e) {
        console.error(e);
        
    }
    
}
export async function deleteSubitem(list_id:string, item_id:string, subitem_id:string) {
    const queryparams = [list_id,item_id,subitem_id].join("/")
    
    try {
        const res = axios.delete("/api/todolists/todoitems/subtodoitems/"+queryparams+"/")
    } catch (error) {
        console.error(error);
        
    }
}