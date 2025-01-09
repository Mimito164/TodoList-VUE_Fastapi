import { ref, watchEffect } from 'vue'
import { defineStore } from 'pinia'
import { fetchOrCreateUser } from '@/requests/back'
import { useWalletStore } from './wallet'

export const useUserStore = defineStore('user', () => {
  const loggedUser = ref()
  const wallet = useWalletStore()
  
  
  watchEffect(async () => {
    if (wallet.address !== "") {
       
      loggedUser.value = await fetchOrCreateUser(wallet.address)
    }
    else {
        loggedUser.value = null
    }
  })
  
  return { loggedUser }
})
