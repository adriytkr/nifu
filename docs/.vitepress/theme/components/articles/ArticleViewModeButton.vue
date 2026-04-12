<script setup lang="ts">
defineProps<{
  isSelected:boolean;
}>();
</script>

<template>
  <button
    class="px-4 py-2 rounded-md font-medium transition-colors duration-200 hover:bg-primary/10"
    :class="{'bg-primary! text-white':isSelected}"
  >
    <slot></slot>
  </button>
</template>
