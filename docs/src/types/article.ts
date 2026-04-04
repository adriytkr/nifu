export interface ArticleSchema{
  data:{
    title:string;
    description:string;
    tags:string[];
  };
  [key:string]:any;
}

export type Heading={
  depth:number;
  text:string;
  slug:string;
};

export interface TocItem{
  depth:number;
  text:string;
  slug:string;
  children:TocItem[];
}
