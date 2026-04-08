<script setup lang="ts">
import AppButtonIcon from '~/components/app/AppButtonIcon.vue';
import KeyboardIcon from '~/components/icons/KeyboardIcon.vue';

import ShortcutsModal from './ShortcutsModal.vue';

import { useUI } from '~/composables/useUi';

const {
  isShortcutsModalOpen,
  openModal,
}=useUI();
</script>

<template>
  <Teleport to="body">
    <ShortcutsModal
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isShortcutsModalOpen,
      }"
    />
  </Teleport>
  <AppButtonIcon @click="openModal('shortcuts')">
    <KeyboardIcon/>
  </AppButtonIcon>
</template>
