<script setup lang="ts">
import { ref } from 'vue';

import CheckpointAnswer from './CheckpointAnswer.vue';
import type { CheckpointChoiceState } from './types';

const props=defineProps<{
  optionCount:number;
  correctIndex:number;
}>();

const selectedChoice=ref<number|null>(null);

function checkState(index:number):CheckpointChoiceState{
  if(selectedChoice.value===null)return 'default';
  if(selectedChoice.value===index){
    if(index===props.correctIndex)return 'correct';
    else return 'incorrect';
  }
  return 'default';
}
</script>

<template>
  <div
    class="border-t-2 border-[var(--sl-color-bg-nav)]"
    :class="{
      'border-emerald-400': selectedChoice !== null && checkState(selectedChoice) === 'correct',
      'border-rose-400': selectedChoice !== null && checkState(selectedChoice) === 'incorrect',
    }"
  >
    <div class="my-4 text-lg font-semibold">
      <slot name="question"></slot>
    </div>
    <div class="my-6 grid gap-2">
      <CheckpointAnswer 
        v-for="i in optionCount" 
        :key="i-1"
        :state="checkState(i-1)"
        :is-disabled="selectedChoice!==null"
        @click="selectedChoice=i-1"
      >
        <slot :name="`option-${i-1}`"></slot>
      </CheckpointAnswer>
    </div>
    <div v-if="selectedChoice!==null" class="mt-0">
      <p
        class="font-bold mb-2"
        :class="selectedChoice===correctIndex
          ?'text-emerald-400'
          :'text-rose-400'"
      >
        {{ selectedChoice===correctIndex?'✨ Correct!':'❌ Not quite.'}}
      </p>
      <div class="text-sm text-zinc-400 leading-relaxed">
        <slot name="explanation"></slot>
      </div>
    </div>
  </div>
</template>
