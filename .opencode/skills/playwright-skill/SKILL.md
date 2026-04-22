--- 
name: playwright-skill
description: "IMPORTANTE - Resolução de Caminho: Esta skill pode ser instalada em diferentes locais (sistema de plugins, instalação manual, global ou específico do projeto). Antes de executar qualquer comando, determine o diretório da skill com base em onde você carregou este arquivo SKILL.md e use esse caminho em todos os comandos abaixo."
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
plugin:

configuração:

tipo: manual
resumo: "Execute `npm run setup` no diretório da skill antes do primeiro uso para instalar o Playwright e o Chromium."

documentação: "SKILL.md"
---

**IMPORTANTE - Resolução de Caminho:**
Esta skill pode ser instalada em diferentes locais (sistema de plugins, instalação manual, global ou específico do projeto). Antes de executar qualquer comando, determine o diretório da skill com base em onde você carregou este arquivo SKILL.md e use esse caminho em todos os comandos abaixo. Substitua `$SKILL_DIR` pelo caminho real descoberto.

Caminhos de instalação comuns:

- Sistema de plugins: `<diretório raiz do plugin>/skills/playwright-skill`
- Global manual: `<diretório inicial do agente>/skills/playwright-skill`
- Específico do projeto: `<projeto>/.agent/skills/playwright-skill`

# Automação de navegador com Playwright

Skill de automação de navegador de uso geral. Criarei código Playwright personalizado para qualquer tarefa de automação que você solicitar e a executarei por meio do executor universal.

**FLUXO DE TRABALHO CRÍTICO - Siga estes passos na ordem:**

1. **Detecção automática de servidores de desenvolvimento** - Para testes em localhost, SEMPRE execute a detecção de servidores PRIMEIRO:

``bash

cd $SKILL_DIR && node -e "require('./lib/helpers').detectDevServers().then(servers => console.log(JSON.stringify(servers)))"

``

- Se **1 servidor for encontrado**: Use-o automaticamente e informe o usuário.

- Se **vários servidores forem encontrados**: Pergunte ao usuário qual testar.

- Se **nenhum servidor for encontrado**: Solicite a URL ou ofereça ajuda para iniciar o servidor de desenvolvimento.

2. **Grave scripts em /tmp** - NUNCA grave arquivos de teste no diretório skill; Sempre use `/tmp/playwright-test-*.js`

3. **Use o navegador visível por padrão** - Sempre use `headless: false` a menos que o usuário solicite especificamente o modo headless

4. **Parametrize URLs** - Sempre torne as URLs configuráveis ​​por meio de variável de ambiente ou constante no início do script

## Como funciona

1. Você descreve o que deseja testar/automatizar
2. Eu detecto automaticamente os servidores de desenvolvimento em execução (ou solicito a URL se estiver testando um site externo)
3. Eu escrevo o código personalizado do Playwright em `/tmp/playwright-test-*.js` (não irá sobrecarregar seu projeto)
4. Eu o executo via: `cd $SKILL_DIR && node run.js /tmp/playwright-test-*.js`
5. Os resultados são exibidos em tempo real, com a janela do navegador visível para depuração
6. Os arquivos de teste são removidos automaticamente de /tmp pelo seu sistema operacional

## Configuração (Primeira vez)

```bash
cd $SKILL_DIR
npm run setup
```

Isso instala o Playwright e o navegador Chromium. Só precisa ser feito uma vez.

## Padrão de Execução

**Etapa 1: Detectar servidores de desenvolvimento (para testes em localhost)**

```bash
cd $SKILL_DIR && node -e "require('./lib/helpers').detectDevServers().then(s => console.log(JSON.stringify(s)))"
```

**Etapa 2: Escrever script de teste em /tmp com parâmetro de URL**

