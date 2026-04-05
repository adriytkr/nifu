<script setup lang="ts">
defineProps<{
  title?:string;
}>();
</script>

<template>
  <section class="mb-12 md:mb-20 lg:mb-32">
    <h2 class="mb-6 text-2xl font-bold" v-if="title">{{ title }}</h2>
    <slot></slot>
  </section>
</template>
