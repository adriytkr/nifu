<script setup lang="ts">
import { ref } from 'vue';

import type {SearchFilter} from '@/types/article';

defineProps<{
  placeholder:string;
}>();

const query=defineModel<string>({
  default:'',
})

const inputRef=ref<HTMLInputElement|null>(null);

function focusInput(){
  if(inputRef.value===null)return;

  inputRef.value.focus();
}

defineExpose<SearchFilter>({
  focusInput,
});
</script>

<template>
  <input
    ref="inputRef"
    type="text"
    v-model="query"
    :placeholder="placeholder"
    class="px-4 py-2 w-full max-w-md border border-surface-border/30 rounded-sm transition-colors duration-200 hover:border-surface-border"
  />
</template>
