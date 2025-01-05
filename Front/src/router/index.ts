import { createRouter, createWebHistory } from 'vue-router'
import MiView from '@/views/MiView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MiView',
      component: MiView,
    },
    {
      path: '/asd',
      name: 'asd',
      component: MiView,
    }
  ],
})

export default router
