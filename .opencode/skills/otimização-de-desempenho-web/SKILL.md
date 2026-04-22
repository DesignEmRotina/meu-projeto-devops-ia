--- 
name: otimização-de-desempenho-web
description: "Otimize o desempenho de sites e aplicativos web, incluindo velocidade de carregamento, Core Web Vitals, tamanho do pacote, estratégias de cache e desempenho em tempo de execução"
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Otimização de Desempenho Web

## Visão Geral

Ajude desenvolvedores a otimizar o desempenho de sites e aplicativos web para melhorar a experiência do usuário, o posicionamento em mecanismos de busca (SEO) e as taxas de conversão. Esta habilidade fornece abordagens sistemáticas para medir, analisar e melhorar a velocidade de carregamento, o desempenho em tempo de execução e as métricas Core Web Vitals.

## Quando usar esta habilidade

- Use quando o site ou aplicativo estiver carregando lentamente
- Use ao otimizar os Core Web Vitals (LCP, FID, CLS)
- Use ao reduzir o tamanho do pacote JavaScript
- Use ao melhorar o Tempo de Interatividade (TTI)
- Use ao otimizar imagens e recursos
- Use ao implementar estratégias de cache
- Use ao depurar gargalos de desempenho
- Use ao se preparar para auditorias de desempenho

## Como funciona

### Etapa 1: Medir o desempenho atual

Ajudarei você a estabelecer métricas de referência:
- Executar auditorias do Lighthouse
- Medir os Core Web Vitals (LCP, FID, CLS)
- Verificar o tamanho dos pacotes
- Analisar o fluxo de rede
- Identificar gargalos de desempenho

### Etapa 2: Identificar problemas

Analise os problemas de desempenho:
- Pacotes JavaScript grandes
- Imagens não otimizadas
- Recursos que bloqueiam a renderização
- Tempos de resposta lentos do servidor
- Cabeçalhos de cache ausentes
- Mudanças de layout
- Tarefas longas bloqueando a thread principal

### Etapa 3: Priorize as Otimizações

Concentre-se em melhorias de alto impacto:
- Otimização do caminho de renderização crítico
- Divisão de código e carregamento lento (lazy loading)
- Otimização de imagens
- Estratégias de cache
- Otimização de scripts de terceiros

### Etapa 4: Implemente as Otimizações

Aplique melhorias de desempenho:
- Otimize os recursos (imagens, fontes, CSS, JS)
- Implemente a divisão de código
- Adicione cabeçalhos de cache
- Carregue recursos não críticos de forma lenta (lazy loading)
- Otimize o caminho de renderização crítico

### Etapa 5: Verifique as Melhorias

Meça o impacto das alterações:
- Execute novamente as auditorias do Lighthouse
- Compare as métricas antes e depois
- Monitore as métricas de usuários reais (RUM)
- Teste em diferentes dispositivos e redes

## Exemplos

