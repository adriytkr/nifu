---
layout: large
---

<script setup lang="ts">
import {provide} from 'vue';

import {useArticles} from '~/composables/useArticles';
import {ViewModeKey} from '~/types/filter';

import ArticleQuery from '~/components/articles/ArticleQuery.vue';
import ArticleViewMode from '~/components/articles/ArticleViewMode.vue';

import ArticleList from '~/components/articles/ArticleList.vue';

const {
  query,
  filteredArticles,
  matchesFound,
  queryRef,
  selectedViewMode,
}=useArticles();

provide(ViewModeKey,selectedViewMode);
</script>

<div class="sm:max-w-md mx-auto">
  <ArticleQuery
    placeholder="Search articles"
    v-model="query"
    ref="queryRef"
  />
  <div class="mt-4">
    <ArticleViewMode v-model="selectedViewMode"/>
  </div>
</div>

<div
  class="not-prose mt-4 px-4"
  v-show="query.trim().length>0"
>
  <p v-show="matchesFound>0">
    {{matchesFound}} {{matchesFound===1?'match':'matches'}} for "{{query}}"
  </p>
  <div v-show="matchesFound===0">
    <p>
      No matches for "{{query}}"
    </p>
    <button
      @click="queryRef.clearInput"
      class="text-primary hover:underline"
    >
      Clear Search
    </button>
  </div>
</div>

<div class="mt-8">
  <ArticleList
    :articles="filteredArticles"
    :view-mode="selectedViewMode"
  />
</div>
