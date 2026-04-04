import type { ArticlesPageT, TSchema } from '@/types/i18n';

export const articlesPageT:TSchema<ArticlesPageT>={
  en:{
    placeholder:'Search articles by name, keywords, ...',
    clear:'Clear Search',
    matches(count,query){
      if(count===0)return `No matches for "${query}"`;
      if(count===1)return `1 match for "${query}"`;
      return `${count} matches for ${query}`;
    },
  },
  'pt-br':{
    placeholder:'Search articles by name, keywords, ...',
    clear:'Clear Search',
    matches(count,query){
      if(count===0)return `No matches for "${query}"`;
      if(count===1)return `1 match for "${query}"`;
      return `${count} matches for ${query}`;
    },
  },
};
