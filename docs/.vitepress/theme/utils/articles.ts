import { ArticleSchema } from '~/types/article.schema';

export function matchArticle(
  article:ArticleSchema,
  query:string,
):boolean{
  const normalizedQuery=query
    .trim()
    .toLowerCase();

  const matchesTitle=article.title
    .toLowerCase()
    .includes(normalizedQuery);

  const matchesDescription=article.description
    .toLowerCase()
    .includes(normalizedQuery);

  const matchesQuery=matchesTitle||matchesDescription;

  return matchesQuery;
}
