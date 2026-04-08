<script setup lang="ts">
import AppIconButton from '~/components/app/AppIconButton.vue';
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
  <AppIconButton @click="openModal('shortcuts')">
    <KeyboardIcon/>
  </AppIconButton>
</template>
