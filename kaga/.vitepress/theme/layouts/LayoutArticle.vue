<script setup lang="ts">
import { Content } from 'vitepress';

import BaseLayout from './LayoutBase.vue';
</script>

<template>
  <BaseLayout>
    <div class="max-w-2xl h-full mx-auto p-4">
      <article class="prose max-w-none prose-a:text-primary prose-headings:text-body prose-p:text-muted prose-strong:text-body prose-hr:bg-border-color
        [&_mjx-container]:inline-block
        [&_mjx-container]:text-muted
        [&_mjx-container[display='true']]:my-8
        [&_mjx-container[display='true']]:flex!
        [&_mjx-container[display='true']]:justify-center!
      ">
        <Content/>
      </article>
    </div>
  </BaseLayout>
</template>
