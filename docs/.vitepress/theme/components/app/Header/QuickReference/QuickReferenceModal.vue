<script setup lang="ts">
import { ref, watch } from 'vue';
import { useData } from 'vitepress';

import {tNav} from '~/i18n/locales/shared/nav';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';

import { useUI } from '~/composables/useUi';

import AppButtonIcon from '~/components/app/AppButtonIcon.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

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
      <AppButtonIcon @click="closeModal('quick-reference')">
        <CloseIcon/>
      </AppButtonIcon>
    </div>
  </dialog>
</template>
