<script setup lang="ts">
import { computed } from 'vue';
import {useData,useRoute} from 'vitepress';

import type { Locale } from '~/i18n';
import {
  convertStringToLocale,
  getAbsoluteUrlWithoutLocale,
} from '~/i18n';

const props=defineProps<{
  locale:Locale;
}>();

const route=useRoute();
const {lang}=useData();

const normalizedTo=computed<string>(()=>
  getAbsoluteUrlWithoutLocale(
    convertStringToLocale(lang.value)??'en',
    route.path,
  )
);
</script>

<template>
  <VpLink
    :to="normalizedTo"
    :locale="locale"
    class="px-6 py-2 text-muted block transition-colors duration-200 hover:text-body hover:no-underline hover:bg-white"
    exact-active-class="font-bold text-body!"
  >
    <slot></slot>
  </VpLink>
</template>
