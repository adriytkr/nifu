<script setup lang="ts">
import AppIconButton from '~/components/app/AppIconButton.vue';
import QuickReferenceIcon from '~/components/icons/QuickReferenceIcon.vue';

import QuickReferenceModal from './QuickReferenceModal.vue';

import { useUI } from '~/composables/useUi';

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
  <AppIconButton @click="openModal('quick-reference')">
    <QuickReferenceIcon/>
  </AppIconButton>
</template>
