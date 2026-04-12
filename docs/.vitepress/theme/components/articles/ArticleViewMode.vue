<script setup lang="ts">
import { ViewMode } from '~/types/filter';

import ArticleViewModeButton from './ArticleViewModeButton.vue';

const selectedViewMode=defineModel<ViewMode>({default:'list'});
</script>

<template>
  <div class="flex gap-x-2">
    <ArticleViewModeButton
      @click="selectedViewMode='list'"
      :is-selected="selectedViewMode==='list'"
    >
      List
    </ArticleViewModeButton>
    <ArticleViewModeButton
      @click="selectedViewMode='grid'"
      :is-selected="selectedViewMode==='grid'"
    >
      Grid
    </ArticleViewModeButton>
  </div>
</template>
