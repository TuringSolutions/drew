<script setup lang="ts">
import NET from "vanta/dist/vanta.globe.min";
import { onMounted, h, ref } from "vue";
import {
  ArrowRightIcon,
  ArrowLeftIcon,
  ArrowDownIcon,
  ChatBubbleLeftRightIcon,
  Cog8ToothIcon,
  BeakerIcon,
  CheckBadgeIcon,
  WrenchScrewdriverIcon,
} from "@heroicons/vue/20/solid";
import TypewriterText from "../../components/TypewriterText.vue";
import FaqSection from "../../components/FaqSection.vue";
onMounted(() => {
  const vantaEffect = NET({
    el: "#VantaHero",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.0,
    minWidth: 200.0,
    scale: 1.0,
    scaleMobile: 1.0,
    color: 0xb91b47,
    chaos: 10.0,
  });
});

const tiles: Array<{
  title: string;
  body: string;
  svgSource: string;
  url: string;
}> = [
  {
    title: "Machine Learning",
    body: "Our team of machine learning developers helps our clients drive business growth and expand their businesses by extracting valuable insights from unstructured data from multiple resources.",
    svgSource: "",
    url: "",
  },
  {
    title: "Business Intelligence",
    body: "We provide BI & Data Warehouse consulting services and offer Big Data analytics solutions to unlock the potential of your data available and set up efficient data management for enhanced decision-making.",
    svgSource: "",
    url: "",
  },
  {
    title: "Predictive Analysis",
    body: "Our professionals create proprietary models for personalized recommendations, churn prediction, dynamic pricing, fraud detection, sentiment analysis, and customer segmentation.",
    svgSource: "",
    url: "",
  },
  {
    title: "Natural Language Processing",
    body: "We analyze text data from social media, emails and audio to uncover audience insights. With our bespoke NLP solutions, you get to know your users better by detecting sentiment, interests, gender, etc.",
    svgSource: "",
    url: "",
  },
  {
    title: "Data Capture and OCR",
    body: "We automate document processing through data capture and & extraction. We help businesses improve accuracy, boost overall efficiency, and reduce human errors.",
    svgSource: "",
    url: "",
  },
  {
    title: "Computer Vision",
    body: "We empower your business with tech solutions for accurate pose estimation, image recognition, and visual search. We can help with its integration and customization according to your needs.",
    svgSource: "",
    url: "",
  },
];

const timelineEvents: Array<string> = [
  "Become data-driven business",
  "Enhance customer experience",
  "Predict customer churn",
  "Mitigate business risks",
  "Forecast future trends",
  "Improve work efficiency",
  "Simplify data management",
  "Increase revenues",
  "Cut down costs",
  "Improve strategic decision making",
];

const industries: Array<{ title: string; body: string }> = [
  {
    title: "Banking & Finance",
    body: "Harness AI to power smart assistants that help with enhanced decision-making, financial apps to plan budgets, score credits, and detect anomalous transactions for fraud prevention.",
  },
  {
    title: "Automotive Manufacturing",
    body: "Adopt AI solutions for smooth vehicle production. Perform complex simulations and design iterations, enable robust visual inspection and equipment defect detection with efficient AI automotive software.",
  },
  {
    title: "Supply Chain & Logistics",
    body: "Facilitate supply planning, invoice and receipt processing, automate warehouse analysis, cargo damage detection, and optimize routes.",
  },
  {
    title: "Insurance",
    body: "Manage claims with the help of AI, predict high loss claims and detect fraud claims, evaluate insurance property cost,  offer more customer-focused services.",
  },
  {
    title: "Retail & E-commerce",
    body: "Predict customer behavior with the help of your AI developer. Enable personalized recommendations, provide customer experience consulting services, increase the efficiency of in-store operations, and cut customer churn.",
  },
  {
    title: "Healthcare & Pharma",
    body: "Let medical professionals use AI-assisted analytics for more effective diagnosis, personalized treatment, and to make better data-based predictions and recommendations, allow advanced evidence analytics to meet life-saving needs.",
  },
];

const developmentProcess: Array<{
  index: number;
  title: string;
  tasks: Array<string>;
  iconHtml: any;
}> = [
  {
    index: 0,
    title: "Discovery",
    tasks: [
      "Analyze requirements",
      "Make high-level estimation",
      "Provide technology consulting",
      "Exploratory data analysis",
    ],
    iconHtml: ChatBubbleLeftRightIcon,
  },
  {
    index: 1,
    title: "Project Setup",
    tasks: [
      "Select the engagement model",
      "Build the core team",
      "Prepare a roadmap for the project",
      "Prepare tech documents",
    ],
    iconHtml: Cog8ToothIcon,
  },
  {
    index: 2,
    title: "Development",
    tasks: [
      "Use Agile development methodology",
      "Progress reporting on each iteration",
      "Perform internal and release testing",
    ],
    iconHtml: BeakerIcon,
  },
  {
    index: 3,
    title: "Live Release",
    tasks: [
      "Final testing of the complete system",
      "Solve possible issues",
      "Live release after approval",
      "Collect feedback",
    ],
    iconHtml: CheckBadgeIcon,
  },
  {
    index: 4,
    title: "Support",
    tasks: [
      "Knowledge transfer",
      "Perform continuous server monitoring",
      "Allocate team members to fix bugs and make improvements",
    ],
    iconHtml: WrenchScrewdriverIcon,
  },
];

