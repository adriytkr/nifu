// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

import vue from '@astrojs/vue';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  integrations: [
      starlight({
          title: 'Akagi',
          components:{
            SocialIcons:'./src/components/layout/GlobalPlugin.astro',
            Footer:'./src/components/layout/TheFooter.astro',
          },
          defaultLocale:'root',
          locales:{
              root:{
                  label:'English',
                  lang:'en',
              },
              'pt-br':{
                  label:'Português',
                  lang:'pt-br',
              },
          },
          sidebar: [
              {
                  label:'View all Articles',
                  link:'/articles',
                  translations:{
                      'pt-br':'Ver todos os artigos'
                  },
              },
              {
                  label: 'Calculus',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/calculus',
                  },
                  translations:{
                      'pt-br':'Cálculo'
                  },
              },
              {
                  label: 'Advanced Calculus',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/advanced-calculus',
                  },
                  translations:{
                      'pt-br':'Cálculo Avançado'
                  },
              },
              {
                  label: 'Linear Algebra',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/linear-algebra',
                  },
                  translations:{
                      'pt-br':'Algebra Linear'
                  },
              },
              {
                  label: 'Physics',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/physics',
                  },
                  translations:{
                      'pt-br':'Física'
                  },
              },
              {
                  label: 'Competitive Programming',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/competitive-programming',
                  },
                  translations:{
                      'pt-br':'Programação Competitiva'
                  },
              },
              {
                  label: 'Statistics',
                  collapsed:true,
                  autogenerate: {
                      directory: 'articles/statistics',
                  },
                  translations:{
                      'pt-br':'Estatística'
                  },
              },
          ],
          customCss: ['./src/assets/styles/custom.css'],
      }),
      vue(),
	],

  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },

  vite: {
    plugins: [tailwindcss()],
  },
});