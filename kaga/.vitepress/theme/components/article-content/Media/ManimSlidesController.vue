<script setup lang="ts">
import AppIconButton from '~/components/app/AppIconButton.vue';

import ArrowIcon from '~/components/icons/ArrowIcon.vue';
import LastPageIcon from '~/components/icons/LastPageIcon.vue';
import PauseIcon from '~/components/icons/PauseIcon.vue';
import PlayIcon from '~/components/icons/PlayIcon.vue';

import LeaveFullScreenIcon from '~/components/icons/LeaveFullScreenIcon.vue';

defineProps<{
  isFullScreen:boolean;
  currentSlide:number;
  totalSlides:number;
  isPlaying:boolean;
}>();

defineEmits<{
  (e:'first'):void;
  (e:'previous'):void;
  (e:'toggle-play'):void;
  (e:'next'):void;
  (e:'last'):void;
  (e:'leave-full-screen'):void;
}>();
</script>

<template>
  <div 
    :class="{
      'absolute z-9999 bottom-0 w-full':isFullScreen,
  }">
    <div :class="{
      'flex items-end justify-between p-4':isFullScreen
    }">
      <div
        class="flex flex-col"
        :class="{
          'flex-col-reverse!':isFullScreen,
        }"
      >
        <div class="flex gap-x-4 mt-4">
          <AppIconButton
            @click="$emit('first')"
            :disabled="currentSlide===0"
          >
            <LastPageIcon class="rotate-180"/>
          </AppIconButton>
          <AppIconButton
            @click="$emit('previous')"
            :disabled="currentSlide===0"
          >
            <ArrowIcon class="rotate-180"/>
          </AppIconButton>
          <AppIconButton
            @click="$emit('toggle-play')"
          >
            <PauseIcon v-if="isPlaying"/>
            <PlayIcon v-else/>
          </AppIconButton>
          <AppIconButton
            @click="$emit('next')"
            :disabled="currentSlide===totalSlides-1"
          >
            <ArrowIcon/>
          </AppIconButton>
          <AppIconButton
            @click="$emit('last')"
            :disabled="currentSlide===totalSlides-1"
          >
            <LastPageIcon/>
          </AppIconButton>
        </div>
        <div class="max-h-[224px] max-w-3xl overflow-auto flex items-end">
          <div>
            <slot></slot>
          </div>
        </div>
      </div>
      <div v-if="isFullScreen">
        <button @click="$emit('leave-full-screen')">
          <LeaveFullScreenIcon/>
        </button>
      </div>
    </div>
  </div>
</template>
