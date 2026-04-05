<script setup lang="ts">
import { useBaseCheckpoint } from '~/composables/useBaseCheckpoint';

import CheckpointHeader from './CheckpointHeader.vue';
import CheckpointActions from './CheckpointActions.vue';
import CheckpointButton from './CheckpointButton.vue';

const {
  isFullScreen,
  toggleFullScreen,
}=useBaseCheckpoint();

defineEmits<{
  (e:'check'):void;
  (e:'reset'):void;
  (e:'reveal-answers'):void;
}>();
</script>

<template>
  <div class="mb-8">
    <CheckpointHeader
      :is-full-screen="isFullScreen"
      @toggle-fullscreen="toggleFullScreen"
    >
      <slot name="title"></slot>
    </CheckpointHeader>
    <div class="my-4">
      <slot name="content"></slot>
    </div>
    <CheckpointActions>
      <CheckpointButton @click="$emit(`check`)">
        Check
      </CheckpointButton>
      <CheckpointButton @click="$emit(`reset`)">
        Reset
      </CheckpointButton>
      <CheckpointButton @click="$emit(`reveal-answers`)">
        Reveal Answers
      </CheckpointButton>
    </CheckpointActions>
  </div>
</template>
