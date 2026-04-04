<script setup lang="ts">
import { nextTick, ref } from 'vue';

import type { ArticleSchema } from '@/types/article';
import type {SearchFilter} from '@/types/article';
import type { Locale } from '@/types/i18n';

import { articlesPageT } from '@/i18n/articles-page';

import { useFilter } from '@/composables/useFilter';

import ArticleList from './ArticleList.vue';
import ArticleSearch from './ArticleSearch.vue';

const props=defineProps<{
  articles:ArticleSchema[];
  locale:Locale;
}>();

const t=articlesPageT[props.locale];

const searchRef=ref<SearchFilter>();

const {
  searchQuery,
  filteredArticles,
  matchesFound,
}=useFilter(props.articles);

async function clearSearch(){
  searchQuery.value='';
  await nextTick();
  searchRef.value?.focusInput();
}
</script>

<template>
  <div class="min-h-full flex flex-col">
    <div class="mb-8">
      <ArticleSearch
        ref="searchRef"
        v-model="searchQuery"
        :placeholder="t.placeholder"
      />
    </div>
    <div v-if="matchesFound>0">
      <p class="mb-4" v-if="searchQuery.trim().length>0">
        {{ t.matches(0,searchQuery) }}
      </p>
      <ArticleList
        :articles="filteredArticles"
        :locale="locale"
      />
    </div>
    <div
      v-else
      class="flex-1 flex flex-col items-center justify-center"
    >
      <p class="mb-2">
        {{ t.matches(0,searchQuery) }}
      </p>
      <button
        class="text-primary hover:underline"
        @click="clearSearch"
      >
        {{ t.clear }}
      </button>
    </div>
  </div>
</template>
