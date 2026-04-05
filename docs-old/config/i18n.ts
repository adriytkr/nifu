import type { NuxtI18nOptions, LocaleObject } from '@nuxtjs/i18n';

import type {Locale} from '../types/i18n';
import {fetchLocaleFiles} from '../utils/i18n';

export const locales:LocaleObject<Locale>[]=[
  {
    code:'en',
    name:'English',
    files:fetchLocaleFiles('en'),
  },
  {
    code:'pt-br',
    name:'Português',
    files:fetchLocaleFiles('pt-br'),
  },
];

export const i18nConfig={
  defaultLocale:'en',
  locales,
  detectBrowserLanguage:false,
} satisfies NuxtI18nOptions<Locale>;
