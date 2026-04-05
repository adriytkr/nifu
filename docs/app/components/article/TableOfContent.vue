<script setup lang="ts">
import { buildToc } from '~/utils/article';
import type { Heading } from '~/types/article';

import TableOfContentsItem from './TableOfContentsItem.vue';

const props=defineProps<{
  headings:Heading[];
}>();

const toc=buildToc(
  props.headings.filter((heading)=>
    heading.depth>1&&
    heading.depth<4
  ),
);
</script>
<template>
  
  <nav class="sticky top-8 max-h-[calc(100vh-4rem)] overflow-y-auto" id="toc-nav">
    <span class="block mb-4 text-xs font-bold uppercase tracking-widest text-body">On this page</span>
    <ul class="space-y-3 text-sm">
      Table of Contents
    </ul>
  </nav>
</template>
