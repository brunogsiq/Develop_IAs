# 04. Testando MCP

> O que é o MCP, os papéis (Host, Client, Server), as primitivas e os transportes estão em [06 - MCP Conceitos](<../../01 - Trilha IA Geral/01 - Estudo/06 - MCP Conceitos.md>), na Trilha IA Geral. Leia antes. Aqui está o que muda para o QA: o servidor MCP é uma **API**, e o seu conhecimento de teste de API se aplica diretamente.

## O MCP no projeto de referência

| Papel | No projeto |
|-------|------------|
| **Host** | O chat dos gerentes |
| **Client** | Parte do backend |
| **Server** | O "MCP bancário", que expõe consultar câmbio, consultar crédito etc. |

No projeto, o mais provável é que o foco seja em **Tools**. Pergunte ao time se o servidor também usa resources, prompts, **sampling** ou **elicitation**: cada um abre novos cenários de teste.

**Autorização:** num servidor remoto, a chamada carrega um token (OAuth 2.1). A pergunta de segurança mais importante é: **a chamada ao MCP carrega a identidade do gerente logado ou de um usuário de serviço?** (ver [06 - Segurança OWASP LLM.md](<06 - Segurança OWASP LLM.md>), seção 6).

## Anatomia de uma Tool

Cada tool tem **nome**, **descrição** e **schema de entrada** (JSON Schema):

```json
{
  "name": "consultar_cambio",
  "description": "Retorna a cotação atual de compra e venda de uma moeda estrangeira em relação ao Real (BRL). Use quando o usuário perguntar sobre dólar, euro ou outra moeda.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "moeda": {
        "type": "string",
        "description": "Código ISO da moeda, ex: USD, EUR",
        "enum": ["USD", "EUR", "GBP"]
      },
      "tipo": {
        "type": "string",
        "enum": ["comercial", "turismo"]
      }
    },
    "required": ["moeda"]
  }
}
```

**Atenção:** a `description` é o que o LLM lê para decidir **quando** usar a ferramenta. Uma descrição vaga causa escolhas erradas. **A descrição também é testável e revisável pelo QA.**

## Como a comunicação funciona por baixo

O MCP usa **JSON-RPC 2.0**, ou seja, requisições e respostas em JSON. **Seu conhecimento de teste de API se aplica diretamente.**

Principais mensagens:

| Método | O que faz |
|--------|-----------|
| `initialize` | Cliente e servidor se apresentam e negociam capacidades |
| `tools/list` | Lista as ferramentas disponíveis |
| `tools/call` | Executa uma ferramenta com parâmetros |
| `resources/list` / `resources/read` | Lista e lê recursos |

Exemplo de chamada:

```json
// Requisição
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "consultar_cambio",
    "arguments": { "moeda": "USD", "tipo": "comercial" }
  }
}

// Resposta
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      { "type": "text", "text": "{\"compra\": 5.42, \"venda\": 5.43, \"atualizado_em\": \"2026-10-29T14:32:00-03:00\"}" }
    ],
    "isError": false
  }
}
```

## Como testar o servidor MCP (camada determinística)

Aqui não há IA envolvida, então é **teste de API clássico**:

- [ ] `tools/list` retorna todas as ferramentas esperadas, com descrições claras
- [ ] Schemas validam parâmetros: obrigatórios, tipos, enums, formatos
- [ ] Parâmetro inválido retorna erro claro (não stack trace, não erro 500 genérico)
- [ ] Dados retornados batem com a API de origem
- [ ] Cliente inexistente → resposta clara de "não encontrado"
- [ ] API de origem fora do ar / timeout → erro tratado (`isError: true` com mensagem útil)
- [ ] **Autorização:** um gerente sem permissão consegue consultar cliente de outra carteira?
- [ ] Dados sensíveis desnecessários não são retornados (minimização de dados, LGPD)
- [ ] Performance: tempo de resposta de cada tool
- [ ] Logs de auditoria registram quem consultou o quê

## Ferramenta prática: MCP Inspector

O "Postman do MCP", ferramenta oficial para conectar num servidor MCP e chamar tools manualmente.

```bash
npx @modelcontextprotocol/inspector
```

Peça ao time para usá-lo no servidor de vocês em ambiente de teste.

## Checklist de aprendizado

- [ ] Concluí o módulo [06 - MCP Conceitos](<../../01 - Trilha IA Geral/01 - Estudo/06 - MCP Conceitos.md>) da Trilha Geral
- [ ] Entendo que é JSON-RPC e que posso testar como API
- [ ] Rodei o MCP Inspector e chamei pelo menos uma tool
- [ ] Vi a lista real de tools do projeto
