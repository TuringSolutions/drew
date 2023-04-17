<script setup lang="ts">
import RINGS from "vanta/dist/vanta.rings.min";
import { onMounted } from "vue";
onMounted(() => {
  const vantaEffect = RINGS({
    el: "#VantaHero",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    maxHeight: 10.0,
    maxWidth: 10.0,
    scale: 1.0,
    scaleMobile: 1.0,
    color: 0xff0077,
  });
});

const expertiseTiles: Array<{ title: string; body: string; svgLink: string }> =
  [
    {
      title: "Object Detection, Tracking and Labeling",
      body: "We extract insights from visual data for various needs: medical image processing, virtual try-ons, visual search, etc.",
      svgLink: "",
    },
    {
      title: "Recommender Systems Based on Visual Search",
      body: "Recommender systems for personalized offers and increased customer engagement and loyalty.",
      svgLink: "",
    },
    {
      title: "Visual Inspection for Defect Detection",
      body: "Automated visual inspection solutions to look for defects on the production line and cargo damage detection.",
      svgLink: "",
    },
    {
      title: "OCR & Data Capture",
      body: "Custom data capture and extraction solutions developed for document process automation.",
      svgLink: "",
    },
    {
      title: "Pose Estimation",
      body: "Solutions to track and analyze human movement and activity, and give feedback on user’s workouts.",
      svgLink: "",
    },
    {
      title: "Video Analysis for Automated Surveillance",
      body: "We develop video analytics solutions for violent behavior detection in real time.",
      svgLink: "",
    },
  ];

const FAQs: Array<{ question: string; answer: string }> = [
  {
    question: "How much does a typical computer vision project cost? ",
    answer:
      "An average computer vision project price starts at about 15k$ and can reach 50-100k$ or more. Since every project is one of a kind, the project price is calculated considering its scope, complexity, data available, domain, and target date.",
  },
  {
    question:
      "What technologies do you use to develop computer vision solutions?",
    answer: "OpenCV, Open3D, OpenCL, scikit-image, PyTorch, Tensorflow, CoreML",
  },
  {
    question: "What computer vision apps can you develop?",
    answer:
      "Using computer vision technology, we can solve the following tasks:",
  },
  {
    question: "How does R&D product development work?",
    answer:
      "Our business consultants and data scientists will help you figure out your project's feasibility. We'll study the requirements, and come up with the idea how to solve your business challenge with computer vision.",
  },
  {
    question: "What domains do you work with?",
    answer:
      "Retail/eCom, Wellness & Fitness, Healthcare, Logistics, Marketing & Advertising, Fintech, Entertainment and Gaming, but we are flexible in applying our computer vision expertise to solve business challenges faced by companies in other domains.",
  },
  {
    question:
      "My project requires work with sensitive data. How do you ensure data privacy?",
    answer: "We don't keep your data. Your data is processed locally.",
  },
  {
    question: "What are the key stages of a computer vision-based project?",
    answer:
      "First, we analyze the requirements and give an estimation. During the project setup, we choose the development model and build the team. We move to agile project development (progress reporting during each iteration and testing). Then we do the final testing and collect the feedback. Post-project support is offered upon the project completion.",
  },
];
</script>

<template>
  <div
    id="VantaHero"
    class="h-banner flex flex-col items-center justify-center bg-slate-700"
  >
    <div class="container flex flex-col gap-6">
      <div
        class="text-2xl font-medium uppercase text-white md:text-3xl xl:text-6xl"
      >
        Computer Vision Solutions
      </div>
      <div class="max-w-3xl text-lg text-gray-300 xl:text-2xl">
        Add value to your business with our ML algorithms for reliable computer
        vision solutions with image analysis, object detection and video
        analysis.
      </div>
    </div>
  </div>

  <section class="py-24">
    <div class="container mx-auto max-w-6xl flex flex-col items-center justify-center xl:grid  xl:grid-cols-12 xl:items-start xl:justify-start ">
      <div class="col-span-5 flex flex-col items-center xl:items-start gap-2">
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
      <div class="xl:col-span-7 flex flex-col gap-4 px-8">
        <div v-for="faq in FAQs" :key="faq['question']" class="flex flex-col">
          <div class="text-lg font-bold">
            {{ faq.question }}
          </div>
          <div class="text-justify">
            {{ faq.answer }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.h-banner {
  min-height: 60vh;
  min-height: 60dvh;
}
</style>
t
