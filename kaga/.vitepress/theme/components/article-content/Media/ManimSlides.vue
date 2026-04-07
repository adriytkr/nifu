<script setup lang="ts">
import { useSlides } from '~/composables/useSlides';

import PlayIcon from '~/components/icons/PlayIcon.vue';

import ManimSlidesController from './ManimSlidesController.vue';
import ManimSlidesHeader from './ManimSlidesHeader.vue';

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
  videoRef,
  videoContainerRef,
  enterFullScreen,
  leaveFullScreen,
  toggleFullScreen,
  isFullScreen,
  handleShortcut,
}=useSlides(props.totalSlides);
</script>

<template>
  <ManimSlidesHeader
    :source-code-link="sourceCodeLink"
    @enter-full-screen="enterFullScreen"
  />
  <div
    :class="{
      'fixed left-0 top-0 w-screen h-screen':isFullScreen,
    }"
    ref="videoContainerRef"
  >
    <div
      tabindex="0"
      ref="videoRef"
      class="rounded-sm focus:ring-offset-2 focus:ring-2 focus:ring-primary"
      :class="{
        'absolute w-full h-full':isFullScreen,
      }"
      @keydown="handleShortcut"
    >
      <div :class="{
        'absolute top-1/2 -translate-y-1/2 w-full':isFullScreen
      }">
        <div class="h-[360px] bg-black rounded-sm">
          <div
            v-if="!isStarted"
            class="group flex flex-col items-center justify-center w-full h-full cursor-pointer"
            @click="start"
          >
            <button class="p-4 text-muted transition-colors duration-200 group-hover:text-white">
              <PlayIcon :size="48"/>
            </button>
          </div>
          <div class="group relative" v-else>
            <iframe
              src="/animations/eigenvectors/presentation.html"
              width="100%"
              height="360px"
              ref="iframeRef"
              class="rounded-sm overflow-hidden pointer-events-none select-none"
              allowfullscreen
              tabindex="-1"
            ></iframe>
          </div>
        </div>
      </div>
    </div>
    <ManimSlidesController
      :is-full-screen="isFullScreen"
      :current-slide="currentSlide"
      :total-slides="totalSlides"
      :is-playing="isPlaying"
      @first="firstSlide"
      @previous="previousSlide"
      @toggle-play="togglePlay"
      @next="nextSlide"
      @last="lastSlide"
      @leave-full-screen="leaveFullScreen"
    >
      <slot :name="`slide-${currentSlide}`"></slot>
    </ManimSlidesController>
  </div>
</template>
