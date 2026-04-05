<script setup lang="ts">
import '~/assets/styles/global.css';

import Header from '~/components/app/Header.vue';
import Footer from '~/components/app/Footer.vue';
</script>

<template>
	<Header/>
	<main>
		<slot></slot>
	</main>
	<Footer/>
</template>
