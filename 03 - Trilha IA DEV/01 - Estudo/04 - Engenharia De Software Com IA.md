# 04. Engenharia de software com IA

> A IA acelera o desenvolvimento, mas não substitui o conhecimento técnico: para revisar o que ela gera, você precisa entender o que está sendo gerado. Este módulo lista o essencial de cada camada (front, back, banco, Docker, DevOps e testes) e como usar a IA em cada uma. Cada camada é aplicada no [projeto principal](<../02 - Projeto/01 - Projeto Principal.md>).

## Como usar a IA em qualquer camada

| Momento | Pedido típico |
|---------|---------------|
| Aprender | "Explique este conceito com um exemplo no meu projeto" |
| Planejar | "Proponha a estrutura de pastas e justifique" |
| Implementar | "Implemente X seguindo as regras do projeto, com testes" |
| Revisar | "Revise este código: segurança, legibilidade e casos de borda" |
| Depurar | "Este é o erro e o stack trace. Liste as hipóteses em ordem de probabilidade" |
| Documentar | "Gere o README e a documentação da API" |

## Front-end

| Grupo | Conteúdo |
|-------|----------|
| Base | HTML5 semântico, CSS3, Flexbox, Grid, responsividade, animações, acessibilidade |
| Linguagem | JavaScript ES6+, TypeScript |
| Framework | React (hooks, React Router, Context API), Next.js (CSR, SSR, SEO) |
| Estado e dados | React Query, Redux Toolkit, Axios, Fetch |
| Formulários | React Hook Form, Zod |
| Estilo | Tailwind CSS (opcional) |

Práticas: landing page, login, cadastro, dashboard, CRUD, consumo de API, tema escuro, responsividade, componentização, formulário validado, estados de carregamento e erro, acessibilidade básica e deploy.

## Back-end

| Grupo | Conteúdo |
|-------|----------|
| Plataforma | Node.js, Express, NestJS |
| APIs | REST, introdução a GraphQL, OpenAPI/Swagger |
| Arquitetura | MVC, SOLID, Clean Code, DDD, Repository Pattern, services, DTO |
| Segurança | JWT, refresh token, RBAC, validação de entrada |
| Operação | middlewares, logs, cache (Redis), upload, paginação, ordenação, filtros, tratamento de erros |

Práticas: API REST com CRUD, JWT, middleware de autorização, upload, Swagger, paginação, logs, cache e Docker.

## Banco de dados

Conteúdo: SQL, PostgreSQL, MySQL, MongoDB, Prisma ORM, modelagem, normalização, relacionamentos, índices, views, procedures, triggers, migrations, backup, restore e performance.

Práticas: modelar o banco, criar tabelas e relacionamentos, escrever queries, criar índices, views e triggers, usar migrations e fazer backup e restore.

> Cuidado com SQL gerado por IA: confira índices, injeção de SQL e queries que leem a tabela inteira.

## Docker

Conteúdo: containers, imagens, Dockerfile, Docker Compose (`docker compose`), volumes, networks, registry (Docker Hub), Docker Desktop, healthcheck, build e variáveis de ambiente.

Práticas: Dockerfile do front e do back, banco em container, Compose com a stack completa, volumes, network, healthcheck e logs.

## DevOps e CI/CD

Conteúdo: CI, CD, pipelines, build, testes, artefatos, deploy, cloud, logs, observabilidade, rollback, blue/green, canary, secrets e ambientes.

Ferramentas: GitHub Actions, Docker, Vercel, Render, Grafana e Prometheus.

Práticas: pipelines de build, testes e deploy, uso de secrets e artefatos, rollback, logs e observabilidade básica.

## Testes e QA

O desenvolvedor também testa. O conteúdo de QA tem uma trilha própria: [Trilha IA QA](<../../02 - Trilha IA QA/README.md>). Para esta trilha, o essencial:

| Tema | Conteúdo |
|------|----------|
| QA manual | Análise de requisitos, plano de testes, casos de teste, BDD, matriz de rastreabilidade, riscos, smoke, sanidade, regressão, integração, exploratório, usabilidade, massa de testes, evidências e relatório |
| Não funcional | Performance, carga, stress e segurança (planejamento) |
| Playwright | Locators, assertions, fixtures, Page Object Model, testes de API, intercept, relatórios, screenshots, vídeos, traces, CI e Docker |
| Cypress | Estrutura, seletores, commands e custom commands, fixtures, intercept, API, Page Objects, relatórios e CI |
| Postman | Collections, environments, variables, testes, pre-request scripts, autorização, Collection Runner, Newman e CI |
| Robot Framework | Keywords, variables, suites, libraries, web, API, relatórios e pipeline |

Práticas: escolha pelo menos uma ferramenta além do Playwright. Cypress: login, cadastro, CRUD, upload, intercept, API, regressão, relatórios e CI. Postman: CRUD, autenticação, variáveis, scripts, execução automatizada com Newman, relatório e pipeline. Robot Framework: automação simples, login, API, relatórios e integração com pipeline.

Onde a IA ajuda nos testes: gerar cenários a partir da história, escrever Page Objects, criar massa de dados fictícia, explicar uma falha intermitente e manter seletores. O prompt [02 - Leitura De DOM E Page Objects](<../../_Wiki/01 - Prompts/02 - Leitura De DOM E Page Objects.md>) é um exemplo pronto.

> Teste gerado por IA também precisa de revisão: confira se ele testa o requisito ou só repete o que o código faz.

## Checklist de aprendizado

- [ ] Sei usar a IA para aprender, planejar, implementar, revisar, depurar e documentar
- [ ] Construí front, back e banco do projeto com apoio de IA, revisando o código
- [ ] Containerizei a aplicação com Docker Compose
- [ ] Criei um pipeline de CI que roda os testes
- [ ] Automatizei pelo menos um fluxo com Playwright ou Cypress
