import type {TFilterSchema} from '../shared/filter';

export const filter:TFilterSchema={
  placeholder:'Pesquisar artigos por título, palavras-chaves, ...',
  matches(count:number,query:string){
    if(count===0)return `Nenhum resultado para "${query}"`;
    if(count===1)return `1 resultado para "${query}"`;

    return `${count} resultados para "${query}"`;
  },
  clear:'Limpar Pesquisa',
  sort:{
    label:'Ordenar por',
    nameAsc:'Nome (A-Z)',
    nameDesc:'Nome (Z-A)',
    difficultyAsc:'Dificuldade (+Fácil)',
    difficultyDesc:'Dificuldade (+Difícil)',
  },
};