let currentDevProcessIndex = ref<number>(0);

const setCurrentIndex = (index: number) =>
  (currentDevProcessIndex.value = index);

const FAQs: Array<{ question: string; answer: string; }> = [
  {
    question: "What is AI in software development?",
    answer:
      "AI is used in software development to help write code faster and more effectively, automate manual tasks, and speed up the testing process. Using AI in software app development, one can expect the app to be more robust, speedy, and almost error-free.",
  },
  {
    question: "How much does an app with AI cost?",
    answer:
      "Custom AI apps may cost from $15 K up to $70-100K and more. The cost usually comes from complexity, functionality, and exclusiveness.",
  },
  {
    question: "What is an AI development company?",
    answer:
      "An AI company is an AI technology vendor who has got broad expertise under their belt, an impressive project portfolio in various business domains. AI, data scientists, software engineers, quality assurance specialists can usually work on an average project.",
  },
  {
    question: "What benefits AI provides business with?",
    answer:
      "Some of the benefits of AI are: <span><ul class='list-disc'><li>Higher revenues</li> <li>reduced costs</li> <li>business process automation</li> <li>improved speed and accuracy</li> <li>simplified data management</li> <li>personalized customer experience, and</li> <li>business risks mitigation</li></ul><span>",
  },
];
</script>

<template>
  <div
    id="VantaHero"
    class="h-banner flex flex-col items-center justify-center bg-slate-700"
  >
    <div class="container flex flex-col gap-6 text-white">
      <div
        class="text-2xl font-medium uppercase text-white md:text-3xl xl:text-6xl"
      >
        AI Software Development
      </div>
      <div class="text-lg text-gray-300 xl:text-2xl">
        Custom-Built AI Software to transform your business
      </div>
    </div>
  </div>

  <section class="py-6">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center"
    >
      <div class="text-center text-xl font-medium">
        We deliver relevant and effective AI software, data science and Big data
        solutions that are uniquely tailored to your business requirements. We
        are here to help you innovate with minimal risk while maximizing better
        results.
      </div>
    </div>
  </section>

  <section class="py-6">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center gap-2"
    >
      <div class="text-2xl font-semibold">Our Expertise</div>
      <div class="text-xl">
        As an AI development agency, we always keep track of bleeding-edge
        technologies, and have developed our in-house proprietary models and
        tools to deliver benefits to our clients with ease.
      </div>
      <div class="grid grid-cols-1 gap-6 md:grid-cols-3">
        <div
          v-for="tile in tiles"
          :key="tile['title']"
          class="flex flex-col items-center gap-2 border border-slate-400 p-4 shadow-xl transition-shadow hover:border-sky-500 hover:shadow-2xl"
        >
          <div class="text-xl font-semibold">
            {{ tile.title }}
          </div>
          <div class="text-justify text-lg">
            {{ tile.body }}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="py-6">
    <div class="container mx-auto flex max-w-6xl flex-col">
      <div class="grid grid-cols-9 items-center justify-between">
        <template
          v-for="(process, index) in developmentProcess"
          :key="process.title"
        >
          <div
            class="group flex flex-col items-center transition-all hover:text-sky-500 hover:duration-200"
            :class="[index == currentDevProcessIndex ? 'text-pink-700' : '']"
            @click="() => setCurrentIndex(index)"
          >
            <component :is="process.iconHtml" class="h-8 w-8" />
            <div>{{ process.title }}</div>
            <div
              class="h-1 w-1/2 transition-all duration-200 group-hover:scale-x-125 group-hover:bg-sky-500 group-hover:duration-300"
              :class="[index == currentDevProcessIndex ? 'bg-pink-700' : '']"
            ></div>
          </div>
          <div class="flex flex-row items-center justify-center">
            <arrow-right-icon
              class="h-5 w-5"
              v-if="index < developmentProcess.length - 1"
            >
            </arrow-right-icon>
          </div>
        </template>
      </div>
      <ul class="flex h-48 flex-col justify-center gap-1 bg-black px-6">
        <div
          v-for="task in developmentProcess[currentDevProcessIndex].tasks"
          :key="task"
        >
          <li class="text-lg font-medium text-white">
            {{ task }}
          </li>
          <div class="h-0.5 w-48 bg-white"></div>
        </div>
      </ul>
    </div>
  </section>

  <section class="py-24">
    <faq-section :faqs="FAQs"></faq-section>
  </section>
  
  <section class="py-6">
    <div class="container mx-auto flex max-w-6xl flex-col">
      
    </div>
  </section>
</template>

<style>
.h-banner {
  min-height: 60vh;
  min-height: 60dvh;
}
</style>
