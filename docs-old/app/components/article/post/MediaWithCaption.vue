<template>
  <figure class="my-8 not-prose">
    <slot name="media"></slot>
    <figcaption
      v-if="$slots.default!==undefined"
      class="mx-16 mt-2 text-sm text-center text-muted"
    >
      <slot></slot>
    </figcaption>
  </figure>
</template>
