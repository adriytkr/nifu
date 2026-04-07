import {
  MaybeRefOrGetter,
  onMounted,
  onUnmounted,
  ref,
  toValue,
  watch,
} from 'vue';
import { DialogContext, SearchDialogContext } from '~/types/dialog';

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

  function focusInput(){
    inputRef.value?.focus();
  }

  function clearSearch(){
    clearInput();
    focusInput();
  }

  watch(
    ()=>toValue(isOpen),
    (newValue)=>{
      if(!newValue)return;

      focusInput();
      clearInput();
    },
  );

  const dialogRef=ref<HTMLDialogElement|null>(null);

  function openDialog(){
    dialogRef.value?.showModal();
  }

  function closeDialog(){
    dialogRef.value?.close();
  }

  function clearInput(){
    searchQuery.value='';
  }

  const context:SearchDialogContext={
    open:openDialog,
    close:closeDialog,
    focusInput,
    clearInput,
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
