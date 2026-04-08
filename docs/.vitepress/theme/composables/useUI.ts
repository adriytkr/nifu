import {computed, Ref, ref, watch} from 'vue';

type ModalName=
  'quick-reference'|
  'shortcuts'|
  'search';

const isQuickReferenceModalOpen=ref(false);
const isShortcutsModalOpen=ref(false);
const isSearchModalOpen=ref(false);

const modalMap:Record<ModalName,Ref<boolean>>={
  'quick-reference': isQuickReferenceModalOpen,
  'shortcuts': isShortcutsModalOpen,
  'search': isSearchModalOpen,
};

const isHeaderVisible=ref(true);

export function useUI(){
  const isSomeModalOpen=computed<boolean>(()=>
    isQuickReferenceModalOpen.value||
    isShortcutsModalOpen.value||
    isSearchModalOpen.value
  );

  function handleScrollVisibility(newValue:boolean){
    console.log('hi');

    if(newValue){
      document.body.style.overflow='hidden';
      return;
    }

    document.body.style.overflow='auto';
  }

  watch(
    isSomeModalOpen,
    handleScrollVisibility,
    {flush:'post'},
  )

  function closeAllModals(){
    isQuickReferenceModalOpen.value=false;
    isShortcutsModalOpen.value=false;
    isSearchModalOpen.value=false;
  }

  function openModal(modal:ModalName){
    modalMap[modal].value=true;
    isHeaderVisible.value=true;
  }

  function closeModal(modal:ModalName){
    modalMap[modal].value=false;
  }

  function toggleModal(modal:ModalName){
    const wasOpen=modalMap[modal].value;
    closeAllModals();

    if(!wasOpen)openModal(modal);
  }

  return{
    isQuickReferenceModalOpen,
    isShortcutsModalOpen,
    isSearchModalOpen,

    isSomeModalOpen,
    closeAllModals,
    openModal,
    closeModal,
    toggleModal,

    isHeaderVisible,
  };
}
