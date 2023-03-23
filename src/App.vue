<script setup lang="ts">
import Foot from './components/Foot.vue';
</script>

<template>
  <div class="flex flex-col items-stretch justify-start">
    <RouterView></RouterView>
  </div>
  <footer>
    <foot></foot>
  </footer>
</template>

<style scoped></style>
