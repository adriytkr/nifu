import type { Heading } from '@types/article';
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

export interface TocItem {
  depth: number;
  text: string;
  slug: string;
  children: TocItem[];
}

export function buildToc(headings:Heading[]):TocItem[]{
  const toc: TocItem[] = [];
  const parentHeadings = new Map<number, TocItem>();

  headings.forEach((h) => {
    const heading: TocItem = { ...h, children: [] };
    parentHeadings.set(heading.depth, heading);

    if (heading.depth === 2) {
      toc.push(heading);
    } else if (heading.depth > 2) {
      const parent = parentHeadings.get(heading.depth - 1);
      if (parent) {
        parent.children.push(heading);
      }
    }
  });
  return toc;
}
