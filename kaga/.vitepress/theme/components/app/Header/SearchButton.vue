<script setup lang="ts">
import { useModal } from '~/composables/useModal';

import SearchIcon from '~icons/SearchIcon.vue';
import KeyboardKey from '../KeyboardKey.vue';

import SearchModal from './SearchModal.vue';

const {
  dialogContext,
  isModalOpen:isSearchModalOpen,
  closeModal: closeSearchModal,
  openModal: openSearchModal,
}=useModal();
</script>

<template>
  <Teleport to="body">
    <SearchModal
      ref="dialogContext"
      @close="closeSearchModal"
      :is-open="isSearchModalOpen"
    />
  </Teleport>
  <button
    class="group flex items-center border border-border-color rounded-sm p-2 transition-colors duration-200 hover:border-body"
    @click="openSearchModal"
  >
    <SearchIcon class="transition-colors duration-200 group-hover:text-body group-focus:text-body"/>
    <span class="ml-2 mr-6">Search articles</span>
    <KeyboardKey>Ctrl K</KeyboardKey>
  </button>
</template>
