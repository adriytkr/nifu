<script setup lang="ts">
import { ref } from 'vue';

import ExternalLinkIcon from '~/components/icons/ExternalLinkIcon.vue';
import ManimSlidesShortcutsModal from './ManimSlidesShortcutsModal.vue';
import { useShortcutsModal } from '~/composables/useShortcutsModal';

defineProps<{
  sourceCodeLink:string;
}>();

defineEmits<{
  (e:'enter-full-screen'):void;
}>();

const {
  isShortcutsModalOpen,
  openShortcutsModal,
  closeShortcutsModal,
}=useShortcutsModal();
</script>

<template>
  <Teleport to="body">
    <div
      class="fixed w-full h-full top-0 left-0 pointer-events-none"
      :class="{
        'pointer-events-auto! bg-black/40 backdrop-blur-xs':isShortcutsModalOpen,
      }"
      @click.self="closeShortcutsModal"
    >
      <ManimSlidesShortcutsModal
        class="opacity-0 transition-opacity duration-200"
        :class="{
          'opacity-100':isShortcutsModalOpen,
        }"
        @close="closeShortcutsModal"
      />
    </div>
  </Teleport>
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
      <button
        class="text-primary font-mono hover:underline"
        @click="openShortcutsModal"
      >
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
