<script setup lang="ts">
import { ref, Suspense } from "vue";
import WalletList from "@/components/WalletList.vue";
import { fetchOrCreateUser } from "@/requests/back";

const input_wallet = ref()

</script>

<template>
<h1>Admin</h1>
<label for="wallet">Wallet Hash</label>
<input type="text" id="wallet" v-model="input_wallet">

<button @click="() => {fetchOrCreateUser(input_wallet)}">Submmit</button>
<hr>

<Suspense>
    <WalletList />
    <template #fallback>
        <div>Loading ...</div>
    </template>
</Suspense>
</template>