<script setup lang="ts">
import type { ChoiceStatus } from '@/types/article';

defineProps<{
  status:ChoiceStatus;
}>();
</script>

<template>
  <button
    class="mt-0 text-left px-4 py-2 rounded-sm cursor-pointer disabled:cursor-default disabled:pointer-events-none text-gray-700 dark:text-gray-300 border transition-all duration-200"
    :class="{
      'border-transparent bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700':status==='default',
      'border-gray-400 bg-gray-100 dark:border-gray-500 dark:bg-gray-800':status==='selected',
      'border-green-400 bg-green-400/20':status==='correct',
      'border-green-800 bg-green-800/20':status==='missed',
      'border-red-600 bg-red-600/20':status==='incorrect',
    }"
  >
    <slot></slot>
  </button>
</template>
