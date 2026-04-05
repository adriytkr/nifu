import tailwindcss from '@tailwindcss/vite';

import {i18nConfig} from './config/i18n';

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/i18n', '@nuxtjs/color-mode'],
  css:['./app/assets/styles/global.css'],
  vite:{
    plugins:[
      tailwindcss(),
    ],
  },
  i18n:i18nConfig,
})