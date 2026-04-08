<script setup lang="ts">
import { computed, ref } from 'vue';
import { useData } from 'vitepress';

import { useHideOnScroll } from '~/composables/useHideOnScroll';
import { useTheme } from '~/composables/useTheme';

import AppLogo from '~icons/LogoIcon.vue';

import NavTooltip from '../NavTooltip.vue';

import BrowserIcon from '~/components/icons/BrowserIcon.vue';
import SearchButton from './Search/SearchButton.vue';
import QuickReferenceButton from './QuickReference/QuickReferenceButton.vue';
import ShortcutsButton from './Shortcuts/ShortcutsButton.vue';
import LanguagePicker from './LanguagePicker/LanguagePicker.vue';
import ThemeToggleButton from './ThemeToggle//ThemeToggleButton.vue';

import {tNav} from '~/i18n/locales/shared/nav';
import {
  convertStringToLocale,
  DEFAULT_LOCALE,
} from '~/i18n';

const {isHeaderVisible}=useHideOnScroll();

const isLanguagePickerModalOpen=ref(false);

const {lang}=useData();
const t=tNav[convertStringToLocale(lang.value)??DEFAULT_LOCALE];

const {theme}=useTheme();
const themeTooltipMessage=computed<string>(()=>
  theme.value==='light'
    ?t.tooltip.theme.light
    :t.tooltip.theme.dark
);
</script>

<template>
  <header
    class="sticky z-50 bg-background transition-transform duration-300 ease-in-out top-0"
    :class="{
      '-translate-y-full':!isHeaderVisible,
    }"
  >
    <nav class="max-w-4xl mx-auto p-4 flex justify-between items-center">
      <VpLink to="/">
        <AppLogo/>
      </VpLink>
      <div class="flex items-center">
        <div class="flex items-center gap-x-4">
          <NavTooltip>
            <VpLink
              to="/articles"
              class="text-muted transition-colors duration-200 hover:text-body focus:text-body"
            >
              <BrowserIcon/>
            </VpLink>
            <template #tooltip>
              {{ t.tooltip.articles }}
            </template>
          </NavTooltip>
          <NavTooltip>
            <QuickReferenceButton/>
            <template #tooltip>
              {{ t.tooltip.quickReference }}
            </template>
          </NavTooltip>
          <NavTooltip>
            <ShortcutsButton/>
            <template #tooltip>
              {{ t.tooltip.shortcuts }}
            </template>
          </NavTooltip>
          <SearchButton/>
        </div>
        <div class="h-5 w-0.5 mx-4 bg-slate-200"></div>
        <div class="flex items-center gap-x-4">
          <NavTooltip :disabled="isLanguagePickerModalOpen">
            <LanguagePicker v-model:open="isLanguagePickerModalOpen"/>
            <template #tooltip>
              {{ t.tooltip.language }}
            </template>
          </NavTooltip>
          <NavTooltip>
            <ThemeToggleButton/>
            <template #tooltip>
              {{ themeTooltipMessage }}
            </template>
          </NavTooltip>
        </div>
      </div>
    </nav>
  </header>
</template>
