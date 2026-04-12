<script setup lang="ts">
import type { ArticleSchema } from '~/types/article.schema';

import ArticleCard from './ArticleCard.vue';

defineProps<{
  articles:ArticleSchema[];
}>();
</script>

<template>
  <ul class="not-prose flex flex-col">
    <ArticleCard
      v-for="article in articles"
      :key="article.slug"
      :article="article"
    />
  </ul>
</template>
