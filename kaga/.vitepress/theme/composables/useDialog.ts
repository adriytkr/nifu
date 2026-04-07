import { ref } from 'vue';

import { DialogContext } from '~/types/dialog';

export function useDialog(){
  const dialogRef=ref<HTMLDialogElement|null>(null);

  function open(){
    dialogRef.value?.showModal();
  }

  function close(){
    dialogRef.value?.close();
  }

  const context:DialogContext={
    open:open,
    close:close,
  };

  return{
    dialogRef,
    open,
    close,
    context,
  };
}
