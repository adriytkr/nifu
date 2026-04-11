<script setup lang="ts">
import {computed} from 'vue';
import {useData} from 'vitepress';

import type { Locale } from '~/i18n';

import LanguagePickerButton from './LanguagePickerButton.vue';
import ChevronLeftIcon from '~/components/icons/base/ChevronLeftIcon.vue';

export interface LocaleItem{
  code:Locale;
  label:string;
}

const isOpen=defineModel('open',{default:false});

const {site,lang}=useData();

const locales=computed<LocaleItem[]>(()=>
  Object
    .entries(site.value.locales)
    .map<LocaleItem>(([code,value])=>({
      code:value.lang as Locale,
      label:value.label,
    }))
);

const currentLanguage=computed<string>(()=>{
  const current=locales.value.find(l=>l.code===lang.value);
  return current!==undefined
    ?current.label
    :'English';
});
</script>

<template>
  <div class="relative">
    <button
      @click="isOpen=!isOpen"
      class="flex items-center gap-x-1 text-muted transition-colors duration-200 hover:text-body"
    >
      {{ currentLanguage }}
       <ChevronLeftIcon
        class="rotate-90"
        :class="{
          '-rotate-90!':isOpen,
        }"
       />
    </button>
    <div
      class="absolute z-50 right-0 top-full w-32 mt-2 bg-surface shadow-xl rounded-sm overflow-hidden opacity-0 pointer-events-none transition-opacity duration-200"
      :class="{
        'opacity-100 pointer-events-auto!':isOpen,
      }"
    >
      <LanguagePickerButton
        v-for="locale in locales"
        :key="locale.code"
        :locale="locale.code"
      >
        {{ locale.label }}
      </LanguagePickerButton>
    </div>
  </div>
</template>
