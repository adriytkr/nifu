<script setup lang="ts">
import { useData, useRoute } from 'vitepress';
import { computed } from 'vue';

import { Locale } from '~/i18n';
import {
  convertStringToLocale,
  makeLocalizedUrl,
} from '~/i18n/utils';

const props=defineProps<{
  to:string;
  locale?:Locale;
  exactActiveClass?:string;
}>();

const route=useRoute();
const { lang }=useData()

const localizedPath=computed(()=>
  makeLocalizedUrl(
    convertStringToLocale(props.locale??lang.value)??'en',
    props.to,
  ),
)

const isActive=computed<boolean>(()=>
  localizedPath.value===route.path
);
</script>

<template>
  <a
    :href="localizedPath"
    :class="[
      $attrs.class,
      isActive&&exactActiveClass,
    ]"
  >
    <slot></slot>
  </a>
</template>
