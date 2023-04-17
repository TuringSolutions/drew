<script setup lang="ts">
import { UserCircleIcon, ChevronRightIcon } from "@heroicons/vue/20/solid";
import NET from "vanta/dist/vanta.net.min";
import { onMounted } from "vue";
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
    points: 9.0,
    maxDistance: 14.0,
    spacing: 20.0,
    backgroundColor: 0xf1b2f,
  });
});

const clientReasons: Array<{
  svgLink: string;
  title: string;
  description: string;
}> = [
  {
    svgLink: "",
    title: "Since 2014",
    description:
      "We are one of the leading companies with 7+ years of experience in Big Data, Machine Learning and Artificial Intelligence.",
  },
  {
    svgLink: "",
    title: "Global Experience",
    description:
      "We have a solid track record of successful Big Data and AI projects completed for a variety of companies all over the world and multiple industries.",
  },
  {
    svgLink: "",
    title: "Value for Results",
    description:
      "Our highly qualified team will take care of all your data needs ensuring high accuracy and quick turnaround.",
  },
  {
    svgLink: "",
    title: "Favorable/Convenient Terms of Cooperation",
    description:
      "We are always ready to offer such terms of cooperation that will be the most suitable for your project needs and goals. T&M and Fixed Price models are offered.",
  },
  {
    svgLink: "",
    title: "High-Quality Results",
    description:
      "Our focus is on compelling results. We build our solutions to address your unique requirements and business-specific challenges.",
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
        About Us
      </div>
      <div class="text-lg text-gray-300 xl:text-2xl">
        We are a leading data science firm and AI-powered solutions provider
        with our own R&D center
      </div>
    </div>
  </div>
  <section class="py-6">
    <div
      class="container mx-auto flex flex-row items-center justify-center gap-6"
    >
      <div class="flex w-1/2 flex-col items-start justify-start">
        <div class="text-xl font-semibold text-black">Established in 2014</div>
        <div class="text-base font-medium">
          Our firm was was founded in 20xx by John Doe, who brought years of
          experience in big data analytics to a new venture to make it a
          success.
        </div>
      </div>
      <div class="flex flex-col items-center justify-center">
        <user-circle-icon class="h-24 w-24 text-black"></user-circle-icon>
        <div class="text-center">John Doe</div>
      </div>
    </div>
  </section>
  <section class="py-6">
    <div class="container mx-auto grid grid-flow-row gap-6 px-6 xl:grid-cols-4">
      <div
        class="flex flex-col items-center justify-center border-blue-400 p-6 shadow-inner shadow-slate-500"
      >
        <div class="pb-2 text-center text-xl font-semibold uppercase">
          Employees
        </div>
        <div class="text-center text-6xl font-black">80</div>
        <div class="text-center text-xl font-bold">We are</div>
        <div class="text-center">
          Data Scientists, Engineers, Architects, Analysts, Designers
        </div>
        <div class="flex flex-row items-center justify-between pt-3">
          <div class="text-lg">Learn More</div>
          <chevron-right-icon
            class="-mb-1 h-5 w-5 text-black"
          ></chevron-right-icon>
        </div>
      </div>
      <div
        class="flex flex-col items-center justify-between p-6 shadow-inner shadow-slate-500"
      >
        <div class="pb-2 text-center text-xl font-semibold uppercase">
          Projects Delivered
        </div>
        <div class="text-center text-6xl font-black">150</div>
        <div class="text-center text-xl font-bold">Clients Geography</div>
        <div class="text-center">USA, UK, EU, Japan</div>
        <div class="flex flex-row items-center justify-center pt-3">
          <div class="text-lg">Learn More</div>
          <chevron-right-icon
            class="-mb-1 h-5 w-5 text-black"
          ></chevron-right-icon>
        </div>
      </div>
      <div
        class="flex flex-col items-center justify-between p-6 shadow-inner shadow-slate-500"
      >
        <div class="pb-2 text-center text-xl font-semibold uppercase">
          Key Industries
        </div>
        <div class="text-center text-6xl font-black">5+</div>
        <div class="text-center text-xl font-bold">Industry Focus</div>
        <div class="text-center">
          Marketing & Advertising, E-commerce, Supply Chain & Logistics Fintech,
          Digital Health IoT
        </div>
      </div>
      <div
        class="flex flex-col items-center justify-between p-6 shadow-inner shadow-slate-500"
      >
        <div class="pb-2 text-center text-xl font-semibold uppercase">
          Locations
        </div>
        <div class="text-center text-6xl font-black">3</div>
        <div class="text-center text-xl font-bold">Our Offices</div>
        <div class="text-center">All over the world</div>
        <div class="flex flex-row items-center justify-center pt-3">
          <div class="text-lg">Contact Us</div>
          <chevron-right-icon
            class="-mb-1 h-5 w-5 text-black"
          ></chevron-right-icon>
        </div>
      </div>
    </div>
  </section>
  <section class="py-6">
    <div
      class="container mx-auto flex max-w-6xl flex-col-reverse items-center justify-center gap-12 px-6 xl:flex-row xl:items-stretch"
    >
      <div class="flex flex-col items-center justify-around">
        <div class="text-xl font-semibold">We are a certified AWS Partner</div>
        <div class="text-xl">
          As a certified cloud development partner, we build and seamlessly
          scale our clients' cloud service solutions within a diverse AWS
          ecosystem. We help solve data and analytics challenges using a broad
          portfolio of purpose-built analytics services, scalable data lakes,
          and warehouses.
        </div>
        <button
          class="text-xl font-medium text-sky-500 hover:text-sky-700 hover:underline"
        >
          Learn more...
        </button>
      </div>
      <div>
        <img
          src="https://indatalabs.com/wp-content/uploads/2023/01/aws-partner-network-advanced-consulting.jpg"
          class="max-w-xl"
        />
      </div>
    </div>
  </section>
  <section class="py-6">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center gap-4 p-6"
    >
      <div class="text-2xl font-semibold">Our Mission</div>
      <div class="text-justify text-xl">
        Our mission is to help our Clients rocket their competitiveness and get
        brilliant results of their work unseen before. We strive to reach these
        goals applying innovative and proprietary development technologies,
        providing exceptional services, and using excellent professional
        expertise. Since 2014, our company helps businesses of all sizes all
        over the world to get valuable insights into data, automate repetitive
        tasks, enhance performance, add AI-driven features, and prevent cost
        overruns. For these 7+ years, we have built a sustainable business based
        on trust, latest innovation, state-of-the-art technologies, and
        experience.
      </div>
    </div>
  </section>
  <section class="py-6 pb-20">
    <div
      class="container mx-auto flex max-w-6xl flex-col items-center justify-center gap-10 p-6"
    >
      <div class="text-2xl font-semibold">Why Clients Choose InData Labs</div>
      <div class="grid grid-cols-6 gap-10">
        <div
          class="contents"
          v-for="clientReason in clientReasons"
          :key="clientReason['title']"
        >
          <div class="col-span-1"></div>
          <div class="col-span-5 flex flex-col items-start">
            <div class="text-xl font-medium">{{ clientReason.title }}</div>
            <div class="text-justify text-lg font-medium">
              {{ clientReason.description }}
            </div>
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
