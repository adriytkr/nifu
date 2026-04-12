<script setup lang="ts">
import {useTooltip} from '~/composables/content/useTooltip';

const {
  reference,
  floating,
  floatingStyles,
  isVisible,
  show,
  hide,
  toggle
}=useTooltip();
</script>

<template>
  <span class="relative inline-block">
    <span
      class="inline-flex underline underline-offset-4 decoration-dotted cursor-help"
      ref="reference"
      tabindex="0"
      @mouseenter="show"
      @mouseleave="hide"
      @focus="show"
      @blur="hide"
      @click="toggle"
      @keydown.esc="hide"
    >
      <slot></slot>
    </span>
    <div
      ref="floating"
      :style="floatingStyles"
      class="reset z-50 w-max max-w-xs p-2 bg-surface rounded shadow-xl text-muted text-xs opacity-0 transition-opacity duration-200 pointer-events-none"
      :class="{ 'opacity-100':isVisible }"
    >
      <slot name="tooltip"></slot>
    </div>
  </span>
</template>
