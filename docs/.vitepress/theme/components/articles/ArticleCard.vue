<script setup lang="ts">
import type { ArticleSchema } from '~/types/article.schema';

import VpLink from '~/components/base/VpLink.vue';

defineProps<{
  article:ArticleSchema;
}>();
</script>

<template>
  <li>
    <VpLink
      class="group grid gap-6 p-4 rounded-md transition-colors duration-200 sm:grid-cols-2 md:grid-cols-[1fr_2fr] hover:bg-primary/10 hover:no-underline"
      :to="`/articles/${article.slug}`"
    >
      <div class="aspect-video overflow-hidden rounded-md">
        <img
          :src="article.thumbnail??'/images/placeholder.png'"
          alt=""
          class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
          loading="lazy"
        />
      </div>
      <div>
        <h2 class="text-body text-xl mb-2 sm:mb-5">{{ article.title }}</h2>
        <p class="text-muted line-clamp-3">{{ article.description }}</p>
      </div>
    </VpLink>
  </li>
</template>
