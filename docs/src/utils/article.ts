import type { GetStaticPaths } from 'astro';
import {getCollection} from 'astro:content';

export const getArticlePaths=(locale:string)=>(async()=>{
  const allArticles=await getCollection('articles');

  const prefix=`${locale}/`;
  const localizedArticles=allArticles.filter(entry=>entry.id.startsWith(prefix));

  return localizedArticles.map(entry=>{
    const slug=entry.id.replace(prefix,'');

    return{
      params:{slug},
      props:{entry},
    };
  });
}) satisfies GetStaticPaths;
