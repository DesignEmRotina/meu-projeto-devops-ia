# Princípios de Design de Schema

> Normalização, chaves primárias, timestamps e relacionamentos.

## Decisão de Normalização

```

Quando normalizar (separar tabelas):
├── Dados se repetem entre linhas
├── Atualizações exigiriam múltiplas alterações
├── Relacionamentos são claros
└── Padrões de consulta se beneficiam disso

Quando desnormalizar (embutir/duplicar):
├── Performance de leitura é crítica
├── Dados raramente mudam
├── Sempre são buscados juntos
└── Consultas mais simples são necessárias

```

## Seleção de Chave Primária

| Tipo | Usar Quando |
|------|-------------|
| **UUID** | Sistemas distribuídos, maior segurança |
| **ULID** | UUID + ordenável por tempo |
| **Auto-incremento** | Apps simples, banco único |
| **Chave natural** | Raramente (quando há significado de negócio) |

## Estratégia de Timestamps

```

Para toda tabela:
├── created_at → Quando foi criada
├── updated_at → Última modificação
└── deleted_at → Soft delete (se necessário)

Use TIMESTAMPTZ (com timezone) e não TIMESTAMP

```

## Tipos de Relacionamento

| Tipo | Quando | Implementação |
|------|--------|---------------|
| **Um-para-Um** | Dados de extensão | Tabela separada com FK |
| **Um-para-Muitos** | Pai-filhos | FK na tabela filha |
| **Muitos-para-Muitos** | Ambos os lados têm muitos | Tabela de junção |

## ON DELETE em Chaves Estrangeiras

```

├── CASCADE → Remove filhos junto com o pai
├── SET NULL → Filhos ficam órfãos
├── RESTRICT → Impede exclusão se houver filhos
└── SET DEFAULT → Filhos recebem valor padrão
