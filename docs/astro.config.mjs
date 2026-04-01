// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  i18n:{
    defaultLocale:'en',
    locales:[
      {
        path:'en',
        codes:['en']
      },
      {
        path:'pt-br',
        codes:['pt-br']
      }
    ],
    routing:{
      prefixDefaultLocale:false,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});