<script setup lang="ts">
import EnterKeyIcon from '~/components/icons/EnterKeyIcon.vue';

defineProps<{
  isSelected:boolean;
}>();
</script>

<template>
  <li class="m-2">
    <a
      href="#"
      class="group flex gap-x-4 items-center p-4 rounded-sm transition-colors duration-200 bg-border-color hover:no-underline hover:bg-primary"
    >
      <div class="flex flex-col">
        <h2 class="text-body font-medium text-lg line-clamp-1 transition-colors duration-200 group-hover:text-white">This is an article</h2>
        <p class="text-sm text-muted line-clamp-2 transition-colors duration-200 group-hover:text-white">
          This is a super long description of the article, really, really long description. Do you believe in me?
        </p>
      </div>
      <span class="opacity-0 transition-opacity duration-200 group-hover:opacity-100">
        <EnterKeyIcon class="text-white"/>
      </span>
    </a>
  </li>
</template>
