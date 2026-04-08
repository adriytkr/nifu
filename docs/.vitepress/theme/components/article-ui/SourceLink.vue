<script setup lang="ts">
defineProps<{
  href:string;
}>();
</script>

<template>
  <a
    :href="href"
    class="inline-flex gap-x-2 items-center no-underline text-body! hover:underline"
  >
    <slot></slot>
  </a>
</template>
