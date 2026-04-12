<script lang="ts">
export interface QueryAPI{
  clearInput:()=>void;
}
</script>

<script setup lang="ts">
import {ref} from 'vue';

import SearchIcon from '~icons/SearchIcon.vue';
import CloseIcon from '../icons/CloseIcon.vue';

defineProps<{
  placeholder:string;
}>();

const inputRef=ref<HTMLInputElement|null>(null);
const query=defineModel<string>({default:''});

function clearInput(){
  inputRef.value?.focus();
  query.value='';
}

defineExpose({clearInput});
</script>

<template>
  <div
    class="w-full flex gap-x-2 px-2 items-center border border-muted bg-white rounded-md cursor-text"
    @click="inputRef?.focus()"
  >
    <SearchIcon/>
    <input
      type="text"
      v-model="query"
      ref="inputRef"
      :placeholder="placeholder"
      class="flex-1 py-2 outline-none font-medium placeholder:font-medium"
    />
    <button @click.self="clearInput">
      <CloseIcon/>
    </button>
  </div>
</template>