### Exemplo 1: Otimizando as Core Web Vitals
```markdown
## Performance Audit Results

### Current Metrics (Before Optimization)
- **LCP (Largest Contentful Paint):** 4.2s ❌ (should be < 2.5s)
- **FID (First Input Delay):** 180ms ❌ (should be < 100ms)
- **CLS (Cumulative Layout Shift):** 0.25 ❌ (should be < 0.1)
- **Lighthouse Score:** 62/100

### Issues Identified

1. **LCP Issue:** Hero image (2.5MB) loads slowly
2. **FID Issue:** Large JavaScript bundle (850KB) blocks main thread
3. **CLS Issue:** Images without dimensions cause layout shifts

### Optimization Plan

#### Fix LCP (Largest Contentful Paint)

**Problem:** Hero image is 2.5MB and loads slowly

**Solutions:**
\`\`\`html
<!-- Before: Unoptimized image -->
<img src="/hero.jpg" alt="Hero">

<!-- After: Optimized with modern formats -->
<picture>
  <source srcset="/hero.avif" type="image/avif">
  <source srcset="/hero.webp" type="image/webp">
  <img 
    src="/hero.jpg" 
    alt="Hero"
    width="1200" 
    height="600"
    loading="eager"
    fetchpriority="high"
  >
</picture>
\`\`\`

**Additional optimizations:**
- Compress image to < 200KB
- Use CDN for faster delivery
- Preload hero image: `<link rel="preload" as="image" href="/hero.avif">`

#### Fix FID (First Input Delay)

**Problem:** 850KB JavaScript bundle blocks main thread

**Solutions:**

1. **Code Splitting:**
\`\`\`javascript
// Before: Everything in one bundle
import { HeavyComponent } from './HeavyComponent';
import { Analytics } from './analytics';
import { ChatWidget } from './chat';

// After: Lazy load non-critical code
const HeavyComponent = lazy(() => import('./HeavyComponent'));
const ChatWidget = lazy(() => import('./chat'));

// Load analytics after page interactive
if (typeof window !== 'undefined') {
  window.addEventListener('load', () => {
    import('./analytics').then(({ Analytics }) => {
      Analytics.init();
    });
  });
}
\`\`\`

2. **Remove Unused Dependencies:**
\`\`\`bash
# Analyze bundle
npx webpack-bundle-analyzer

# Remove unused packages
npm uninstall moment  # Use date-fns instead (smaller)
npm install date-fns
\`\`\`

3. **Defer Non-Critical Scripts:**
\`\`\`html
<!-- Before: Blocks rendering -->
<script src="/analytics.js"></script>

<!-- After: Deferred -->
<script src="/analytics.js" defer></script>
\`\`\`

#### Fix CLS (Cumulative Layout Shift)

**Problem:** Images without dimensions cause layout shifts

**Solutions:**
\`\`\`html
<!-- Before: No dimensions -->
<img src="/product.jpg" alt="Product">

<!-- After: With dimensions -->
<img 
  src="/product.jpg" 
  alt="Product"
  width="400" 
  height="300"
  style="aspect-ratio: 4/3;"
>
\`\`\`

**For dynamic content:**
\`\`\`css
/* Reserve space for content that loads later */
.skeleton-loader {
  min-height: 200px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
\`\`\`

### Results After Optimization

- **LCP:** 1.8s ✅ (improved by 57%)
- **FID:** 45ms ✅ (improved by 75%)
- **CLS:** 0.05 ✅ (improved by 80%)
- **Lighthouse Score:** 94/100 ✅
```

