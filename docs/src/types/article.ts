export type ArticleTagType='calculus';

export interface ArticleSchema{
  data:{
    title:string;
    description:string;
    thumbnail?:string;
    tags:ArticleTagType[];
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

export interface SearchFilter{
  focusInput:()=>void;
}

export type ArticleTagList=Record<ArticleTagType,string>;

export type ChoiceState=
  |'idle'
  |'selected'
  |'correct'
  |'incorrect'
  |'missed'
  |'hidden'
  |'disabled';

export type CheckpointType2Field<T>={
  validator:(value:T)=>boolean;
  default:T;
}

export type Schema=Record<string,CheckpointType2Field<any>>;

export type FormState=Record<string,any>;
