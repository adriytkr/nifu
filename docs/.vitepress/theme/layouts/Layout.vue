<script setup lang="ts">
import { useData } from 'vitepress';

import { useShortcuts } from '~/composables/useShortcuts';

import NormalLayout from './LayoutNormal.vue';
import ArticleLayout from './LayoutArticle.vue';

const { frontmatter }=useData();

useShortcuts();
</script>

<template>
  <NormalLayout v-if="frontmatter.layout==='normal'"/>
  <ArticleLayout v-else-if="frontmatter.layout==='article'"/>
  <div v-else>
    <p>Couldn't load any layout :/</p>
  </div>
</template>
