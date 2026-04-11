<script setup lang="ts">
import { ref } from 'vue';
import {useData} from 'vitepress';

import type {SearchFilter} from '~/types/articles';
import {tFilter} from '~/i18n/locales/shared/filter';
import type { Locale } from '~/i18n';

import SearchIcon from '~icons/base/SearchIcon.vue';
import CloseIcon from '~icons/base/CloseIcon.vue';
import IconButton from '../base/IconButton.vue';

const {lang}=useData();
const t=tFilter[lang.value as Locale];

const query=defineModel<string>({default:''})
const inputRef=ref<HTMLInputElement|null>(null);

function focusInput(){
  if(inputRef.value===null)return;
  inputRef.value.focus();
}

function clearInput(){
  query.value='';
  focusInput();
}

defineExpose<SearchFilter>({focusInput});
</script>

<template>
  <div class="group p-2 bg-surface flex items-center md:max-w-md w-full border border-border-color rounded-sm transition-colors duration-200">
    <SearchIcon
      class="text-muted cursor-text transition-colors duration-200 group-hover:text-body"
      @click="focusInput"
    />
    <input
      ref="inputRef"
      type="text"
      class="mx-4 flex-1 outline-none"
      :placeholder="t.placeholder"
      v-model="query"
    >
    <IconButton
      v-show="query"
      @click="clearInput"
    >
      <CloseIcon/>
    </IconButton>
  </div>
</template>
