<script setup lang="ts">
const date=new Date().getFullYear();
</script>

<template>
  <footer>
    <div class="max-w-4xl mx-auto p-4 flex justify-between items-center">
      <span>
        &copy; {{date}}
      </span>
      <span>
        Powered by <a href="https://astro.build/">Nuxt</a>
      </span>
    </div>
  </footer>
</template>
