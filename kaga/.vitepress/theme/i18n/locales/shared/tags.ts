import type { TSchema } from '~/i18n/types';

import { tags as tags_en } from '../en/tags';
import { tags as tags_pt_br } from '../pt-br/tags';

export type TTagsSchema=Record<string,string>;

export const tTags:TSchema<TTagsSchema>={
  en:tags_en,
  'pt-br':tags_pt_br,
};
