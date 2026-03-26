// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

import vue from '@astrojs/vue';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Akagi',
			components:{
				SocialIcons:'./src/components/base/GlobalPlugin.astro',
				Footer:'./src/components/base/TheFooter.astro',
			},
			sidebar: [
				{
					label:'View all Articles',
					link:'/articles',
				},
				{
					label: 'Calculus',
					collapsed:true,
					autogenerate: {
						directory: 'articles/calculus',
					},
				},
				{
					label: 'Advanced Calculus',
					collapsed:true,
					autogenerate: {
						directory: 'articles/advanced-calculus',
					},
				},
				{
					label: 'Linear Algebra',
					collapsed:true,
					autogenerate: {
						directory: 'articles/linear-algebra',
					},
				},
				{
					label: 'Physics',
					collapsed:true,
					autogenerate: {
						directory: 'articles/physics',
					},
				},
				{
					label: 'Competitive Programming',
					collapsed:true,
					autogenerate: {
						directory: 'articles/competitive-programming',
					},
				},
				{
					label: 'Statistics',
					collapsed:true,
					autogenerate: {
						directory: 'articles/statistics',
					},
				},
			],
			customCss: ['./src/assets/styles/custom.css'],
		}),
		vue(),
	],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});