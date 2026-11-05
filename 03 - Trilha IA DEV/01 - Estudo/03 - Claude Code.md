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

## Estrutura de um projeto

Cada arquivo e pasta ensina ao agente como trabalhar **naquele** projeto, para você não repetir as mesmas instruções toda vez. Os nomes das pastas são sempre em inglês: uma pasta chamada "ganchos" não é reconhecida.

```text
seu-projeto/
├── CLAUDE.md                  manual do projeto, lido no início de cada sessão
├── CLAUDE.local.md            suas preferências pessoais (não vai para o Git)
├── .mcp.json                  integrações externas (GitHub, Jira, Slack, bancos)
└── .claude/
    ├── settings.json          permissões, modelo, ferramentas e hooks do time
    ├── settings.local.json    seus ajustes pessoais (não vai para o Git)
    ├── rules/                 regras por assunto: code-style.md, testing.md, api-conventions.md
    ├── commands/              comandos com barra: review.md vira /review
    ├── skills/
    │   └── deploy/            uma pasta por skill, com SKILL.md e arquivos de apoio
    ├── agents/                subagentes: code-reviewer.md, security-auditor.md
    └── hooks/                 scripts automáticos: validate-bash.sh
```

| Item | Responde à pergunta | Compartilhado com o time? |
|------|---------------------|---------------------------|
| `CLAUDE.md` | O que é o projeto? | Sim |
| `CLAUDE.local.md` | Quais são minhas preferências? | Não |
| `.mcp.json` | Com quais ferramentas externas o agente conversa? | Sim |
| `settings.json` | O que o agente pode fazer e com qual configuração? | Sim |
| `settings.local.json` | Quais são meus ajustes de permissão? | Não |
| `rules/` | Como escrever o código? | Sim |
| `commands/` e `skills/` | Como fazer tarefas? | Sim |
| `agents/` | Quem faz o quê? | Sim |
| `hooks/` | O que checar automaticamente? | Sim |

**Regras práticas**

- Arquivos com `.local` no nome são pessoais: coloque-os no `.gitignore`.
- Mantenha o `CLAUDE.md` enxuto (referência comum: abaixo de ~500 linhas). Tudo que está nele é lido em toda sessão e ocupa contexto. Detalhes vão para `rules/` (que pode valer só para certas pastas) ou para `skills/`.
- **Skills** usam divulgação progressiva: o agente vê só nome e descrição e carrega o conteúdo completo quando a tarefa combina. Dá para ter dezenas sem pesar o contexto.
- **Subagentes** trabalham em janela de contexto isolada: uma auditoria pode ler centenas de arquivos e devolver só a conclusão.
- **Hooks** rodam antes ou depois de uma ação do agente: validar um comando e bloquear algo perigoso, formatar código, rodar o linter.
- Não precisa de tudo de cara. Comece com um `CLAUDE.md` enxuto; quando ele crescer, mova partes para `rules/`; quando repetir uma tarefa, transforme em comando ou skill.

> Esta estrutura muda com as versões. Confira os nomes e o formato atuais na documentação oficial.

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
- [ ] Sei o que vai em `rules/`, `commands/`, `skills/`, `agents/` e `hooks/`, e coloquei os arquivos `.local` no `.gitignore`
- [ ] Usei o modo de planejamento antes de uma mudança grande
- [ ] Configurei permissões sem liberar comandos perigosos
- [ ] Criei pelo menos uma Skill
- [ ] Conectei um servidor MCP
