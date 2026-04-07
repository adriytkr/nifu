<script setup lang="ts">
import SourceLink from './SourceLink.vue';
import GithubIcon from '../icons/GithubIcon.vue';

defineProps<{
  href:string;
}>();
</script>

<template>
  <SourceLink :href="href">
    <GithubIcon/>
    <slot></slot>
  </SourceLink>
</template>
