<script setup lang="ts">
import { get_user } from "@/requests/back"


const wallets = await get_user()
// console.log(wallets)

</script>

<template>
<ul>
    <li v-for="wallet in wallets">{{ wallet.wallet }}</li>
</ul>
</template>