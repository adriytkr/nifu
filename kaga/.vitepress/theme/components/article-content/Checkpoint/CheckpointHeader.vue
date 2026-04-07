<script setup lang="ts">
import EnterFullScreenIcon from '~/components/icons/EnterFullScreenIcon.vue';
import LeaveFullScreenIcon from '~/components/icons/LeaveFullScreenIcon.vue';

const isFullScreen=defineModel<boolean>({
  default:false,
});
</script>

<template>
  <div class="not-prose flex justify-between items-center">
    <span class="text-muted text-sm">
      <slot></slot>
    </span>
    <button
      class="bg-transparent p-1 text-muted hover:text-body transition-colors duration-200"
      @click="isFullScreen=!isFullScreen"
    >
      <EnterFullScreenIcon v-if="!isFullScreen"/>
      <LeaveFullScreenIcon v-else/>
    </button>
  </div>
</template>
