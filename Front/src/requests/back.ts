import axios from "axios"

const BACK_URL = import.meta.env.VITE_BACK_URL

export async function fetchUser(): Promise<{id:string, wallet:string}[]> {
    try {
        const response = await axios.get(BACK_URL+"/api/users/")
        return response.data
    } catch(e) {
        console.error(e)
        return []
    }
}

export async function fetchOrCreateUser(wallet:string): Promise<{id:string, todolistIDs:Array<string>,wallet:string}> {
    const res = await axios.post(BACK_URL+"/api/user/", { wallet,  todolistIDs:[] } )
    
    return res.data
}

export async function fetchLists(userID:String) {
    const res = await axios.get(BACK_URL+"/api/todolists/"+userID+"/")
    return res.data
}


export async function fetchList(userID:String,listID:string) {
    const res = await axios.get(BACK_URL+"/api/todolists/"+userID+"/"+listID+"/")
    return res.data
}

export async function createList(user_id:string, todolist_name:string) {
    console.log(user_id, todolist_name);
    
    const res = await axios.post(BACK_URL+"/api/todolists/", { user_id, todolist_name })
    return res.data
}