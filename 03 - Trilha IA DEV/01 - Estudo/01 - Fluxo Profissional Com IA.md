# 01. Fluxo profissional com IA

> Em uma empresa, o código não nasce no editor: nasce de uma história de usuário, passa por um quadro de tarefas, um branch, um pull request, uma revisão e um pipeline. Este módulo cobre Git, GitHub, Jira e Trello, e onde a IA entra em cada etapa.

> **Por que este é o primeiro módulo:** os agentes dos módulos 02 e 03 editam arquivos e fazem commits. Com Git e branches, toda mudança da IA pode ser revisada no diff e desfeita. Sem eles, um erro do agente vira trabalho perdido.

## Objetivos

- Dominar o Git além do básico.
- Usar o GitHub para colaboração: issues, PRs, revisão e Actions.
- Organizar o trabalho no Jira e no Trello.
- Reproduzir um fluxo profissional de ponta a ponta usando IA.

## O fluxo

```text
Receber User Story → Analisar → Documentar → Criar BDD → Criar tarefas (Jira)
   → Branch (Git) → Desenvolver (Cursor / Copilot / Claude Code) → Pull Request
   → Code Review (humano + IA) → QA → Automação → CI/CD → Deploy → Documentação
```

| Etapa | Onde a IA ajuda |
|-------|-----------------|
| Analisar a história | Encontrar ambiguidades e gerar perguntas ([Assistentes de IA no dia a dia, Trilha Geral](<../../01 - Trilha IA Geral/01 - Estudo/04 - Assistentes De IA No Dia A Dia.md>)) |
| Criar tarefas | Quebrar a história em tarefas técnicas |
| Desenvolver | Implementar com o agente ([02](<02 - IDEs Com IA Cursor E Copilot.md>), [03](<03 - Claude Code.md>)) |
| Commit | Sugerir mensagens no padrão Conventional Commits |
| Pull Request | Escrever a descrição e o resumo das mudanças |
| Code Review | Revisão automática no PR (Copilot, Claude Code em GitHub Actions); a aprovação final é humana |
| QA | Gerar cenários e automação ([Trilha IA QA](<../../02 - Trilha IA QA/README.md>)) |
| CI/CD | Escrever e depurar workflows |

## Git

| Grupo | Comandos e conceitos |
|-------|----------------------|
| Básico | `init`, `clone`, `add`, `commit`, `status`, `log`, `diff` |
| Branches | `branch`, `switch` (ou `checkout`), `merge`, resolução de conflitos |
| Histórico | `rebase`, `squash`, `cherry-pick`, `tag` |
| Desfazer | `restore`, `reset`, `revert`, `stash` |
| Investigação | `bisect`, `blame` |
| Produtividade | hooks, aliases |
| Padrões | Conventional Commits (`feat:`, `fix:`, `docs:`), Git Flow, trunk-based |

Práticas: criar repositório, trabalhar em branches, provocar e resolver conflito, fazer rebase, cherry-pick, tag, stash, revert, achar um bug com `bisect` e aplicar Git Flow.

## GitHub

| Recurso | Para que serve |
|---------|----------------|
| Repository e README | Apresentar o projeto |
| Issues e templates | Registrar tarefas e bugs com padrão |
| Pull Requests e Code Review | Propor e revisar mudanças |
| Projects | Quadro de tarefas integrado às issues |
| Discussions e Wiki | Conversa e documentação |
| Releases e Packages | Publicar versões |
| Actions | CI/CD |
| Secrets e Variables | Configuração segura para pipelines |
| Dependabot | Atualizar dependências e alertar vulnerabilidades |

Práticas: publicar o projeto, escrever um README profissional, criar issue e PR, revisar um PR, montar um Project, criar Wiki e Release, configurar Secrets e criar uma Action.

## Jira

Conteúdo: Scrum, Kanban, backlog, sprint, épico, história, tarefa, bug, workflow, filtros (JQL), dashboard e relatórios.

Práticas: criar projeto Scrum e Kanban, criar épico, história, tarefa e bug, planejar uma sprint, configurar o backlog, criar filtro e dashboard e gerar relatórios.

## Trello

Conteúdo: quadros, listas, cartões, etiquetas, checklists, automações (Butler) e Power-Ups.

Práticas: organizar o plano de estudos e o projeto em Kanban, com checklists e etiquetas, e acompanhar as entregas.

> Jira e Trello têm plano gratuito. Confira os limites atuais em [atlassian.com](https://www.atlassian.com/software/jira/pricing) e [trello.com](https://trello.com/pricing).

## Práticas do módulo

1. Executar o fluxo completo com uma história pequena: Jira → branch → implementação com IA → PR → revisão → merge.
2. Usar IA para escrever a descrição do PR e comparar com a sua.
3. Pedir uma revisão de código à IA e classificar cada comentário: útil, irrelevante ou errado.

## Checklist de aprendizado

- [ ] Uso rebase, stash, cherry-pick e revert com segurança
- [ ] Sigo Conventional Commits
- [ ] Abri e revisei um PR completo no GitHub
- [ ] Organizei uma sprint no Jira
- [ ] Executei o fluxo profissional de ponta a ponta com IA
