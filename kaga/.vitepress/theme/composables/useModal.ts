import {
  ref,
  watch,
  onUnmounted,
} from 'vue';

export function useModal(){
  const dialogRef=ref<HTMLDialogElement|null>(null);
  const isModalOpen=ref(false);

  function openModal(){
    isModalOpen.value=true;
    document.body.style.overflow='hidden';
    dialogRef.value?.showModal();
  }

  function closeModal(){
    isModalOpen.value=false;
    document.body.style.overflow='auto';
    dialogRef.value?.close();
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
    dialogRef,
    isModalOpen,
    openModal,
    closeModal,
  };
}
