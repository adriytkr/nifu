<script setup lang="ts">
import { ChoiceStatus } from '~/types/articles/checkpoint-type1';

defineProps<{
  status:ChoiceStatus;
}>();
</script>

<template>
  <button
    class="reset block w-full text-left px-4 py-2 rounded-sm border border-transparent"
    :class="{
      'bg-slate-200':status==='idle',
      'bg-slate-200 border-surface-border!':status==='selected',
      'bg-green-50 border-green-500!':status==='correct',
      'bg-red-50 border-red-500!':status==='incorrect',
      'bg-yellow-50 border-yellow-500!':status==='missed',
    }"
  >
    <slot></slot>
  </button>
</template>
