<template>
    <header
        class="sticky top-0 flex w-full bg-white border-gray-200 z-99999 dark:border-gray-800 dark:bg-gray-900 lg:border-b"
    >
        <div class="flex flex-row p-4 ml-auto">
            <a href="/settings">
                <Cog6ToothIcon class="w-6 h-6 hover:text-orange-500 hover:cursor-pointer mr-3" />
            </a>
            <UserIcon class="w-6 h-6 hover:text-orange-500 hover:cursor-pointer" />
        </div>
    </header>
</template>

<script setup lang="ts">
import { UserIcon, Cog6ToothIcon } from '@heroicons/vue/24/outline';
</script>