<script setup lang="ts">
import placeholderThumbnail from '@assets/images/placeholder.webp';

defineProps<{
  href:string;
  title:string;
  description:string;
  thumbnail?:string;
  thumbnailAlt?:string;
}>();
</script>

<template>
  <a
    class="group flex flex-col bg-white rounded-sm overflow-hidden hover:no-underline"
    :href="href"
  >
    <div class="aspect-video">
      <img
        :src="thumbnail??placeholderThumbnail.src"
        :alt="thumbnailAlt??''"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="flex-1 p-4 pt-8">
      <h2 class="font-medium text-lg text-body transition-colors duration-200 group-hover:text-primary">{{title}}</h2>
      <p class="text-sm text-muted">{{description}}</p>
    </div>
  </a>
</template>
