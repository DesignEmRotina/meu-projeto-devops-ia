nome: construtor_MCP
description: Princípios para construção de servidores MCP (Model Context Protocol). Design de ferramentas, padrões de recursos e boas práticas.
allowed-tools: Ler, Escrever, Editar, Glob, Grep
---

# MCP Builder

> Princípios para construção de servidores MCP.

---

## 1. Visão Geral do MCP

### O que é MCP?

**Model Context Protocol** — padrão para conectar sistemas de IA a ferramentas externas e fontes de dados.

### Conceitos Fundamentais

| Conceito                 | Finalidade                         |
| ------------------------ | ---------------------------------- |
| **Tools (Ferramentas)**  | Funções que a IA pode executar     |
| **Resources (Recursos)** | Dados que a IA pode ler            |
| **Prompts**              | Templates de prompts pré-definidos |

---

## 2. Arquitetura do Servidor

### Estrutura do Projeto

```
my-mcp-server/
├── src/
│   └── index.ts      # Entrada principal
├── package.json
└── tsconfig.json
```

### Tipos de Transporte

| Tipo          | Uso                           |
| ------------- | ----------------------------- |
| **Stdio**     | Local, baseado em CLI         |
| **SSE**       | Baseado na web, com streaming |
| **WebSocket** | Tempo real, bidirecional      |

---

## 3. Princípios de Design de Ferramentas

### Bom Design de Ferramentas

| Princípio         | Descrição                                   |
| ----------------- | ------------------------------------------- |
| Nome claro        | Orientado à ação (get_weather, create_user) |
| Propósito único   | Fazer uma única coisa bem                   |
| Entrada validada  | Schema com tipos e descrições               |
| Saída estruturada | Formato de resposta previsível              |

### Design do Schema de Entrada

| Campo       | Obrigatório?                   |
| ----------- | ------------------------------ |
| Type        | Sim — object                   |
| Properties  | Definir cada parâmetro         |
| Required    | Listar parâmetros obrigatórios |
| Description | Legível para humanos           |

---

## 4. Padrões de Recursos

### Tipos de Recursos

| Tipo     | Uso                        |
| -------- | -------------------------- |
| Estático | Dados fixos (config, docs) |
| Dinâmico | Gerado sob demanda         |
| Template | URI com parâmetros         |

### Padrões de URI

| Padrão        | Exemplo             |
| ------------- | ------------------- |
| Fixo          | `docs://readme`     |
| Parametrizado | `users://{userId}`  |
| Coleção       | `files://project/*` |

---

## 5. Tratamento de Erros

### Tipos de Erro

| Situação             | Resposta                              |
| -------------------- | ------------------------------------- |
| Parâmetros inválidos | Mensagem de erro de validação         |
| Não encontrado       | Mensagem clara de “não encontrado”    |
| Erro de servidor     | Erro genérico, detalhes apenas em log |

### Boas Práticas

* Retornar erros estruturados
* Não expor detalhes internos
* Registrar logs para debug
* Fornecer mensagens acionáveis

---

## 6. Manipulação Multimodal

### Tipos Suportados

| Tipo     | Codificação        |
| -------- | ------------------ |
| Texto    | Texto simples      |
| Imagens  | Base64 + tipo MIME |
| Arquivos | Base64 + tipo MIME |

---

## 7. Princípios de Segurança

### Validação de Entrada

* Validar todas as entradas das ferramentas
* Sanitizar dados fornecidos pelo usuário
* Limitar acesso a recursos

### Chaves de API

* Usar variáveis de ambiente
* Não registrar segredos em logs
* Validar permissões

---

## 8. Configuração

### Configuração do Claude Desktop

| Campo   | Finalidade              |
| ------- | ----------------------- |
| command | Executável a ser rodado |
| args    | Argumentos do comando   |
| env     | Variáveis de ambiente   |

---

## 9. Testes

### Categorias de Teste

| Tipo       | Foco                   |
| ---------- | ---------------------- |
| Unitário   | Lógica das ferramentas |
| Integração | Servidor completo      |
| Contrato   | Validação de schemas   |

---

## 10. Checklist de Boas Práticas

* [ ] Nomes de ferramentas claros e orientados à ação
* [ ] Schemas de entrada completos com descrições
* [ ] Saída JSON estruturada
* [ ] Tratamento de erros para todos os cenários
* [ ] Validação de entrada
* [ ] Configuração baseada em ambiente
* [ ] Logs para depuração

---

> **Lembre-se:** ferramentas MCP devem ser simples, focadas e bem documentadas. A IA depende das descrições para utilizá-las corretamente.

---