### Exemplo 2: Reduzindo o tamanho do pacote JavaScript
```markdown
## Bundle Size Optimization

### Current State
- **Total Bundle:** 850KB (gzipped: 280KB)
- **Main Bundle:** 650KB
- **Vendor Bundle:** 200KB
- **Load Time (3G):** 8.2s

### Analysis

\`\`\`bash
# Analyze bundle composition
npx webpack-bundle-analyzer dist/stats.json
\`\`\`

**Findings:**
1. Moment.js: 67KB (can replace with date-fns: 12KB)
2. Lodash: 72KB (using entire library, only need 5 functions)
3. Unused code: ~150KB of dead code
4. No code splitting: Everything in one bundle

### Optimization Steps

#### 1. Replace Heavy Dependencies

\`\`\`bash
# Remove moment.js (67KB) → Use date-fns (12KB)
npm uninstall moment
npm install date-fns

# Before
import moment from 'moment';
const formatted = moment(date).format('YYYY-MM-DD');

# After
import { format } from 'date-fns';
const formatted = format(date, 'yyyy-MM-dd');
\`\`\`

**Savings:** 55KB

#### 2. Use Lodash Selectively

\`\`\`javascript
// Before: Import entire library (72KB)
import _ from 'lodash';
const unique = _.uniq(array);

// After: Import only what you need (5KB)
import uniq from 'lodash/uniq';
const unique = uniq(array);

// Or use native methods
const unique = [...new Set(array)];
\`\`\`

**Savings:** 67KB

#### 3. Implement Code Splitting

\`\`\`javascript
// Next.js example
import dynamic from 'next/dynamic';

// Lazy load heavy components
const Chart = dynamic(() => import('./Chart'), {
  loading: () => <div>Loading chart...</div>,
  ssr: false
});

const AdminPanel = dynamic(() => import('./AdminPanel'), {
  loading: () => <div>Loading...</div>
});

// Route-based code splitting (automatic in Next.js)
// pages/admin.js - Only loaded when visiting /admin
// pages/dashboard.js - Only loaded when visiting /dashboard
\`\`\`

#### 4. Remove Dead Code

\`\`\`javascript
// Enable tree shaking in webpack.config.js
module.exports = {
  mode: 'production',
  optimization: {
    usedExports: true,
    sideEffects: false
  }
};

// In package.json
{
  "sideEffects": false
}
\`\`\`

#### 5. Optimize Third-Party Scripts

\`\`\`html
<!-- Before: Loads immediately -->
<script src="https://analytics.com/script.js"></script>

<!-- After: Load after page interactive -->
<script>
  window.addEventListener('load', () => {
    const script = document.createElement('script');
    script.src = 'https://analytics.com/script.js';
    script.async = true;
    document.body.appendChild(script);
  });
</script>
\`\`\`

### Results

- **Total Bundle:** 380KB ✅ (reduced by 55%)
- **Main Bundle:** 180KB ✅
- **Vendor Bundle:** 80KB ✅
- **Load Time (3G):** 3.1s ✅ (improved by 62%)

### Exemplo 3: Estratégia de Otimização de Imagem

```markdown
## Image Optimization

### Current Issues
- 15 images totaling 12MB
- No modern formats (WebP, AVIF)
- No responsive images
- No lazy loading

### Optimization Strategy

#### 1. Convert to Modern Formats

\`\`\`bash
# Install image optimization tools
npm install sharp

# Conversion script (optimize-images.js)
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function optimizeImage(inputPath, outputDir) {
  const filename = path.basename(inputPath, path.extname(inputPath));
  
  // Generate WebP
  await sharp(inputPath)
    .webp({ quality: 80 })
    .toFile(path.join(outputDir, \`\${filename}.webp\`));
  
  // Generate AVIF (best compression)
  await sharp(inputPath)
    .avif({ quality: 70 })
    .toFile(path.join(outputDir, \`\${filename}.avif\`));
  
  // Generate optimized JPEG fallback
  await sharp(inputPath)
    .jpeg({ quality: 80, progressive: true })
    .toFile(path.join(outputDir, \`\${filename}.jpg\`));
}

// Process all images
const images = fs.readdirSync('./images');
images.forEach(img => {
  optimizeImage(\`./images/\${img}\`, './images/optimized');
});
\`\`\`

#### 2. Implement Responsive Images

\`\`\`html
<!-- Responsive images with modern formats -->
<picture>
  <!-- AVIF for browsers that support it (best compression) -->
  <source 
    srcset="
      /images/hero-400.avif 400w,
      /images/hero-800.avif 800w,
      /images/hero-1200.avif 1200w
    "
    type="image/avif"
    sizes="(max-width: 768px) 100vw, 50vw"
  >
  
  <!-- WebP for browsers that support it -->
  <source 
    srcset="
      /images/hero-400.webp 400w,
      /images/hero-800.webp 800w,
      /images/hero-1200.webp 1200w
    "
    type="image/webp"
    sizes="(max-width: 768px) 100vw, 50vw"
  >
  
  <!-- JPEG fallback -->
  <img 
    src="/images/hero-800.jpg"
    srcset="
      /images/hero-400.jpg 400w,
      /images/hero-800.jpg 800w,
      /images/hero-1200.jpg 1200w
    "
    sizes="(max-width: 768px) 100vw, 50vw"
    alt="Hero image"
    width="1200"
    height="600"
    loading="lazy"
  >
</picture>
\`\`\`

#### 3. Lazy Loading

\`\`\`html
<!-- Native lazy loading -->
<img 
  src="/image.jpg" 
  alt="Description"
  loading="lazy"
  width="800"
  height="600"
>

<!-- Eager loading for above-the-fold images -->
<img 
  src="/hero.jpg" 
  alt="Hero"
  loading="eager"
  fetchpriority="high"
>
\`\`\`

#### 4. Next.js Image Component

\`\`\`javascript
import Image from 'next/image';

// Automatic optimization
<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority  // For above-the-fold images
  quality={80}
/>

// Lazy loaded
<Image
  src="/product.jpg"
  alt="Product"
  width={400}
  height={300}
  loading="lazy"
/>
\`\`\`

### Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Total Image Size | 12MB | 1.8MB | 85% reduction |
| LCP | 4.5s | 1.6s | 64% faster |
| Page Load (3G) | 18s | 4.2s | 77% faster |
```

