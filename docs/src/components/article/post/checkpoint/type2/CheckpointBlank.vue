<script setup lang="ts">
import type { FormState } from '@/types/article';
import { inject } from 'vue';

defineProps<{
  name:string;
}>();

const state=inject<FormState>('checkpoint-state',{});
</script>

<template>
  {{ state }}
  <input v-model="state[name]"/>
</template>
