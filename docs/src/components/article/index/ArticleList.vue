<script setup lang="ts">
import type { ArticleSchema } from '@/types/article';

import ArticleCard from './ArticleCard.vue';

defineProps<{
  articles:ArticleSchema[];
}>();
</script>

<template>
  <div class="w-full max-w-4xl grid grid-cols-3 gap-4 p-4">
    <ArticleCard
      v-for="article in articles"
      :key="article.id"
      :href="article.data.to"
      :title="article.data.title"
      :description="article.data.description"
      :difficulty="article.data.difficulty"
    />
  </div>
</template>
