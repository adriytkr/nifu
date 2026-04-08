<script setup lang="ts">
import type {Article} from '~/types/articles';

import ArticleCard from './ArticleCard/Card.vue';

defineProps<{
  articles:Article[];
}>();
</script>

<template>
  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
    <ArticleCard
      v-for="article in articles"
      :key="article.slug"
      :slug="article.slug"
      :title="article.title"
      :description="article.description"
      :thumbnail="article.thumbnail"
      :tags="article.tags"
      :difficulty="article.difficulty"
    />
  </div>
</template>
