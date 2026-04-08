<script setup lang="ts">
import AppButtonIcon from '~/components/app/AppButtonIcon.vue';

import ArrowIcon from '~/components/icons/ArrowIcon.vue';
import LastPageIcon from '~/components/icons/LastPageIcon.vue';
import PauseIcon from '~/components/icons/PauseIcon.vue';
import PlayIcon from '~/components/icons/PlayIcon.vue';

import LeaveFullScreenIcon from '~/components/icons/LeaveFullScreenIcon.vue';

const props = defineProps<{
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

import {ref, watch} from 'vue';
import VisibilityOnIcon from '~/components/icons/VisibilityOnIcon.vue';
import VisibilityOffIcon from '~/components/icons/VisibilityOffIcon.vue';

const showText=ref(true);

watch(
  ()=>props.isFullScreen,
  ()=>showText.value=true,
);
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
        class="w-full flex flex-col"
        :class="{
          'flex-col-reverse!':isFullScreen,
        }"
      >
        <div class="flex w-full mt-4 items-center justify-between">
          <div class="flex gap-x-4 justify-between items-center">
            <AppButtonIcon
              @click="$emit('first')"
              :disabled="currentSlide===0"
            >
              <LastPageIcon class="rotate-180"/>
            </AppButtonIcon>
            <AppButtonIcon
              @click="$emit('previous')"
              :disabled="currentSlide===0"
            >
              <ArrowIcon class="rotate-180"/>
            </AppButtonIcon>
            <AppButtonIcon
              @click="$emit('toggle-play')"
            >
              <PauseIcon v-if="isPlaying"/>
              <PlayIcon v-else/>
            </AppButtonIcon>
            <AppButtonIcon
              @click="$emit('next')"
              :disabled="currentSlide===totalSlides-1"
            >
              <ArrowIcon/>
            </AppButtonIcon>
            <AppButtonIcon
              @click="$emit('last')"
              :disabled="currentSlide===totalSlides-1"
            >
              <LastPageIcon/>
            </AppButtonIcon>
            <AppButtonIcon
              @click="showText=!showText"
              v-if="isFullScreen"
            >
              <span v-if="showText" class="flex items-center text-sm gap-x-2 text-muted transition-colors duration-200 hover:text-body">
                <VisibilityOnIcon/>
                <span>Show</span>
              </span>
              <span v-else class="flex items-center text-sm gap-x-2 text-muted transition-colors duration-200 hover:text-body">
                <VisibilityOffIcon/>
                <span>Hide</span>
              </span>
            </AppButtonIcon>
          </div>
          <div v-if="isFullScreen">
            <button @click="$emit('leave-full-screen')">
              <LeaveFullScreenIcon/>
            </button>
          </div>
        </div>
        <div
          class="max-h-[224px] max-w-3xl overflow-auto flex items-end transition-opacity duration-200"
          :class="{
            'opacity-0':!showText
          }"
        >
          <div :class="{
            'bg-white/5 backdrop-blur-sm rounded-sm p-4':isFullScreen,
          }">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
