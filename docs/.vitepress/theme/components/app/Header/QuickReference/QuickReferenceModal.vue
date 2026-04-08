<script setup lang="ts">
import { useDialog } from '~/composables/useDialog';

import type { DialogContext } from '~/types/dialog';

import {tNav} from '~/i18n/locales/shared/nav';
import { useData } from 'vitepress';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

import { useUI } from '~/composables/useUi';
import { ref, watch } from 'vue';
import AppIconButton from '../../AppIconButton.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';

const {
  isQuickReferenceModalOpen,
  closeModal,
}=useUI();

const dialogRef=ref<HTMLDialogElement|null>(null);

watch(
  isQuickReferenceModalOpen,
  (newValue)=>{
    if(newValue){
      dialogRef.value?.showModal();
      return;
    }

    dialogRef.value?.close();
  },
);
</script>

<template>
  <dialog
    ref="dialogRef"
    class="w-2xl p-4 shadow-lg bg-background rounded-sm top-1/2 left-1/2 -translate-1/2 backdrop:bg-black/40 backdrop:backdrop-blur-sm"
    @click.self="closeModal('quick-reference')"
  >
    <div class="flex justify-between items-center">
      <h2 class="font-medium">
        {{ t.quickReference.title }}
      </h2>
      <AppIconButton @click="closeModal('quick-reference')">
        <CloseIcon/>
      </AppIconButton>
    </div>
  </dialog>
</template>
