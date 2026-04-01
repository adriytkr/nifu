<script setup lang="ts">
import CheckpointHeader from './CheckpointHeader.vue';
import CheckpointContent from './CheckpointContent.vue';
import CheckpointChoice from './CheckpointChoice.vue';
import CheckpointButton from './CheckpointButton.vue';
import CheckpointExplanation from './CheckpointExplanation.vue';

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
        'sl-markdown-content fixed z-999 inset-0 p-6 bg-white dark:bg-gray-900':isFullScreen,
        'relative':!isFullScreen,
      }"
    >
      <div
        :class="{
          'max-w-3xl mx-auto py-12 text-2xl':isFullScreen,
        }"
      >
        <CheckpointHeader
          :is-full-screen="isFullScreen"
          @toggle-fullscreen="toggleFullScreen"
        >
          <slot name="title"></slot>
        </CheckpointHeader>
        <CheckpointContent>
          <template #question>
            <slot name="question"></slot>
          </template>
          <template #command>
            <slot name="command"></slot>
          </template>
        </CheckpointContent>
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
        <CheckpointExplanation
          v-if="isSubmitted"
          :is-visible="isExplanationVisible"
          @toggle="isExplanationVisible=!isExplanationVisible"
        >
          <slot name="explanation"></slot>
        </CheckpointExplanation>
      </div>
    </div>
  </Teleport>
</template>
