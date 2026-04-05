<script setup lang="ts">
import BaseLayout from './base-layout.vue';
</script>

<template>
  <BaseLayout>
    <div class="max-w-2xl h-full mx-auto p-4">
      <article>
        <slot></slot>
      </article>
    </div>
  </BaseLayout>
</template>
