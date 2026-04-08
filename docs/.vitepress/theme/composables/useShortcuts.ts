import {onMounted,onUnmounted} from 'vue';

import { useUI } from '~/composables/useUi';

export function useShortcuts(){
  const {
    isSomeModalOpen,
    closeAllModals,
    toggleModal,
  }=useUI();

  let velocity = 0;
  const acceleration = 1.8;
  const friction = 0.92;
  const maxSpeed = 22;
  const startDelay = 450;

  let scrollTimer:ReturnType<typeof setTimeout>|null=null;
  let isLoopRunning=false;
  let activeDirection:'up'|'down'|null=null;

  function scrollLoop() {
    if(isSomeModalOpen.value){
      activeDirection=null;
      velocity=0;
      isLoopRunning=false;
      return;
    }

    if(
      Math.abs(velocity)<0.1&&
      activeDirection===null
    ){
      velocity=0;
      isLoopRunning=false;
      return;
    }

    if(activeDirection === 'down')velocity+=acceleration;
    if(activeDirection === 'up')velocity-=acceleration;

    velocity*=friction;
    if(velocity>maxSpeed)velocity=maxSpeed;
    if(velocity<-maxSpeed)velocity=-maxSpeed;

    window.scrollBy(0,velocity);

    isLoopRunning=true;
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

    if(!event.ctrlKey&&key==='r'){
      event.preventDefault();
      toggleModal('quick-reference');
      return;
    }

    if(key==='?'||key==='h'){
      event.preventDefault();
      toggleModal('shortcuts');
      return;
    }

    if(event.repeat)return;

    const isDown=key==='j'||key==='arrowdown';
    const isUp=key==='k'||key==='arrowup';

    if(
      (isDown||isUp)&&
      !isSomeModalOpen.value
    ){
      event.preventDefault();
      activeDirection=(key==='j'||key==='arrowdown')
        ?'down'
        :'up';

      window.scrollBy({
        top:(key==='j'||key==='arrowdown')?40:-40,
        behavior:'smooth',
      });

      scrollTimer=setTimeout(
        ()=>{
          if(!isLoopRunning)scrollLoop();
        },
        startDelay,
      );
    }
  }

  function handlekeyUp(event:KeyboardEvent){
    const key=event.key.toLowerCase();

    const isDown=key==='j'||key==='arrowdown';
    const isUp=key==='k'||key==='arrowup';

    if(isUp||isDown){
      activeDirection=null;

      if(scrollTimer!==null){
        clearTimeout(scrollTimer);
        scrollTimer=null;
      }
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
