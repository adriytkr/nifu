import {
  ref,
  watch,
  onUnmounted,
} from 'vue';

import { DialogContext } from '~/types/dialog';

export function useModal(){
  const dialogContext=ref<DialogContext|null>(null);
  const isModalOpen=ref(false);

  function openModal(){
    isModalOpen.value=true;
    document.body.style.overflow='hidden';
    dialogContext.value?.open();
  }

  function closeModal(){
    isModalOpen.value=false;
    document.body.style.overflow='auto';
    dialogContext.value?.close();
  }

  function handleEsc(event:KeyboardEvent){
    if(event.key==='Escape'&&isModalOpen.value)
      closeModal();
  }

  watch(
    isModalOpen,
    (isOpen)=>{
      if(isOpen){
        window.addEventListener('keydown',handleEsc);
        return;
      }

      window.removeEventListener('keydown',handleEsc);
    },
    {immediate:true},
  );

  onUnmounted(()=>window.removeEventListener('keydown', handleEsc));

  return{
    dialogContext,
    isModalOpen,
    openModal,
    closeModal,
  };
}
