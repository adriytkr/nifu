<script setup lang="ts">
import { onMounted, onUnmounted, ref, watch } from 'vue';

import SearchIcon from '~icons/SearchIcon.vue';
import KeyboardKey from '~/components/app/KeyboardKey.vue';

import SearchModal from './SearchModal.vue';
import { SearchDialogContext } from '~/types/dialog';

import {tNav} from '~/i18n/locales/shared/nav';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';
import { useData } from 'vitepress';

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

const emit=defineEmits<{
  (e:'show-header'):void;
}>();

const searchContext=ref<SearchDialogContext|null>(null);
const isModalOpen=ref(false);

function openModal(){
  isModalOpen.value=true;
  document.body.style.overflow='hidden';
  searchContext.value?.open();
}

function closeModal(){
  isModalOpen.value=false;
  document.body.style.overflow='auto';
  searchContext.value?.close();
}

function handleEsc(event:KeyboardEvent){
  if(event.key==='Escape'&&isModalOpen.value)
    closeModal();
}

watch(
  isModalOpen,
  (isOpen)=>{
    if(isOpen){
      window.addEventListener('keydown',handleEsc);
      return;
    }

    window.removeEventListener('keydown',handleEsc);
  },
  {immediate:true},
);

onUnmounted(()=>window.removeEventListener('keydown', handleEsc));

function handleKeyDown(event:KeyboardEvent){
  const commandFlag=
    (event.ctrlKey||event.metaKey)&&
    event.key.toLowerCase()==='k';

  if(!commandFlag)return;

  event.preventDefault();

  if(isModalOpen.value){
    searchContext.value?.focusInput();
    return;
  }

  if(document.fullscreenElement)document.exitFullscreen();

  emit('show-header');
  searchContext.value?.clearInput();
  openModal();
}

onMounted(()=>window.addEventListener('keydown',handleKeyDown));
onUnmounted(()=>window.removeEventListener('keydown',handleKeyDown));
</script>

<template>
  <Teleport to="body">
    <SearchModal
      ref="searchContext"
      @close="closeModal"
      :is-open="isModalOpen"
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isModalOpen,
      }"
    />
  </Teleport>
  <button
    class="group flex items-center border border-border-color bg-surface rounded-sm p-2 transition-colors duration-200 hover:border-body"
    @click="openModal"
  >
    <SearchIcon class="text-muted transition-colors duration-200 group-hover:text-body group-focus:text-body"/>
    <span class="ml-2 mr-10">
      {{ t.search.placeholder }}
    </span>
    <KeyboardKey is-not-single>Ctrl K</KeyboardKey>
  </button>
</template>
