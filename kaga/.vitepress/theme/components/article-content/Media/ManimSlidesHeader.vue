<script setup lang="ts">
import ExternalLinkIcon from '~/components/icons/ExternalLinkIcon.vue';

defineProps<{
  sourceCodeLink:string;
}>();

defineEmits<{
  (e:'enter-full-screen'):void;
}>();
</script>

<template>
  <div class="mb-2 flex justify-between items-center">
    <div>
      <a
        :href="sourceCodeLink"
        class="no-underline font-mono hover:underline"
      >
        [Source Code]
        <!-- <ExternalLinkIcon/> -->
      </a>
    </div>
    <div class="flex gap-x-2">
      <button class="text-primary font-mono hover:underline">
        [Shortcuts]
      </button>
      <button
        @click="$emit('enter-full-screen')"
        class="text-primary font-mono hover:underline"
      >
        [Full Screen]
      </button>
    </div>
  </div>
</template>
