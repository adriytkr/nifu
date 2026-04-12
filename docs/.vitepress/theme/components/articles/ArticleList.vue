<script setup lang="ts">
import { inject } from 'vue';

import type { ArticleSchema } from '~/types/article.schema';
import { ViewMode, ViewModeKey } from '~/types/filter';

import ArticleCard from './ArticleCard.vue';

defineProps<{
  articles:ArticleSchema[];
  viewMode:ViewMode;
}>();

const selectedViewMode=inject(ViewModeKey);
</script>

<template>
  <ul 
    class="not-prose"
    :class="{
      'flex flex-col':selectedViewMode==='list',
      'grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2':selectedViewMode==='grid',
    }"
  >
    <ArticleCard
      v-for="article in articles"
      :key="article.slug"
      :article="article"
    />
  </ul>
</template>
