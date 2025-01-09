<script setup lang="ts">

import { useWalletStore } from '@/stores/wallet';

const wallet = useWalletStore()

</script>

<template>

<nav>
    <ul>
        <li>
            <h5 class="pico-color-pink-500 ">📓 Crypto TodoList</h5>
        </li>
    </ul>
    <ul>
        <li>
            <button class="" v-if="wallet.address == ''" type="button" @click="wallet.connectWallet">Conectate</button>
            <button :style="{pointerEvents: 'none'}" v-else>{{ wallet.address }}</button>
        </li>
    </ul>
</nav>

</template>