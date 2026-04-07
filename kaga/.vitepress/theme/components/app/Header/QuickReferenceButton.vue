<script setup lang="ts">
import { useModal } from '~/composables/useModal';

import AppIconButton from '../AppIconButton.vue';
import QuickReferenceIcon from '~/components/icons/QuickReferenceIcon.vue';

import QuickReferenceModal from './QuickReferenceModal.vue';

const {
  dialogContext,
  isModalOpen:isQuickReferenceModalOpen,
  closeModal: closeQuickReferenceModal,
  openModal: openQuickReferenceModal,
}=useModal();
</script>

<template>
  <Teleport to="body">
    <QuickReferenceModal
      ref="dialogContext"
      @close="closeQuickReferenceModal"
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isQuickReferenceModalOpen,
      }"
    />
  </Teleport>
  <AppIconButton @click="openQuickReferenceModal">
    <QuickReferenceIcon/>
  </AppIconButton>
</template>
