nome: design-de-frontend
descrição: Pensamento e tomada de decisão em design para interfaces web. Use ao projetar componentes, layouts, esquemas de cores, tipografia ou criar interfaces estéticas. Ensina princípios, não valores fixos.
ferramentas-permitidas: Ler, Escrever, Editar, Glob, Grep, Bash
---

# Sistema de Design Frontend

> **Filosofia:** Cada pixel tem um propósito. Contenção é luxo. Psicologia do usuário orienta decisões.  
> **Princípio Central:** PENSE, não memorize. PERGUNTE, não presuma.

---

## 🎯 Regra de Leitura Seletiva (OBRIGATÓRIA)

**Leia SEMPRE os arquivos OBRIGATÓRIOS, e os OPCIONAIS apenas quando necessário:**

| Arquivo | Status | Quando Ler |
|-------|--------|-----------|
| [psicologia-de-ux.md](psicologia-de-ux.md) | 🔴 **OBRIGATÓRIO** | Sempre ler primeiro |
| [sistema-de-cores.md](sistema-de-cores.md) | ⚪ Opcional | Decisões de cor/paleta |
| [sistema-de-tipografia.md](sistema-de-tipografia.md) | ⚪ Opcional | Seleção/combinação de fontes |
| [efeitos-visuais.md](efeitos-visuais.md) | ⚪ Opcional | Glassmorphism, sombras, gradientes |
| [guia-de-animação.md](guia-de-animação.md) | ⚪ Opcional | Quando animação for necessária |
| [motion-graphics.md](motion-graphics.md) | ⚪ Opcional | Lottie, GSAP, 3D |
| [árvores-de-decisão.md](árvores-de-decisão.md) | ⚪ Opcional | Templates de contexto |

> 🔴 **psicologia-de-ux.md = SEMPRE LER. Os demais = apenas se forem relevantes.**

---

## 🔧 Scripts de Execução

**Execute para auditorias (não leia, apenas rode):**

| Script | Finalidade | Uso |
|------|-----------|-----|
| `scripts/auditoria-de-ux.py` | Auditoria de Psicologia UX e Acessibilidade | `python scripts/auditoria-de-ux.py <project_path>` |

---

## ⚠️ CRÍTICO: PERGUNTE ANTES DE PRESUMIR (OBRIGATÓRIO)

> **PARE! Se o pedido do usuário for aberto, NÃO use seus padrões favoritos por padrão.**

### Quando o pedido for vago, PERGUNTE:

**Cor não especificada?**  
> "Qual paleta de cores você prefere? (azul/verde/laranja/neutra/outra?)"

**Estilo não especificado?**  
> "Qual estilo você busca? (minimalista/ousado/retrô/futurista/orgânico?)"

**Layout não especificado?**  
> "Você tem preferência de layout? (coluna única/grid/assimétrico/full-width?)"

### ⛔ Tendências padrão da IA a EVITAR (ANTI SAFE HARBOR):

| Tendência da IA | Por que é ruim | Pense em vez disso |
|-----------------|---------------|-------------------|
| **Bento Grids (clichê moderno)** | Usado em todo design de IA | Esse conteúdo PRECISA mesmo de grid? |
| **Hero dividido (esq/dir)** | Previsível e sem graça | E se usar tipografia massiva ou narrativa vertical? |
| **Gradientes mesh/aurora** | Fundo preguiçoso “moderno” | Que combinação radical de cores faz sentido aqui? |
| **Glassmorphism** | Ideia genérica de “premium” | E um flat sólido de alto contraste? |
| **Azul fintech/ciano profundo** | Zona de conforto | Por que não vermelho, preto ou verde neon? |
| **“Orquestrar / Empoderar”** | Copy gerado por IA | Como um humano falaria isso? |
| Fundo escuro + glow neon | Visual “cara de IA” | O que a MARCA realmente precisa? |
| **Tudo arredondado** | Genérico e seguro | Onde usar bordas duras/brutalistas? |

> 🔴 **“Cada estrutura ‘segura’ escolhida aproxima você de um template genérico. ARRISQUE.”**

---

## 1. Análise de Restrições (SEMPRE PRIMEIRO)

Antes de qualquer decisão de design, RESPONDA ou PERGUNTE:

| Restrição | Pergunta | Por que importa |
|---------|----------|----------------|
| **Prazo** | Quanto tempo temos? | Define complexidade |
| **Conteúdo** | Pronto ou placeholder? | Afeta flexibilidade |
| **Marca** | Existe guideline? | Pode limitar decisões |
| **Tecnologia** | Qual stack? | Define possibilidades |
| **Público** | Quem exatamente? | Direciona tudo |

