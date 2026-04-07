import {
  ref,
  watch,
  onUnmounted,
} from 'vue';

export function useShortcutsModal(){
  const isShortcutsModalOpen=ref(false);

  function openShortcutsModal(){
    isShortcutsModalOpen.value=true;
    document.body.style.overflow='hidden';
  }

  function closeShortcutsModal(){
    isShortcutsModalOpen.value=false;
    document.body.style.overflow='auto';
  }

  function handleEsc(event:KeyboardEvent){
    if(event.key==='Escape'&&isShortcutsModalOpen.value)
      closeShortcutsModal();
  }

  watch(
    isShortcutsModalOpen,
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
    isShortcutsModalOpen,
    openShortcutsModal,
    closeShortcutsModal,
  };
}
