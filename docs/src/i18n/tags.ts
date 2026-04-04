import type { TSchema } from '@/types/i18n';
import type { ArticleTagList } from '@/types/article';

export const tagTranslations:TSchema<ArticleTagList>={
  en:{
    calculus:'Calculus',
  },
  'pt-br':{
    calculus:'Cálculo',
  }
} as const;
