import type {
  Article,
  ArticleDifficulty,
  SortingFilter,
} from '~/types/articles';

export function isArticleMatch(
  article:Article,
  query:string,
  tags:string[],
):boolean{
  const normalizedQuery=query.toLowerCase();

  const matchTitle=
    article.title
      .toLowerCase()
      .includes(normalizedQuery)

  const matchDescription=
    article.description
      .toLowerCase()
      .includes(normalizedQuery);

  const matchQuery=matchTitle||matchDescription;

  const matchTags=
    tags.some(tag=>
      tag
        .toLowerCase()
        .includes(normalizedQuery)
    );

  return matchQuery||matchTags;
}

export function sortArticles(
  articles:Article[],
  sorting:SortingFilter,
):Article[]{
  const difficultyWeight:Record<ArticleDifficulty,number>={
    'training':1,
    'easy':2,
    'medium':3,
    'hard':4,
    'insane':5,
  };

  const sorted=[...articles].sort((a,b)=>{
    switch(sorting){
      case 'nameAsc':
        return a.title.localeCompare(b.title);
      case 'nameDesc':
        return b.title.localeCompare(a.title);
      case 'difficultyAsc':
        return difficultyWeight[a.difficulty]-difficultyWeight[b.difficulty];
      case 'difficultyDesc':
        return difficultyWeight[b.difficulty]-difficultyWeight[a.difficulty];
    }
  });

  return sorted;
}
