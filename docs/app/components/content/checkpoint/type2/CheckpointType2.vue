<script setup lang="ts">
import type { Schema } from '~/types/article';

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
  <CommonCheckpoint
    @check="checkAnswers"
    @reset="reset"
    @reveal-answers="revealAnswers"
  >
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #content :state="formState">
      <slot name="question"></slot>
    </template>
  </CommonCheckpoint>
</template>
