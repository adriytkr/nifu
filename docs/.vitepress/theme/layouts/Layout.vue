<script setup lang="ts">
import { useData } from 'vitepress';

import ArticleLayout from './LayoutArticle.vue';

const { frontmatter }=useData();
</script>

<template>
  <ArticleLayout v-if="frontmatter.layout===undefined"/>
</template>
