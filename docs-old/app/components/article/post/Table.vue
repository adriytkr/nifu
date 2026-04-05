<script setup lang="ts">
defineProps<{
  rows:number;
  cols:number;
  horizontal?:boolean;
}>();
</script>

<template>
  <table>
    <tr
       v-for="row in rows"
       :key="row"
    >
      <td
        v-for="col in cols"
        :key="col"
      >
        <slot :name="`cell-${row}-${col}`"></slot>
      </td>
    </tr>
  </table>
</template>
