import {
  onMounted,
  onUnmounted,
  ref,
} from 'vue';
import { useUI } from './useUi';

export function useSearchModal(){
  const selectedItemIndex=ref(-1);

  function handleArrowUp(){
    if(selectedItemIndex.value-1<0)return;

    selectedItemIndex.value--;
  }

  function handleArrowDown(){
    // add if logic to prevent overflow

    selectedItemIndex.value++;
  }

  function selectItem(index:number){
    if(index===-1)return;

    console.log(index);
  }

  const{
    isSearchModalOpen,
    closeModal,
  }=useUI();

  function handleKeyDown(event:KeyboardEvent){
    if(!isSearchModalOpen.value)return;

    switch(event.code){
      case 'ArrowUp':
        handleArrowUp();
        break;
      case 'ArrowDown':
        handleArrowDown();
        break;
      case 'Enter':
        selectItem(selectedItemIndex.value);
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

  function clearInput(){
    searchQuery.value='';
  }

  function clearSearch(){
    clearInput();
    focusInput();
  }

  const dialogRef=ref<HTMLDialogElement|null>(null);

  return{
    dialogRef,
    inputRef,
    searchQuery,
    clearInput,
    focusInput,
    clearSearch,
    selectedItemIndex,
  };
}
