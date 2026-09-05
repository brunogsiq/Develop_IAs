IA-Software-Engineer/
│
├── README.md
│
├── 00 - Como utilizar esta formação.md
├── 01 - Roadmap.md
├── 02 - Cronograma.md
│
├── Modulo 01 - Introdução à IA/
│   ├── teoria.md
│   ├── exemplos.md
│   ├── práticas.md
│   ├── desafios.md
│   ├── checklist.md
│   ├── projeto.md
│   └── referências.md
│
├── Modulo 02 - Engenharia de Prompt/
│
├── Modulo 03 - Claude/
│
├── Modulo 04 - Cursor/
│
├── Modulo 05 - MCP/
│
├── Modulo 06 - Agentes/
│
├── Modulo 07 - Git/
│
├── Modulo 08 - GitHub/
│
├── Modulo 09 - Jira/
│
├── Modulo 10 - Trello/
│
├── Modulo 11 - Front-end/
│
├── Modulo 12 - Back-end/
│
├── Modulo 13 - Banco de Dados/
│
├── Modulo 14 - Docker/
│
├── Modulo 15 - DevOps/
│
├── Modulo 16 - QA Manual/
│
├── Modulo 17 - Playwright/
│
├── Modulo 18 - Cypress/
│
├── Modulo 19 - Postman/
│
├── Modulo 20 - Projeto Final/
│
└── Portfólio/

> Esta formação foi projetada para capacitar um profissional a utilizar Inteligência Artificial como parte do fluxo de trabalho de Engenharia de Software, QA, Desenvolvimento Front-end, Desenvolvimento Back-end e DevOps.
>
> Ao final do treinamento, o aluno será capaz de desenvolver aplicações completas utilizando IA como copiloto, automatizar testes, estruturar documentação técnica, gerenciar projetos ágeis e construir um portfólio profissional.

---

# Metodologia da Formação

A formação é baseada em um único projeto que evolui durante todo o curso.

Diferente de cursos tradicionais, aqui não existem exercícios isolados.

Todo novo conhecimento será aplicado imediatamente em um projeto real.

Cada módulo possui:

- Objetivos
- Conteúdo Teórico
- Ferramentas
- Exemplos
- Exercícios Guiados
- Práticas
- Desafio
- Integração ao Projeto
- Checklist de Aprendizado
- Material Complementar
- Entregáveis

---

# Projeto Principal

Durante toda a formação será desenvolvido um sistema completo contendo:

- Front-end
- Back-end
- Banco de Dados
- API REST
- Docker
- Git
- GitHub
- CI/CD
- QA Manual
- QA Automação
- Documentação Técnica
- Deploy

Todo o projeto será desenvolvido utilizando IA.

---

# Ferramentas Utilizadas

## Inteligência Artificial

- ChatGPT
- Claude
- Cursor
- Gemini
- DeepSeek
- Perplexity
- Grok

## Desenvolvimento

- Visual Studio Code
- Git
- GitHub
- Docker
- Docker Compose

## Gestão

- Jira
- Trello
- GitHub Projects

## Front-end

- HTML5
- CSS3
- JavaScript
- TypeScript
- React
- Next.js

## Back-end

- Node.js
- Express
- NestJS

## Banco de Dados

- PostgreSQL
- Prisma ORM

## QA

- Playwright
- Cypress
- Postman
- Robot Framework

## DevOps

- GitHub Actions
- Vercel
- Render

---

# Módulo 01 — Introdução à Inteligência Artificial

## Objetivos

- Entender o funcionamento dos LLMs.
- Conhecer os principais modelos.
- Aprender conceitos fundamentais.

## Conteúdo

- História da IA
- IA Generativa
- Machine Learning
- Deep Learning
- LLM
- Tokens
- Context Window
- Embeddings
- Hallucinations
- Temperatura
- Fine Tuning
- RAG
- Agentes

## Comparação entre modelos

- ChatGPT
- Claude
- Gemini
- Grok
- DeepSeek
- Perplexity

## Práticas

- Comparar respostas entre todos os modelos.
- Identificar diferenças.
- Medir qualidade das respostas.

## Desafio

Resolver um mesmo problema utilizando cinco IAs diferentes.

---

# Módulo 02 — Engenharia de Prompt

## Objetivos

Aprender a conversar profissionalmente com IAs.

## Conteúdo

