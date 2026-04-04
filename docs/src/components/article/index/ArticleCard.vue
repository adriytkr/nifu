<script setup lang="ts">
import { inject } from 'vue';

import type {
  ArticleTagType,
  ArticleTagList,
} from '@/types/article';

import { tagTranslations } from '@/i18n/tags';
import placeholderThumbnail from '@assets/images/placeholder.webp';

import ArticleTag from './ArticleTag.vue';

defineProps<{
  href:string;
  title:string;
  description:string;
  thumbnail?:string;
  thumbnailAlt?:string;
  tags?:ArticleTagType[];
}>();

const t=inject<ArticleTagList>('tags',tagTranslations.en);
</script>

<template>
  <a
    class="group flex flex-col bg-white rounded-sm overflow-hidden hover:no-underline"
    :href="href"
  >
    <div class="aspect-video">
      <img
        :src="thumbnail??placeholderThumbnail.src"
        :alt="thumbnailAlt??''"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="flex-1 flex flex-col p-4 pt-8">
      <div class="flex-1 mb-4">
        <h2 class="mb-2 font-medium text-lg text-body transition-colors duration-200 group-hover:text-primary">{{title}}</h2>
        <p class="text-sm text-muted line-clamp-3">{{description}}</p>
      </div>
      <div>
        <ArticleTag
          v-for="tag in tags"
          :key="tag"
        >
          {{ t?.[tag]??tag }}
        </ArticleTag>
      </div>
    </div>
  </a>
</template>
