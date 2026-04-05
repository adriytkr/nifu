<script setup lang="ts">
import MediaWithCaption from './MediaWithCaption.vue';

defineProps<{
  id:string;
  title:string;
}>();
</script>

<template>
  <MediaWithCaption>
    <template #media>
      <YouTube
        id={id}
        title={title}
        params="vq=hd720"
        class="w-full h-auto rounded-sm"
      />
    </template>
    <slot></slot>
  </MediaWithCaption>
</template>
