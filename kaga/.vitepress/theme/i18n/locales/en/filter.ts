import type {TFilterSchema} from '../shared/filter';

export const filter:TFilterSchema={
  placeholder:'Search articles by title, keywords, ...',
  matches(count:number,query:string){
    if(count===0)return `No matches for "${query}"`;
    if(count===1)return `1 match for "${query}"`;

    return `${count} matches for "${query}"`;
  },
  clear:'Clear Search',
  sort:{
    label:'Sort by',
    nameAsc:'Name (A-Z)',
    nameDesc:'Name (Z-A)',
    difficultyAsc:'Difficulty (+Easy)',
    difficultyDesc:'Difficulty (+Hard)',
  },
};
