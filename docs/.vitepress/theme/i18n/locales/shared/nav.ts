import type { TSchema } from '../../types';
import { nav as nav_en } from '../en/nav';
import { nav as nav_pt_br } from '../pt-br/nav';

export type TNavSchema={
  tooltip:{
    articles:string;
    quickReference:string;
    shortcuts:string;
    language:string;
    search:string;
    theme:{
      light:string;
      dark:string;
    },
  },
  search:{
    placeholder:string;
    modal:{
      placeholder:string;
      toSelect:string;
      toNavigate:string;
      toClose:string;
    },
  },
  shortcuts:{
    title:string;
    list:{
      searchArticles:string;
      quickReference:string;
      shortcutsModal:string;
      scrollUp:string;
      scrollDown:string;
    },
  },
  quickReference:{
    title:string;
  },
};

export const tNav:TSchema<TNavSchema>={
  en:nav_en,
  'pt-br':nav_pt_br,
};
