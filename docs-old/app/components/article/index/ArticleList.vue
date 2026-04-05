<script setup lang="ts">
import type { ArticleSchema } from '~/types/article';

import ArticleCard from './ArticleCard.vue';

defineProps<{
  articles:ArticleSchema[];
}>();
</script>

<template>
  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
    <ArticleCard
      v-for="article in articles"
      :key="article.id"
      :title="article.data.title"
      :description="article.data.description"
      :tags="article.data.tags"
    />
  </div>
</template>
