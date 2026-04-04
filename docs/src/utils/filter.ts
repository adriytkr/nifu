import type { ArticleSchema } from '@/types/article';

export function checkArticleMatch(
  article:ArticleSchema,
  query:string,
  tags:string[],
):boolean{
  const normalizedQuery=query.toLowerCase();

  const matchesTitle=article.data.title
    .toLowerCase()
    .includes(normalizedQuery);

  const matchesDescription=
    article.data.description
      .toLowerCase()
      .includes(normalizedQuery);

  const matchesQuery=matchesTitle||matchesDescription;

  const matchesTag=
    tags.length===0||
    tags.some(tag=>article.data.tags.includes(tag));

  const matchesFlag=
    matchesQuery&&
    matchesTag;

  return matchesFlag;
}
