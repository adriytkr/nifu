import {ref} from 'vue';

export function useBaseCheckpoint(){
  const isFullScreen=ref<boolean>(false);

  function handleEsc(event:KeyboardEvent){
    if(event.key==='Escape'&&isFullScreen.value)toggleFullScreen();
  }

  function toggleFullScreen(){
    isFullScreen.value=!isFullScreen.value;

    if(isFullScreen.value){
      document.body.style.overflow='hidden';
      window.addEventListener('keydown',handleEsc)
    }else{
      document.body.style.overflow='';
      window.removeEventListener('keydown',handleEsc)
    }
  }

  return{
    isFullScreen,
    toggleFullScreen,
  };
}
