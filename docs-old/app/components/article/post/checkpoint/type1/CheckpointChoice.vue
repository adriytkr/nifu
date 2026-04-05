<script setup lang="ts">
import type { ChoiceState } from '~/types/article';

defineProps<{
  state:ChoiceState;
}>();
</script>

<template>
  <button
    class="px-3 py-1 rounded-sm text-left bg-slate-100 border border-transparent [&>astro-slot>*:first-child]:mt-0 [&>astro-slot>*:last-child]:mb-0"
    :class="{
      '1':state==='idle',
      '2':state==='selected',
      '3':state==='correct',
      '4':state==='incorrect',
      '5':state==='missed',
      '6':state==='hidden',
      '7':state==='disabled',
    }"
  >
    {{ state }}
    <slot></slot>
  </button>
</template>