## Melhores Práticas

### ✅ Faça Isso

- **Meça Primeiro** - Sempre estabeleça métricas de referência antes de otimizar
- **Use o Lighthouse** - Execute auditorias regularmente para acompanhar o progresso
- **Otimize Imagens** - Use formatos modernos (WebP, AVIF) e imagens responsivas
- **Dividir Código** - Divida pacotes grandes em partes menores
- **Carregamento Lento** - Adie o carregamento de recursos não críticos
- **Cache Agressivo** - Defina cabeçalhos de cache adequados para ativos estáticos
- **Minimize o Trabalho da Thread Principal** - Mantenha a execução do JavaScript em blocos de menos de 50ms
- **Pré-carregue Recursos Críticos** - Use `<link rel="preload">` para ativos críticos
- **Use CDN** - Sirva ativos estáticos a partir de uma CDN para uma entrega mais rápida
- **Monitore Usuários Reais** - Monitore as Core Web Vitals de usuários reais

### ❌ Não Faça Isso

- **Não Otimize às Cegas** - Meça primeiro, depois otimize
- **Não Ignore Dispositivos Móveis** - Teste em dispositivos móveis reais e redes lentas
- **Não bloqueie a renderização** - Evite CSS e JavaScript que bloqueiem a renderização
- **Não carregue tudo antecipadamente** - Carregue recursos não críticos de forma assíncrona
- **Não se esqueça das dimensões** - Sempre especifique a largura e a altura da imagem
- **Não use scripts síncronos** - Use os atributos async ou defer
- **Não ignore scripts de terceiros** - Eles geralmente causam problemas de desempenho
- **Não ignore a compressão** - Sempre comprima e minimize os recursos

## Armadilhas comuns

### Problema: Otimizado para desktop, mas lento em dispositivos móveis
**Sintomas:** Boa pontuação no Lighthouse em desktops, baixa em dispositivos móveis
**Solução:**
- Teste em dispositivos móveis reais
- Use a limitação de taxa de transferência do Chrome DevTools para dispositivos móveis
- Otimize para redes 3G/4G
- Reduza o tempo de execução do JavaScript
```bash
# Teste com limitação de taxa de transferência
lighthouse https://yoursite.com --throttling.cpuSlowdownMultiplier=4
```

### Problema: Pacote JavaScript grande
**Sintomas:** Tempo de interação (TTI) longo, FID alto
**Solução:**
- Analisar o pacote com webpack-bundle-analyzer
- Remover dependências não utilizadas
- Implementar divisão de código
- Carregar código não crítico de forma preguiçosa
```bash
# Analisar pacote
npx webpack-bundle-analyzer dist/stats.json
```

