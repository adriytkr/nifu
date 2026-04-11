<script setup lang="ts">
import ChevronLeftIcon from '~icons/base/ChevronLeftIcon.vue';
</script>

<template>
  <AccordionBase>
    <template #label="{isOpen}">
      <slot name="label"></slot>
      <ChevronLeftIcon
        class="rotate-90"
        :class="{ '-rotate-90!':isOpen }"
      />
    </template>
    <slot></slot>
  </AccordionBase>
</template>
