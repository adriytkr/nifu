import type { GetStaticPaths } from 'astro';
import {getCollection} from 'astro:content';

export const getArticlePaths=(locale:string)=>(async()=>{
  const allArticles=await getCollection('articles');

  const prefix=`${locale}/`;
  console.log(prefix,allArticles);

  const localizedArticles=allArticles.filter(entry=>entry.id.startsWith(prefix));

  console.log(localizedArticles);

  return localizedArticles.map(entry=>{
    const slug=entry.id.replace(prefix,'');

    return{
      params:{slug},
      props:{entry},
    };
  });
}) satisfies GetStaticPaths;
