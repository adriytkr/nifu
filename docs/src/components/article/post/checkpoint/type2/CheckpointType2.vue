<script setup lang="ts">
import type { Schema } from '@/types/article';
import { useCheckpointType2 } from '@/composables/useCheckpointType2';

import BaseCheckpoint from '../BaseCheckpoint.vue';
import { provide } from 'vue';

import CheckpointBlank from './CheckpointBlank.vue';

const props= defineProps<{
  schema:Schema;
  
}>();

const {formState}=useCheckpointType2(props.schema);

provide('checkpoint-state',formState);
</script>

<template>
  <BaseCheckpoint
    @check="null"
    @reset="null"
    @reveal-answers="null"
  >
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #content :state="formState">
      <slot name="question" :state="formState"></slot>
      {{ formState }}
    </template>
  </BaseCheckpoint>
      <CheckpointBlank name="mariana"></CheckpointBlank>
</template>
