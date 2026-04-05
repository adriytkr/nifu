<script setup lang="ts">
import { nextTick, ref } from 'vue';

import type { ArticleSchema } from '~/types/article';
import type {SearchFilter} from '~/types/article';

import { useFilter } from '~/composables/useFilter';

import ArticleList from './ArticleList.vue';
import ArticleSearch from './ArticleSearch.vue';

const props=defineProps<{
  articles:ArticleSchema[];
}>();

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
      />
    </div>
    <div v-if="matchesFound>0">
      <p class="mb-4" v-if="searchQuery.trim().length>0">
        No matches found
      </p>
      <ArticleList :articles="filteredArticles"/>
    </div>
    <div
      v-else
      class="flex-1 flex flex-col items-center justify-center"
    >
      <p class="mb-2">
        No matches found for "bismarck"
      </p>
      <button
        class="text-primary hover:underline"
        @click="clearSearch"
      >
        Clear Search
      </button>
    </div>
  </div>
</template>
