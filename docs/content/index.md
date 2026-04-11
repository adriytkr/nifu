---
layout: normal
---

<script setup lang="ts">
import BrowserIcon from '~/components/icons/base/BrowserIcon.vue';
import YoutubeLogoIcon from '~/components/icons/base/YoutubeLogoIcon.vue';

import ArticleList from '~/components/articles/ArticleList.vue';

import { data as articles } from '~/content/en-featured-articles.data.ts';
</script>

<section class="py-24">
  <div class="max-w-2xl mx-auto px-4 flex flex-col items-center">
    <h1 class="mb-2 font-bold uppercase text-4xl text-center">
    Kaga — Understand, don't memorize
    </h1>
    <span class="mb-4 block text-sm text-center">
      <i>(Knowledge Arises from Geometry and Algorithms)</i>
    </span>
    <p class="mb-8 text-center">
      Enjoy clear, intuitive lessons about Math, Physics and Coding
    </p>
    <div class="flex flex-wrap gap-4">
      <VpLink
        to="/articles"
        class="inline-flex items-center gap-x-2 px-4 py-2 bg-primary rounded-sm text-white transition-colors duration-200 hover:no-underline hover:bg-secondary"
      >
        <BrowserIcon/>
        <span>Browse Articles</span>
      </VpLink>
      <a
        href="https://www.youtube.com/@adriytkr"
        class="inline-flex items-center gap-x-2 px-4 py-2 bg-red-600 rounded-sm text-white transition-colors duration-200 hover:no-underline hover:bg-red-800"
      >
        <YoutubeLogoIcon/>
        <span>My Channel</span>
      </a>
    </div>
  </div>
</section>

<section class="mb-24">
  <div class="max-w-4xl mx-auto px-4">
    <h2 class="mb-4 text-2xl font-bold">Featured Articles</h2>
    <ArticleList
      v-if="articles"
      :articles="articles"
    />
  </div>
</section>

<section class="mb-24 bg-surface">
  <div class="max-w-2xl mx-auto px-4 py-16">
    <h2 class="mb-2 text-2xl font-bold">What is so special about this blog?</h2>
    <p class="mb-4">
      The Internet is infested with explanations that teach memorization — just plug this value into the formula ah thing — and don't teach intuition.
    </p>
    <p class="mb-4">
      However, you won't find this type of content here. By placing intuition over memorization, <strong>harder complex feel as natural as breathing</strong>.
    </p>
    <ImageWithCaption src="/images/admiral-graf-spee.jpg">
      The articles are full of interactive components
    </ImageWithCaption>
    <p class="mt-4">
      The articles are structured in a way that makes you feel an discoverer. You are not just given concepts to memorize, you build them.
    </p>
  </div>
</section>

<section class="mb-24">
  <div class="max-w-2xl mx-auto px-4">
    <h2 class="mb-2 text-2xl font-bold">About me</h2>
    <p class="mb-4">
      I am from Brazil and here we have a culture where rapid results are incentivated, but as consequence people end up more memorizing concepts to get fast result rather than understand what they are even doing.
    </p>
    <p>
      So I came up with a solution, I built this blog (+ my youtube channel) to promote a different way of learning — one that encourages critical thinking and is dynamic.
    </p>
  </div>
</section>
