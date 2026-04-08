<script setup lang="ts">
import { ref } from 'vue';
import { useData } from 'vitepress';

import { SortingFilter } from '~/types/articles';

import ChevronLeftIcon from '../icons/ChevronLeftIcon.vue';
import ArticleSortByItem from './ArticleSortByItem.vue';

import { tFilter } from '~/i18n/locales/shared/filter';
import { convertStringToLocale } from '~/i18n';

const sortingFilter=defineModel<SortingFilter>({default:'nameAsc'});
const isOpen=ref(false);

const {lang}=useData();
const t=tFilter[convertStringToLocale(lang.value)??'en'];

const sortings:SortingFilter[]=[
  'nameAsc',
  'nameDesc',
  'difficultyAsc',
  'difficultyDesc',
];

function selectSorting(sorting:SortingFilter){
  sortingFilter.value=sorting;
  isOpen.value=false;
}
</script>

<template>
  <div class="flex gap-x-2 items-center">
    <span class="text-xs text-muted">
      {{ t.sort.label }}
    </span>
    <div class="relative">
      <button
        @click="isOpen=!isOpen"
        class="flex items-center gap-x-1 border border-border-color bg-surface px-4 py-2 rounded-sm"
      >
        <span>
          {{ t.sort[sortingFilter] }}
        </span>
        <ChevronLeftIcon
          class="rotate-90"
          :class="{
            '-rotate-90!':isOpen,
          }"
        />
      </button>
      <div
        class="absolute shadow-2xl hidden min-w-max w-full right-0 rounded-sm overflow-hidden"
        :class="{
          'block!':isOpen,
        }"
      >
        <ArticleSortByItem
          v-for="sorting in sortings"
          :key="sorting"
          @click="selectSorting(sorting)"
          :is-selected="sortingFilter===sorting"
        >
          {{ t.sort[sorting] }}
        </ArticleSortByItem>
      </div>
    </div>
  </div>
</template>
