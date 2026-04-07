import {
  MaybeRefOrGetter,
  onMounted,
  onUnmounted,
  ref,
  toValue,
  watch,
} from 'vue';
import { DialogContext } from '~/types/dialog';

export function useSearchModal(isOpen:MaybeRefOrGetter<boolean>){
  const selectedItemIndex=ref(-1);

  function handleArrowUp(){
    if(selectedItemIndex.value-1<0)return;

    selectedItemIndex.value--;
  }

  function handleArrowDown(){
    // add if logic to prevent overflow

    selectedItemIndex.value++;
  }

  function handleKeyDown(event:KeyboardEvent){
    switch(event.code){
      case 'ArrowUp':
        handleArrowUp();
        break;
      case 'ArrowDown':
        handleArrowDown();
        break;
    }
  }

  onMounted(()=>window.addEventListener('keydown',handleKeyDown));
  onUnmounted(()=>window.removeEventListener('keydown',handleKeyDown));

  const inputRef=ref<HTMLInputElement|null>(null);
  const searchQuery=ref('');

  function clearSearch(){
    searchQuery.value='';
    inputRef.value?.focus();
  }

  watch(
    ()=>toValue(isOpen),
    (newValue)=>{
      if(newValue)inputRef.value?.focus();
    },
  );

  const dialogRef=ref<HTMLDialogElement|null>(null);

  function openDialog(){
    dialogRef.value?.showModal();
  }

  function closeDialog(){
    dialogRef.value?.close();
  }

  const context:DialogContext={
    open:openDialog,
    close:closeDialog,
  };

  return{
    selectedItemIndex,
    inputRef,
    searchQuery,
    clearSearch,
    dialogRef,
    context,
  };
}
