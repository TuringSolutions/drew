<script setup lang="ts">
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { ChevronDownIcon } from "@heroicons/vue/20/solid";
const services: Array<{
  id: string;
  description: string;
  logo: string;
  url: string;
}> = [
  {
    id: "Computer Vision",
    description: "",
    logo: "",
    url: "/services/computervision",
  },
  {
    id: "Software Development",
    description: "",
    logo: "",
    url: "/services/softwaredev",
  },
];
</script>

<template>
  <div class="absolute top-0 right-0 z-20 mt-6 mr-14 flex flex-row gap-2">
    <popover v-slot="{ open }" class="relative">
      <popover-button
        :class="open ? '' : 'text-opacity-90'"
        class="group inline-flex items-center px-3 py-2 text-lg font-medium text-white hover:text-sky-400 hover:text-opacity-100"
      >
        <router-link to="/">
          <span>Home</span>
        </router-link>
      </popover-button>
    </popover>
    <popover v-slot="{ open }" class="relative">
      <popover-button
        :class="open ? '' : 'text-opacity-90'"
        class="group inline-flex items-center px-3 py-2 text-lg font-medium text-white hover:text-sky-400 hover:text-opacity-100"
      >
        <router-link to="/aboutus"> About Us </router-link>
      </popover-button>
    </popover>

    <popover v-slot="{ open }" class="relative">
      <popover-button
        :class="open ? '' : 'text-opacity-90'"
        class="group inline-flex items-end gap-1 px-3 py-2 text-lg font-medium text-white hover:text-sky-400 hover:text-opacity-100"
      >
        <span>Services</span>
        <chevron-down-icon
          :class="open ? '' : 'text-opacity-70'"
          class="h-6 w-6 text-orange-500 transition duration-100 ease-in-out group-hover:text-sky-400 group-hover:text-opacity-90"
          aria-hidden="true"
        ></chevron-down-icon>
      </popover-button>
      <popover-panel
        class="absolute right-0 mt-2 z-10 min-w-max bg-sky-800 text-white rounded-md py-2 px-4"
      >
        <div
          v-for="service in services"
          :key="service.id"
          class="flex flex-col items-start justify-start"
        >
          <div>
            <router-link :to="service.url" class="flex flex-row items-center justify-start">
              <div class="text-lg font-medium hover:text-sky-300">
                {{ service.id }}
              </div>
            </router-link>
          </div>
        </div>
      </popover-panel>
    </popover>
  </div>
</template>
