<template>
    {{ props.id }}
</template>

<script setup lang="ts">

import { ref, onMounted } from 'vue';

const props = defineProps({
    id: String
})

</script>