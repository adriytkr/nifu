<script setup lang="ts">
import CheckpointQuestion from './CheckpointQuestion.vue';

defineProps<{
  answer:boolean;
}>();
</script>

<template>
  <CheckpointQuestion
    :option-count="2"
    :correctIndex="answer?0:1"
  >
    <template #question>
       <slot name="question"></slot>
    </template>
    <template #option-0>
      <slot name="option-0">True</slot>
    </template>
    <template #option-1>
      <slot name="option-1">False</slot>
    </template>
    <template #explanation>
      <slot name="explanation"></slot>
    </template>
  </CheckpointQuestion>
</template>
