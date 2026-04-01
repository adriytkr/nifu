<script setup lang="ts">
import Checkpoint from './Checkpoint.vue';

const props=defineProps<{
  choicesCount:number;
  correctChoices:number[];
}>();
</script>

<template>
  <Checkpoint
    :choices-count="choicesCount"
    :correct-choices="correctChoices"
  >
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #question>
      <slot name="question"></slot>
    </template>
    <template #command>
      <p v-if="correctChoices.length===1">Choose 1 answer</p>
      <p v-else>Choose all answers that apply</p>
    </template>
    <template
      v-for="i in choicesCount"
      :key="i"
      #[`choice-${i-1}`]
    >
      <slot :name="`choice-${i-1}`"></slot>
    </template>
    <template #explanation>
      <slot name="explanation"></slot>
    </template>
  </Checkpoint>
</template>
