import { init } from '@web3-onboard/vue'
import injectedModule from '@web3-onboard/injected-wallets'

const injected = injectedModule()
// const infuraKey = '<INFURA_KEY>'
// const rpcUrl = `https://mainnet.infura.io/v3/${infuraKey}`

export default () => init({
  wallets: [injected],
  chains: [
    {
      id: '0x1',
      token: 'ETH',
      label: 'Ethereum Mainnet',
    //   rpcUrl
    }
  ],
  connect: {
    autoConnectLastWallet: true,
  }
})