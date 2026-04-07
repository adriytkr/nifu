<script setup lang="ts">
import { useModal } from '~/composables/useModal';

import AppIconButton from '../AppIconButton.vue';
import QuickReferenceIcon from '~/components/icons/QuickReferenceIcon.vue';

import QuickReferenceModal from './QuickReferenceModal.vue';

const {
  dialogContext,
  closeModal: closeQuickReferenceModal,
  openModal: openQuickReferenceModal,
}=useModal();
</script>

<template>
  <Teleport to="body">
    <QuickReferenceModal
      ref="dialogContext"
      @close="closeQuickReferenceModal"
    />
  </Teleport>
  <AppIconButton @click="openQuickReferenceModal">
    <QuickReferenceIcon/>
  </AppIconButton>
</template>
