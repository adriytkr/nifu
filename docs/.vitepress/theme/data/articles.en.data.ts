import { createContentLoader } from 'vitepress';

import type { ArticleSchema } from '~/types/article.schema';

const loader=createContentLoader(
  'articles/**/*.md',
  {
    transform:raw=>raw.map<ArticleSchema>(
      article=>({
        slug:article.url
          .split('/')
          .pop()!,
        title:article.frontmatter.title,
        description:article.frontmatter.description,
      })
    ),
  }
);

export default loader;