- O que é um Prompt
- Estrutura de um Prompt
- Persona
- Objetivo
- Contexto
- Restrições
- Formato da resposta
- Exemplos
- Engenharia de Contexto
- Cadeia de Refinamento
- Prompt Reutilizável

---

## Exemplo de Prompt Ruim

> Faça casos de teste para login.

### Problemas

- Não possui contexto.
- Não define objetivo.
- Não informa formato.
- Não define papel da IA.

---

## Exemplo de Prompt Bom

> Atue como QA Sênior.
>
> Crie casos de teste em BDD para uma tela de Login contendo Email e Senha.

### Melhorias

- Papel definido.
- Objetivo definido.
- Escopo conhecido.

---

## Exemplo de Prompt Excelente

> Atue como um QA Sênior especialista em Engenharia de Software.
>
> Analise exclusivamente a documentação fornecida.
>
> Não invente regras.
>
> Caso exista alguma lacuna registre como Ponto de Atenção.
>
> Elabore cenários em BDD contendo:
>
> - Cenários positivos
> - Cenários negativos
> - Validação de obrigatoriedade
> - Regras de negócio
> - Navegação
> - Limites
> - Critérios de aceitação
> - Rastreabilidade

### Resultado

Comparar os três resultados e analisar:

- Qualidade
- Clareza
- Precisão
- Reutilização

---

## Práticas

- Criar 20 prompts.
- Melhorar cada prompt até atingir nível excelente.
- Criar biblioteca pessoal de prompts.
- Comparar respostas entre Claude, ChatGPT e Gemini.

---

# Módulo 03 — Claude

## Conteúdo

- Interface
- Projects
- Artifacts
- Contexto
- Memória
- Organização
- Documentação
- Revisão de Código
- Análise de Requisitos
- Engenharia de Prompt aplicada ao Claude

## Práticas

- Criar um Project.
- Criar documentação técnica.
- Gerar BDD.
- Revisar código.
- Revisar User Stories.
- Criar Plano de Testes.

---

# Módulo 04 — Cursor

## Conteúdo

- Instalação
- Interface
- Chat
- Composer
- Agent
- Rules
- Contexto automático
- Refatoração
- Debug
- IA aplicada ao desenvolvimento

## Práticas

- Criar CRUD.
- Corrigir bugs.
- Refatorar projeto.
- Gerar testes.
- Criar documentação.
- Utilizar apenas IA durante uma sessão completa de desenvolvimento.

---

# Módulo 05 — MCP (Model Context Protocol)

## Conteúdo

- O que é MCP
- Servidores
- Ferramentas
- Agentes
- Memória
- Integrações

## Práticas

- Configurar um servidor MCP.
- Criar agente para documentação.
- Criar agente para revisão de código.
- Criar agente para QA.

---

# Módulo 06 — Git

## Conteúdo

- Commit
- Branch
- Merge
- Rebase
- Cherry Pick
- Tags

## Práticas

- Criar repositório.
- Trabalhar em Branches.
- Resolver conflitos.
- Organizar histórico.

---

# Módulo 07 — GitHub

## Conteúdo

- Repository
- README
- Wiki
- Issues
- Pull Requests
- Discussions
- GitHub Projects

## Práticas

- Publicar projeto.
- Abrir Pull Request.
- Fazer Code Review.
- Organizar backlog.

---

# Módulo 08 — Jira e Trello

## Jira

### Conteúdo

- Scrum
- Kanban
- Sprint
- Epic
- Story
- Bug
- Task

### Práticas

- Criar backlog.
- Criar Sprint.
- Criar Bugs.
- Acompanhar desenvolvimento.

---

## Trello

### Conteúdo

- Quadros
- Etiquetas
- Checklists
- Automações

### Práticas

- Organizar estudos.
- Organizar projeto.
- Criar fluxo Kanban.

---

# Módulo 09 — Desenvolvimento Front-end

## Tecnologias

- HTML
- CSS
- JavaScript
- TypeScript
- React
- Next.js

## Práticas

- Landing Page.
- Login.
- Dashboard.
- CRUD.
- Consumo de API.
- Componentização.
- Responsividade.

---

# Módulo 10 — Desenvolvimento Back-end

## Tecnologias

- Node.js
- Express
- NestJS

## Práticas

