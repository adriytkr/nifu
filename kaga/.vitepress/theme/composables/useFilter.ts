import {ref,computed} from 'vue';

import type {Article, SortingFilter} from '~/types/articles';
import {isArticleMatch, sortArticles} from '~/utils/filter';

export function useFilter(articles:Article[]){
  const searchQuery=ref('');
  const selectedSortingFilter=ref<SortingFilter>('nameAsc');

  const filteredArticles=computed<Article[]>(()=>{
    const result=articles.filter(article=>
      isArticleMatch(
        article,
        searchQuery.value,
      )
    )

    return sortArticles(
      result,
      selectedSortingFilter.value,
    );
  });

  const matchesFound=computed<number>(()=>
    filteredArticles.value.length
  );

  return{
    searchQuery,
    selectedSortingFilter,
    filteredArticles,
    matchesFound,
  };
}
