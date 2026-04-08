<script setup lang="ts">
import { SearchFilter, SortingFilter } from '~/types/articles';

import ArticleSearch from './ArticleSearch.vue';
import ArticleSortBy from './ArticleSortBy.vue';
import { ref } from 'vue';

const query=defineModel<string>('query',{default:''});
const sorting=defineModel<SortingFilter>('sorting',{default:'nameAsc'});

const searchRef=ref<SearchFilter|null>(null);

function focusInput(){
  searchRef.value?.focusInput();
}

defineExpose<SearchFilter>({
  focusInput,
});
</script>

<template>
  <div class="mb-8 gap-y-4 flex flex-col items-center md:flex-row md:justify-between">
    <ArticleSearch
      ref="searchRef"
      v-model="query"
    />
    <ArticleSortBy v-model="sorting"/>
  </div>
</template>
