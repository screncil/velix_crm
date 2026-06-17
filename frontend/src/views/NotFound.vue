<template>
  <div class="h-screen flex flex-col items-center justify-center">
    <h1 class="text-5xl font-bold text-orange-500">404</h1>
    <button
      @click="goBack"
      class="mt-6 text-orange-600/30 hover:underline hover:cursor-pointer"
    >
      На попередню сторінку
    </button>
  </div>
</template>


<script setup lang='ts'>
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  router.back()
}
</script>