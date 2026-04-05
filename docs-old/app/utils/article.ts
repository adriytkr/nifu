import type {
  Heading,
  TocItem,
  ArticleSchema
} from '~/types/article';

export function checkArticleMatch(
  article:ArticleSchema,
  query:string,
  tags:string[],
):boolean{
  const normalizedQuery=query.toLowerCase();

  const matchesTitle=article.data.title
    .toLowerCase()
    .includes(normalizedQuery);

  const matchesDescription=
    article.data.description
      .toLowerCase()
      .includes(normalizedQuery);

  const matchesQuery=matchesTitle||matchesDescription;

  const matchesTag=
    tags.length===0||
    tags.some(tag=>article.data.tags.includes(tag));

  const matchesFlag=
    matchesQuery&&
    matchesTag;

  return matchesFlag;
}

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
