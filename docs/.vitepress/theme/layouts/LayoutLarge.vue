<script setup lang="ts">
import { Content } from 'vitepress';

import LayoutBase from './LayoutBase.vue';
</script>

<template>
  <LayoutBase>
    <div class="max-w-4xl h-full mx-auto px-4 py-12">
      <article class="prose max-w-none prose-headings:text-body prose-p:text-muted prose-hr:bg-surface prose-hr:h-0.5">
        <Content/>
      </article>
    </div>
  </LayoutBase>
</template>
