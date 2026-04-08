---
layout: normal
---

<script setup lang="ts">
import { nextTick, ref } from 'vue';

import type { SearchFilter } from '~/types/articles/article';
import {useFilter} from '~/composables/useFilter';

import ArticleFilter from '~/components/articles/ArticleFilter.vue';
import ArticleList from '~/components/articles/ArticleList.vue';

import {filter} from '~/i18n/locales/en/filter';
import { data as articles } from '~/content/en-articles.data.ts';

const {
  searchQuery,
  selectedSortingFilter,
  filteredArticles,
  matchesFound,
}=useFilter(articles);

const searchRef=ref<SearchFilter>();

async function clearSearch(){
  searchQuery.value='';
  await nextTick();
  searchRef.value?.focusInput();
}
</script>

<div class="min-h-full flex flex-col">
  <ArticleFilter
    ref="searchRef"
    v-model:query="searchQuery"
    v-model:sorting="selectedSortingFilter"
  />
  <div v-if="matchesFound>0">
    <p class="mb-4" v-if="searchQuery.trim().length>0">
      {{filter.matches(matchesFound,searchQuery)}}
    </p>
    <ArticleList :articles="filteredArticles"/>
  </div>
  <div
    v-else
    class="flex-1 flex flex-col items-center justify-center"
  >
    <p class="mb-2">
      {{filter.matches(0,searchQuery)}}
    </p>
    <button
      class="text-primary hover:underline"
      @click="clearSearch"
    >
      {{filter.clear}}
    </button>
  </div>
</div>
