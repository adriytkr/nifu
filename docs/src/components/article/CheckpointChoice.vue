<script setup lang="ts">
import type { ChoiceStatus } from '@/types/article';

defineProps<{
  status:ChoiceStatus;
}>();
</script>

<template>
  <button
    class="text-left rounded-sm w-full mt-0 border bg-transparent px-4 py-2 cursor-pointer disabled:cursor-auto"
    :class="{
      'border-gray-300':status==='default',
      'border-black':status==='selected',
      'border-green-400':status==='correct',
      'border-green-600':status==='missed',
      'border-red-500':status==='incorrect',
    }"
  >
    <slot></slot>
  </button>
</template>
