<script setup lang="ts">
import TestimonialCard from "../components/TestimonialCard.vue";
import HelpCase from "../components/HelpCase.vue";
import {
  ArrowSmallRightIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  ChevronDoubleRightIcon,
  ChevronDoubleDownIcon,
  UserIcon,
  BuildingOfficeIcon,
  AtSymbolIcon,
  EnvelopeIcon,
  PhoneIcon,
} from "@heroicons/vue/20/solid";

import { computed, onMounted, ref } from "vue";
import NET from "vanta/dist/vanta.net.min";
import AwsCard from "../components/AwsCard.vue";

onMounted(() => {
  const vantaEffect = NET({
    el: "#VantaHero",
    mouseControls: true,
    touchControls: true,
    gyroControls: true,
    scale: 1.0,
    scaleMobile: 1.0,
  });
});

const VantaHero = ref();

interface Testimonial {
  imageSrc: string;
  authorName: string;
  designation: string;
  company: string;
  testimonialBody: string;
}

interface AWSUseCase {
  caseTitle: string;
  caseBody: Array<{ subtitle: string; description: string }>;
}

const Testimonials: Array<Testimonial> = [
  {
    imageSrc: "",
    authorName: "John Doe",
    designation: "CEO",
    company: "AILabs",
    testimonialBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
  },
  {
    imageSrc: "",
    authorName: "Jane Doe",
    designation: "CTO",
    company: "AILabs",
    testimonialBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
  },
  {
    imageSrc: "",
    authorName: "John Doe",
    designation: "CEO",
    company: "AILabs",
    testimonialBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
  },
  {
    imageSrc: "",
    authorName: "Jane Doe",
    designation: "CTO",
    company: "AILabs",
    testimonialBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
  },
];

const useCases: Array<{ title: string; subtitle: string; url: string }> = [
  {
    title: "Big Data Analytics",
    subtitle: "Enhance your data analytics",
    url: "/",
  },
  {
    title: "Predictive Analysis",
    subtitle: "Predict churn to prevent cost overrun",
    url: "/",
  },
  {
    title: "Natural Language Processing",
    subtitle: "Better understand your brand perception",
    url: "/",
  },
  {
    title: "Data Capture and OCR",
    subtitle: "Enhance accuracy and eliminate errors",
    url: "/",
  },
];

const HelpCases: Array<{ caseTitle: string; caseBody: string; url: string }> = [
  {
    caseTitle: "PoC of an AI-Based Solution",
    caseBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
    url: "/",
  },
  {
    caseTitle: "MVP of an AI-Based Product",
    caseBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
    url: "/",
  },
  {
    caseTitle: "AI-Driven Mobile/Web App Development",
    caseBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
    url: "/",
  },
  {
    caseTitle: "ML Consulting",
    caseBody:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo expedita voluptas culpa sapiente alias molestiae. Numquam corrupti in laborum sed rerum et corporis.",
    url: "/",
  },
];

const AWSUseCases: Array<AWSUseCase> = [
  {
    caseTitle: "Improve Customer Experience",
    caseBody: [
      {
        subtitle: "AWS Personalize",
        description: "Recommendation, Personalization",
      },
      {
        subtitle: "AWS Kendra",
        description:
          "Enhance web & apps with NLP to help users find what they search for",
      },
      {
        subtitle: "AWS Connect",
        description: "Contact center to support millions of customers",
      },
    ],
  },
  {
    caseTitle: "Data Extraction & Analysis",
    caseBody: [
      {
        subtitle: "AWS Comprehend",
        description:
          "Sentiment analysis, Topic modelling, Key-phrase extraction, Entity detection, Classification",
      },
      {
        subtitle: "AWS Comprehend Medical",
        description: "Extract information from unstructured medical text",
      },
      {
        subtitle: "AWS Textract",
        description:
          "Document extraction, Document redaction, Table extraction",
      },
    ],
  },
  {
    caseTitle: "Computer Vision",
    caseBody: [
      {
        subtitle: "AWS Rekognition",
        description:
          "Object detection, Text detection, Image moderation, Activity detection",
      },
      {
        subtitle: "AWS Lookout for Vision",
        description:
          "Detect defects, Automate inspection, Identify vehicle & structure damage",
      },
    ],
  },
  {
    caseTitle: "Language AI",
    caseBody: [
      {
        subtitle: "AWS Lex",
        description: "Conversational chatbots, BI chatbots",
      },
      {
        subtitle: "AWS Transcribe",
        description:
          "Speech-to-text, Create transcripts, Content redaction, Vocabulary filtering",
      },
      {
        subtitle: "AWS Polly",
        description: "Text-to-speech, Text dictation",
      },
    ],
  },
  {
    caseTitle: "Business metrics",
    caseBody: [
      {
        subtitle: "AWS Forecast",
        description:
          "Forecast business outcomes, Retail forecasting, Demand forecasting",
      },
      {
        subtitle: "AWS Fraud Detector",
        description:
          "Identify suspicious online payments, Detect new account fraud, Prevent loyalty program abuse",
      },
      {
        subtitle: "AWS Lookout for Metrics",
        description:
          "Detect anomalies in business metrics and identify their root cause, Understand churn & retention, Optimize your digital ad spend, Boost user engagement",
      },
    ],
  },
];

