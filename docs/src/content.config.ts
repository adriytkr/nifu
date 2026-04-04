import {defineCollection} from 'astro:content';
import {z} from 'astro/zod';
import {glob} from 'astro/loaders';

const articleSchema=z.object({
  title:z.string(),
  description:z.string(),
  thumbnail:z.string().optional(),
  tags:z.array(z.string()).default([]),
  featured:z.boolean().default(false),
});

const articlesCollection=defineCollection({
  loader:glob({
    base:'./src/content/articles',
    pattern:'**/*.{md,mdx}',
  }),
  schema:articleSchema,
});

export const collections={
  articles:articlesCollection,
};
