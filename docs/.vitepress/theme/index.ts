import { Theme,inBrowser } from 'vitepress';

import './assets/styles/main.css';
import 'lite-youtube-embed/src/lite-yt-embed.css';

import Layout from './layouts/Layout.vue';

import VpLink from './components/base/VpLink.vue';

import Theorem from './components/content/Theorem.vue';
import Accordion from './components/content/Accordion/Accordion.vue';
import Quote from './components/content/Quote.vue';

import Media from './components/Media/Media.vue';
import Image from './components/Media/Image.vue';
import Youtube from './components/Media/Youtube.vue';

import DefinitionTooltip from './components/content/DefinitionTooltip.vue';

// import CheckpointType2 from './components/article/Checkpoint/Type2/CheckpointType2.vue';
// import CheckpointBlank from './components/article/Checkpoint/Type2/CheckpointBlank.vue';
// import CheckpointSelect from './components/article/Checkpoint/Type2/CheckpointSelect.vue';

import Presentation from './components/content/Presentation/Presentation.vue';

export default {
  Layout,
  enhanceApp({ app, router, siteData }){
    app.component('VpLink',VpLink);

    app.component('Theorem',Theorem);
    app.component('Accordion',Accordion);
    app.component('Quote',Quote);

    app.component('Media',Media);
    app.component('Image',Image);
    app.component('Youtube',Youtube);

    app.component('Definition',DefinitionTooltip);

    // app.component('CheckpointType2',CheckpointType2);
    // app.component('CheckpointBlank',CheckpointBlank);
    // app.component('CheckpointSelect',CheckpointSelect);

    app.component('Presentation',Presentation);

    if(inBrowser)import('lite-youtube-embed');
  },
} satisfies Theme

