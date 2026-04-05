<script setup lang="ts">
import Logo from './Logo.vue';
import SearchArticle from './SearchArticle.vue';
import LanguagePicker from './LanguagePicker.vue';
import ThemeToggleButton from './ThemeToggleButton.vue';
</script>

<template>
  <header class="sticky z-50 transition-transform duration-300 ease-in-out top-0 bg-surface [&.scroll-down]:-translate-y-full [&.scroll-up]:translate-y-0">
    <nav class="max-w-4xl mx-auto p-4 flex justify-between items-center">
      <NuxtLinkLocale href="/">
        <Logo/>
      </NuxtLinkLocale>
      <div class="flex items-center">
        <div class="flex items-center gap-x-4">
          <NuxtLinkLocale to='/articles'>Articles</NuxtLinkLocale>
          <SearchArticle/>
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

<!-- <script>
// Hide on scroll logic
const header=document.querySelector('header');
let lastScroll=0;

window.addEventListener('scroll',()=>{
  const currentScroll=window.pageYOffset;

  if(header===null)return;

  if(currentScroll<=0){
    header.classList.remove('scroll-down');
    return;
  }

  const scrollDown=
    currentScroll>lastScroll&&
    !header.classList.contains('scroll-down');

  if(scrollDown){
    header.classList.remove('scroll-up');
    header.classList.add('scroll-down');
    return;
  }

  const scrollUp=
    currentScroll<lastScroll&&
    header.classList.contains('scroll-down');

  if(scrollUp){
    header.classList.remove('scroll-down');
    header.classList.add('scroll-up');
  }

  lastScroll=currentScroll;
});
</script> -->
