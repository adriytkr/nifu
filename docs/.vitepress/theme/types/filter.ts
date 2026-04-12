import {InjectionKey} from 'vue';

export type ViewMode='grid'|'list';
export const ViewModeKey=Symbol() as InjectionKey<ViewMode>;
