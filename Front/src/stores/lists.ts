import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import { useUserStore } from './users'

export const useLists = defineStore('lists', () => {
    const userStore = useUserStore().loggedUser._id
    const userID = ref("")

    userID.value = userStore.loggedUser._id

    const lists = ref([])
    const selectedList = ref("")

    function fetchLists() {

    }
})

