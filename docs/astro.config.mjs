// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import vue from '@astrojs/vue';

import mdx from '@astrojs/mdx';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
  i18n:{
    defaultLocale:'en',
    locales:[
      'en',
      'pt-br',
    ],
    routing:{
      prefixDefaultLocale:false,
    },
  },

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [vue(), mdx()],

  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});