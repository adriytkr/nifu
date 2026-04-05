import { reactive } from 'vue';

import type { FormState, Schema } from '~/types/article';

export function useCheckpointType2(schema:Schema){
  const formState=reactive<FormState>(
    Object
      .keys(schema)
      .reduce((acc,key)=>{
        acc[key]=schema[key]?.default;
        return acc;
      },{} as FormState),
  );

  return{
    formState,
  };
}
