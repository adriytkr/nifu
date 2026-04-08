<script setup lang="ts">
import {Content} from 'vitepress';

import BaseLayout from './LayoutBase.vue';
</script>

<template>
  <BaseLayout>
    <div class="max-w-4xl h-full mx-auto p-4 [&>div]:h-full [&>div>div]:h-full">
      <Content/>
    </div>
  </BaseLayout>
</template>