### Público → Abordagem de Design

| Público | Considerações |
|------|--------------|
| **Gen Z** | Ousado, rápido, mobile-first |
| **Millennials** | Limpo, minimalista |
| **Gen X** | Familiar, confiável |
| **Boomers** | Legível, alto contraste |
| **B2B** | Profissional, dados |
| **Luxo** | Elegância, espaço |

---

## 2. Princípios de Psicologia UX

### Leis Fundamentais

| Lei | Princípio | Aplicação |
|---|----------|----------|
| **Lei de Hick** | Mais escolhas = decisões mais lentas | Limite opções |
| **Lei de Fitts** | Maior + mais perto = mais fácil | Dimensione CTAs |
| **Lei de Miller** | ~7 itens na memória | Agrupe conteúdo |
| **Von Restorff** | Diferente = memorável | Destaque CTAs |
| **Posição Serial** | Início/fim lembrados | Info-chave nesses pontos |

### Níveis Emocionais do Design

```

VISCERAL → Primeira impressão
COMPORTAMENTAL → Uso
REFLEXIVO → Memória e significado

```

### Construção de Confiança

- Indicadores de segurança
- Prova social
- Contato claro
- Consistência visual
- Transparência

---

## 3. Princípios de Layout

### Proporção Áurea (φ = 1.618)

```

Conteúdo : Sidebar ≈ 62% : 38%
Escala de títulos × 1.618
Espaçamentos progressivos

```

### Grid de 8 Pontos

```

4px, 8px, 16px, 24px, 32px, 48px...

```

### Dimensionamento

| Elemento | Observação |
|-------|------------|
| Alvos de toque | Conforto mínimo |
| Botões | Hierarquia visual |
| Inputs | Alinhar com botões |
| Cards | Padding consistente |
| Leitura | 45–75 caracteres |

---

## 4. Princípios de Cor

### Regra 60–30–10

```

60% Base
30% Suporte
10% Destaque

```

### Psicologia das Cores

| Objetivo | Cores | Evite |
|-------|-------|------|
| Confiança | Azul | Vermelho agressivo |
| Crescimento | Verde | Cinza industrial |
| Urgência | Laranja/vermelho | Azul passivo |
| Luxo | Teal escuro, dourado | Tons baratos |
| Minimalismo | Neutros | Excesso |

---

## 5. Tipografia

### Escalas

| Contexto | Razão |
|--------|-------|
| UI densa | 1.125–1.2 |
| Web geral | 1.25 |
| Editorial | 1.333 |
| Hero | 1.5–1.618 |

### Legibilidade

- 16px+ corpo
- Altura de linha 1.4–1.6
- Contraste WCAG

---

## 6. Efeitos Visuais

### Glassmorphism (com cuidado)

- Transparência
- Blur
- Borda sutil
- ⚠️ Evite o clichê azul/branco

### Sombras

- Elevação coerente
- Offset vertical maior
- Glow no dark mode

---

## 7. Animação

### Duração baseada em

- Distância
- Tamanho
- Importância
- Contexto

### Performance

- Apenas transform/opacity
- Respeitar prefers-reduced-motion

---

## 8. Checklist de “Uau”

### Indicadores Premium

- [ ] Espaço em branco
- [ ] Profundidade sutil
- [ ] Animações suaves
- [ ] Detalhes refinados

### Confiança

- [ ] Prova social
- [ ] Valor claro
- [ ] Imagens profissionais

---

## 9. Anti-Padrões

### ❌ Design Preguiçoso

- Fontes padrão sem critério
- Imagens genéricas
- Espaçamento inconsistente
- Baixo contraste

### ❌ Tendências de IA

- Roxo em tudo (BANIMENTO DO ROXO ✅)
- Grid bento sem motivo
- Clone Vercel
- Não perguntar preferências

---

## 10. Processo de Decisão

```

1. Restrições
2. Conteúdo
3. Direção visual
4. Execução
5. Revisão

```

---

## Skills Relacionadas

| Skill | Quando Usar |
|-----|-----------|
| **design_de_frontend** | Antes de codar |
| **diretrizes_de_design_web** | Depois de codar |

---

> **Lembrete Final:** Design é raciocínio, não cópia. Cada projeto exige decisões novas baseadas em contexto real. **Evite o “Safe Harbor SaaS Moderno”.**
```
