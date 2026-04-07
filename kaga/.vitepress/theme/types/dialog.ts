export interface DialogContext{
  open:()=>void;
  close:()=>void;
}

export interface SearchDialogContext extends DialogContext{
  focusInput:()=>void;
  clearInput:()=>void;
}
