<script setup lang="ts">
import { fetchUser } from "@/requests/back"


const wallets = await fetchUser()
// console.log(wallets)

</script>

<template>
<ul>
    <li v-for="wallet in wallets">{{ wallet.wallet }}</li>
</ul>
</template>