let currentAWSCase = ref<AWSUseCase | null>();

const toggleAWSCase = (index: number) => {
  if (currentAWSCase.value?.caseTitle == AWSUseCases[index].caseTitle) {
    currentAWSCase.value = null;
    return;
  }
  currentAWSCase.value = AWSUseCases[index];
};

let centerTestimonialIndex = ref(0);

let centerTestimonial = computed<Testimonial>(() =>
  centerTestimonialIndex.value < Testimonials.length
    ? (Testimonials.at(
        centerTestimonialIndex.value % Testimonials.length
      ) as Testimonial)
    : Testimonials[centerTestimonialIndex.value % Testimonials.length]
);

const turnTestimonialsLeft = () => {
  centerTestimonialIndex.value = centerTestimonialIndex.value - 1;
};

const turnTestimonialsRight = () => {
  centerTestimonialIndex.value = centerTestimonialIndex.value + 1;
};
</script>

<template>
  <div
    id="VantaHero"
    class="hero flex flex-col items-center justify-center gap-24 bg-slate-900"
  >
    <div class="flex flex-col items-center justify-center gap-3 px-6 xl:px-8">
      <div
        class="text-3xl font-medium uppercase text-white md:text-5xl xl:text-8xl"
      >
        Big on Data Science & AI
      </div>
      <div class="text-center text-xl text-gray-300 xl:text-3xl">
        Empowering your business needs with Data Science and Technology
      </div>
    </div>

    <button
      type="button"
      class="focus-visible:outline-3 inline-flex items-center bg-gray-100 p-4 text-xl font-semibold text-gray-900 shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-stone-400 xl:p-6 xl:text-3xl"
    >
      <div class="uppercase">Book a free consultation</div>
      <arrow-small-right-icon class="-mr-2 h-10 w-10" aria-hidden="true" />
    </button>
  </div>

  <section class="bg-slate-700">
    <div
      class="grid grid-cols-1 divide-y px-4 md:grid-cols-2 md:divide-y-0 md:p-4 xl:grid-cols-4 xl:divide-x xl:px-0 xl:py-6"
    >
      <div
        v-for="useCase in useCases"
        :key="useCase.title"
        class="flex h-24 flex-col items-center justify-center xl:h-36"
      >
        <router-link
          to="/"
          class="focus-visible:outline-3 ease-in-out hover:scale-105 hover:transition hover:duration-200 focus-visible:outline focus-visible:outline-stone-400"
        >
          <div
            class="text-center text-xl font-semibold uppercase text-white xl:text-3xl"
          >
            {{ useCase.title }}
          </div>
          <div class="text-md text-center font-medium text-gray-300">
            {{ useCase.subtitle }}
          </div>
        </router-link>
      </div>
    </div>
  </section>

  <section>
    <div
      class="grid grid-cols-1 justify-items-stretch gap-8 py-8 xl:grid-cols-11 xl:gap-0 xl:py-12"
    >
      <div
        class="flex flex-col items-center justify-center text-black xl:col-span-4 xl:col-start-2 xl:items-end"
      >
        <div
          class="text-center text-2xl font-medium uppercase xl:text-right xl:text-4xl"
        >
          Trusted by<br />
          innovative companies
        </div>
      </div>
      <div
        class="flex flex-row flex-wrap items-center justify-center gap-6 xl:col-span-4 xl:col-start-7"
      >
        <image class="w-80" src="/pngwing.com.png"> </image>
        <image class="w-64" src="/pngwing.com.png"> </image>
        <image class="w-64" src="/pngwing.com.png"> </image>
        <image class="w-64" src="/pngwing.com.png"> </image>
        <image class="w-80" src="/pngwing.com.png"> </image>
        <image class="w-64" src="/pngwing.com.png"> </image>
        <image class="w-64" src="/pngwing.com.png"> </image>
        <image class="w-80" src="/pngwing.com.png"> </image>
      </div>
    </div>
  </section>

  <section class="bg-black text-white">
    <div
      class="grid grid-cols-1 justify-items-stretch gap-8 py-8 xl:grid-cols-11 xl:gap-0 xl:py-12"
    >
      <div
        class="flex flex-col items-center justify-center xl:col-span-4 xl:col-start-2 xl:items-end"
      >
        <div
          class="text-center text-2xl font-medium uppercase xl:text-right xl:text-4xl"
        >
          Let our clients<br />
          do the talking
        </div>
      </div>
      <div
        class="flex flex-row items-center justify-center gap-3 xl:col-span-4 xl:col-start-7 xl:justify-between"
      >
        <chevron-left-icon
          class="h-32 cursor-pointer"
          @click="turnTestimonialsLeft"
        ></chevron-left-icon>

        <testimonial-card
          class="testimonial-card bg-white text-black"
          :image-src="centerTestimonial.imageSrc"
          :key="centerTestimonial.authorName"
          :author-name="centerTestimonial.authorName"
          :designation="centerTestimonial.designation"
          :company="centerTestimonial.company"
          :testimonial-body="centerTestimonial.testimonialBody"
        />

        <chevron-right-icon
          class="h-32 cursor-pointer"
          @click="turnTestimonialsRight"
        ></chevron-right-icon>
      </div>
    </div>
  </section>

  <section>
    <div
      class="grid grid-cols-11 justify-items-stretch gap-8 py-8 xl:gap-12 xl:py-12"
    >
      <div
        class="col-span-9 col-start-2 text-center text-2xl font-medium uppercase xl:text-4xl"
      >
        How we can help you
      </div>
      <div class="col-span-9 col-start-2 grid grid-cols-1 gap-6 md:grid-cols-2">
        <help-case
          v-for="helpCase in HelpCases"
          :case-title="helpCase.caseTitle"
          :case-body="helpCase.caseBody"
          :url="helpCase.url"
        ></help-case>
      </div>
    </div>
  </section>

  <section class="bg-black text-white">
    <div class="grid grid-cols-11 gap-y-8 py-8 xl:py-12">
      <div class="col-span-7 col-start-3 text-center text-xl">
        Being a leading data science company, we help our clients extract
        valuable business insights from their data to better understand their
        audience, forecast demand, reduce risks, prevent cost overruns, and much
        more. We use different tools and AI services, including AWS
      </div>

      <div class="col-span-7 col-start-3 xl:hidden">
        <div class="flex flex-col items-center gap-4 bg-slate-800 p-6">
          <div
            v-for="(awsCase, index) in AWSUseCases"
            class="flex flex-col gap-2"
          >
            <button @click="() => toggleAWSCase(index)">
              <div class="flex flex-row items-center justify-center">
                <div class="text-lg font-medium uppercase">
                  {{ awsCase.caseTitle }}
                </div>
                <chevron-double-down-icon
                  class="h-6 text-white"
                  v-if="currentAWSCase?.caseTitle == awsCase.caseTitle"
                ></chevron-double-down-icon>
              </div>
            </button>
            <div v-show="currentAWSCase?.caseTitle == awsCase.caseTitle">
              <aws-card :centered="true" :current-aws-case="awsCase">
              </aws-card>
            </div>
          </div>
        </div>
      </div>

      <div class="col-span-7 col-start-3 hidden xl:block">
        <div
          class="grid grid-flow-dense grid-cols-5 grid-rows-5 gap-y-2 gap-x-6 bg-slate-800 p-6"
        >
          <button
            v-for="(awsCase, index) in AWSUseCases"
            :key="awsCase.caseTitle"
            class="col-span-2 col-start-1"
            @click="() => toggleAWSCase(index)"
          >
            <div class="flex flex-row items-center justify-end gap-2">
              <div class="text-right text-lg font-semibold">
                {{ awsCase.caseTitle }}
              </div>
              <div>
                <chevron-double-right-icon
                  class="h-4 text-white transition ease-linear"
                  :class="[
                    currentAWSCase?.caseTitle == awsCase.caseTitle
                      ? 'opacity-100'
                      : 'opacity-0',
                  ]"
                ></chevron-double-right-icon>
              </div>
            </div>
          </button>
          <div class="col-span-full col-start-3 row-span-full h-56">
            <aws-card
              :centered="false"
              :current-aws-case="currentAWSCase as AWSUseCase"
              v-show="currentAWSCase != null"
            ></aws-card>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="grid grid-cols-11 justify-items-stretch gap-4 py-8 xl:py-12">
      <div
        class="col-span-9 col-start-2 flex flex-col text-center text-2xl font-medium uppercase xl:text-4xl"
      >
        <div class="text-center text-2xl font-medium uppercase xl:text-4xl">
          Get Started with Data Science Today
        </div>
      </div>
      <div class="col-span-7 col-start-3 md:col-span-3 md:col-start-3">
        <div class="flex h-full w-full flex-row">
          <div class="flex aspect-square items-center justify-center bg-black">
            <user-icon class="h-6 w-6 text-white"></user-icon>
          </div>
          <label for="sendername" class="sr-only">Name</label>
          <input
            id="sendername"
            type="text"
            class="w-full border-2 border-black p-2"
            placeholder="Name"
          />
        </div>
      </div>
      <div class="col-span-7 col-start-3 md:col-span-4 md:col-start-6">
        <div class="flex h-full w-full flex-row">
          <div class="flex aspect-square items-center justify-center bg-black">
            <building-office-icon
              class="h-6 w-6 text-white"
            ></building-office-icon>
          </div>
          <label for="companyname" class="sr-only">Company Name</label>
          <input
            id="companyname"
            type="text"
            class="w-full border-2 border-black p-2"
            placeholder="Company Name"
          />
        </div>
      </div>
      <div class="col-span-7 col-start-3 md:col-span-4 md:col-start-3">
        <div class="flex h-full w-full flex-row">
          <div class="flex aspect-square items-center justify-center bg-black">
            <at-symbol-icon class="h-6 w-6 text-white"></at-symbol-icon>
          </div>
          <label for="senderemail" class="sr-only">Email ID</label>
          <input
            id="senderemail"
            type="email"
            class="w-full border-2 border-black p-2"
            placeholder="Email ID"
          />
        </div>
      </div>
      <div class="col-span-7 col-start-3 md:col-span-3 md:col-start-7">
        <div class="flex h-full w-full flex-row">
          <div class="flex aspect-square items-center justify-center bg-black">
            <phone-icon class="h-6 w-6 text-white"></phone-icon>
          </div>
          <label for="senderphone" class="sr-only">Phone Number</label>
        <input
          id="senderphone"
          class="w-full border-2 border-black p-2"
          type="tel"
          placeholder="Phone Number"
        />
        </div>
      </div>
      <div class="col-span-7 col-start-3">
        <label for="messagebody" class="sr-only">Message</label>
        <textarea
          id="messagebody"
          type="email"
          class="h-36 w-full border-2 border-black p-2"
          placeholder="Message"
        ></textarea>
      </div>
      <div class="col-span-7 col-start-3">
        <button class="block w-full bg-black p-4 font-semibold text-white">
          SUBMIT
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  height: 100vh;
  height: 100dvh;
}

.testimonial-card {
  min-height: 20em;
}
</style>
