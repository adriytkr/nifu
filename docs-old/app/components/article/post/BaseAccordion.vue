<template>
  <div class="group my-8">
    <button class="px-0 mb-2 bg-transparent flex gap-x-1 items-center text-muted">
      <slot name="label"></slot>
    </button>
    <div
      class="grid overflow-hidden transition-all duration-400 ease-in-out grid-rows-[1fr] group-data-is-open:grid-rows-[0fr]"
    >
      <div class="min-h-0 text-gray-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 dark:text-gray-300">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
