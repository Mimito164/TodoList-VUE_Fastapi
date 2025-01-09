import { computed } from 'vue'
import { defineStore } from 'pinia'
import { useOnboard } from '@web3-onboard/vue'

export const useWalletStore = defineStore('wallet', () => {
  // const { wallets, connectWallet, disconnectConnectedWallet, connectedWallet } = useOnboard()
  const onboard = useOnboard()
  const address = computed(() => {
    if (onboard.connectedWallet.value) {
      return onboard.connectedWallet.value.accounts[0].address
    }
    return ""
  })

  function connectWallet() {
    onboard.connectWallet()
  }
    
  return { address, connectWallet }
})
