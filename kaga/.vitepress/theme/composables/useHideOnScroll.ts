import {
  onMounted,
  onUnmounted,
  ref,
} from 'vue';

export function useHideOnScroll(){
  const scrollClass=ref('');
  let lastScrollY=0;

  function handleScroll(){
    const currentScrollY=window.scrollY;

    if(Math.abs(currentScrollY-lastScrollY)<10)return;

    const scrollDownFlag=
      currentScrollY>lastScrollY&&
      currentScrollY>80;

    if(scrollDownFlag)hideHeader();
    else showHeader();
    
    lastScrollY=currentScrollY;
  };

  function showHeader(){
    scrollClass.value='scroll-up';
  }

  function hideHeader(){
    scrollClass.value='scroll-down';
  }

  onMounted(()=>window.addEventListener('scroll',handleScroll));
  onUnmounted(()=>window.removeEventListener('scroll',handleScroll));

  return{
    scrollClass,
    showHeader,
    hideHeader,
  };
}
