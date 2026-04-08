<script setup lang="ts">
import {useSearchModal} from '~/composables/useSearchModal';

import KeyboardKey from '~/components/app/KeyboardKey.vue';
import ArrowKeyIcon from '~/components/icons/ArrowKeyIcon.vue';
import EnterKeyIcon from '~/components/icons/EnterKeyIcon.vue';

import AppButtonIcon from '~/components/app/AppButtonIcon.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';

import SearchModalItem from './SearchModalItem.vue';
import SearchIcon from '~/components/icons/SearchIcon.vue';

import {tNav} from '~/i18n/locales/shared/nav';
import {tFilter} from '~/i18n/locales/shared/filter';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';
import { useData } from 'vitepress';

import { useUI } from '~/composables/useUi';
import { watch } from 'vue';

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];
const t2=tFilter[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

const {
  dialogRef,
  inputRef,
  searchQuery,
  clearInput,
  focusInput,
  clearSearch,
  selectedItemIndex,
}=useSearchModal();

const {
  isSearchModalOpen,
  closeModal,
}=useUI();

watch(
  isSearchModalOpen,
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
    class="w-2xl shadow-lg bg-background rounded-sm top-10 left-1/2 -translate-x-1/2 backdrop:bg-black/40 backdrop:backdrop-blur-sm"
    @click.self="closeModal('search')"
  >
    <div class="p-4 flex items-center border border-border-color m-4">
      <SearchIcon
        class="text-muted cursor-text transition-colors duration-200 group-hover:text-body peer-focus-within:text-body"
        @click="focusInput"
      />
      <input
        type="text"
        class="mx-4 flex-1 outline-none"
        :placeholder="t.search.modal.placeholder"
        ref="inputRef"
        v-model="searchQuery"
      >
      <AppButtonIcon
        v-show="searchQuery.length>0"
        @click="clearSearch"
      >
        <CloseIcon/>
      </AppButtonIcon>
    </div>
    <div class="max-h-120 min-h-60 w-full overflow-y-auto">
      <div v-show="true">
        <p class="mx-4 mb-4">
          {{ t2.matches(10,searchQuery) }}
        </p>
        <ul>
          <SearchModalItem
            v-for="i in 10"
            :key="i"
            :is-selected="selectedItemIndex===i-1"
          />
        </ul>
      </div>
      <div
        class="w-full h-full flex justify-center items-center"
        v-show="false"
      >
        <div class="flex flex-col">
          <span>
            {{ t2.matches(0,searchQuery) }}
          </span>
          <button
            @click="clearSearch"
            class="text-primary hover:underline"
          >
            {{ t2.clear }}
          </button>
        </div>
      </div>
    </div>
    <ul class="p-4 flex gap-x-6 items-center">
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          <EnterKeyIcon/>
        </KeyboardKey>
        <span>
          {{ t.search.modal.toSelect }}
        </span>
      </li>
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          <ArrowKeyIcon class="-rotate-90"/>
        </KeyboardKey>
        <KeyboardKey>
          <ArrowKeyIcon class="rotate-90"/>
        </KeyboardKey>
        <span>
          {{ t.search.modal.toNavigate }}
        </span>
      </li>
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          Esc
        </KeyboardKey>
        <span>
          {{ t.search.modal.toClose }}
        </span>
      </li>
    </ul>
  </dialog>
</template>
