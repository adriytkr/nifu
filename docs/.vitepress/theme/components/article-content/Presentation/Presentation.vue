<script setup lang="ts">
import { usePresentation } from '~/composables/usePresentation';

import PlayIcon from '~/components/icons/presentation/PlayIcon.vue';
import Controller from './Controller.vue';

const props=defineProps<{
  totalSlides:number;
  sourceCodeLink:string;
}>();

const {
  iframeRef,
  currentSlide,
  isPlaying,
  isStarted,
  start,
  firstSlide,
  previousSlide,
  togglePlay,
  nextSlide,
  lastSlide,
}=usePresentation(props.totalSlides);
</script>

<template>
  <h1>Manim Slides</h1>
  <!-- <Controller/> -->
</template>