- API REST.
- CRUD.
- JWT.
- Upload.
- Middleware.
- Swagger.

---

# Módulo 11 — Banco de Dados

## Tecnologias

- PostgreSQL
- SQL
- Prisma

## Práticas

- Modelagem.
- Relacionamentos.
- Queries.
- Migrations.

---

# Módulo 12 — Docker

## Conteúdo

- Containers
- Dockerfile
- Compose
- Volumes
- Networks

## Práticas

- Containerizar Front-end.
- Containerizar Back-end.
- Containerizar Banco.

---

# Módulo 13 — QA

## Conteúdo

- Planejamento
- BDD
- Testes Manuais
- Testes Exploratórios
- Regressão
- Integração

## Práticas

- Plano de Testes.
- Casos BDD.
- Matriz de Rastreabilidade.
- Checklist.

---

# Módulo 14 — Automação

## Ferramentas

- Playwright
- Cypress
- Postman
- Robot Framework

## Práticas

- Login.
- CRUD.
- API.
- Relatórios.
- Pipeline.

---

# Módulo 15 — DevOps

## Conteúdo

- GitHub Actions
- CI/CD
- Deploy
- Build
- Pipeline

## Práticas

- Criar Pipeline.
- Executar testes automáticos.
- Publicar aplicação.

---

# Módulo 16 — Projeto Final

## Desenvolver

- Front-end
- Back-end
- Banco
- Docker
- GitHub
- CI/CD
- QA
- Automação
- Deploy

---

# Projeto Evolutivo

O sistema crescerá ao longo da formação:

1. Landing Page
2. Login
3. Cadastro
4. CRUD
5. API REST
6. Banco de Dados
7. Dashboard
8. Docker
9. GitHub
10. Jira
11. QA Manual
12. QA Automação
13. CI/CD
14. Deploy

---

# Checklist Final

Ao concluir a formação, o aluno deverá ser capaz de:

- Desenvolver aplicações Full Stack.
- Utilizar Claude profissionalmente.
- Utilizar Cursor profissionalmente.
- Criar prompts de alta qualidade.
- Desenvolver APIs REST.
- Trabalhar com React.
- Trabalhar com Node.js.
- Modelar bancos de dados.
- Utilizar Docker.
- Versionar projetos com Git.
- Trabalhar com GitHub.
- Gerenciar projetos com Jira.
- Organizar tarefas com Trello.
- Planejar testes.
- Criar cenários BDD.
- Automatizar testes.
- Configurar pipelines de CI/CD.
- Publicar aplicações.
- Construir um portfólio profissional.

---

# Resultado Esperado

Ao final desta formação, o aluno terá desenvolvido competências práticas em:

- Inteligência Artificial aplicada à Engenharia de Software.
- Engenharia de Prompt.
- Desenvolvimento Front-end.
- Desenvolvimento Back-end.
- Banco de Dados.
- QA Manual.
- QA Automação.
- DevOps.
- Documentação Técnica.
- Gestão Ágil.
- Versionamento.
- Desenvolvimento assistido por IA.

Revisei toda a evolução da conversa. A estrutura em Markdown ficou boa, mas **ela perdeu uma quantidade considerável de conteúdo importante**. Eu estimaria que ela preserva cerca de **75–80%** do que discutimos. Para transformar isso em uma formação realmente robusta (algo próximo de um curso profissional), eu faria as seguintes correções.

---

# 1. Engenharia de Prompt (Incompleta) ⭐⭐⭐⭐⭐

Você pediu muito mais do que "Prompt ruim, bom e excelente".

Faltou incluir:

## Estruturas de Prompt

* Zero-shot
* One-shot
* Few-shot
* Chain of Thought
* Tree of Thought
* Prompt Chaining
* Self Consistency
* Role Prompting
* Context Prompting
* XML Prompting
* Markdown Prompting
* JSON Prompting

---

## Como uma IA interpreta um Prompt

Explicar:

```
Sistema

↓

Persona

↓

Objetivo

↓

Contexto

↓

Restrições

↓

Exemplos

↓

Formato

↓

Resposta
```

Isso é extremamente importante.

---

## Exercício

Dar um prompt.

Melhorá-lo.

Melhorá-lo novamente.

Até chegar ao nível profissional.

---

# 2. Claude (Muito superficial)

Faltou estudar:

Projects

Artifacts

Styles

Memory

Knowledge

