import type { TSchema } from '~/i18n/types';
import { ArticleDifficulty } from '~/types/articles';

import { difficulties as difficulties_en } from '../en/difficulties';
import { difficulties as difficulties_pt_br } from '../pt-br/difficulties';

export type TDifficultiesSchema=Record<ArticleDifficulty,string>;

export const tDifficulties:TSchema<TDifficultiesSchema>={
  en:difficulties_en,
  'pt-br':difficulties_pt_br,
};
