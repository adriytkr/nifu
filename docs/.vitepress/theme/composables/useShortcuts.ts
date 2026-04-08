import {onMounted,onUnmounted} from 'vue';

import { useUI } from '~/composables/useUi';

export function useShortcuts(){
  const {
    isSomeModalOpen,
    closeAllModals,
    toggleModal,
    isHeaderVisible,
  }=useUI();

  let isMovingDown = false;
  let isMovingUp = false;
  const scrollSpeed = 12;

  function scrollLoop(){
    if(isMovingDown)window.scrollBy(0,scrollSpeed);
    if(isMovingUp)window.scrollBy(0, -scrollSpeed);
    
    if(isMovingDown||isMovingUp)requestAnimationFrame(scrollLoop);
  }

  function moveUp(){
    isMovingUp=true;
    requestAnimationFrame(scrollLoop);
  }

  function moveDown(){
    isMovingDown=true;
    requestAnimationFrame(scrollLoop);
  }

  function handleKeyDown(event:KeyboardEvent){
    if(document.fullscreenElement!==null)return;

    const key=event.key.toLowerCase();

    const isInputFocused=
      event.target instanceof HTMLInputElement||
      event.target instanceof HTMLTextAreaElement;
      
    if(key==='escape'&&isSomeModalOpen.value){
      event.preventDefault();
      closeAllModals();
      return;
    }

    if(event.ctrlKey&&key==='k'){
      event.preventDefault();
      toggleModal('search');
      return;
    }

    if(isInputFocused)return;

    if(key==='r'){
      event.preventDefault();
      toggleModal('quick-reference');
      return;
    }

    if(key==='?'||key==='h'){
      event.preventDefault();
      toggleModal('shortcuts');
      return;
    }

    if(
      event.key==='j'&&
      !isMovingDown&&
      !isSomeModalOpen.value
    ){
      event.preventDefault();
      moveDown();
      return;
    }

    if(
      event.key==='k'&&
      !isMovingUp&&
      !isSomeModalOpen.value
    ){
      event.preventDefault();
      moveUp();
      return;
    }
  }

  function handlekeyUp(event:KeyboardEvent){
    const key=event.key.toLowerCase();

    switch(key){
      case 'j':
        isMovingDown=false;
      case 'k':
        isMovingUp=false;
    }
  }

  onMounted(()=>{
    window.addEventListener('keydown',handleKeyDown);
    window.addEventListener('keyup',handlekeyUp);
  });

  onUnmounted(()=>{
    window.removeEventListener('keydown',handleKeyDown);
    window.removeEventListener('keyup',handlekeyUp);
  });
}
