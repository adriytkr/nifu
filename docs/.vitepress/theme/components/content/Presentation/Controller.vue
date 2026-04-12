<script setup lang="ts">
import NextIcon from '~icons/Presentation/NextIcon.vue';
import LastPageIcon from '~icons/Presentation/LastPageIcon.vue';
import PauseIcon from '~icons/Presentation/PauseIcon.vue';
import PlayIcon from '~icons/Presentation/PlayIcon.vue';

const props=defineProps<{
  currentSlide:number;
  totalSlides:number;
  isPlaying:boolean;
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
    <button
      @click="$emit('first-slide')"
      :disabled="currentSlide===0"
    >
      <LastPageIcon class="rotate-180"/>
    </button>
    <button
      @click="$emit('previous-slide')"
      :disabled="currentSlide===0"
    >
      <NextIcon class="rotate-180"/>
    </button>
    <button
      @click="$emit('toggle-play')"
    >
      <PauseIcon v-if="isPlaying"/>
      <PlayIcon v-else/>
    </button>
    <button
      @click="$emit('next-slide')"
      :disabled="currentSlide===totalSlides-1"
    >
      <NextIcon/>
    </button>
    <button
      @click="$emit('last-slide')"
      :disabled="currentSlide===totalSlides-1"
    >
      <LastPageIcon/>
    </button>
  </div>
</template>
