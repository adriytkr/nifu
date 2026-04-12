<script setup lang="ts">
import { ref } from 'vue';
import ChevronIcon from '~/components/icons/ChevronIcon.vue';

const isOpen=ref(false);

function toggle(){
  isOpen.value=!isOpen.value;
}
</script>

<template>
  <div class="bg-surface p-2 rounded-md">
    <button
      @click="toggle"
      class="flex gap-x-1 items-center font-medium"
    >
      <slot name="label"></slot>
      <chevron-icon
        :class="{
          'rotate-90':!isOpen,
          '-rotate-90':isOpen,
        }"
      />
    </button>
    <div
      class="grid overflow-hidden transition-all duration-300 ease-in-out"
      :class="{
        'grid-rows-[0fr]':!isOpen,
        'grid-rows-[1fr] mt-7':isOpen,
      }"
    >
      <div class="min-h-0 reset">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
