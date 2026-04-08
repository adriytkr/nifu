import { createContentLoader } from 'vitepress';

import { Article } from '~/types/articles/article';

const formatURL=(url:string):string=>
  url.split('/').pop()?.replace('.html','')??'';

export default createContentLoader('articles/**/*.md', {
  transform(raw){
    return raw.map<Article>(({url,frontmatter})=>({
      slug:formatURL(url),
      title:frontmatter.title,
      description:frontmatter.description,
      thubmnail:frontmatter.thubmnail,
      tags:frontmatter.tags,
      difficulty:frontmatter.difficulty,
    }));
  }
})
