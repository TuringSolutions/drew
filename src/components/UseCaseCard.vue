<script setup lang="ts">
defineProps<{
  imageSrc: string;
  cardTitle: string;
  cardBody: string;
  learnMoreUrl: string;
}>();
</script>

<template>
  <div>
    <div class="flex flex-col items-stretch justify-between">
      <div class="flex flex-row items-center justify-start">
        <image :src="imageSrc" />
        <div>
          {{ cardTitle }}
        </div>
      </div>
      <div>
        {{ cardBody }}
      </div>
      <div class="flex flex-row items-stretch justify-end">Learn More &gt;</div>
    </div>
  </div>
</template>
