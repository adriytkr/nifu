import type { CheckpointType2Field } from '@/types/article';

export const schema:Record<string,CheckpointType2Field<any>>={
  age:{
    validator:(x:number)=>x>0,
    default:-3,
  } satisfies CheckpointType2Field<number>,
};