Long Context

Extended Thinking

API

SDK

CLI

Claude Code

GitHub Integration

MCP

Computer Use

Prompt Library

Templates

Comparação entre modelos Claude

Custos

Limitações

Tokens

Rate Limits

---

# 3. Cursor

Faltou metade do conteúdo.

Por exemplo:

Rules

Project Rules

Global Rules

Composer

Chat

Background Agent

Agent Mode

Inline Edit

Auto Complete

Indexação

Contexto

Terminal

Git Integration

Debug

MCP

Modelos suportados

Comparação GPT x Claude dentro do Cursor

Workspace

Extensions

---

# 4. MCP

Extremamente superficial.

Deveria conter:

O que é

Como funciona

Cliente

Servidor

Protocolos

Ferramentas

Resources

Prompts

Sampling

Roots

Transport

stdio

HTTP

SSE

Integrações

Claude

Cursor

VS Code

GitHub

Prática

Criar MCP

---

# 5. Agentes

Nem apareceu.

Hoje é obrigatório estudar.

Tipos

Single Agent

Multi Agent

Supervisor

Worker

Planner

Executor

Memory

Workflow

Crew

Ferramentas

---

# 6. Front-end

Está muito básico.

Faltou:

HTML Semântico

CSS Moderno

Flex

Grid

Animations

Responsividade

Tailwind

React

Hooks

Router

Context API

React Query

Redux

Next

SSR

CSR

SEO

Forms

Zod

React Hook Form

Axios

Fetch

---

# 7. Back-end

Muito básico.

Faltou:

Arquitetura

MVC

SOLID

Clean Code

DDD

Repository Pattern

JWT

Refresh Token

RBAC

Middlewares

Services

DTO

Validação

Swagger

Logs

Cache

Redis

Upload

---

# 8. Banco

Muito simples.

Faltou:

Normalização

Índices

Views

Procedures

Triggers

Backup

Restore

ORM

Relacionamentos

---

# 9. Docker

Faltou:

Volumes

Networks

Images

Registry

Docker Hub

Docker Desktop

Healthcheck

---

# 10. Git

Muito básico.

Faltou:

Stash

Cherry Pick

Reset

Revert

Bisect

Hooks

Aliases

Squash

Conventional Commits

Git Flow

---

# 11. GitHub

Faltou:

Actions

Secrets

Variables

Dependabot

Projects

Discussions

Releases

Packages

Wiki

Templates

---

# 12. DevOps

Muito pequeno.

Deveria conter:

CI

CD

Pipelines

Artifacts

Containers

Deploy

Cloud

Logs

Observabilidade

Rollback

Blue Green

Canary

---

# 13. QA

Aqui ficou muito abaixo do que normalmente conversamos.

Faltou:

Análise de requisitos

BDD

Casos de Teste

Plano de Testes

Matriz

Riscos

Smoke

Sanidade

Regressão

Integração

Usabilidade

Performance

Carga

Stress

API

Segurança

Exploratório

Massa de Testes

---

# 14. Automação

Faltou:

Playwright

Fixtures

POM

API

Intercept

Reports

CI

Docker

GitHub Actions

Postman

Collections

Environments

Robot Framework

---

# 15. Projeto

Aqui eu faria uma mudança enorme.

Você queria algo cronológico.

Então o projeto deveria crescer.

Exemplo:

Semana 1

Landing Page

↓

Semana 2

Login

↓

Semana 3

Cadastro

↓

Semana 4

Banco

↓

Semana 5

API

↓

Semana 6

CRUD

↓

Semana 7

Docker

↓

Semana 8

Testes

↓

Semana 9

Pipeline

↓

Semana 10

Deploy

---

# 16. Exercícios

Foi a maior perda.

Você pediu várias práticas.

Eu criaria para **todo módulo**.

Exemplo

```
Exercício 1

...

Exercício 2

...

Exercício 3

...

Desafio

...

Projeto

...
```

---

# 17. Sites Oficiais

Você pediu isto.

Só colocamos alguns.

Eu adicionaria documentação oficial para tudo.

---

# 18. Preços

Você perguntou:

Claude

Cursor

Jira

Trello

Planos

Gratuito

Pro

Business

Enterprise

Isso desapareceu.

---

# 19. Fluxo Profissional

Este foi outro ponto importante.

Você queria aprender um fluxo real.

