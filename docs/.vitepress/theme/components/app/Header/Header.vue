<script setup lang="ts">
import {ref} from 'vue';

import MenuIcon from '~icons/MenuIcon.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';
import NavItem from './NavItem.vue';

const dialogRef=ref<HTMLDialogElement|null>(null);
const isOpen=ref(false);

function openMenu(){
  dialogRef.value?.showModal();
  isOpen.value=true;
}

function closeMenu(){
  dialogRef.value?.close();
  isOpen.value=false;
}
</script>

<template>
  <Teleport to="body">
    <dialog
      ref="dialogRef"
      class="backdrop:backdrop-blur-xs"
      @click.self="closeMenu"
    >
      <div
        class="fixed left-1/2 top-1/2 -translate-1/2 max-w-md w-full opacity-0 scale-0 transition-transform duration-200"
        :class="{ 'opacity-100 scale-100':isOpen }"
      >
        <nav class="m-4 p-4 bg-surface rounded-md">
          <div class="flex justify-end">
            <button @click="closeMenu">
              <CloseIcon/>
            </button>
          </div>
          <ul class="group/nav flex flex-col gap-y-4">
            <NavItem to="/about">About</NavItem>
            <NavItem to="/articles">Articles</NavItem>
          </ul>
        </nav>
      </div>
    </dialog>
  </Teleport>
  <header>
    <div class="max-w-2xl mx-auto p-4">
      <button @click="openMenu">
        <MenuIcon/>
      </button>
    </div>
  </header>
</template>
