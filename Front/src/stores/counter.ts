import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  
  const doubleCount = computed(() => {return count.value * 2})
  const doubleDoubleCount = computed(() => {return doubleCount.value * 2})

  
  function increment() {
    count.value++
  }

  return { count, doubleCount, doubleDoubleCount, increment }
})
