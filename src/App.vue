<script setup lang="ts">
import Foot from './components/Foot.vue';
import TopNav from './components/TopNav.vue';
</script>

<template>
  <div class="flex flex-col items-stretch justify-start h-full">
    <top-nav></top-nav>
    <RouterView></RouterView>
    <footer>
    <foot></foot>
  </footer>
  </div>
  
</template>

<style scoped></style>
