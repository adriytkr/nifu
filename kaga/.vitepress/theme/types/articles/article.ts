export type ArticleDifficulty=
  'training'|
  'easy'|
  'medium'|
  'hard'|
  'insane';

export type Article={
  slug:string;
  title:string;
  description:string;
  thumbnail?:string;
  tags:string[];
  difficulty:ArticleDifficulty;
}
