<script setup lang="ts">
import CheckpointChoice from './CheckpointChoice.vue';
import CheckpointButton from './CheckpointButton.vue';

import { useCheckpoint } from '@/composables/useCheckpoint';

const props=defineProps<{
  choicesCount:number;
  correctChoices:number[];
}>();

const {
  getStatus,
  selectChoice,
  emptyState,
  isSubmitted,
  checkChoices,
  retry,
  isFullScreen,
  toggleFullScreen,
  isExplanationVisible,
}=useCheckpoint(props.correctChoices);
</script>

<template>
  <Teleport to="body" :disabled="!isFullScreen">
    <div
      :class="{
        'fixed z-999 inset-0 bg-white p-6':isFullScreen,
        'relative':!isFullScreen,
      }"
    >
      <div class="flex justify-between items-center">
        <span class="text-gray-400">
          <slot name="title"></slot>
        </span>
        <button
          class="bg-transparent cursor-pointer"
          @click="toggleFullScreen"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
            <path d="M120-120v-200h80v120h120v80H120Zm520 0v-80h120v-120h80v200H640ZM120-640v-200h200v80H200v120h-80Zm640 0v-120H640v-80h200v200h-80Z"/>
          </svg>
        </button>
      </div>
      <div class="mt-2 mb-6">
        <slot name="question"></slot>
      </div>
      <div class="font-bold">
        <slot name="command"></slot>
      </div>
      <div class="flex flex-col gap-y-4 my-4">
        <CheckpointChoice
          v-for="i in choicesCount"
          :key="i"
          :status="getStatus(i-1)"
          :disabled="isSubmitted"
          @click="selectChoice(i-1)"
        >
          <slot :name="`choice-${i-1}`"></slot>
        </CheckpointChoice>
      </div>
      <div class="flex gap-x-4 items-center">
        <CheckpointButton
          @click="checkChoices"
          :disabled="emptyState"
          v-if="!isSubmitted"
        >
          Check
        </CheckpointButton>
        <CheckpointButton
          v-if="isSubmitted"
          @click="retry"
        >
          Retry
        </CheckpointButton>
      </div>
      <div v-if="isSubmitted">
        <button
          class="px-0 bg-transparent flex gap-x-1 items-center"
          @click="isExplanationVisible=!isExplanationVisible"
        >
          <!-- Light Bulb Icon -->
          <svg class="inline-block" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
            <path d="M423.5-103.5Q400-127 400-160h160q0 33-23.5 56.5T480-80q-33 0-56.5-23.5ZM320-200v-80h320v80H320Zm10-120q-69-41-109.5-110T180-580q0-125 87.5-212.5T480-880q125 0 212.5 87.5T780-580q0 81-40.5 150T630-320H330Zm24-80h252q45-32 69.5-79T700-580q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 54 24.5 101t69.5 79Zm126 0Z"/>
          </svg>
          Show explanation
          <!-- Chevron Icon -->
          <svg
            class="inline-block mt-0"
            :class="{
              'rotate-90':!isExplanationVisible,
              '-rotate-90':isExplanationVisible,
            }"
            xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor"
          >
            <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/>
          </svg>
        </button>
        <div
          class="grid overflow-hidden transition-all duration-400 ease-in-out"
          :class="{
            'grid-rows-[0fr]':!isExplanationVisible,
            'grid-rows-[1fr]':isExplanationVisible,
          }"
        >
          <div class="min-h-0">
            <slot name="explanation"></slot>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>
