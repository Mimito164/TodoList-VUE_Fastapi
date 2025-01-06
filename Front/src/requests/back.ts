import axios from "axios"
import { isExportAssignment } from "typescript"

const BACK_URL = import.meta.env.VITE_BACK_URL

export async function get_user(): Promise<{id:string, wallet:string}[]> {
    try {
        const response = await axios.get(BACK_URL+"/api/users")
        return response.data
    } catch(e) {
        console.error(e)
        return []
    }
}

export async function create_user(wallet:string): Promise<{id:string, wallet:string}> {
    const res = await axios.post(BACK_URL+"/api/user", { wallet, id:"" } )
    return res.data
}

export async function delete_user() {
    
}