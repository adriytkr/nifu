<script setup lang="ts">
import VpLink from '~/components/base/VpLink.vue';

defineProps<{
  to:string;
}>();
</script>

<template>
  <li class="group text-body">
    <VpLink
      :to="to"
      class="block text-center text-inherit py-2 font-medium transition-colors duration-200 group-hover/nav:text-muted group-focus-within/nav:text-muted hover:text-primary! focus-within:text-primary! hover:no-underline"
    >
      <slot></slot>
    </VpLink>
  </li>
</template>
