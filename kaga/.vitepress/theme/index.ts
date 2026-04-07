import { Theme,inBrowser } from 'vitepress';

import './assets/styles/main.css';
import 'lite-youtube-embed/src/lite-yt-embed.css';

import Layout from './layouts/Layout.vue';

import VpLink from './components/app/VpLink.vue';

import SourceLink from './components/article-ui/SourceLink.vue';
import SourceLinkGithub from './components/article-ui/SourceLinkGithub.vue';

import TheoremBox from './components/article-content/TheoremBox.vue';

import MediaWithCaption from './components/article-content/Media/MediaWithCaption.vue';
import ImageWithCaption from './components/article-content/Media/ImageWithCaption.vue';
import YoutubeVideo from './components/article-content/Media/YoutubeVideo.vue';

import AccordionBase from './components/article-content/Accordion/AccordionBase.vue';
import AccordionCommon from './components/article-content/Accordion/AccordionCommon.vue';

import TheQuote from './components/article-content/TheQuote.vue';

import CheckpointType1Single from './components/article-content/Checkpoint/type1/CheckpointType1Single.vue';

import CheckpointType2 from './components/article-content/Checkpoint/Type2/CheckpointType2.vue';
import CheckpointBlank from './components/article-content/Checkpoint/Type2/CheckpointBlank.vue';
import CheckpointSelect from './components/article-content/Checkpoint/Type2/CheckpointSelect.vue';

import ManimSlides from './components/article-content/Media/ManimSlides.vue';

export default {
  Layout,
  enhanceApp({ app, router, siteData }){
    app.component('VpLink',VpLink);

    app.component('SourceLink',SourceLink);
    app.component('SourceLinkGithub',SourceLinkGithub);

    app.component('TheoremBox',TheoremBox);

    app.component('MediaWithCaption',MediaWithCaption);
    app.component('ImageWithCaption',ImageWithCaption);
    app.component('YoutubeVideo',YoutubeVideo);

    app.component('AccordionBase',AccordionBase);
    app.component('AccordionCommon',AccordionCommon);

    app.component('TheQuote',TheQuote);

    app.component('CheckpointType1Single',CheckpointType1Single);

    app.component('CheckpointType2',CheckpointType2);
    app.component('CheckpointBlank',CheckpointBlank);
    app.component('CheckpointSelect',CheckpointSelect);

    app.component('ManimSlides',ManimSlides);

    if(inBrowser)import('lite-youtube-embed');
  },
} satisfies Theme

