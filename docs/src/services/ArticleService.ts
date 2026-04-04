import { getCollection } from 'astro:content';

import type { Locale } from '@/types/i18n';
import type { ArticleSchema } from '@/types/article';

export class ArticleService{
  public static async getAllArticlesByLocale(locale:Locale):Promise<ArticleSchema[]>{
    const allArticles=await getCollection(
      'articles',
      article=>
        article.data.featured===true&&
        article.id.startsWith(`${locale}/`)
    );

    return allArticles;
  }
}
