# Referência de Psicologia em UX

> Mergulho profundo em leis de UX, design emocional, construção de confiança e psicologia comportamental.

---

## 1. Leis Fundamentais de UX

### Lei de Hick

**Princípio:** O tempo para tomar uma decisão aumenta de forma logarítmica conforme cresce o número de escolhas.

```
Tempo de Decisão = a + b × log₂(n + 1)
Onde n = número de escolhas
```

**Aplicação:**

* Navegação: Máx. 5–7 itens de primeiro nível
* Formulários: Quebrar em etapas (divulgação progressiva)
* Opções: Definir valores padrão quando possível
* Filtros: Priorizar os mais usados e ocultar os avançados

**Exemplo:**

```
❌ Ruim: 15 itens de menu em uma única navegação
✅ Bom: 5 categorias principais + “Mais”

❌ Ruim: 20 campos de formulário de uma vez
✅ Bom: Wizard em 3 etapas com 5–7 campos cada
```

---

### Lei de Fitts

**Princípio:** O tempo para alcançar um alvo depende da distância e do tamanho.

```
MT = a + b × log₂(1 + D/W)
Onde D = distância, W = largura
```

**Aplicação:**

* CTAs: Botões principais maiores (mín. 44px de altura)
* Alvos de toque: 44×44px no mínimo no mobile
* Posicionamento: Ações importantes próximas ao cursor natural
* Cantos: “Cantos mágicos” (bordas infinitas são mais fáceis de atingir)

**Dimensionamento de Botões:**

```css
.btn-primary { height: 48px; padding: 0 24px; }
.btn-secondary { height: 40px; padding: 0 16px; }
.btn-tertiary { height: 36px; padding: 0 12px; }

@media (hover: none) {
  .btn { min-height: 44px; min-width: 44px; }
}
```

---

### Lei de Miller

**Princípio:** Uma pessoa média consegue manter 7±2 elementos na memória de curto prazo.

**Aplicação:**

* Listas: Agrupar em blocos de 5–7 itens
* Navegação: Máx. 7 itens
* Conteúdo: Quebrar textos longos com títulos
* Telefones: 555-123-4567 (em blocos)

---

### Efeito Von Restorff (Efeito de Isolamento)

**Princípio:** Um item que se destaca é mais facilmente lembrado.

**Aplicação:**

* CTAs: Cor distinta do restante da interface
* Preços: Destacar o plano recomendado
* Informações críticas: Diferenciação visual
* Novidades: Badges ou callouts

---

### Efeito da Posição Serial

**Princípio:** Itens no início (primazia) e no final (recência) são mais lembrados.

**Aplicação:**

* Navegação: Itens mais importantes primeiro e por último
* Listas: Informações-chave no topo e no fim
* Formulários: Campos críticos no início
* CTAs: Repetir no topo e no rodapé

---

### Lei de Jakob

**Princípio:** Usuários passam mais tempo em outros sites. Eles preferem que o seu funcione como os que já conhecem.

**Aplicação:**

* Padrões familiares
* Ícones reconhecíveis
* Vocabulário comum (“Entrar” em vez de “Acessar Portal”)
* Logo no canto superior esquerdo
* Feedback visual padronizado

---

### Lei de Tesler (Conservação da Complexidade)

**Princípio:** A complexidade não pode ser eliminada, apenas transferida do usuário para o sistema.

**Aplicação:**

* Autodetecção de dados
* Preenchimento automático
* Defaults inteligentes
* Integrações como SSO

---

### Lei de Parkinson

**Princípio:** Uma tarefa se expande até consumir todo o tempo disponível.

**Aplicação:**

* Auto-save
* Redução de etapas
* Validação em tempo real
* Onboarding rápido

---

### Limite de Doherty

**Princípio:** Produtividade aumenta quando o sistema responde em menos de 400ms.

**Aplicação:**

* Feedback imediato
* Skeleton screens
* UI otimista
* Microanimações

---

### Lei de Postel (Princípio da Robustez)

