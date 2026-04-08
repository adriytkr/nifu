<script setup lang="ts">
import { ArticleDifficulty } from '~/types/articles';
import { tTags } from '~/i18n/locales/shared/tags';
import { useData } from 'vitepress';

import CardTag from './CardTag.vue';
import CardDifficulty from './CardDifficulty.vue';
import { convertStringToLocale } from '~/i18n';

const props=defineProps<{
  slug:string;
  title:string;
  description:string;
  thumbnail?:string;
  thumbnailAlt?:string;
  tags?:string[];
  difficulty:ArticleDifficulty;
}>();

const {lang}=useData();
const t=tTags[convertStringToLocale(lang.value)??'en'];
</script>

<template>
  <VpLink
    :to="`/articles/${slug}`"
    class="group flex flex-col bg-surface rounded-sm overflow-hidden hover:no-underline"
  >
    <div class="aspect-video">
      <img
        :src="thumbnail??'/images/placeholder-img.png'"
        :alt="thumbnailAlt??''"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="flex-1 flex flex-col p-4 pt-8">
      <div>
        <CardDifficulty :difficulty="difficulty"/>
      </div>
      <div class="flex-1">
        <h2 class="mb-2 font-medium text-lg text-body transition-colors duration-200 group-hover:text-primary">{{title}}</h2>
        <p class="text-sm text-muted line-clamp-3">{{description}}</p>
      </div>
      <div class="mt-4" v-if="tags!==undefined">
        <CardTag
          v-for="tag in tags"
          :key="tag"
        >
          {{ t[tag]??tag }}
        </CardTag>
      </div>
    </div>
  </VpLink>
</template>
