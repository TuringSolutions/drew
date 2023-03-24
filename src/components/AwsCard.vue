<script setup lang="ts">
defineProps<{
  currentAwsCase?: {
    caseTitle: string;
    caseBody: Array<{ subtitle: string; description: string }>;
  }, centered: boolean
}>();
</script>

<template>
  <div class="flex flex-col gap-4 h-full bg-white text-black divide-y p-4" :class="[centered? 'items-center justify-center' : '']">
    <div v-for="subCase in currentAwsCase?.caseBody" :key="subCase.subtitle" :class="[centered? 'text-center' : '']">
      <span class="font-bold">{{ subCase.subtitle }}</span>
      <span>- {{ subCase.description }}</span>
    </div>
  </div>
</template>
