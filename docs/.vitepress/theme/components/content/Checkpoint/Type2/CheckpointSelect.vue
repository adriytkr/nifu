<script setup lang="ts">
import type {
  FormState,
  validationState
} from '~/types/articles/article';

import type { Type2Select } from '~/types/article/checkpoint-type2';

import {computed,inject} from 'vue';

const props=defineProps<{
  name:string;
  options:Type2Select<any>[];
}>();

const formState=inject<FormState>('form-state');
const validationState=inject<validationState>('form-validation');

if(formState===undefined)
  throw Error('This must be used inside a CheckpointType2 Context');
</script>

<template>
  {{formState}}
  <select v-model="formState[name]">
    <option
      v-for="option in options"
      :key="option.value"
    >
      {{option.label}}
    </option>
  </select>
</template>

