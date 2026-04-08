import {
  onMounted,
  onUnmounted,
} from 'vue';

import { useUI } from './useUi';

export function useHideOnScroll(){
  let lastScrollY=0;

  const {isHeaderVisible}=useUI();

  function handleScroll(){
    const currentScrollY=window.scrollY;

    if(Math.abs(currentScrollY-lastScrollY)<10)return;

    const scrollDownFlag=
      currentScrollY>lastScrollY&&
      currentScrollY>80;

    if(scrollDownFlag)isHeaderVisible.value=false;
    else isHeaderVisible.value=true;

    lastScrollY=currentScrollY;
  };

  onMounted(()=>window.addEventListener('scroll',handleScroll));
  onUnmounted(()=>window.removeEventListener('scroll',handleScroll));

  return{
    isHeaderVisible,
  };
}
