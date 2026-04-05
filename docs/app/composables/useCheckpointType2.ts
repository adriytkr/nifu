import { reactive } from 'vue';

import type {
  FormState,
  Schema,
  Type2State,
  validationState,
} from '~/types/article';

export function useCheckpointType2(schema:Schema){
  const formState=reactive<FormState>(
    Object
      .keys(schema)
      .reduce((acc,key)=>{
        acc[key]=schema[key]?.default;
        return acc;
      },{} as FormState)
  );

  const validationState=reactive<Record<string,Type2State>>(
    Object
      .keys(schema)
      .reduce((acc,key)=>{
        acc[key]='idle';
        return acc;
      }, {} as validationState)
  );

  function checkAnswers(){
    Object
      .keys(schema)
      .forEach(key=>{
        const field=schema[key];
        const isCorrect=field?.validator(formState[key]);

        validationState[key]=isCorrect
          ?'correct'
          :'incorrect';
      });
  }

  function reset(){
    Object
      .keys(schema)
      .forEach(key=>{
        const field=schema[key];

        formState[key]=field?.default;
        validationState[key]='idle';
      });
  }

  function revealAnswers(){
    Object
      .keys(schema)
      .forEach(key=>{
        const field=schema[key];

        const isCorrect=field?.validator(formState[key]);

        if(isCorrect){
          validationState[key]='correct';
          return;
        }

        validationState[key]='revealed';
        formState[key]=field?.answer;
      });
  }

  provide('form-state',formState);
  provide('form-validation',validationState);

  return{
    checkAnswers,
    reset,
    revealAnswers,
  };
}
