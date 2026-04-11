<script setup lang="ts">
const date=new Date().getFullYear();
</script>

<template>
  <footer class="bg-primary text-white">
    <div class="max-w-4xl mx-auto px-4 py-8 text-sm">
      <p class="text-center mb-4">
        <i>
          "If you cannot explain a concept to a five-years-old boy, you don't understand it well enough."
        </i>
      </p>
      <div class="flex justify-between items-center">
        <span>
          &copy; {{date}} Kaga
        </span>
        <span>
          Powered by
          <a
            href="https://vitepress.dev/"
            class="text-white font-bold"
          >
            Vitepress
          </a>
        </span>
      </div>
    </div>
  </footer>
</template>
