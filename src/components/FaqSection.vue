<script setup lang="ts">
defineProps<{
  faqs: Array<{
    question: string;
    answer: string;
  }>;
}>();
</script>

<template>
  <div
    class="container mx-auto flex max-w-6xl flex-col items-center justify-center xl:grid xl:grid-cols-12 xl:items-start xl:justify-start"
  >
    <div class="col-span-5 flex flex-col items-center gap-2 xl:items-start">
      <div class="text-2xl font-semibold">Frequently Asked Questions</div>
      <div class="text-center xl:text-left">
        Can't find your question here? Reach out to
        <span>
          <RouterLink to="/support" class="text-sky-700 hover:underline">
            our support team
          </RouterLink>
        </span>
        .
      </div>
    </div>
    <div class="flex flex-col gap-4 px-8 xl:col-span-7">
      <div v-for="faq in faqs" :key="faq['question']" class="flex flex-col">
        <div class="text-lg font-bold">
          {{ faq.question }}
        </div>
        <div
          class="text-justify"
          v-html="faq.answer"
        ></div>
        
      </div>
    </div>
  </div>
</template>
