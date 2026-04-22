descrição: Adicionar ou atualizar funcionalidades em uma aplicação existente. Usado para desenvolvimento iterativo.

```

# /aprimoramento – Atualizar Aplicação

$ARGUMENTS

---

## Tarefa

Este comando adiciona novas funcionalidades ou realiza atualizações em uma aplicação já existente.

### Etapas:

1. **Entender o Estado Atual**

   * Carregar o estado do projeto com `python .agent/scripts/gerenciador_de_sessões.py info`
   * Compreender as funcionalidades existentes e a stack tecnológica

2. **Planejar as Mudanças**

   * Definir o que será adicionado ou alterado
   * Identificar os arquivos afetados
   * Verificar dependências envolvidas

3. **Apresentar o Plano ao Usuário** (para mudanças significativas)

   ```
   "Para adicionar um painel administrativo:
   - Vou criar 15 novos arquivos
   - Atualizar 8 arquivos
   - Leva aproximadamente 10 minutos

   Posso iniciar?"
   ```

4. **Aplicar**

   * Acionar os agentes relevantes
   * Realizar as alterações
   * Executar testes

5. **Atualizar o Preview**

   * Hot reload ou reinicialização do servidor

---

## Exemplos de Uso

```
/aprimoramento adicionar modo escuro
/aprimoramento criar painel de administração
/aprimoramento integrar sistema de pagamento
/aprimoramento adicionar recurso de busca
/aprimoramento editar página de perfil
/aprimoramento tornar responsivo
```

---

## Atenção

* Obter aprovação para mudanças grandes
* Alertar sobre solicitações conflitantes (ex.: “usar Firebase” quando o projeto utiliza PostgreSQL)
* Fazer commit de cada mudança usando Git
