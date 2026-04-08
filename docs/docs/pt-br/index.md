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
    <h1 class="mb-2 text-4xl font-bold">Bem-vindo ao Kaga</h1>
    <p class="mb-6 italic text-sm text-muted font-medium">
      (O Conhecimento Surge da Geometria e dos Algoritmos)
    </p>
    <p class="mb-8 leading-relaxed">
      O Kaga não é um blog comum. Eu mostro como as coisas realmente funcionam por baixo do capô. Ao priorizar a
      <strong>intuição sobre a memorização</strong> e usar analogias inteligentes, eu faço tópicos difíceis parecerem
      <strong>óbvios e intuitivos</strong>.
    </p>
    <VpLink to="/articles"
      class="inline-flex gap-x-2 items-center bg-primary/80 px-6 py-3 text-white font-bold rounded-lg transition-colors duration-200 hover:no-underline hover:bg-primary">
      <BrowserIcon />
      Explorar Artigos
    </VpLink>
  </div>
</LandingSection>

<LandingSection title="Artigos em Destaque">
  <ArticleList v-if="articles" :articles="articles" />
</LandingSection>

<LandingSection title="O que esperar por aqui?">
  <p class="mb-4">
    Este não é um livro didático digital. Você não encontrará fórmulas secas ou explicações que pulam o "porquê". Em vez
    disso, encontrará um laboratório para a sua curiosidade.
  </p>
  <p class="mb-6">
    Além disso, não haverá apenas textos. Teremos primeiramente:
  </p>
  <ul class="pl-10 flex flex-col gap-y-2">
    <li>
      <strong>Animações Visuais:</strong> Visualize tópicos complexos.
    </li>
    <li>
      <strong>Gráficos Interativos:</strong> Altere variáveis e veja o gráfico reagir instantaneamente.
    </li>
    <li>
      <strong>Exemplos do Mundo Real:</strong> Saiba como os temas se relacionam com o mundo real.
    </li>
    <li>
      <strong>Portais de Conhecimento:</strong> Teste seu entendimento ao longo do caminho, não apenas no final.
    </li>
  </ul>
</LandingSection>

<LandingSection title="Por que eu construí isso?">
  <p class="mb-4">
    Passei tempo demais lendo livros ou assistindo vídeos que focavam no <i>como</i> sem explicar o <i>porquê</i>.
  </p>
  <p class="mb-4">
    A maioria dos recursos prioriza a memorização, ensinando você a seguir passos, enquanto ignora completamente a
    engenharia <strong>"por baixo do capô"</strong>. Acredito firmemente que entender a lógica subjacente é o que leva
    ao <strong>verdadeiro domínio</strong> do assunto.
  </p>
  <p>
    Construí esta plataforma para oferecer uma abordagem diferente de aprendizado: uma que favorece a intuição em vez da
    memorização, sendo ao mesmo tempo desafiadora e dinâmica.
  </p>
</LandingSection>