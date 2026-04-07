<script setup lang="ts">
import { useHideOnScroll } from '~/composables/useHideOnScroll';

import AppLogo from '~icons/LogoIcon.vue';

import BrowserIcon from '~/components/icons/BrowserIcon.vue';

import SearchButton from './SearchButton.vue';
import QuickReferenceButton from './QuickReferenceButton.vue';

import LanguagePicker from './LanguagePicker.vue';
import ThemeToggleButton from './ThemeToggleButton.vue';

const {scrollClass,showHeader}=useHideOnScroll();
</script>

<template>
  <header :class="[
      'sticky z-50 bg-background transition-transform duration-300 ease-in-out top-0 [&.scroll-down]:-translate-y-full [&.scroll-up]:translate-y-0',
      scrollClass,
    ]"
  >
    <nav class="max-w-4xl mx-auto p-4 flex justify-between items-center">
      <VpLink to="/">
        <AppLogo/>
      </VpLink>
      <div class="flex items-center">
        <div class="flex items-center gap-x-4">
          <VpLink
            to="/articles"
            class="text-muted transition-colors duration-200 hover:text-body focus:text-body"
          >
            <BrowserIcon/>
          </VpLink>
          <QuickReferenceButton/>
          <SearchButton @show-header="showHeader"/>
        </div>
        <div class="h-5 w-0.5 mx-4 bg-slate-200"></div>
        <div class="flex items-center gap-x-4">
          <LanguagePicker/>
          <ThemeToggleButton/>
        </div>
      </div>
    </nav>
  </header>
</template>
