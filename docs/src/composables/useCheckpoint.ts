import {ref,computed} from 'vue';
import type { ChoiceStatus } from '@/types/article';

export function useCheckpoint(correctChoices:number[]){
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

  const isSubmitted=ref<boolean>(false);
  const selectedChoices=ref<number[]>([]);

  const emptyState=computed<boolean>(()=>selectedChoices.value.length===0);

  function getStatus(choiceIndex:number):ChoiceStatus{
    const isSelected=selectedChoices.value.includes(choiceIndex);

    if(!isSubmitted.value)return isSelected?'selected':'default';

    const isCorrect=correctChoices.includes(choiceIndex);

    if(isSelected)return isCorrect?'correct':'incorrect';

    if(isCorrect){
      if(correctChoices.length===1)return 'correct';
      return 'missed';
    }

    return 'default';
  }

  function selectChoice(choiceIndex:number){
    if(isSubmitted.value)return;

    const isSelected=selectedChoices.value.includes(choiceIndex);

    if(isSelected){
      const index=selectedChoices.value.indexOf(choiceIndex);
      selectedChoices.value.splice(index,1);
      return;
    }

    if(correctChoices.length===1){
      selectedChoices.value[0]=choiceIndex;
      return;
    }

    selectedChoices.value.push(choiceIndex);
  }

  function checkChoices(){
    if(emptyState.value)return;

    isSubmitted.value=true;
  }

  const isExplanationVisible=ref<boolean>(false);

  function retry(){
    isSubmitted.value=false;
    isExplanationVisible.value=false;
    selectedChoices.value=[];
  }

  return{
    getStatus,
    selectChoice,
    emptyState,
    isSubmitted,
    checkChoices,
    retry,
    isFullScreen,
    toggleFullScreen,
    isExplanationVisible,
  };
}