**Princípio:** Seja conservador no que produz e tolerante no que aceita.

**Aplicação:**

* Aceitar múltiplos formatos de entrada
* Remover espaços automaticamente
* Fallbacks visuais
* Busca tolerante a erros

---

### Navalha de Occam

**Princípio:** A solução mais simples tende a ser a melhor.

**Aplicação:**

* Menos cliques
* Menos cores e fontes
* Texto direto
* Eliminar ornamentos desnecessários

---

## 2. Percepção Visual (Princípios da Gestalt)

### Lei da Proximidade

Elementos próximos são percebidos como relacionados.

### Lei da Similaridade

Elementos semelhantes são percebidos como um grupo.

### Lei da Região Comum

Elementos dentro da mesma área são agrupados.

### Lei da Conectividade Uniforme

Elementos conectados visualmente são percebidos como relacionados.

### Lei da Prägnanz (Simplicidade)

O cérebro prefere formas simples e estáveis.

### Figura/Fundo

Diferencia claramente o que está em foco e o que é contexto.

### Ponto Focal

O que mais se destaca chama atenção primeiro.

---

## 3. Vieses Cognitivos e Comportamento

### Efeito Zeigarnik

Tarefas incompletas são mais lembradas.

### Efeito Gradiente de Meta

Quanto mais perto da meta, maior a motivação.

### Regra do Pico-Fim

As pessoas lembram mais do pico emocional e do final da experiência.

### Efeito Estético-Usabilidade

Interfaces bonitas parecem mais fáceis de usar.

### Viés de Ancoragem

A primeira informação influencia decisões.

### Prova Social

As pessoas seguem o comportamento de outras.

### Escassez

O que é raro parece mais valioso.

### Viés de Autoridade

Autoridades influenciam decisões.

### Aversão à Perda

Evitar perdas é mais forte que obter ganhos.

### Falso Consenso

Assumir que todos pensam como você.

### Maldição do Conhecimento

Esquecer que o usuário não sabe o que você sabe.

### Efeito Degrau (Foot-in-the-Door)

Pequenos compromissos levam a grandes compromissos.

---

## 4. Design Emocional (Don Norman)

### Três Níveis de Processamento

* **Visceral:** Primeira impressão
* **Comportamental:** Uso e eficiência
* **Reflexivo:** Significado e identidade

---

## 5. Sistema de Construção de Confiança

### Categorias de Sinais de Confiança

* Segurança
* Prova social
* Transparência
* Profissionalismo
* Autoridade

---

## 6. Gestão de Carga Cognitiva

### Tipos

* Intrínseca
* Extrínseca
* Germânica

### Estratégias

* Simplificação
* Agrupamento
* Divulgação progressiva
* Padrões familiares
* Externalização da memória

---

## 7. Design Persuasivo (Ético)

* Escassez real
* Prova social legítima
* Autoridade verdadeira
* Urgência honesta
* Compromisso progressivo

---

## 8. Personas de Usuário (Resumo)

### Gen Z

Mobile-first, visual, rápido

### Millennials

Valor, experiência, transparência

### Geração X

Eficiência, clareza, pragmatismo

### Baby Boomers

Legibilidade, simplicidade, confiança

---

## 9. Mapeamento Emocional de Cores

| Emoção       | Cores          | Uso        |
| ------------ | -------------- | ---------- |
| Confiança    | Azul, Verde    | Financeiro |
| Urgência     | Vermelho       | Erros      |
| Luxo         | Preto, Dourado | Premium    |
| Criatividade | Rosa, Teal     | Arte       |

---

## 10. Checklist Psicológico Pré-Lançamento

* [ ] Navegação com até 7 escolhas
* [ ] CTAs acessíveis
* [ ] Conteúdo em blocos
* [ ] Feedback < 400ms
* [ ] CTA em destaque
* [ ] Prova social visível
* [ ] Escassez ética
* [ ] Redução de ruído visual
* [ ] Acessibilidade garantida
* [ ] Foco claro no elemento principal

---