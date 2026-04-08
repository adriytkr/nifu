import type {TNavSchema} from '../shared/nav';

export const nav:TNavSchema={
  tooltip:{
    articles:'Browse Articles',
    quickReference:'Quick Reference',
    shortcuts:'Show Shortcuts',
    language:'Switch Language',
    search:'Search Articles',
    theme:{
      light:'Switch to dark mode',
      dark:'Switch to light mode',
    },
  },
  search:{
    placeholder:'Search Articles',
    modal:{
      placeholder:'What are you looking for?',
      toSelect:'to select',
      toNavigate:'to navigate',
      toClose:'to close',
    },
  },
  shortcuts:{
    title:'Keyboard Shortcuts',
    list:{
      searchArticles:'Search Articles',
      quickReference:'Quick Reference',
      shortcutsModal:'Keyboard Shortcuts',
      scrollUp:'Scroll up',
      scrollDown:'Scroll down',
    },
  },
  quickReference:{
    title:'Quick Reference',
  },
};
