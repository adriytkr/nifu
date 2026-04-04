import type { GetStaticPaths } from 'astro';
import {getCollection} from 'astro:content';

import type { Heading, TocItem } from '@/types/article';
import type { Locale } from '@/types/i18n';

export const getArticlePaths=(locale:Locale)=>(async()=>{
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

export function buildToc(headings:Heading[]):TocItem[]{
  const toc:TocItem[]=[];
  const parentHeadings=new Map<number,TocItem>();

  headings.forEach((h) =>{
    const heading:TocItem={
      ...h,
      children:[],
    };

    parentHeadings.set(heading.depth,heading);

    if(heading.depth===2){
      toc.push(heading);
      return;
    }
    
    if(heading.depth>2){
      const parent=parentHeadings.get(heading.depth-1);
      if(parent)parent.children.push(heading);
    }
  });

  return toc;
}
