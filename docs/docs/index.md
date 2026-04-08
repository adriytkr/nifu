---
layout: normal
---

<script setup lang="ts">
import LandingSection from '~/components/landing/Section.vue';
import BrowserIcon from '~/components/icons/BrowserIcon.vue';

import ArticleList from '~/components/articles/ArticleList.vue';

import { data as articles } from '~/content/en-featured-articles.data.ts';
</script>

<LandingSection>
  <div class="px-0 text-center md:px-32">
    <h1 class="mb-2 text-4xl font-bold">Welcome to Kaga</h1>
    <p class="mb-6 italic text-sm text-muted font-medium">
      (Knowledge Arises from Geometry and Algorithms)
    </p>
    <p class="mb-8 leading-relaxed">
      Kaga isn't your run-of-the-mill blog. I show how things actually work under the hood. By prioritizing <strong>intuition over memorization</strong> and using clever analogies, I make hard topics feel <strong>obvious and intuitive</strong>.
    </p>
    <VpLink
      to="/articles"
      class="inline-flex gap-x-2 items-center bg-primary/80 px-6 py-3 text-white font-bold rounded-lg transition-colors duration-200 hover:no-underline hover:bg-primary"
    >
      <BrowserIcon/>
      Browse Articles
    </VpLink>
  </div>
</LandingSection>

<LandingSection title="Featured Articles">
  <ArticleList
    v-if="articles"
    :articles="articles"
  />
</LandingSection>

<LandingSection title="What to expect here?">
  <p class="mb-4">
    This isn't a digital textbook. You won't find dry formulas or explanations that skip the why. Instead, you'll find a sandbox for your curiosity.
  </p>
  <p class="mb-6">
    Also, there won't be only texts. There will be first
  </p>
  <ul class="pl-10 flex flex-col gap-y-2">
    <li>
      <strong>Visual Animations:</strong> Visualize complex topics.
    </li>
    <li>
      <strong>Interactive Graphs:</strong> Change variables and watch the graph react instantly.
    </li>
    <li>
      <strong>Real-World examples:</strong> Learn how the topics are related to the Real World.
    </li>
    <li>
      <strong>Knowledge Gates:</strong> Test your understanding as you go, not just at the end.
    </li>
  </ul>
</LandingSection>

<LandingSection title="Why did I build this?">
  <p class="mb-4">
    I spent far too long reading textbooks or watching videos that focused on the <i>how</i> without explaining the <i>why</i>.
  </p>
  <p class="mb-4">
    Most resources prioritize memorization, teaching you how to follow steps, while completely ignoring the <strong>"under the hood"</strong> engineering. I firmly believe that understanding the underlying logic is what leads to <strong>true mastery</strong> of the subject.
  </p>
  <p>
    I built this platform to offer a different approach to learn: one that favors intuition over memorization, while being challenging and dynamic.
  </p>
</LandingSection>
