<template>
  <div class="reset">
    <div class="reset py-1 px-8 bg-primary rounded-t-md rounded-tl-md text-white">
      <slot name="title"></slot>
    </div>
    <div class="reset px-8 py-4 bg-surface rounded-b-md rounded-bl-md border-3 border-t-0 border-primary">
      <slot></slot>
    </div>
  </div>
</template>
