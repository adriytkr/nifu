<script setup lang="ts">
import {useSearchModal} from '~/composables/useSearchModal';
import type { SearchDialogContext } from '~/types/dialog';

import KeyboardKey from '../KeyboardKey.vue';
import ArrowKeyIcon from '~/components/icons/ArrowKeyIcon.vue';
import EnterKeyIcon from '~/components/icons/EnterKeyIcon.vue';

import AppIconButton from '../AppIconButton.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';

import SearchModalItem from './SearchModalItem.vue';
import SearchIcon from '~/components/icons/SearchIcon.vue';

const props=defineProps<{
  isOpen:boolean;
}>();

defineEmits<{
  (e:'close'):void;
}>();

const {
  selectedItemIndex,
  inputRef,
  searchQuery,
  clearSearch,
  context,
  dialogRef,
}=useSearchModal(()=>props.isOpen);

defineExpose<SearchDialogContext>(context);
</script>

<template>
  <dialog
    ref="dialogRef"
    class="w-2xl shadow-lg bg-background rounded-sm top-1/2 left-1/2 -translate-1/2 backdrop:bg-black/40 backdrop:backdrop-blur-sm"
    @click.self="$emit('close')"
  >
    <div class="p-4 flex">
      <div class="group flex flex-1 items-center mr-4">
        <SearchIcon
          class="text-muted cursor-text transition-colors duration-200 group-hover:text-body peer-focus-within:text-body"
          @click="context.focusInput()"
        />
        <input
          type="text"
          class="mx-4 flex-1 outline-none"
          placeholder="Search articles"
          ref="inputRef"
          v-model="searchQuery"
        >
        <AppIconButton
          v-show="searchQuery.length>0"
          @click="context.clearInput();context.focusInput()"
        >
          <CloseIcon/>
        </AppIconButton>
      </div>
      <KeyboardKey is-not-single>Ctrl K</KeyboardKey>
    </div>
    <hr class="border-t-border-color">
    <div class="max-h-60 h-60 w-full overflow-y-auto">
      <div v-if="false">
        <p class="mx-6 my-2">
          5 matches for "{{ searchQuery }}"
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
        v-show="true"
      >
        <div class="flex flex-col">
          <span>
            No articles for "{{ searchQuery }}"
          </span>
          <button
            @click="clearSearch"
            class="text-primary hover:underline"
          >
            Clear Search
          </button>
        </div>
      </div>
    </div>
    <hr class="border-t-border-color">
    <ul class="p-4 flex gap-x-6 items-center">
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          <EnterKeyIcon/>
        </KeyboardKey>
        <span>to select</span>
      </li>
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          <ArrowKeyIcon class="-rotate-90"/>
        </KeyboardKey>
        <KeyboardKey>
          <ArrowKeyIcon class="rotate-90"/>
        </KeyboardKey>
        <span>to navigate</span>
      </li>
      <li class="flex items-center gap-x-2">
        <KeyboardKey>
          esc
        </KeyboardKey>
        <span>to close</span>
      </li>
    </ul>
  </dialog>
</template>
