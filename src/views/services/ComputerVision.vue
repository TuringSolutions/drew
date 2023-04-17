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

const keyBenefits: Array<{
  title: string;
  body: string;
  benefits: Array<string>;
}> = [
  {
    title: "Automate Manufacturing Parts Search and Reduce Time and Expenses",
    body: "You can't afford excessive downtime searching for a desirable product manually. A vast array of components adds to the arising difficulties. Our team is ready to help you get back up and running in no time and evade unnecessary time and money losses. An ML model analyses a picture and demonstrates the most similar ones from the database. Automating manufacturing parts search, you cut down on expenses, improve workflow efficiency, and prevent downtime.",
    benefits: [
      "Easy search for products",
      "Quick search for similar objects",
      "Downtime prevention",
    ],
  },
  {
    title: "Ensure On-Site Safety with Forklift Collision Prevention System",
    body: "With the increasing complexity of supply chain operations and forklift traffic, it becomes paramount to reduce the risks of employee injuries to a minimum. Embed our forklift accident prevention solutions to control the speed, movement, and location of your forklifts on site. Our engineers utilize high-end technologies to help you solve the most challenging forklift safety scenarios and increase employer safety. With real-time monitoring, an operator under risk receives prompt alerts in case of arising danger.",
    benefits: [
      "Safe working environment",
      "Avoiding injury payments",
      "Real-time monitoring",
    ],
  },
  {
    title:
      "Make Process-Chain Efficient with Analogue Meters Reading Automation",
    body: "Harsh working conditions and human errors make manual analogue meters reading ineffective. Here, automation is a go-to solution to exponentially reduce the number of incorrect meter readings, cut down expenses, and optimize analogue meters reading on the whole. Switch to automated analogue meter reading to increase meters reading accuracy and prevent energy fraud and electrical losses.",
    benefits: [
      "Real-time and accurate gauge measurement",
      "Saving resources",
      "Reducing fraud instances",
    ],
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

  <section class="py-12">
    <div class="container mx-auto max-w-6xl text-xl">
      Our team of experts at InData Labs helps businesses in Healthcare,
      Manufacturing, Fitness and Sports, E-commerce, Marketing and Logistics,
      and other industries solve business challenges and fuel growth with the
      help of computer vision technology. No matter what solution you need - a
      surveillance video system, building a visual inspection system, invoice
      processing app, or pose estimation implementation for enhancing your
      customer experience and automating business processes, we'll find the
      right way to address it.
    </div>
  </section>

  <section class="py-12">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center"
    >
      <div class="text-2xl font-medium uppercase">
        Computer Vision Expertise
      </div>
      <div class="py-2 text-xl">
        Our computer vision software development team builds custom solutions
        for varied use cases
      </div>
      <div class="grid grid-cols-3 items-stretch gap-4">
        <div
          v-for="tile in expertiseTiles"
          :key="tile.title"
          class="flex h-56 flex-col items-center justify-start gap-6 border border-sky-500 p-6 hover:shadow"
        >
          <div class="text-center text-xl font-medium uppercase">
            {{ tile.title }}
          </div>
          <div class="text-justify text-lg">
            {{ tile.body }}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="py-12">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center gap-6"
    >
      <div>Benefits</div>
      <div class="grid grid-rows-3 items-start justify-center gap-8">
        <template v-for="benefit in keyBenefits" :key="benefit.title">
          <div class="flex flex-col items-stretch justify-center gap-2">
            <div class="text-center text-xl font-semibold uppercase">
              {{ benefit.title }}
            </div>
            <div class="text-justify text-lg">
              {{ benefit.body }}
            </div>
            <div class="text-center text-lg font-medium">Key Benefits:</div>
            <ul class="flex flex-col items-center justify-start">
              <li
                v-for="subBenefit in benefit.benefits"
                :key="subBenefit"
                class="text-lg"
              >
                {{ subBenefit }}
              </li>
            </ul>
          </div>
        </template>
      </div>
    </div>
  </section>

  <section class="py-24">
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
