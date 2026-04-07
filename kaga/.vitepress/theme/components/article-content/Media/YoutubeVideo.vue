<script setup lang="ts">
defineProps<{
  id:string;
}>();
</script>

<template>
  <MediaWithCaption>
    <template #media>
      <lite-youtube
        :videoid="id"
        class="relative w-full h-auto rounded-sm overflow-hidden"
        params="modestbranding=1&rel=0&vq=hd720"
      />
    </template>
    <template #caption>
      <slot></slot>
    </template>
  </MediaWithCaption>
</template>
