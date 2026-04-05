import {
  defineCollection,
  z
} from '@nuxt/content';

export const articleSchema=z.object({
  title:z.string(),
  description:z.string(),
  thumbnail:z.string().optional(),
  tags:z.array(z.string()),
  featured:z.boolean().default(false),
});

export const articlesCollection=
  defineCollection({
    type:'page',
    source:'articles/**/*.md',
    schema:articleSchema,
  });
