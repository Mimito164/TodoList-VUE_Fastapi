<script setup lang="ts">

import { useWalletStore } from '@/stores/wallet';

const wallet = useWalletStore()

</script>

<template>

<div class="navWrapper">
    <nav class="demo" style="height: 3em;">
        <a href="#" class="brand">
            <span>📌 Crypto TodoList</span>
        </a>
        <div class="menu">
            <button  v-if="wallet.address == ''" @click="wallet.connectWallet">Connect</button>
            <button :style="{pointerEvents: 'none'}" v-else>{{ wallet.address }}</button>

        </div> 
    </nav>
</div>


</template>

<style scoped>
.navWrapper {
    overflow: hidden;
    height: 3em;
}
</style>