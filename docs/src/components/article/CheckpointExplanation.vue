<script setup lang="ts">
defineProps<{
  isVisible:boolean;
}>();

defineEmits<{
  (e:'toggle'):void;
}>();
</script>

<template>
  <div>
    <button
      class="px-0 mt-4 bg-transparent flex gap-x-1 items-center text-gray-700 dark:text-gray-300"
      @click="$emit('toggle')"
    >
      <!-- Light Bulb Icon -->
      <svg class="inline-block" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
        <path d="M423.5-103.5Q400-127 400-160h160q0 33-23.5 56.5T480-80q-33 0-56.5-23.5ZM320-200v-80h320v80H320Zm10-120q-69-41-109.5-110T180-580q0-125 87.5-212.5T480-880q125 0 212.5 87.5T780-580q0 81-40.5 150T630-320H330Zm24-80h252q45-32 69.5-79T700-580q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 54 24.5 101t69.5 79Zm126 0Z"/>
      </svg>
      Show explanation
      <!-- Chevron Icon -->
      <svg
        class="inline-block mt-0"
        :class="{
          'rotate-90':!isVisible,
          '-rotate-90':isVisible,
        }"
        xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor"
      >
        <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/>
      </svg>
    </button>
    <div
      class="grid overflow-hidden transition-all duration-400 ease-in-out"
      :class="{
        'grid-rows-[0fr]':!isVisible,
        'grid-rows-[1fr]':isVisible,
      }"
    >
      <div class="min-h-0 text-gray-700 dark:text-gray-300">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
