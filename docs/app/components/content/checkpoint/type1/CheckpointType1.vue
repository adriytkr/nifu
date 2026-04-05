<script setup lang="ts">
const props=defineProps<{
  choicesCount:number;
  correctChoices:number[];
  max?:number;
}>();

const {
  selectChoice,
  getChoiceState,
  checkChoices,
  resetChoices,
  revealAnswers,
}=useCheckpointType1(
  props.correctChoices,
  props.max,
);
</script>

<template>
  <CommonCheckpoint
    @check="checkChoices"
    @reset="resetChoices"
    @reveal-answers="revealAnswers"
  >
    <template #title>
      <slot name="title"></slot>
    </template>
    <template #content>
      <div>
        <slot name="question"></slot>
      </div>
      <div class="mb-4 font-bold">
        <slot name="command"></slot>
      </div>
      <div class="mb-4 flex flex-col gap-y-2">
        <CheckpointType1Choice
          v-for="i in choicesCount"
          :key="i"
          :state="getChoiceState(i)"
          :disabled="false"
          @click="selectChoice(i)"
        >
          <slot :name="`choice-${i}`"></slot>
        </CheckpointType1Choice>
      </div>
    </template>
  </CommonCheckpoint>
</template>
