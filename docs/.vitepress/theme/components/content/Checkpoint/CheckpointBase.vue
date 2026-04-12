<script setup lang="ts">
import AccordionCommon from '../Accordion/_api/AccordionCommon.vue';

defineEmits<{
  (e:'check'):void;
  (e:'reset'):void;
  (e:'reveal'):void;
}>();
</script>

<template>
  <div class="group mb-8">
    <div class="my-4">
      <slot name="body"></slot>
    </div>
    <div class="flex gap-x-4">
      <button @click="$emit('check')">Check</button>
      <button @click="$emit('reset')">Reset</button>
      <button @click="$emit('reveal')">Reveal</button>
    </div>
    <AccordionCommon>
      <template #label>
        Show solution
      </template>
      <slot name="explanation"></slot>
    </AccordionCommon>
  </div>
</template>
