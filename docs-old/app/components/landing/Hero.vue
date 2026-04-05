<script setup lang="ts">
import LandingSection from './Section.vue';
</script>

<template>
  <LandingSection>
    <div class="px-0 text-center md:px-32">
      <h1 class="mb-2 text-4xl font-bold">Welcome to Kaga</h1>
      <p class="mb-6 italic text-sm text-muted font-medium">
        (Knowledge Arises from Geometry and Algorithms)
      </p>
      <p class="mb-8 leading-relaxed">
        Kaga isn't your run-of-the-mill blog. I show how things actually work under the hood. By prioritizing <strong>intuition over memorization</strong> and using clever analogies, I make hard topics feel <strong>obvious and intuitive</strong>.
      </p>
      <NuxtLinkLocale
        to="/articles"
        class="inline-flex gap-x-2 items-center bg-primary/80 px-6 py-3 text-white font-bold rounded-lg transition-colors duration-200 hover:no-underline hover:bg-primary"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">
          <path d="m300-300 280-80 80-280-280 80-80 280Zm180-120q-25 0-42.5-17.5T420-480q0-25 17.5-42.5T480-540q25 0 42.5 17.5T540-480q0 25-17.5 42.5T480-420Zm0 340q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q133 0 226.5-93.5T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 133 93.5 226.5T480-160Zm0-320Z"/>
        </svg>
        Browse Articles
      </NuxtLinkLocale>
    </div>
  </LandingSection>
</template>
