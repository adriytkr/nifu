<script setup lang="ts">
import { useDialog } from '~/composables/useDialog';

import type { DialogContext } from '~/types/dialog';

const {
  dialogRef,
  context,
}=useDialog();

defineExpose<DialogContext>(context);
</script>

<template>
  <dialog
    ref="dialogRef"
    class="w-2xl shadow-lg bg-background rounded-sm top-1/2 left-1/2 -translate-1/2 backdrop:bg-black/40 backdrop:backdrop-blur-sm"
    @click.self="$emit('close')"
  >
    <h1>Quick Reference</h1>
  </dialog>
</template>
