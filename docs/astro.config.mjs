// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'My Docs',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }],
			sidebar: [
				{
					label: 'Calculus',
					autogenerate: { directory: 'calculus' },
				},
				{
					label: 'Advanced Calculus',
					autogenerate: { directory: 'advanced-calculus' },
				},
				{
					label: 'Linear Algebra',
					autogenerate: { directory: 'linear-algebra' },
				},
				{
					label: 'Physics',
					autogenerate: { directory: 'physics' },
				},
				{
					label: 'Competitive Programming',
					autogenerate: { directory: 'competitive-programming' },
				},
			],
			customCss: ['./src/assets/styles/custom.css'],
		}),
	],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});
