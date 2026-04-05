<script setup lang="ts">
import LanguagePickerButton from './LanguagePickerButton.vue';
</script>

<template>
  <div class="relative">
    <button data-select-language-btn>English</button>
    <div
      data-select-language-wrapper
      class="absolute right-0 top-full mt-2 bg-surface shadow-xl rounded-sm overflow-hidden opacity-0 pointer-events-none transition-opacity duration-200 [&.is-open]:opacity-100 [&.is-open]:pointer-events-auto"
    >
      <LanguagePickerButton locale="en">English</LanguagePickerButton>
      <LanguagePickerButton locale="pt-br">Português</LanguagePickerButton>
    </div>
  </div>
</template>
