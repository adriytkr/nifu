<script setup lang="ts">
import { useData } from 'vitepress';

import LayoutArticle from './LayoutArticle.vue';
import LayoutLarge from './LayoutLarge.vue';

const { frontmatter }=useData();
</script>

<template>
  <LayoutArticle v-if="frontmatter.layout===undefined"/>
  <LayoutLarge v-else-if="frontmatter.layout==='large'"/>
</template>