```javascript
// /tmp/playwright-test-page.js
const { chromium } = require('playwright');

// URL parametrizada (detectada ou fornecida pelo usuário)
const TARGET_URL = 'http://localhost:3001'; // <-- Detectado automaticamente ou pelo usuário

(async () => {

const browser = await chromium.launch({ headless: false });

const page = await browser.newPage();

await page.goto(TARGET_URL);

console.log('Página carregada:', await page.title());

await page.screenshot({ path: '/tmp/screenshot.png', fullPage: true });

console.log('📸 Captura de tela salva em /tmp/screenshot.png');

await browser.close();
})();
```

**Etapa 3: Executar a partir do diretório de habilidades**

```bash
cd $SKILL_DIR && node run.js /tmp/playwright-test-page.js
```

## Padrões Comuns

### Testar uma Página (Múltiplas Portas de Visualização)

```javascript
// /tmp/playwright-test-responsive.js
const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3001'; // Detecção automática

(async () => {

const browser = await chromium.launch({ headless: false, slowMo: 100 });

const page = await browser.newPage();

// Teste em desktop

await page.setViewportSize({ width: 1920, height: 1080 });

await page.goto(TARGET_URL);

console.log('Desktop - Título:', await page.title());

await page.screenshot({ path: '/tmp/desktop.png', fullPage: true });

// Teste em dispositivos móveis

await page.setViewportSize({ width: 375, height: 667 });

await page.screenshot({ path: '/tmp/mobile.png', fullPage: true });

await browser.close();
})();
```

### Fluxo de Login de Teste

```javascript
// /tmp/playwright-test-login.js
const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3001'; // Detecção automática

(async () => {

const browser = await chromium.launch({ headless: false });

const page = await browser.newPage();

await page.goto(`${TARGET_URL}/login`);

await page.fill('input[name="email"]', 'test@example.com');

await page.fill('input[name="password"]', 'password123');

await page.click('button[type="submit"]');

// Aguardar redirecionamento

await page.waitForURL('**/dashboard');

console.log('✅ Login realizado com sucesso, redirecionado para o painel');

await browser.close();
})();

```

### Preencher e Enviar Formulário

```javascript
// /tmp/playwright-test-form.js
const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3001'; // Detecção automática

(async () => {

const browser = await chromium.launch({ headless: false, slowMo: 50 });

const page = await browser.newPage();

await page.goto(`${TARGET_URL}/contact`);

await page.fill('input[name="name"]', 'John Doe');

await page.fill('input[name="email"]', 'john@example.com');

await page.fill('textarea[name="message"]', 'Mensagem de teste');

await page.click('button[type="submit"]');

// Verificar envio

await page.waitForSelector('.success-message');

console.log('✅ Formulário enviado com sucesso');

await browser.close();
})();
```

### Verificar links quebrados

```javascript
const { chromium } = require('playwright');

(async () => {

const browser = await chromium.launch({ headless: false });

const page = await browser.newPage();

await page.goto('http://localhost:3000');

const links = await page.locator('a[href^="http"]').all();

const results = { working: 0, broken: [] };

for (const link of links) {

const href = await link.getAttribute('href');

try {

const response = await page.request.head(href);

if (response.ok()) {

results.working++;

} else {
results.broken.push({ url: href, status: response.status() });

}
} catch (e) {
results.broken.push({ url: href, error: e.message });

}
}

console.log(`✅ Links funcionando: ${results.working}`);

console.log(`❌ Links quebrados:`, results.broken);

await browser.close();

})();

```

### Capturar tela com tratamento de erros

```javascript
const { chromium } = require('playwright');

(async () => {

const browser = await chromium.launch({ headless: false });

const page = await browser.newPage();

try {

await page.goto('http://localhost:3000', {
waitUntil: 'networkidle',

timeout: 10000,
});

await page.screenshot({
path: '/tmp/screenshot.png',

fullPage: true,

});

console.log('📸 Captura de tela salva em /tmp/screenshot.png');

} catch (error) {

console.error('❌ Erro:', error.message);

} finally {
await browser.close();

}
})();

``

### Testando o Design Responsivo

```javascript
// /tmp/playwright-test-responsive-full.js
const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3001'; // Detecção automática

