<script setup lang="ts">
import { UserCircleIcon } from "@heroicons/vue/20/solid";
defineProps<{
  imageSrc: string;
  authorName: string;
  designation: string;
  company: string;
  testimonialBody: string;
}>();
</script>

<template>
  <div
    class="flex flex-col-reverse items-center justify-center gap-6 rounded-3xl border bg-white p-10 shadow-inner md:flex-row xl:gap-12"
  >
    <div class="flex flex-col items-center justify-center">
      <image :src="imageSrc" alt="" v-if="imageSrc != ''"></image>
      <UserCircleIcon v-else class="h-20 w-20"></UserCircleIcon>
      <div class="text-center font-semibold uppercase">
        {{ authorName }}
      </div>
      <div class="text-center">
        {{ designation }}
      </div>
      <div class="text-center">
        {{ company }}
      </div>
    </div>
    <div>
      <blockquote
        class="text-center text-xl font-semibold leading-8 md:text-left"
      >
        {{ testimonialBody }}
      </blockquote>
    </div>
  </div>
</template>
