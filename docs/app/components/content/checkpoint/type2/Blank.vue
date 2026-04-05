<script setup lang="ts">
import type { FormState, validationState } from '~/types/article';

const props=defineProps<{
  name:string;
}>();

const formState=inject<FormState>('form-state');
const validationState=inject<validationState>('form-validation');

if(formState===undefined)
  throw Error('This must be used inside a CheckpointType2 Context');

const isLegitimate=computed<boolean>(()=>
  formState!==undefined&&
  formState[props.name]!==undefined&&
  validationState!==undefined&&
  validationState[props.name]!==undefined
);
</script>

<template>
  <template v-if="isLegitimate">
    <input
      type="text"
      v-model.number="formState[name]"
      class="w-16 px-2 py-1 border rounded-sm transition-colors duration-200 hover:border-body"
      :class="{
        'border-muted':validationState[name]==='idle',
        'border-green-500 bg-green-50':validationState[name]==='correct',
        'border-red-500 bg-red-50':validationState[name]==='incorrect',
        'border-yellow-500 bg-yellow-50':validationState[name]==='revealed',
      }"
    >
  </template>
</template>