(async () => {

const browser = await chromium.launch({ headless: false });

const page = await browser.newPage();

const viewports = [
{ name: 'Desktop', width: 1920, height: 1080 },

{ name: 'Tablet', width: 768, height: 1024 },

{ name: 'Mobile', width: 375, height: 667 },

];

for (const viewport of viewports) {

console.log(
`Testando ${viewport.name} (${viewport.width}x${viewport.height})`,

);

await page.setViewportSize({

width: viewport.width,

height: viewport.height,

});

await page.goto(TARGET_URL);
await page.waitForTimeout(1000);

await page.screenshot({
path: `/tmp/${viewport.name.toLowerCase()}.png`,

fullPage: true,

});

}

console.log('✅ Todas as viewports testadas');

await browser.close();

})();
```

## Execução Inline (Tarefas Simples)

Para tarefas rápidas e pontuais, você pode executar código inline sem criar arquivos:

```bash
# Tirar uma captura de tela rápida
cd $SKILL_DIR && node run.js "
const browser = await chromium.launch({ headless: false });
const page = await browser.newPage();
await page.goto('http://localhost:3001');
await page.screenshot({ path: '/tmp/quick-screenshot.png', fullPage: true });
console.log('Captura de tela salva');
await browser.close();
"
```

**Quando usar inline em vez de arquivos:**

- **Inline**: Tarefas rápidas e pontuais (captura de tela, verificar se um elemento existe, obter o título da página)
- **Arquivos**: Testes complexos, verificações de design responsivo, qualquer coisa que o usuário queira Executar novamente

## Funções auxiliares disponíveis

Funções utilitárias opcionais em `lib/helpers.js`:

```javascript
const helpers = require('./lib/helpers');

// Detectar servidores de desenvolvimento em execução (CRÍTICO - use isso primeiro!)
const servers = await helpers.detectDevServers();

console.log('Servidores encontrados:', servers);

// Clique seguro com nova tentativa
await helpers.safeClick(page, 'button.submit', { retries: 3 });

// Digitação segura com limpeza
await helpers.safeType(page, '#username', 'testuser');

// Capturar captura de tela com registro de data e hora
await helpers.takeScreenshot(page, 'test-result');

// Lidar com banners de cookies
await helpers.handleCookieBanner(page);

// Extrair dados da tabela
const data = await helpers.extractTableData(page, 'table.results');

``

Consulte `lib/helpers.js` para obter a lista completa.

## Cabeçalhos HTTP personalizados

Configure cabeçalhos personalizados para todas as solicitações HTTP por meio de variáveis ​​de ambiente. Útil para:

- Identificar tráfego automatizado para seu backend
- Obter respostas otimizadas para LLM (por exemplo, erros em texto simples em vez de HTML formatado)
- Adicionar tokens de autenticação globalmente

### Configuração

**Cabeçalho único (caso comum):**

```bash
PW_HEADER_NAME=X-Automated-By PW_HEADER_VALUE=playwright-skill \

cd $SKILL_DIR && node run.js /tmp/my-script.js
```

**Múltiplos cabeçalhos (formato JSON):**

```bash
PW_EXTRA_HEADERS='{"X-Automated-By":"playwright-skill","X-Debug":"true"}' \

cd $SKILL_DIR && node run.js /tmp/my-script.js
```

### Como funciona

Os cabeçalhos são Aplicado automaticamente ao usar `helpers.createContext()`:

```javascript
const context = await helpers.createContext(browser);

const page = await context.newPage();

// Todas as requisições desta página incluem seus cabeçalhos personalizados
```

Para scripts que usam a API Playwright diretamente, use o `getContextOptionsWithHeaders()` injetado:

```javascript
const context = await browser.newContext(
getContextOptionsWithHeaders({ viewport: { width: 1920, height: 1080 } }),
);

```

## Uso Avançado

Para obter documentação completa da API do Playwright, consulte [API_REFERENCE.md](API_REFERENCE.md):

