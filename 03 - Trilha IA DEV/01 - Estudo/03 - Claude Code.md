# 03. Claude Code

> Claude Code é o agente de desenvolvimento da Anthropic. Ele lê o projeto, edita arquivos, executa comandos e trabalha com Git, no terminal, no VS Code, em IDEs JetBrains, no app desktop e na web.

> Documentação oficial: [docs.claude.com](https://docs.claude.com) (seção Claude Code). Confira lá a instalação atual e os planos que dão acesso.

## Objetivos

- Entender a diferença entre Claude (chat) e Claude Code (agente).
- Configurar o projeto para que o agente trabalhe bem.
- Controlar permissões e revisar o que o agente faz.
- Criar Skills reutilizáveis.

## Claude × Claude Code

| | Claude (claude.ai) | Claude Code |
|---|---|---|
| Onde roda | Navegador e app | Terminal, IDE, desktop e web |
| Acesso ao projeto | Só o que você anexa | Lê e navega pelo repositório |
| Ações | Responde e gera conteúdo | Edita arquivos, executa comandos, faz commits |
| Melhor para | Análise, escrita, pesquisa | Implementar, depurar, refatorar, testar |

## Conceitos principais

| Conceito | O que é |
|----------|---------|
| **CLAUDE.md** | Arquivo de memória do projeto: stack, comandos, padrões e regras. Gere a primeira versão com `/init` |
| **Permissões** | O agente pede autorização para editar arquivos e rodar comandos; dá para pré-aprovar comandos seguros nas configurações |
| **Modo de planejamento** | O agente investiga e propõe um plano antes de alterar qualquer coisa |
| **Comandos (`/`)** | Atalhos como `/init`, `/clear` e comandos personalizados do projeto |
| **Subagentes** | Agentes auxiliares com contexto próprio, para tarefas paralelas ou de busca |
| **Hooks** | Scripts executados automaticamente em eventos (ex.: rodar o lint depois de cada edição) |
| **MCP** | Conectar ferramentas externas (GitHub, Jira, banco de dados) |
| **Skills** | Pacotes de instruções especializadas que o agente carrega quando a tarefa pede |
| **Modo não interativo** | `claude -p "..."` para usar em scripts e pipelines de CI |
| **Integração com o GitHub** | Mencionar o agente em issues e pull requests e rodá-lo no GitHub Actions para revisar PRs e implementar tarefas (confira a configuração atual na documentação oficial) |

## Fluxo de trabalho recomendado

```text
Explorar (ler o código e entender)
   ↓
Planejar (pedir um plano e revisar)
   ↓
Implementar (em passos pequenos)
   ↓
Verificar (rodar testes, revisar o diff)
   ↓
Commitar / abrir PR
```

## Skills

Uma Skill é uma pasta com um arquivo `SKILL.md` (nome, descrição e instruções), e opcionalmente scripts e modelos. O agente lê a descrição e carrega a Skill quando a tarefa combina com ela.

Ideias de Skills para criar:
- QA Sênior (análise de requisitos e BDD)
- Code Review com critérios do time
- Front-end e Back-end com os padrões do projeto
- Documentação técnica
- Análise de requisitos

### Desafio: Skill de QA

Criar uma Skill que processe:

```text
User Story
   ↓
Análise
   ↓
Pontos de Atenção
   ↓
BDD
   ↓
Plano de Testes
   ↓
Sugestões de Automação
```

## Segurança

- Leia cada comando antes de aprovar, principalmente os que apagam arquivos, fazem push ou instalam pacotes.
- Não pré-aprove comandos destrutivos.
- Mantenha `.env` e segredos fora do alcance do agente.
- Trate conteúdo externo (páginas, issues, arquivos baixados) como dado, não como instrução: é por aí que entra o prompt injection.
- Revise o diff completo antes de commitar.

## Práticas

1. Instalar, autenticar e abrir um projeto.
2. Rodar `/init` e melhorar o `CLAUDE.md` gerado.
3. Pedir uma análise da arquitetura do projeto.
4. Localizar onde uma funcionalidade é implementada.
5. Corrigir um bug usando o modo de planejamento.
6. Refatorar um módulo e criar testes.
7. Gerar a documentação do projeto.
8. Configurar permissões para os comandos de teste.
9. Criar uma Skill e um comando personalizado.
10. Revisar todas as alterações antes de aceitar.
11. Comparar Claude Code e Cursor na mesma tarefa.

## Checklist de aprendizado

- [ ] Sei explicar a diferença entre Claude e Claude Code
- [ ] Tenho um `CLAUDE.md` útil no meu projeto
- [ ] Usei o modo de planejamento antes de uma mudança grande
- [ ] Configurei permissões sem liberar comandos perigosos
- [ ] Criei pelo menos uma Skill
- [ ] Conectei um servidor MCP
