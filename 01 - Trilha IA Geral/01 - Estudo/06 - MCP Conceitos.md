# 06. MCP: conceitos

> O **Model Context Protocol** é o padrão que conecta aplicações de IA a ferramentas e dados. Este módulo traz o que qualquer profissional precisa saber. Testar um servidor MCP fica na [Trilha IA QA](<../../02 - Trilha IA QA/01 - Estudo/04 - Testando MCP.md>); construir um, na [Trilha IA DEV](<../../03 - Trilha IA DEV/01 - Estudo/06 - MCP Para Desenvolvedores.md>).

## O que é

Um **protocolo aberto** que padroniza como aplicações de IA se conectam a ferramentas e fontes de dados externas. Foi lançado pela Anthropic em novembro de 2024 e hoje é adotado por OpenAI, Google, Microsoft e outros.

A analogia oficial: **o MCP é a "porta USB-C" da IA.** Um padrão único de conexão no lugar de um cabo diferente para cada aparelho.

## Por que existe

**Sem MCP:** cada aplicação de IA precisa de uma integração própria com cada sistema.

```
3 IAs × 4 sistemas = 12 integrações diferentes para criar e manter
```

**Com MCP:** cada sistema expõe um servidor MCP uma única vez, e qualquer IA compatível consegue usá-lo.

```
3 IAs + 4 servidores MCP = 7 peças, todas no mesmo padrão
```

Se amanhã a empresa trocar o modelo de IA, os servidores MCP continuam os mesmos.

## Os três papéis

| Papel | O que é | Exemplo |
|-------|---------|---------|
| **Host** | A aplicação que o usuário usa | VS Code com Copilot, Claude Desktop, um chat corporativo |
| **Client** | Componente dentro do host que conversa com um servidor MCP | Criado pelo host, um por servidor |
| **Server** | Expõe ferramentas e dados num formato padronizado | Servidor de arquivos, de GitHub, de banco de dados, de uma API interna |

```
┌──────────────── Host ────────────────┐
│   LLM  ◄──►  MCP Client  ◄── JSON-RPC ──►  MCP Server ──► sistemas e dados
└───────────────────────────────────────┘
```

## As primitivas

| Primitiva | O que é | Exemplo |
|-----------|---------|---------|
| **Tools** | Ações ou consultas que o LLM pode decidir chamar | `consultar_cambio`, `criar_issue` |
| **Resources** | Dados de leitura que a aplicação pode anexar ao contexto | Um manual, um esquema de banco |
| **Prompts** | Modelos de interação prontos | "Resumir o pull request" |

Também há recursos no sentido inverso, do servidor pedindo algo ao cliente: **sampling** (o servidor pede ao LLM do host para gerar um texto) e **elicitation** (o servidor pede ao usuário uma informação ou confirmação).

Cada tool tem **nome**, **descrição** e **schema de entrada** (JSON Schema). A descrição é o que o LLM lê para decidir **quando** usar a ferramenta: uma descrição vaga causa escolhas erradas.

## Como a comunicação funciona

- **Formato:** JSON-RPC 2.0, requisições e respostas em JSON (`initialize`, `tools/list`, `tools/call`, `resources/read`).
- **Transportes:**

| Transporte | Uso |
|------------|-----|
| `stdio` | Servidor roda na sua máquina, como processo local |
| `Streamable HTTP` | Servidor remoto via HTTP, o mais comum em ambiente corporativo |

- **Autorização:** para servidores remotos, a especificação define autorização baseada em **OAuth 2.1**: o cliente obtém um token e o envia em cada requisição.

## O que cada papel precisa perguntar

| Papel | Pergunta |
|-------|----------|
| Todos | Quais servidores MCP estão instalados na minha ferramenta e o que eles podem acessar? |
| Dev | As descrições e schemas das tools estão claros? Os erros são tratados? |
| Arquiteto | O servidor usa a identidade do usuário ou um usuário de serviço? Ele só lê ou também altera? |
| QA | Como testo o servidor como API e como meço se a IA escolhe a tool certa? |
| DevOps / SRE | Onde o servidor roda, como é versionado, monitorado e onde ficam os segredos? |
| Segurança | O servidor é de terceiros? Quem aprovou e em qual versão? |

> Um servidor MCP de terceiros tem o mesmo nível de confiança de qualquer dependência que executa código na sua máquina. Instale só de fontes confiáveis.

## Prática

1. Leia "Introduction" e "Core architecture" em [modelcontextprotocol.io](https://modelcontextprotocol.io).
2. Veja quais servidores MCP estão configurados no seu VS Code, Claude Desktop ou outra ferramenta, e o que cada um acessa.
3. Rode o MCP Inspector e liste as tools de um servidor de exemplo:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

## Checklist de aprendizado

- [ ] Sei explicar o MCP com a analogia do USB-C
- [ ] Sei explicar Host, Client e Server
- [ ] Sei a diferença entre Tools, Resources e Prompts
- [ ] Sei por que a descrição de uma tool importa
- [ ] Sei as perguntas de segurança da minha função sobre um servidor MCP
- [ ] Fiz o curso "Introduction to Model Context Protocol" (Claude Academy)
