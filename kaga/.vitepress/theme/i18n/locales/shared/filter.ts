import type {TSchema} from '~/i18n/types';
import { SortingFilter } from '~/types/articles';

import { filter as filter_en } from '../en/filter';
import { filter as filter_pt_br } from '../pt-br/filter';

export type TSort=Record<SortingFilter,string>;
export type SortProperty=TSort&{
  label:string;
}

export type TFilterSchema={
  placeholder:string;
  matches:(count:number,query:string)=>string;
  clear:string;
  sort:SortProperty;
}

export const tFilter:TSchema<TFilterSchema>={
  en:filter_en,
  'pt-br':filter_pt_br,
};
