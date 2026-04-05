<script setup lang="ts">
const {
  isFullScreen,
  toggleFullScreen,
}=useBaseCheckpoint();
</script>

<template>
  <div class="mb-8">
    <CheckpointHeader
      :is-full-screen="isFullScreen"
      @toggle-fullscreen="toggleFullScreen"
    >
      <slot name="title"></slot>
    </CheckpointHeader>
    <div class="my-4">
      <slot name="content"></slot>
    </div>
    <CheckpointActions>
      <slot name="actions"></slot>
    </CheckpointActions>
  </div>
</template>
