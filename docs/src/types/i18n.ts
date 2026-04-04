export type Locale='en'|'pt-br';

export type TSchema<T>=Record<Locale,T>;

export interface ArticlesPageT{
  placeholder:string;
  clear:string;
  matches:(count:number,query:string)=>string;
};