### Problema: Imagens causando mudanças de layout
**Sintomas:** Pontuação CLS alta, conteúdo pulando
**Solução:**
- Sempre especificar largura e altura
- Usar a propriedade CSS aspect-ratio
- Reservar espaço com carregadores de esqueleto
```css
img {

aspect-ratio: 16 / 9;

width: 100%;

height: auto;
}
```

### Problema: Tempo de resposta lento do servidor
**Sintomas:** Alto TTFB (Tempo até o primeiro byte)
**Solução:**
- Implementar cache no servidor
- Usar CDN para arquivos estáticos
- Otimizar consultas ao banco de dados
- Considerar geração de sites estáticos (SSG)
```javascript
// Next.js: Geração estática
export async function getStaticProps() {

const data = await fetchData();

return {

props: { data },

revalidate: 60 // Regenerar a cada 60 segundos
};

}
```

## Lista de Verificação de Desempenho

### Imagens
- [ ] Converter para formatos modernos (WebP, AVIF)
- [ ] Implementar imagens responsivas
- [ ] Adicionar carregamento lento (lazy loading)
- [ ] Especificar dimensões (largura/altura)
- [ ] Comprimir imagens (< 200 KB cada)
- [ ] Usar CDN para distribuição

### JavaScript
- [ ] Tamanho do pacote < 200 KB (compactado com gzip)
- [ ] Implementar divisão de código
- [ ] Carregar código não crítico de forma lenta (lazy loading)
- [ ] Remover dependências não utilizadas
- [ ] Minificar e comprimir
- [ ] Usar async/defer para scripts

### CSS
- [ ] Inserir CSS crítico em linha
- [ ] Adiar CSS não crítico
- [ ] Remover CSS não utilizado
- [ ] Minificar arquivos CSS
- [ ] Usar contenção de CSS

### Cache
- [ ] Definir cabeçalhos de cache para ativos estáticos
- [ [ ] Implementar service worker
- [ ] Usar cache de CDN
- [ ] Armazenar em cache as respostas da API
- [ ] Versionar ativos estáticos

### Principais métricas da Web
- [ ] LCP < 2,5s
- [ ] FID < 100ms
- [ ] CLS < 0,1
- [ ] TTFB < 600ms
- [ ] TTI < 3,8s

## Ferramentas de desempenho

### Ferramentas de medição
- **Lighthouse** - Auditoria de desempenho abrangente
- **WebPageTest** - Análise detalhada em cascata
- **Chrome DevTools** - Criação de perfil de desempenho
- **PageSpeed ​​Insights** - Métricas de usuários reais
- **Extensão Web Vitals** - Monitorar métricas principais da Web

### Ferramentas de análise
- **webpack-bundle-analyzer** - Visualizar a composição do pacote
- **source-map-explorer** - Analisar o tamanho do pacote
- **Bundlephobia** - Verificar os tamanhos dos pacotes antes da instalação
- **ImageOptim** - Ferramenta de compressão de imagens

### Ferramentas de Monitoramento
- **Google Analytics** - Rastreamento de Core Web Vitals
- **Sentry** - Monitoramento de desempenho
- **New Relic** - Monitoramento de desempenho de aplicativos
- **Datadog** - Monitoramento de usuários reais

## Habilidades Relacionadas

- `@react-best-practices` - Padrões de desempenho do React
- `@frontend-dev-guidelines` - Padrões de desenvolvimento frontend
- `@systematic-debugging` - Depuração de problemas de desempenho
- `@senior-architect` - Arquitetura para desempenho

## Recursos Adicionais

- [Web.dev Performance](https://web.dev/performance/)
- [Core Web Vitals](https://web.dev/vitals/)
- [Documentação do Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [MDN Performance](https://developers.google.com/web/tools/lighthouse) Guia de Desempenho do Next.js
- Guia de Otimização de Imagens

- **Dica profissional:** Concentre-se primeiro nas Core Web Vitals (LCP, FID, CLS) - elas têm o maior impacto na experiência do usuário e no ranqueamento em SEO!