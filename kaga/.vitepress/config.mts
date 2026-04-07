import { defineConfig } from 'vitepress';
import tailwindcss from '@tailwindcss/vite';
import { fileURLToPath } from 'node:url';

// https://vitepress.dev/reference/site-config
export default defineConfig({
  srcDir: "docs",
  title: "Kaga",
  description: "Yet to be written",
  head: [
    [
      'script',
      { id: 'check-theme' },
      `
        (function(){
          const theme=localStorage.getItem('theme')||'light';
          document.documentElement.dataset.theme=theme;
        })();
      `
    ],
  ],
  locales:{
    root:{
      lang:'en',
      label:'English',
    },
    'pt-br':{
      lang:'pt-br',
      label:'Português',
    },
  },
  vite:{
    plugins:[
      tailwindcss(),
    ],
    resolve:{
      alias:{
        '~':fileURLToPath(new URL('./theme',import.meta.url)),
        '~~':fileURLToPath(new URL('..',import.meta.url)),
        '~content':fileURLToPath(new URL('../content',import.meta.url)),
        '~icons':fileURLToPath(new URL('./theme/components/icons',import.meta.url)),
      },
    },
    publicDir:fileURLToPath(new URL('../public',import.meta.url)),
  },
  vue:{
    template:{
      compilerOptions:{
        isCustomElement:tag=>tag==='lite-youtube',
      },
    },
  },
  cleanUrls:true,
  markdown:{
    toc:{
      level:[2,3,4],
    },
    math:true,
  },
  themeConfig:{
    outline:[2,4],
  },
})
