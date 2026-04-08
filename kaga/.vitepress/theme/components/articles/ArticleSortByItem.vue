<script setup lang="ts">
const {isSelected=false}=defineProps<{
  isSelected?:boolean;
}>();
</script>

<template>
  <button
    class="w-full flex justify-between items-center gap-x-1 text-left bg-surface py-2 px-4 text-muted hover:bg-border-color"
    :class="{
      'font-medium text-body!':isSelected,
    }"
  >
    <slot></slot>
    <span v-if="isSelected">&#10003;</span>
  </button>
</template>
