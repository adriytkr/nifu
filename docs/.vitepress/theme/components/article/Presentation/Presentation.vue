<script setup lang="ts">
import { usePresentation } from '~/composables/content/usePresentation';

import Controller from './Controller.vue';

const props=defineProps<{
  totalSlides:number;
}>();

const {
  iframeRef,
  currentSlide,
  isPlaying,
  isStarted,
  start,

  goToFirstSlide,
  goToLastSlide,

  goToNextSlide,
  goToPreviousSlide,

  togglePlay,
}=usePresentation(props.totalSlides);
</script>

<template>
  <div>
    <div class="w-full aspect-video bg-black rounded-t-md rounded-tr-md"></div>
    <div class="bg-surface p-4 rounded-bl-md rounded-b-md">
      <Controller
        :total-slides="5"
        :current-slide="1"
        @first-slide="goToFirstSlide"
        @last-slide="goToLastSlide"
        @previous-slide="goToPreviousSlide"
        @next-slide="goToNextSlide"
        @toggle-play="togglePlay"
      />
      <div class="h-48 overflow-y-auto">
        <template
          v-for="i in totalSlides"
          :key="i"
        >
          <div v-show="currentSlide===i-1">
            <slot :name="`slide-${i}`"></slot>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>
