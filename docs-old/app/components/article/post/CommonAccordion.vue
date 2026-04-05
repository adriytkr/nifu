<script setup lang="ts">
import BaseAccordion from './BaseAccordion.vue';
</script>

<template>
  <BaseAccordion>
    <template #label>
      <slot name="label"></slot>
      <!-- Chevron Icon -->
      <svg
        class="inline-block mt-0 -rotate-90 group-data-is-open:rotate-90"
        xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor"
      >
        <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/>
      </svg>
    </template>
    <slot></slot>
  </BaseAccordion>
</template>
