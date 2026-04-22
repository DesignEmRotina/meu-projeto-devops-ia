descrição: Iniciar, parar e verificar o status do servidor de preview. Gerenciamento do servidor local de desenvolvimento.
---

# /pre-visualizar - Gerenciamento de Preview

$ARGUMENTS

---

## Tarefa

Gerenciar o servidor de preview: iniciar, parar e verificar status.

### Comandos

```

/pre-visualizar            - Mostrar status atual
/pre-visualizar começar    - Iniciar servidor
/pre-visualizar parar      - Parar servidor
/pre-visualizar recomeçar  - Reiniciar
/pre-visualizar checar     - Verificação de saúde

```

---

## Exemplos de Uso

### Iniciar Servidor
```

/pre-visualizar começar

Resposta:
🚀 Iniciando preview...
Porta: 3000
Tipo: Next.js

✅ Preview pronto!
URL: [http://localhost:3000](http://localhost:3000)

```

### Verificação de Status
```

/pre-visualizar

Resposta:
=== Status do Preview ===

🌐 URL: [http://localhost:3000](http://localhost:3000)
📁 Projeto: C:/projects/my-app
🏷️ Tipo: nextjs
💚 Saúde: OK

```

### Conflito de Porta
```

/pre-visualizar começar

Resposta:
⚠️ A porta 3000 está em uso.

Opções:

1. Iniciar na porta 3001
2. Fechar a aplicação na porta 3000
3. Especificar outra porta

Qual opção? (padrão: 1)

````

---

## Técnico

O preview automático utiliza o script `visualização_automática.py`:

```bash
python .agent/scripts/visualização_automática.py start [porta]
python .agent/scripts/visualização_automática.py stop
python .agent/scripts/visualização_automática.py status
````


