<script setup lang="ts">
import {useTheme} from '~/composables/useTheme';

import IconButton from '~/components/base/IconButton.vue';
import SunIcon from '~/components/icons/theme/SunIcon.vue';
import MoonIcon from '~/components/icons/theme/MoonIcon.vue';

const {theme,toggleTheme}=useTheme();
</script>

<template>
  <IconButton @click="toggleTheme">
     <SunIcon v-if="theme==='light'"/>
     <MoonIcon v-else/>
  </IconButton>
</template>
