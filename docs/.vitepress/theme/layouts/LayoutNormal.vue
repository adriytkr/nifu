<script setup lang="ts">
import {Content} from 'vitepress';

import LayoutBase from './LayoutBase.vue';
</script>

<template>
  <LayoutBase>
    <div class="h-full [&>div]:h-full [&>div>div]:h-full">
      <Content/>
    </div>
  </LayoutBase>
</template>
