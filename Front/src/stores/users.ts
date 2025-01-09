import { ref, watchEffect } from 'vue'
import { defineStore } from 'pinia'
import { fetchOrCreateUser } from '@/requests/back'
import { useWalletStore } from './wallet'

export const useUsersStore = defineStore('user', () => {
  const loggedUser = ref()
  const wallet = useWalletStore()
  
  
  watchEffect(() => {
    if (wallet.address !== "") {
        
      loggedUser.value = fetchOrCreateUser(wallet.address)
    }
    else {
        loggedUser.value = null
    }
  })
  
  return { loggedUser }
})
