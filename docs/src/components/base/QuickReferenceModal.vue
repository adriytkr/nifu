<script setup lang="ts">
defineEmits<{
  (e:'close'):void;
}>();
</script>

<template>
  <div class="quickReference-overlay" @click.self="$emit('close')">
    <div class="quickReference">
      <div class="quickReference-top">
        <h1 class="quickReference-title">Quick Reference</h1>
        <button class="quickReference-closeBtn" @click="$emit('close')">
          <svg class="quickReference-closeBtn-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 -960 960 960"  fill="#e3e3e3">
            <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.quickReference-overlay{
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.3);
  backdrop-filter:
    blur(8px)
    saturate(180%);
  position:fixed;
  left:0;
  top:0;
  z-index:9999;
  display:flex;
  justify-content:center;
  align-items:center;
}

.quickReference{
  min-width:730px;
  padding:24px;
  background-color:#1a1a1a;
  border-radius:6px;
}

.quickReference-top{
  display:flex;
  justify-content:space-between;
  align-items:center;
}

.quickReference-closeBtn{
  background-color:transparent;
  border:none;
  cursor:pointer;
}

.quickReference-closeBtn-icon{
  display:block;
}
</style>
