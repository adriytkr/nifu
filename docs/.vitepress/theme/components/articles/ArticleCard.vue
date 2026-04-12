<script setup lang="ts">
import { inject } from 'vue';

import type { ArticleSchema } from '~/types/article.schema';
import { ViewModeKey } from '~/types/filter';

import VpLink from '~/components/base/VpLink.vue';

defineProps<{
  article:ArticleSchema;
}>();

const selectedViewMode=inject(ViewModeKey);
</script>

<template>
  <li>
    <VpLink
      class="group block"
      :class="{
        'grid gap-6 p-4 transition-colors duration-200 sm:grid-cols-2 md:grid-cols-[1fr_2fr] hover:bg-primary/10 hover:no-underline':selectedViewMode==='list',
        'hover:ring-4 hover:ring-primary':selectedViewMode==='grid',
      }"
      :to="`/articles/${article.slug}`"
    >
      <div class="aspect-video overflow-hidden">
        <img
          :src="article.thumbnail??'/images/placeholder.png'"
          alt=""
          class="w-full h-full object-cover"
          :class="{
            'transition-transform duration-500 group-hover:scale-110':selectedViewMode==='list'
          }"
          loading="lazy"
        />
      </div>
      <div v-show="selectedViewMode==='list'">
        <h2 class="text-body text-xl mb-2 sm:mb-5">{{ article.title }}</h2>
        <p class="text-muted line-clamp-3">{{ article.description }}</p>
      </div>
    </VpLink>
  </li>
</template>
