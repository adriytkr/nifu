<script setup lang="ts">
import placeholderImage from '~/assets/images/placeholder.webp';

import MediaWithCaption from './MediaWithCaption.vue';

defineProps<{
  src?:string;
  alt?:string;
  zoomable:boolean;
}>();
</script>

<template>
  <MediaWithCaption>
    <template #media>
      <img
        :src="src??placeholderImage"
        :alt="alt??''"
        class="w-full h-auto block object-cover rounded-sm"
      />
    </template>
    <slot></slot>
  </MediaWithCaption>
</template>