Eu criaria um capítulo inteiro.

```
Receber User Story

↓

Analisar

↓

Documentar

↓

Criar BDD

↓

Criar Tasks

↓

Jira

↓

Git

↓

Cursor

↓

Claude

↓

Desenvolvimento

↓

QA

↓

Automação

↓

CI/CD

↓

Deploy
```

---

# 20. Portfólio

Também ficou pequeno.

Eu faria:

GitHub

LinkedIn

README

Documentação

Arquitetura

BDD

Swagger

Vídeo

Deploy

Artigo

---

Sim, mas eu faria uma mudança importante na estratégia.

**Eu não adicionaria exercícios aleatórios.**

Criaria uma metodologia única que será repetida em **todos os módulos**.

Isso faz com que você aprenda por repetição, aumentando muito a retenção.

---

# Estrutura Padrão de Exercícios (Aplicável a Todos os Módulos)

Cada módulo deverá possuir exatamente esta estrutura.

```text
1. Exercício Guiado

2. Exercício de Fixação

3. Exercício de Comparação

4. Exercício de Pesquisa

5. Exercício de Debug

6. Exercício de Refatoração

7. Exercício de Integração

8. Mini Projeto

9. Desafio

10. Desafio Avançado

11. Revisão

12. Autoavaliação
```

---

# Exercício 1 — Guiado

## Objetivo

Executar o conteúdo juntamente com o material didático.

## Exemplo

Você executará exatamente os mesmos passos apresentados durante o módulo.

Não existe liberdade para alterar.

Objetivo:

Aprender.

---

# Exercício 2 — Fixação

Agora você fará sozinho.

Sem consultar o material.

Exemplo:

Após aprender Git:

* criar branch
* merge
* commit
* push

---

# Exercício 3 — Comparação

Comparar ferramentas.

Exemplo:

Resolver o mesmo problema utilizando:

* ChatGPT
* Claude
* Cursor
* Gemini

Responder:

* Quem explicou melhor?
* Quem escreveu melhor?
* Quem programou melhor?
* Quem documentou melhor?

---

# Exercício 4 — Pesquisa

Pesquisar na documentação oficial.

Nunca utilizar apenas IA.

Responder:

* O que a documentação diz?
* O que mudou?
* Existe limitação?

---

# Exercício 5 — Debug

Receber um projeto com erro.

Descobrir:

* onde está
* por que aconteceu
* como resolver

---

# Exercício 6 — Refatoração

Receber código ruim.

Transformar em código profissional.

Explicar todas as mudanças.

---

# Exercício 7 — Integração

Integrar o conteúdo estudado ao projeto principal.

Exemplo:

Aprendeu React?

Adicionar React ao projeto.

Aprendeu Docker?

Dockerizar o projeto.

Aprendeu Playwright?

Automatizar login.

---

# Exercício 8 — Mini Projeto

Criar um projeto pequeno.

Exemplo:

HTML

↓

Landing Page

Git

↓

Repositório

Docker

↓

Container

Claude

↓

Documentação

---

# Exercício 9 — Desafio

Sem passo a passo.

Resolver sozinho.

Utilizar somente documentação.

---

# Exercício 10 — Desafio Avançado

Resolver utilizando:

Claude

*

Cursor

*

GitHub

*

Docker

*

Playwright

Tudo integrado.

---

# Exercício 11 — Revisão

Responder:

O que aprendi?

O que ainda tenho dificuldade?

Como posso melhorar?

---

# Exercício 12 — Autoavaliação

Avalie de 1 a 5.

```text
Conhecimento

⭐⭐⭐⭐☆

Prática

⭐⭐⭐☆☆

Confiança

⭐⭐☆☆☆

Velocidade

⭐⭐⭐☆☆
```

---

# Exercícios Específicos por Módulo

Agora sim começam os exercícios específicos.

---

# Módulo IA

## Exercícios

1. Explique um LLM para uma criança de 10 anos.
2. Explique para um gerente.
3. Explique para um desenvolvedor.
4. Compare GPT × Claude × Gemini.
5. Descubra qual responde melhor para QA.
6. Descubra qual responde melhor para programação.
7. Descubra qual responde melhor para documentação.
8. Faça uma tabela comparativa.
9. Pesquise as limitações de cada modelo.
10. Apresente um relatório com suas conclusões.

