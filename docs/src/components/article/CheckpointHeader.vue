<script setup lang="ts">
defineProps<{
  isFullScreen:boolean;
}>();

defineEmits<{
  (e:'toggle-fullscreen'):void;
}>();
</script>

<template>
  <div class="flex justify-between items-center">
    <span class="text-gray-500 dark:text-gray-400">
      <slot></slot>
    </span>
    <button
      class="bg-transparent cursor-pointer p-1 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors duration-200"
      @click="$emit('toggle-fullscreen')"
    >
      <!-- Enter Full Screen Icon -->
      <svg v-if="isFullScreen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
        <path d="M240-120v-120H120v-80h200v200h-80Zm400 0v-200h200v80H720v120h-80ZM120-640v-80h120v-120h80v200H120Zm520 0v-200h80v120h120v80H640Z"/>
      </svg>
      <!-- Leave Full Screen Icon -->
      <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
        <path d="M120-120v-200h80v120h120v80H120Zm520 0v-80h120v-120h80v200H640ZM120-640v-200h200v80H200v120h-80Zm640 0v-120H640v-80h200v200h-80Z"/>
      </svg>
    </button>
  </div>
</template>
