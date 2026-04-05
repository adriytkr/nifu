<script setup lang="ts">
import type { Locale } from '~~/types/i18n';

defineProps<{
  locale:Locale;
}>();
</script>

<template>
  <button
    @click="$i18n.locale=locale"
    class="px-6 py-2 text-muted block! transition-colors duration-200 hover:text-body hover:no-underline hover:bg-white"
    :class="{
      'font-bold text-body!':locale===$i18n.locale
    }"
  >
    <slot></slot>
  </button>
</template>
