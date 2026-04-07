<script setup lang="ts">
import {useSearchModal} from '~/composables/useSearchModal';

import ArrowKeyIcon from '~/components/icons/ArrowKeyIcon.vue';

import KeyboardKey from '../KeyboardKey.vue';
import SearchModalItem from './SearchModalItem.vue';

const props=defineProps<{
  isOpen:boolean;
}>();

const {
  selectedItemIndex,
  inputRef,
  searchQuery,
  clearSearch,
}=useSearchModal(()=>props.isOpen);
</script>

<template>
  <dialog class="absolute w-2xl shadow-lg bg-background rounded-sm top-1/2 left-1/2 -translate-1/2">
    <div class="p-4 flex">
      <input
        type="text"
        class="flex-1 outline-none"
        placeholder="Search articles"
        ref="inputRef"
        v-model="searchQuery"
      >
      <KeyboardKey>Ctrl K</KeyboardKey>
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
