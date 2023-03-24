<script setup lang="ts">
defineProps<{
  currentAwsCase?: {
    caseTitle: string;
    caseBody: Array<{ subtitle: string; description: string }>;
  };
  centered: boolean;
}>();
</script>

<template>
  <div
    class="flex h-full flex-col gap-2 bg-white p-4 text-black"
    :class="[centered ? 'items-center justify-center' : '']"
  >
    <div
      v-for="subCase in currentAwsCase?.caseBody"
      :key="subCase.subtitle"
      class="contents"
    >
      <div :class="[centered ? 'text-center' : '']">
        <span class="font-bold">{{ subCase.subtitle }}</span>
        <span>- {{ subCase.description }}</span>
      </div>
      <div class="w-1/3 h-0.5 bg-sky-600" :class="[centered? 'mx-auto': '']">
      </div>
    </div>
  </div>
</template>
