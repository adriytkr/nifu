import { ref, computed } from 'vue';

import type { ArticleSchema } from '@/types/article';
import { checkArticleMatch } from '@/utils/article';

export function useFilter(initialArticles:ArticleSchema[]){
  const searchQuery=ref('');

  const filteredArticles=computed<ArticleSchema[]>(()=>
    initialArticles.filter(article=>{
      return checkArticleMatch(
        article,
        searchQuery.value,
        [],
      );
    })
  );

  const matchesFound=computed<number>(()=>filteredArticles.value.length);

  return{
    searchQuery,
    filteredArticles,
    matchesFound,
  };
}
