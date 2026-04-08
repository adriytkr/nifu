<script setup lang="ts">
import { tDifficulties } from '~/i18n/locales/shared/difficulties';
import { useData } from 'vitepress';

import { ArticleDifficulty } from '~/types/articles';
import { convertStringToLocale } from '~/i18n';

const props = defineProps<{
  difficulty:ArticleDifficulty;
}>();

const {lang}=useData();
const t=tDifficulties[convertStringToLocale(lang.value)??'en'];
</script>

<template>
  <span class="flex items-center gap-x-2">
    <span
      :class="[
        'w-2 h-2 aspect-square rounded-full',
        {
          'bg-blue-400': difficulty === 'training',
          'bg-green-400': difficulty === 'easy',
          'bg-yellow-500': difficulty === 'medium',
          'bg-red-600': difficulty === 'hard',
          'bg-black': difficulty === 'insane',
        }
      ]"
    ></span>
    <span
      :class="[
        'text-body text-xs font-medium uppercase',
        {
          'text-blue-400': difficulty === 'training',
          'text-green-400': difficulty === 'easy',
          'text-yellow-500': difficulty === 'medium',
          'text-red-600': difficulty === 'hard',
          'text-black': difficulty === 'insane',
        },
      ]"
    >
      {{ t[difficulty] }}
    </span>
  </span>
</template>
