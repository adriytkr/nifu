<script setup lang="ts">
import placeholderThumbnail from '@assets/images/placeholder.webp';

import ArticleTag from './ArticleTag.vue';

const props=defineProps<{
  title:string;
  description:string;
  thumbnail?:string;
  thumbnailAlt?:string;
  tags?:string[];
}>();
</script>

<template>
  <NuxtLinkLocale
    :to="`/articles/${''}`"
    class="group flex flex-col bg-white rounded-sm overflow-hidden hover:no-underline"
  >
    <div class="aspect-video">
      <img
        :src="thumbnail??placeholderThumbnail"
        :alt="thumbnailAlt??''"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="flex-1 flex flex-col p-4 pt-8">
      <div class="flex-1">
        <h2 class="mb-2 font-medium text-lg text-body transition-colors duration-200 group-hover:text-primary">{{title}}</h2>
        <p class="text-sm text-muted line-clamp-3">{{description}}</p>
      </div>
      <div class="mt-4" v-if="tags!==undefined">
        <ArticleTag
          v-for="tag in tags"
          :key="tag"
        >
          {{ tag }}
        </ArticleTag>
      </div>
    </div>
  </NuxtLinkLocale>
</template>
