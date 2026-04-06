<script setup lang="ts">
import {ref} from 'vue';

import { useSlides } from '~/composables/useSlides';

import AppButton from '~/components/app/AppButton.vue';
import MediaWithCaption from './MediaWithCaption.vue';
import PlayIcon from '~/components/icons/PlayIcon.vue';

const props=defineProps<{
  slides:number;
}>();

const isStarted=ref(false);

const {
  iframeRef,
  currentSlide,
  previousSlide,
  nextSlide,
  resetPresentation,
}=useSlides(props.slides);
</script>

<template>
  <div
    class="flex flex-col items-center justify-center h-[500px] bg-black rounded-sm cursor-pointer"
    v-if="!isStarted"
    @click="isStarted=true"
  >
    <button class="p-4 text-muted transition-colors duration-200 hover:text-white">
      <PlayIcon :size="48"/>
    </button>
  </div>
  <div v-else>
    <MediaWithCaption>
      <template #media>
        <iframe 
          src="/animations/eigenvectors/presentation.html"
          width="100%" 
          height="500px" 
          ref="iframeRef"
          class="rounded-sm overflow-hidden"
          allowfullscreen
        ></iframe>
      </template>
      <slot></slot>
    </MediaWithCaption>
    <div class="flex flex-col">
      <div class="flex gap-x-4 mb-4">
        <AppButton @click="resetPresentation">
          Reset
        </AppButton>
        <AppButton
          @click="previousSlide"
          :disabled="currentSlide===0"
        >
          Previous
        </AppButton>
        <AppButton
          @click="nextSlide"
          :disabled="currentSlide===slides-1"
        >
          Next
        </AppButton>
      </div>
      <slot :name="`slide-${currentSlide}`"></slot>
    </div>
  </div>
</template>
