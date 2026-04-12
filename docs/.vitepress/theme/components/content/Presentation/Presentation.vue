<script setup lang="ts">
import { usePresentation } from '~/composables/content/usePresentation';

import Controller from './Controller.vue';
import PlayIcon from '~/components/icons/Presentation/PlayIcon.vue';
import PauseIcon from '~/components/icons/Presentation/PauseIcon.vue';

const props=defineProps<{
  totalSlides:number;
  presentation:string;
  thumbnail:string;
}>();

const {
  iframeRef,
  isStarted,
  isLoaded,
  isPlaying,
  feedbackRef,
  start,

  currentSlide,

  goToFirstSlide,
  goToLastSlide,

  goToNextSlide,
  goToPreviousSlide,

  togglePlay,
}=usePresentation(props.totalSlides);
</script>

<template>
  <div>
    <div class="relative w-full aspect-video bg-black rounded-t-md rounded-tr-md">
      <button
        class="group w-full h-full absolute cursor-pointer outline-none rounded-md focus:ring-2 focus:ring-primary focus:ring-offset-2"
        @click="start"
        v-if="!isStarted"
      >
        <img
          :src="thumbnail"
          alt="alt"
          class="w-full h-full my-0! object-cover rounded-md"
        />
        <span class="absolute -translate-1/2 left-1/2 top-1/2 px-4 py-2 bg-gray-700 rounded-md text-white text-2xl transition-colors duration-200 group-hover:bg-primary group-focus:bg-primary">
          <PlayIcon/>
        </span>
      </button>
      <div
        v-if="isStarted&&!isLoaded"
        class="absolute w-full h-full left-0 top-0 flex justify-center items-center"
      >
        <div class="w-8 h-8 border-2 border-slate-300 border-t-primary animate-spin rounded-full"></div>
      </div> 
      <div
        class="absolute w-full h-full"
        v-if="isStarted"
      >
        <div
          class="absolute w-full rounded-md h-full flex justify-center items-center left-0 top-0 pointer-events-none opacity-0"
          ref="feedbackRef"
        >
          <span class="bg-black/70 p-4 rounded-full text-white text-2xl">
            <PlayIcon v-if="isPlaying"/>
            <PauseIcon v-else/>
          </span>
        </div>
        <iframe
          src="/presentations/jacobian-matrix/Presentation.html"
          class="w-full h-full rounded-md focus-within:ring-1 focus-within:ring-primary focus-within:ring-offset-2"
          ref="iframeRef"
          @click="togglePlay"
          @load="isLoaded=true"
        ></iframe>
      </div>
    </div>
    <div class="bg-surface p-4 rounded-bl-md rounded-b-md">
      <Controller
        :total-slides="5"
        :current-slide="1"
        :is-playing="isPlaying"
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
