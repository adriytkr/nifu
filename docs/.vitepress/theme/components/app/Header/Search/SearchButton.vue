<script setup lang="ts">
import { useData } from 'vitepress';

import {tNav} from '~/i18n/locales/shared/nav';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';

import { useUI } from '~/composables/useUi';
import SearchIcon from '~icons/SearchIcon.vue';
import KeyboardKey from '~/components/app/KeyboardKey.vue';
import SearchModal from './SearchModal.vue';
import NavTooltip from '../NavTooltip.vue';
import AppButtonIcon from '../../AppButtonIcon.vue';

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

const {
  isSearchModalOpen,
  openModal,
}=useUI();
</script>

<template>
  <Teleport to="body">
    <SearchModal
      class="opacity-0 transition-opacity duration-200"
      :class="{
        'opacity-100':isSearchModalOpen,
      }"
    />
  </Teleport>
  <button
    class="group items-center border border-border-color bg-surface rounded-sm p-2 transition-colors duration-200 hover:border-body hidden md:flex"
    @click="openModal('search')"
  >
    <SearchIcon class="text-muted transition-colors duration-200 group-hover:text-body group-focus:text-body"/>
    <span class="ml-2 mr-10">
      {{ t.search.placeholder }}
    </span>
    <KeyboardKey is-not-single>Ctrl K</KeyboardKey>
  </button>
  <NavTooltip class="md:hidden">
    <AppButtonIcon @click="openModal('search')">
      <SearchIcon/>
    </AppButtonIcon>
    <template #tooltip>
      {{ t.tooltip.search }}
    </template>
  </NavTooltip>
</template>