- Melhores práticas para seletores e localizadores
- Interceptação de rede e simulação de API
- Autenticação e gerenciamento de sessão
- Testes de regressão visual
- Emulação de dispositivos móveis
- Testes de desempenho
- Técnicas de depuração
- Integração CI/CD

## Dicas

- **CRÍTICO: Detecte os servidores PRIMEIRO** - Sempre execute `detectDevServers()` antes de escrever o código de teste para testes em localhost
- **Cabeçalhos personalizados** - Use as variáveis ​​de ambiente `PW_HEADER_NAME`/`PW_HEADER_VALUE` para identificar o tráfego automatizado para o seu backend
- **Use /tmp para arquivos de teste** - Escreva em `/tmp/playwright-test-*.js`, nunca no diretório de habilidades ou no projeto do usuário
- **Parametrize URLs** - Coloque a URL detectada/fornecida em uma constante `TARGET_URL` no início de cada script
- **PADRÃO: Navegador visível** - Sempre use `headless: false` a menos que o usuário solicite explicitamente o modo headless
- **Modo headless** - Use `headless: true` somente quando o usuário solicitar especificamente a execução "headless" ou "em segundo plano"
- **Modo lento:** Use `slowMo: 100` para tornar as ações visíveis e mais fáceis de acompanhar
- **Estratégias de espera:** Use `waitForURL`, `waitForSelector` e `waitForLoadState` em vez de tempos limite fixos
- **Tratamento de erros:** Sempre use try-catch para uma automação robusta
- **Saída do console:** Use `console.log()` para acompanhar o progresso e mostrar o que está acontecendo

## Solução de problemas

**Playwright não instalado:**

```bash
cd $SKILL_DIR && npm run setup
```

**Módulo não encontrado:**

Certifique-se de executar a partir do diretório da skill por meio do wrapper `run.js`

**Navegador Não abre:**
Verifique `headless: false` e ​​certifique-se de que a exibição esteja disponível

**Elemento não encontrado:**
Adicione wait: `await page.waitForSelector('.element', { timeout: 10000 })`

## Exemplo de uso

```
Usuário: "Teste se a página de marketing está com boa aparência"

Claude: Vou testar a página de marketing em diferentes tamanhos de tela. Primeiro, deixe-me detectar os servidores em execução...
[Executa: detectDevServers()]
[Saída: Servidor encontrado na porta 3001]
Encontrei seu servidor de desenvolvimento em execução em http://localhost:3001

[Grava script de automação personalizado em /tmp/playwright-test-marketing.js com URL parametrizada]
[Executa: cd $SKILL_DIR && node run.js /tmp/playwright-test-marketing.js]
[Mostra os resultados com capturas de tela de /tmp/]
```

```
Usuário: "Verificar se o login redireciona corretamente"

Claude: Vou testar o fluxo de login. Primeiro, deixe-me verificar os servidores em execução...
[Executa: detectDevServers()]
[Saída: Servidores encontrados nas portas 3000 e 3001]
Encontrei 2 servidores de desenvolvimento. Qual devo testar?
- http://localhost:3000
- http://localhost:3001

Usuário: "Usar 3001"

[Grava a automação de login em /tmp/playwright-test-login.js]
[Executa: cd $SKILL_DIR && node run.js /tmp/playwright-test-login.js]
[Relatórios: ✅ Login bem-sucedido, redirecionado para /dashboard]
```

## Observações

- Cada automação é escrita sob medida para sua solicitação específica
- Não se limita a scripts pré-construídos - qualquer tarefa de navegador é possível
- Detecta automaticamente servidores de desenvolvimento em execução para eliminar URLs fixas
- Scripts de teste gravados em `/tmp` para limpeza automática (sem arquivos desnecessários)
- O código é executado de forma confiável com a resolução adequada de módulos via `run.js`
- Divulgação progressiva - API_REFERENCE.md carregado somente quando recursos avançados são necessários

## Quando usar
Esta skill é aplicável para executar O fluxo de trabalho ou as ações descritas na visão geral.
