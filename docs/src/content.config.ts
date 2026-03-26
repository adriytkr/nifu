import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

import { z } from 'astro/zod';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend:(context)=>z.object({
				title: z.string(),
				description: z.string(),
				categories: z.array(z.string()).optional(),
				thumbnail: context.image().optional(),
				featured: z.boolean().default(false),
				isArticle:z.boolean().default(false),
				isFeatured:z.boolean().default(false),
			}),
		}),
	}),
};
