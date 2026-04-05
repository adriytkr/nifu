import { defineContentConfig } from '@nuxt/content';

import {articlesCollection} from './utils/article';

export default defineContentConfig({
  collections:{
    articles:articlesCollection,
  }
})
