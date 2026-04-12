<script setup lang="ts">
import type { Schema } from '~/types/article';
import {useCheckpointType2} from '~/composables/content/checkpoint/useCheckpointType2';

import CheckpointBase from '../CheckpointBase.vue';

const props= defineProps<{
  schema:Schema;
}>();

const {
  checkAnswers,
  reset,
  revealAnswers,
}=useCheckpointType2(props.schema);
</script>

<template>
  <CheckpointBase
    @check="checkAnswers"
    @reset="reset"
    @reveal-answers="revealAnswers"
  >
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #body>
      <slot name="body"></slot>
    </template>
    <template #actions>
      <AppButton @click="$emit('check')">Check</AppButton>
      <AppButton @click="$emit('reset')">Reset</AppButton>
      <AppButton @click="$emit('reveal')">Reveal</AppButton>
    </template>
  </CheckpointBase>
</template>
