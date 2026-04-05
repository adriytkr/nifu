import { ref } from 'vue';

import type { ChoiceState } from '@/types/article';

export function useCheckpointType1(
  correctChoices:number[],
  max?:number,
){
  const isSubmitted=ref<boolean>(false);
  const isRevealed=ref<boolean>(false);

  const selectedChoices=ref<number[]>([]);

  const isSelected=(index:number):boolean=>
    selectedChoices.value.includes(index);

  const isCorrect=(index:number):boolean=>
    correctChoices.includes(index);

  function selectChoice(index:number){
  }

  function getChoiceState(index:number):ChoiceState{
    return 'idle';
  }

  function checkChoices(){
  }

  function resetChoices(){
  }

  function revealAnswers(){
  }

  return{
    selectChoice,
    getChoiceState,
    checkChoices,
    resetChoices,
    revealAnswers,
  };
}
