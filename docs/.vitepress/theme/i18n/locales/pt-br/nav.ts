import type {TNavSchema} from '../shared/nav';

export const nav:TNavSchema={
  tooltip:{
    articles:'Explorar Artigos',
    quickReference:'Referência',
    shortcuts:'Mostrar Atalhos',
    language:'Mudar idioma',
    search:'Procurar Artigos',
    theme:{
      light:'Mudar para modo escuro',
      dark:'Mudar para modo claro',
    },
  },
  search:{
    placeholder:'Procurar artigos',
    modal:{
      placeholder:'O que você está procurando?',
      toSelect:'para selecionar',
      toNavigate:'para navegar',
      toClose:'para fechar',
    },
  },
  shortcuts:{
    title:'Atalhos de teclado',
    list:{
      searchArticles:'Pesquisar artigos',
      quickReference:'Referência Rápida',
      shortcutsModal:'Atalhos de teclado',
      scrollUp:'Rolar para cima',
      scrollDown:'Rolar para baixo',
    },
  },
  quickReference:{
    title:'Referência Rápida',
  },
};
