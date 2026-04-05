<script setup lang="ts">
defineProps<{
  slug:string;
}>();
</script>

<template>
  <li>
    <NuxtLinkLocale
      :to="`#${slug}`"
      class="inline-block text-muted no-underline transition-colors hover:text-body [&.active]:text-primary [&.active]:font-medium"
    >
      <slot></slot>
    </NuxtLinkLocale>
  </li>
</template>
