# 02. IDEs com IA: Cursor e GitHub Copilot

> Desenvolvimento assistido por IA dentro do editor. Cursor e GitHub Copilot (no VS Code) seguem a mesma ideia: autocompletar, conversar sobre o código e delegar tarefas a um agente que lê, edita e executa comandos no projeto.

> Os nomes dos modos e menus mudam com frequência. Confira sempre a documentação: [docs.cursor.com](https://docs.cursor.com) e [docs.github.com/copilot](https://docs.github.com/copilot).

## Objetivos

- Usar os modos de interação certos para cada tarefa.
- Dar contexto ao assistente com regras e instruções do projeto.
- Revisar tudo o que a IA altera antes de aceitar.

## Modos de interação

| Modo | Cursor | Copilot (VS Code) | Quando usar |
|------|--------|-------------------|-------------|
| Autocompletar | Tab | Sugestões inline | Escrever código linha a linha |
| Edição inline | Inline Edit (`Ctrl+K`) | Inline chat (`Ctrl+I`) | Alterar um trecho selecionado |
| Chat / perguntas | Chat (Ask) | Chat (Ask) | Entender código, tirar dúvidas |
| Agente | Agent (antigo Composer) | Agent | Tarefas em vários arquivos, executar comandos e testes |
| Agente em segundo plano | Background/Cloud Agents | Copilot coding agent (a partir de uma issue) | Tarefas longas que viram um PR |

## Contexto e regras

O assistente só conhece o que está no contexto. Os dois produtos permitem instruções persistentes:

| Recurso | Cursor | Copilot |
|---------|--------|---------|
| Regras do projeto | `.cursor/rules/` (arquivos `.mdc`); o antigo `.cursorrules` ainda é aceito | `.github/copilot-instructions.md` |
| Regras do usuário | User Rules nas configurações (antigas "Global Rules") | Instruções pessoais nas configurações |
| Prompts reutilizáveis | Comandos e regras aplicadas sob demanda | Arquivos `.prompt.md` |
| Referenciar contexto | `@arquivo`, `@pasta`, `@docs`, `@web` | `#arquivo`, `#codebase`, ferramentas |
| Indexação | Indexa o projeto para busca semântica | Busca no workspace |
| MCP | Suportado (`.cursor/mcp.json`) | Suportado (`.vscode/mcp.json`) |

Boa prática: escreva nas regras o que um desenvolvedor novo precisaria saber, como stack, padrões de código, comandos de teste e o que não fazer.

## Outros recursos

- **Terminal integrado:** o agente executa comandos (instalar, testar, rodar). Leia o comando antes de aprovar.
- **Git:** mensagens de commit, revisão de diff e resolução de conflitos com IA.
- **Debug:** colar o erro ou o stack trace e pedir hipóteses de causa.
- **Modelos:** os dois permitem escolher o modelo (Claude, GPT, Gemini e outros). Compare o resultado na mesma tarefa.
- **Extensões:** o Cursor é baseado no VS Code e aceita a maioria das extensões.

## Alternativas

Windsurf, Claude Code ([03 - Claude Code](<03 - Claude Code.md>)), OpenAI Codex e geradores de aplicação como Lovable, Bolt.new, v0 e Replit. Veja o [catálogo de ferramentas](<../../01 - Trilha IA Geral/02 - Consulta/03 - Catálogo De Ferramentas De IA.md>).

## Cuidados

- **Revise cada diff.** A IA pode alterar arquivos que você não pediu.
- **Rode os testes** depois de cada mudança gerada.
- **Não aceite dependências desconhecidas** sem verificar se o pacote existe e é confiável (pacotes inventados são um vetor de ataque).
- **Segredos:** não deixe `.env` e chaves no contexto do agente.

## Práticas

1. Criar um projeto do zero com o agente.
2. Implementar um CRUD.
3. Corrigir um bug a partir do stack trace.
4. Refatorar um módulo e explicar as mudanças.
5. Criar regras do projeto e comparar o resultado antes e depois.
6. Gerar testes automatizados para uma função.
7. Gerar documentação do projeto.
8. Integrar um servidor MCP (veja [06 - MCP Para Desenvolvedores](<06 - MCP Para Desenvolvedores.md>)).
9. Comparar dois modelos na mesma tarefa dentro do editor.
10. Comparar Cursor, Copilot e Claude Code implementando a mesma funcionalidade: tempo, qualidade do código, uso de contexto e limitações.
11. Fazer uma sessão inteira de desenvolvimento usando só a IA, revisando tudo.

## Checklist de aprendizado

- [ ] Sei quando usar autocompletar, edição inline, chat e agente
- [ ] Criei regras de projeto e vi a diferença no resultado
- [ ] Usei referências de contexto (`@` / `#`) para guiar a IA
- [ ] Revisei e rejeitei pelo menos uma alteração ruim da IA
- [ ] Comparei duas ferramentas na mesma tarefa
