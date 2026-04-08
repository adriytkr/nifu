<script setup lang="ts">
import {useTheme} from '~/composables/useTheme';

import AppButtonIcon from '../AppButtonIcon.vue';
import SunIcon from '~/components/icons/SunIcon.vue';
import MoonIcon from '~/components/icons/MoonIcon.vue';

const {theme,toggleTheme}=useTheme();
</script>

<template>
  <AppButtonIcon @click="toggleTheme">
     <SunIcon v-if="theme==='light'"/>
     <MoonIcon v-else/>
  </AppButtonIcon>
</template>
