<script setup lang="ts">
defineEmits<{
  (e:'check'):void;
  (e:'reset'):void;
  (e:'reveal-answers'):void;
}>();
</script>

<template>
  <BaseCheckpoint>
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #content>
      <slot name="content"></slot>
    </template>
    <template #actions>
      <CheckpointButton @click="$emit(`check`)">
        Check
      </CheckpointButton>
      <CheckpointButton @click="$emit(`reset`)">
        Reset
      </CheckpointButton>
      <CheckpointButton @click="$emit(`reveal-answers`)">
        Reveal Answers
      </CheckpointButton>
    </template>
  </BaseCheckpoint>
</template>

