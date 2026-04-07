<script setup lang="ts">
import {ref} from 'vue';

const isOpen=ref(false);
</script>

<template>
  <div class="my-5">
    <button
      @click="isOpen=!isOpen"
      class="px-0 mb-2 bg-transparent flex gap-x-1 items-center text-muted"
    >
      <slot name="label" :is-open="isOpen"></slot>
    </button>
    <div
      class="grid overflow-hidden transition-all duration-400 ease-in-out"
      :class="{
        'grid-rows-[0fr]':!isOpen,
        'grid-rows-[1fr]':isOpen,
      }"
    >
      <div class="min-h-0 text-gray-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 dark:text-gray-300">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
