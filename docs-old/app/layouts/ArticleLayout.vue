<script setup lang="ts">
import type {Heading} from '~/types/article';

import BaseLayout from './BaseLayout.vue';
import TableOfContent from '~/components/article/post/TableOfContent.vue';

defineProps<{
  headings?:Heading[];
}>();
</script>

<template>
  <BaseLayout>
    <div class="flex">
      <div class="flex-1"></div>
      <article class="prose max-w-2xl mx-auto my-8 px-4 w-full prose-p:text-body prose-headings:text-body prose-strong:text-body prose-hr:border-t-2 prose-a:text-primary prose-a:no-underline prose-a:hover:underline prose-li:text-body">
        <slot></slot>
      </article>
      <aside class="flex-1 ml-8 my-8">
        <TableOfContent :headings="headings"/>
      </aside>
    </div>
  </BaseLayout>
</template>
