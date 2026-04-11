<script setup lang="ts">
import KagaLogo from '~icons/app/KagaLogo.vue';
import BrowserIcon from '~/components/icons/base/BrowserIcon.vue';
import LanguagePicker from './LanguagePicker.vue';
import ThemeToggleButton from './ThemeToggleButton.vue';
</script>

<template>
  <header class="bg-surface border-b-4 border-b-primary">
    <nav class="max-w-4xl mx-auto p-4 flex justify-between items-center">
      <VpLink to="/">
        <KagaLogo/>
      </VpLink>
      <ul class="flex items-center gap-x-4">
        <VpLink
          to="/articles"
          class="text-muted transition-colors duration-200 hover:text-body focus:text-body"
        >
          <BrowserIcon/>
        </VpLink>
        <ThemeToggleButton/>
        <LanguagePicker/>
      </ul>
    </nav>
  </header>
</template>
