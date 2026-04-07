<script setup lang="ts">
defineProps<{
  href:string;
}>();
</script>

<template>
  <a
    :href="href"
    class="flex gap-x-2 items-center no-underline text-black! hover:underline"
  >
    <slot></slot>
  </a>
</template>
