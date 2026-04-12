<script setup lang="ts">
import NextIcon from '~icons/Presentation/NextIcon.vue';
import LastPageIcon from '~icons/Presentation/LastPageIcon.vue';
import PauseIcon from '~icons/Presentation/PauseIcon.vue';
import PlayIcon from '~icons/Presentation/PlayIcon.vue';

const props=defineProps<{
  currentSlide:number;
  totalSlides:number;
}>();

defineEmits<{
  (e:'first-slide'):void;
  (e:'last-slide'):void;

  (e:'previous-slide'):void;
  (e:'next-slide'):void;

  (e:'toggle-play'):void;
}>();
</script>

<template>
  <div class="flex items-center gap-x-2">
    <button @click="$emit('first-slide')">
      <LastPageIcon class="rotate-180"/>
    </button>
    <button @click="$emit('previous-slide')">
      <NextIcon class="rotate-180"/>
    </button>
    <button @click="$emit('toggle-play')">
      <PauseIcon/>
      <!-- <PlayIcon/> -->
    </button>
    <button @click="$emit('next-slide')">
      <NextIcon/>
    </button>
    <button @click="$emit('last-slide')">
      <LastPageIcon/>
    </button>
  </div>
</template>
