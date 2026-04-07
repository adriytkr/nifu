<script setup lang="ts">
import { useModal } from '~/composables/useModal';

import ExternalLinkIcon from '~/components/icons/ExternalLinkIcon.vue';
import ManimSlidesShortcutsModal from './ManimSlidesShortcutsModal.vue';

defineProps<{
  sourceCodeLink:string;
}>();

defineEmits<{
  (e:'enter-full-screen'):void;
}>();

const {
  dialogContext,
  isModalOpen:isShortcutsModalOpen,
  openModal:openShortcutsModal,
  closeModal:closeShortcutsModal,
}=useModal();
</script>

<template>
  <Teleport to="body">
    <ManimSlidesShortcutsModal
      ref="dialogContext"
      @close="closeShortcutsModal"
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isShortcutsModalOpen,
      }"
    />
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
