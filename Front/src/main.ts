
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import onboardInit from '@/librarySettings/onboardInit'

import App from './App.vue'
import router from './router'

const app = createApp(App)

onboardInit();
app.use(createPinia())
app.use(router)
// app.use(
//     Vue3Toastify,
//     {
//         autoClose:3000
//     } as ToastContainerOptions
// )
app.mount('#app')
