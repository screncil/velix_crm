<template>
    <div class="min-h-screen xl:flex ">
        <Sidebar />
        <div
            class="flex-1 ease-in-out"
         >
            <Header />
            <div class="p-4 mx-auto max-w-(--breakpoint-2xl) md:p-6">
              <slot></slot>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import Sidebar from '../components/Sidebar.vue';
import Header from '../components/Header.vue';
</script>