<script setup lang="ts">
import { onMounted, ref } from "vue";

let typeValue = ref<string>();
let typeStatus = ref<Boolean>(false);
const props = defineProps<{ displayTextArray: Array<string> }>();
let typingSpeed = ref<number>(100);
let erasingSpeed = ref<number>(100);
let newTextDelay = ref<number>(2000);
let displayTextArrayIndex = ref<number>(0);
let charIndex = ref<number>(0);

const typeText = () => {
  if (
    charIndex.value < props.displayTextArray[displayTextArrayIndex.value].length
  ) {
    if (!typeStatus.value) {
      typeStatus.value = true;
    }
    typeValue.value += props.displayTextArray[
      displayTextArrayIndex.value
    ].charAt(charIndex.value);
    charIndex.value += 1;
    setTimeout(typeText, typingSpeed.value);
  } else {
    typeStatus.value = false;
    setTimeout(eraseText, newTextDelay.value);
  }
};

const eraseText = () => {
  if (charIndex.value > 0) {
    if (!typeStatus.value) typeStatus.value = true;
    typeValue.value = props.displayTextArray[
      displayTextArrayIndex.value
    ].substring(0, charIndex.value - 1);
    charIndex.value -= 1;
    setTimeout(eraseText, erasingSpeed.value);
  } else {
    typeStatus.value = false;
    displayTextArrayIndex.value += 1;
    if (displayTextArrayIndex.value >= props.displayTextArray.length)
      displayTextArrayIndex.value = 0;
    setTimeout(typeText, typingSpeed.value + 1000);
  }
};

onMounted(() => {
    setTimeout(typeText, newTextDelay.value + 500)
})
</script>

<template>
  <div>
    <span class="typed-text">{{ typeValue }}</span>
    <span class="blinking-cursor">|</span>
    <span class="cursor" :class="{ typing: typeStatus }">&nbsp;</span>
  </div>
</template>

<style scoped>
.typed-text {
    color: #d2b94b;
}

.blinking-cursor {
  font-size: 2rem;
  color: #2c3e50;
  -webkit-animation: 1s blink step-end infinite;
  -moz-animation: 1s blink step-end infinite;
  -ms-animation: 1s blink step-end infinite;
  -o-animation: 1s blink step-end infinite;
  animation: 1s blink step-end infinite;
}

@keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: #2c3e50;
  }
}

@-moz-keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: #2c3e50;
  }
}

@-webkit-keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: #2c3e50;
  }
}

@-ms-keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: #2c3e50;
  }
}

@-o-keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: #2c3e50;
  }
}
</style>
