<script setup lang="ts">
import {
    ArrowLongRightIcon
} from "@heroicons/vue/20/solid";

defineProps<{ caseTitle: string; caseBody: string; url: string }>();
</script>

<template>
    <div class="group flex h-80 flex-col items-center justify-around bg-black text-white p-6 relative cursor-pointer overflow-hidden z-10">
        <div class="absolute top-0 right-0 z-0">
            <img src="../assets/graph.svg" class="h-24 w-24 group-hover:scale-150 transition ease-linear duration-300"/>
        </div>
        <div class="text-3xl uppercase text-center z-10">
            {{ caseTitle }}
        </div>
        <div class="text-center">
            {{ caseBody }}
        </div>
        <RouterLink :to="url">
            <div class="flex flex-row items-center justify-center gap-3 group-hover:text-rose-400 ">
                <div class="uppercase text-xl font-medium">Learn More</div>
                <arrow-long-right-icon class="h-6 w-6 group-hover:text-rose-400 group-hover:scale-x-125 transition ease-linear duration-200"></arrow-long-right-icon>
            </div>
        </RouterLink>
    </div>
</template>