---

# Engenharia de Prompt

1. Criar um prompt ruim.
2. Melhorá-lo.
3. Melhorá-lo novamente.
4. Criar um prompt profissional.
5. Criar um prompt reutilizável.
6. Criar um prompt em Markdown.
7. Criar um prompt em XML.
8. Criar um prompt em JSON.
9. Criar um prompt para Claude.
10. Criar um prompt para Cursor.
11. Criar um prompt para ChatGPT.
12. Comparar as respostas.

---

# Claude

1. Criar um Project.
2. Criar Artifacts.
3. Revisar documentação.
4. Gerar requisitos.
5. Gerar arquitetura.
6. Criar BDD.
7. Criar Plano de Testes.
8. Refatorar um documento.
9. Revisar código.
10. Criar documentação técnica completa.

---

# Cursor

1. Criar projeto.
2. Criar CRUD.
3. Refatorar CRUD.
4. Corrigir bugs.
5. Utilizar Agent.
6. Criar Rules.
7. Criar documentação.
8. Criar testes.
9. Integrar Git.
10. Integrar MCP.

---

# Git

1. Criar repositório.
2. Criar branches.
3. Resolver conflitos.
4. Rebase.
5. Cherry Pick.
6. Tags.
7. Git Flow.
8. Conventional Commits.
9. Pull Request.
10. Code Review.

---

# GitHub

1. Criar Repository.
2. README profissional.
3. Wiki.
4. Issues.
5. Pull Request.
6. GitHub Projects.
7. GitHub Actions.
8. Secrets.
9. Releases.
10. Templates.

---

# Jira

1. Criar projeto Scrum.
2. Criar projeto Kanban.
3. Criar Sprint.
4. Criar Epic.
5. Criar Story.
6. Criar Task.
7. Criar Bug.
8. Criar Dashboard.
9. Criar Filtros.
10. Gerar Relatórios.

---

# Front-end

1. Landing Page.
2. Login.
3. Cadastro.
4. Dashboard.
5. CRUD.
6. Consumo API.
7. Tema Dark.
8. Responsividade.
9. Componentização.
10. Deploy.

---

# Back-end

1. API REST.
2. CRUD.
3. JWT.
4. Middleware.
5. Upload.
6. Swagger.
7. Paginação.
8. Logs.
9. Cache.
10. Docker.

---

# Banco

1. Modelagem.
2. SQL.
3. Relacionamentos.
4. Índices.
5. Procedures.
6. Views.
7. Triggers.
8. Backup.
9. Restore.
10. Integração.

---

# Docker

1. Dockerfile.
2. Compose.
3. Volumes.
4. Networks.
5. Banco.
6. API.
7. Front.
8. Healthcheck.
9. Build.
10. Deploy.

---

# QA

1. Plano de Testes.
2. Casos de Teste.
3. BDD.
4. Exploratório.
5. Regressão.
6. Smoke.
7. Integração.
8. API.
9. Performance (planejamento).
10. Relatório Final.

---

# Playwright

1. Login.
2. Cadastro.
3. CRUD.
4. API.
5. Fixtures.
6. POM.
7. Reports.
8. CI.
9. Docker.
10. GitHub Actions.

---

# Projeto Final

Durante toda a formação, o projeto deverá evoluir incrementalmente:

1. Landing Page.
2. Sistema de Login.
3. Cadastro de Usuários.
4. Dashboard Administrativo.
5. API REST.
6. Banco de Dados.
7. Autenticação JWT.
8. Dockerização.
9. Testes Manuais (BDD).
10. Testes Automatizados (Playwright).
11. Pipeline CI/CD.
12. Deploy.
13. Monitoramento.
14. Documentação Técnica.
15. Publicação do Portfólio no GitHub.

---

## Recomendação de melhoria

Há uma oportunidade de tornar esse material ainda mais robusto: para **cada exercício**, adicione quatro blocos padronizados:

* **Objetivo**: o que será aprendido.
* **Critérios de aceitação**: como saber se o exercício foi concluído com sucesso.
* **Erros comuns**: problemas frequentes e como evitá-los.
* **Material de apoio**: links para a documentação oficial e leituras recomendadas.

Isso transforma a lista de exercícios em um roteiro de prática guiada, muito mais próximo da experiência de um bootcamp profissional do que de uma simples coleção de tarefas.
