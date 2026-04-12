import { ref,computed } from 'vue';

import {data as articles} from '~data/articles.en.data';
import type { ArticleSchema } from '~/types/article.schema';
import { matchArticle } from '~/utils/articles';

import type { QueryAPI } from '~/components/articles/ArticleQuery.vue';

export function useArticles(){
  const query=ref('');
  const queryRef=ref<QueryAPI|null>(null);

  const filteredArticles=computed<ArticleSchema[]>(()=>
    (articles as ArticleSchema[]).filter(article=>
      matchArticle(
        article,
        query.value,
      )
    )
  );

  const matchesFound=computed(()=>
    filteredArticles.value.length
  );

  return{
    query,
    queryRef,
    filteredArticles,
    matchesFound,
  };
}
