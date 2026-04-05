<script setup lang="ts">
import type {
  CheckpointType2Field,
  Schema,
} from '~/types/article';

const age:CheckpointType2Field<number>={
  validator(val:number){
    return val===20;
  },
  default:null,
  answer:20,
};

const schema:Schema={
  age,
};
</script>

<template>
  <CheckpointType2 :schema="schema">
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #question>
      <slot name="question"></slot>
    </template>
  </CheckpointType2>
</template>
