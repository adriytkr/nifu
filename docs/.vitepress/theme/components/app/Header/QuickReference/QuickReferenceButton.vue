<script setup lang="ts">
import { useUI } from '~/composables/useUi';

import AppButtonIcon from '~/components/app/AppButtonIcon.vue';
import QuickReferenceIcon from '~/components/icons/QuickReferenceIcon.vue';

import QuickReferenceModal from './QuickReferenceModal.vue';

const {
  isQuickReferenceModalOpen,
  openModal,
}=useUI();
</script>

<template>
  <Teleport to="body">
    <QuickReferenceModal
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isQuickReferenceModalOpen,
      }"
    />
  </Teleport>
  <AppButtonIcon @click="openModal('quick-reference')">
    <QuickReferenceIcon/>
  </AppButtonIcon>
</template>
