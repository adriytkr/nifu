import type { Locale } from '@/types/i18n';

export const getAbsoluteUrlByLocale=(locale:Locale,url:string):string=>
  locale==='en'
    ?url
    :`${locale}/${url}`
