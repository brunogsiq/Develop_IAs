# Projeto principal

> A trilha usa **um único projeto que evolui** do começo ao fim. Cada módulo estudado é aplicado nele. Assim você aprende por integração, não por exercícios soltos, e termina com um projeto de portfólio completo.

## O que será construído

Um sistema web completo, desenvolvido com IA como copiloto, contendo: front-end, back-end, banco de dados, API REST, autenticação, Docker, Git e GitHub, CI/CD, QA manual e automatizado, documentação técnica e deploy. Na fase final, o sistema ganha uma **funcionalidade com IA** (assistente, busca com RAG ou ferramenta via MCP).

Sugestão de tema: um sistema de cadastro e gestão (tarefas, produtos, biblioteca, agenda). Escolha algo simples de entender, para o foco ficar na engenharia.

## Etapas de evolução

| # | Etapa | Módulos relacionados |
|---|-------|----------------------|
| 1 | Repositório no GitHub, quadro no Jira e fluxo de branches: Git desde a primeira linha | [01](<../01 - Estudo/01 - Fluxo Profissional Com IA.md>) |
| 2 | Landing page | [04](<../01 - Estudo/04 - Engenharia De Software Com IA.md>) |
| 3 | Login e cadastro | 04 |
| 4 | Front-end com CRUD e dashboard | 04 |
| 5 | API REST | 04 |
| 6 | Banco de dados e migrations | 04 |
| 7 | Autenticação com JWT | 04 |
| 8 | Docker e Docker Compose | 04 |
| 9 | QA manual com BDD | 04 + [Trilha IA QA](<../../02 - Trilha IA QA/README.md>) |
| 10 | Automação de testes (Playwright) e testes de API | 04 |
| 11 | CI/CD com GitHub Actions | 04 |
| 12 | Deploy (Vercel / Render) | 04 |
| 13 | Monitoramento e logs | 04 |
| 14 | Funcionalidade com IA: API, MCP ou RAG | [05](<../01 - Estudo/05 - API E Tool Calling.md>), [06](<../01 - Estudo/06 - MCP Para Desenvolvedores.md>), [07](<../01 - Estudo/07 - RAG E Embeddings.md>) |
| 15 | Automação com agente ou n8n | [08](<../01 - Estudo/08 - Agentes E Automação.md>) |
| 16 | Documentação final e portfólio | [02 - Desafio Final E Portfólio](<02 - Desafio Final E Portfólio.md>) |

## Workflow completo de engenharia com IA

Cada funcionalidade do projeto deve passar por este fluxo:

```text
Requisito
  ↓
Jira (história e tarefas)
  ↓
Claude (análise de requisitos, pontos de atenção)
  ↓
BDD
  ↓
GitHub Issue → Branch
  ↓
Cursor / Copilot / Claude Code (front, back, banco)
  ↓
Pull Request → Code Review com IA + revisão humana
  ↓
QA manual → Playwright
  ↓
CI/CD → Deploy
  ↓
Documentação (README, Wiki, Obsidian)
```

## Regras do projeto

- Toda alteração entra por **pull request**, mesmo trabalhando sozinho.
- Todo código gerado por IA é **lido e entendido** antes do merge.
- Cada etapa termina com: código no GitHub, testes passando e documentação atualizada.
- Registre no README as decisões técnicas e onde a IA ajudou ou errou.

## Checklist do projeto

- [ ] Etapa 1: repositório, quadro no Jira e fluxo de branches em uso
- [ ] Etapas 2 a 7: aplicação funcionando localmente
- [ ] Etapa 8: aplicação sobe com `docker compose up`
- [ ] Etapas 9 e 10: plano de testes, BDD e automação
- [ ] Etapas 11 a 13: pipeline, deploy e monitoramento
- [ ] Etapas 14 e 15: funcionalidade com IA
- [ ] Etapa 16: portfólio publicado
