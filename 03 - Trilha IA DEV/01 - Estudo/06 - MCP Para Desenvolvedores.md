# 06. MCP para desenvolvedores

> O MCP (Model Context Protocol) padroniza como aplicações de IA se conectam a ferramentas e dados. Na trilha de QA você aprendeu o que é e como testar; aqui o foco é **usar e construir** servidores MCP.

**Pré-requisito:** leia [06 - MCP Conceitos](<../../01 - Trilha IA Geral/01 - Estudo/06 - MCP Conceitos.md>) da Trilha IA Geral (o que é, por que existe, Host/Client/Server, Tools/Resources/Prompts e JSON-RPC). Este módulo não repete esse conteúdo.

> Documentação oficial: [modelcontextprotocol.io](https://modelcontextprotocol.io).

## Objetivos

- Conectar servidores MCP prontos ao Claude, ao Claude Code, ao Cursor e ao VS Code.
- Construir um servidor MCP próprio.
- Entender permissões, autenticação e riscos.

## Conceitos adicionais

| Conceito | O que é |
|----------|---------|
| **Tools / Resources / Prompts** | As três primitivas que o **servidor** oferece (ver Trilha IA Geral, módulo 06) |
| **Roots** | O cliente informa ao servidor quais pastas ou URIs ele pode acessar |
| **Sampling** | O servidor pede ao cliente que faça uma chamada ao modelo |
| **Elicitation** | O servidor pede uma informação adicional ao usuário durante a execução |
| **Transportes** | `stdio` (processo local) e **Streamable HTTP** (remoto). O antigo transporte HTTP+SSE foi substituído pelo Streamable HTTP |
| **Autenticação** | Servidores remotos usam OAuth; servidores locais herdam as permissões do seu usuário |

## Onde configurar

| Cliente | Como |
|---------|------|
| Claude (app / claude.ai) | Conectores nas configurações |
| Claude Code | `claude mcp add ...` ou arquivo `.mcp.json` no projeto |
| VS Code (Copilot) | `.vscode/mcp.json` |
| Cursor | `.cursor/mcp.json` |

## Construindo um servidor

O jeito mais rápido é com os SDKs oficiais (Python, TypeScript e outros). O laboratório da Trilha IA QA já tem um servidor completo em Python, que consulta a PTAX do dólar no Banco Central: [02 - Laboratório](<../../02 - Trilha IA QA/02 - Laboratório/README.md>). Use-o como ponto de partida.

O esqueleto, com o SDK Python:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("meu-servidor")

@mcp.tool()
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b

if __name__ == "__main__":
    mcp.run()  # stdio por padrão
```

- A docstring vira a **descrição** da tool e os tipos dos parâmetros viram o **schema**.
- Teste o servidor sem IA com o MCP Inspector: `npx @modelcontextprotocol/inspector python servidor.py`.

## Segurança

- **Menor privilégio:** exponha só o necessário e prefira ferramentas de leitura.
- **Ferramentas que escrevem** (apagar, enviar, pagar) precisam de confirmação explícita.
- **Dados compartilhados:** tudo o que a tool retorna vai para o contexto do modelo e, portanto, para o provedor do modelo.
- **Prompt injection indireto:** conteúdo vindo de fora (e-mail, issue, página) pode conter instruções maliciosas.
- **Servidores de terceiros:** instale só de fontes confiáveis; um servidor MCP roda com as suas permissões.

## Práticas

1. Configurar um servidor pronto (filesystem ou GitHub) no Claude Code e no VS Code.
2. Listar as tools expostas e ler as descrições.
3. Rodar o servidor do laboratório da Trilha IA QA e chamá-lo pelo Inspector.
4. Criar um servidor próprio com 2 tools (ex.: consultar um CSV de produtos e calcular um desconto).
5. Adicionar um Resource (ex.: o arquivo de regras de negócio).
6. Conectar o servidor ao Cursor ou ao Copilot e usá-lo no modo agente.
7. Documentar os riscos: que dados saem, quem pode chamar, o que pode ser alterado.

## Checklist de aprendizado

- [ ] Configurei servidores MCP em pelo menos dois clientes
- [ ] Construí um servidor com tools próprias
- [ ] Testei o servidor no MCP Inspector, sem IA
- [ ] Sei a diferença entre stdio e Streamable HTTP
- [ ] Documentei os riscos de um servidor
