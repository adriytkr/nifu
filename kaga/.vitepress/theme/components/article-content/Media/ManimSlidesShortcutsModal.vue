<script setup lang="ts">
import { DialogContext } from '~/types/dialog';
import { useDialog } from '~/composables/useDialog';

import AppIconButton from '~/components/app/AppIconButton.vue';
import CloseIcon from '~/components/icons/CloseIcon.vue';

import KeyboardKey from '~/components/app/KeyboardKey.vue';
import ArrowKeyIcon from '~/components/icons/ArrowKeyIcon.vue';

defineEmits<{
  (e:'close'):void;
}>();

const {
  dialogRef,
  context,
}=useDialog();

defineExpose<DialogContext>(context);
</script>

<template>
  <dialog
    ref="dialogRef"
    class="w-xl shadow-lg bg-background p-4 rounded-sm top-1/2 left-1/2 -translate-1/2 backdrop:bg-black/40 backdrop:backdrop-blur-sm"
    @click.self="$emit('close')"
  >
    <header class="flex justify-between items-center mb-4">
      <h2 class="font-medium">Keyboard Shortcuts</h2>
      <AppIconButton @click="$emit('close')">
        <CloseIcon/>
      </AppIconButton>
    </header>
    <p class="mb-8">
      Your video should be focused to use these shortcuts (click anywhere on the video to focus).
    </p>
    <ul class="flex flex-col gap-y-4">
      <li class="flex justify-between items-center">
        <span>Play/Pause</span>
        <KeyboardKey>Space</KeyboardKey>
      </li>
      <li class="flex justify-between items-center">
        <span>Previous Slide</span>
        <KeyboardKey>
          <ArrowKeyIcon class="rotate-180"/>
        </KeyboardKey>
      </li>
      <li class="flex justify-between items-center">
        <span>Next Slide</span>
        <KeyboardKey>
          <ArrowKeyIcon/>
        </KeyboardKey>
      </li>
      <li class="flex justify-between items-center">
        <span>First Slide</span>
        <KeyboardKey>
          <ArrowKeyIcon class="-rotate-90"/>
        </KeyboardKey>
      </li>
      <li class="flex justify-between items-center">
        <span>Last Slide</span>
        <KeyboardKey>
          <ArrowKeyIcon class="rotate-90"/>
        </KeyboardKey>
      </li>
      <li class="flex justify-between items-center">
        <span>Toggle Full Screen Mode</span>
        <KeyboardKey>F</KeyboardKey>
      </li>
    </ul>
  </dialog>
</template>
