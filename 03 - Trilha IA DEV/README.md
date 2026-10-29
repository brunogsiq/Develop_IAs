# Trilha de Estudo: IA DEV

> Trilha para usar Inteligência Artificial como parte do fluxo profissional de engenharia de software: desenvolver com agentes, trabalhar num fluxo profissional, construir aplicações com IA e entregar um projeto de portfólio completo. Serve para desenvolvedores, arquitetos e DevOps / SRE.

**Pré-requisito:** [01 - Trilha IA Geral](<../01 - Trilha IA Geral/README.md>). Fundamentos de LLM, engenharia de prompt, assistentes de IA, MCP, RAG, agentes, riscos e privacidade são explicados lá; aqui eles viram código.

## A ideia central

O objetivo não é só "usar IA". É usar IA **mantendo o controle**: entender o que está sendo produzido, tomar as decisões técnicas e responder pela qualidade, pela segurança e pelo resultado.

Ao final, você deve conseguir:

1. Trabalhar em um fluxo profissional: Jira, Git, GitHub, PR, code review e CI/CD.
2. Desenvolver com Cursor, Copilot e Claude Code, revisando o que geram.
3. Construir aplicações completas: front, back, banco, Docker, testes e deploy.
4. Construir funcionalidades com IA: API, tool calling, MCP, RAG e agentes.
5. Publicar um projeto de portfólio documentado.

## Como a trilha está organizada

```
03 - Trilha IA DEV/
├── 01 - Estudo/       08 módulos, na ordem de estudo
├── 02 - Projeto/      o projeto que evolui durante toda a trilha + desafio final e portfólio
├── 03 - Exercícios/   a estrutura padrão de exercícios e os exercícios de cada módulo
└── 04 - Consulta/     checklist de competências e referências
```

### Metodologia

- **Um projeto contínuo:** cada módulo é aplicado no [projeto principal](<02 - Projeto/01 - Projeto Principal.md>), em vez de exercícios soltos.
- **Mesma estrutura de exercícios em todo módulo:** guiado, fixação, comparação, pesquisa, debug, refatoração, integração, mini projeto, desafio, desafio avançado, revisão e autoavaliação ([estrutura padrão](<03 - Exercícios/01 - Estrutura Padrão Dos Exercícios.md>)).
- **Documentação oficial como fonte:** a IA aponta o caminho; a documentação confirma.
- **Comparação entre ferramentas:** resolver o mesmo problema em ferramentas diferentes e registrar as diferenças.

### 01. Estudo

| # | Módulo | Assunto |
|---|--------|---------|
| 01 | [Fluxo Profissional Com IA](<01 - Estudo/01 - Fluxo Profissional Com IA.md>) | Git, GitHub, Jira, Trello e o fluxo da história ao deploy |
| 02 | [IDEs Com IA Cursor E Copilot](<01 - Estudo/02 - IDEs Com IA Cursor E Copilot.md>) | Modos de interação, regras de projeto e desenvolvimento assistido |
| 03 | [Claude Code](<01 - Estudo/03 - Claude Code.md>) | Agente de desenvolvimento, CLAUDE.md, permissões e Skills |
| 04 | [Engenharia De Software Com IA](<01 - Estudo/04 - Engenharia De Software Com IA.md>) | Front, back, banco, Docker, DevOps e testes |
| 05 | [API E Tool Calling](<01 - Estudo/05 - API E Tool Calling.md>) | Chamar modelos pela API, ferramentas, streaming, tokens e custo |
| 06 | [MCP Para Desenvolvedores](<01 - Estudo/06 - MCP Para Desenvolvedores.md>) | Conectar e construir servidores MCP |
| 07 | [RAG E Embeddings](<01 - Estudo/07 - RAG E Embeddings.md>) | Busca semântica, bancos vetoriais e avaliação de RAG |
| 08 | [Agentes E Automação](<01 - Estudo/08 - Agentes E Automação.md>) | Padrões de agentes, n8n, Obsidian e integrações |

### Por papel

| Papel | Foco sugerido |
|-------|---------------|
| Desenvolvedor | Trilha completa, na ordem |
| Arquiteto | 02 e 03 para conhecer as ferramentas; 05 a 08 com atenção às decisões (modelo, custo, identidade, RAG × agente) |
| DevOps / SRE | 01 a 04 (pipelines, Docker, CI/CD com IA); 06 (operar servidores MCP); 05 e 08 para custo, limites e observabilidade |

### 02. Projeto

| Arquivo | Assunto |
|---------|---------|
| [01 - Projeto Principal](<02 - Projeto/01 - Projeto Principal.md>) | Etapas de evolução e workflow completo de engenharia com IA |
| [02 - Desafio Final E Portfólio](<02 - Projeto/02 - Desafio Final E Portfólio.md>) | O que entregar e como apresentar |

### 03. Exercícios

| Arquivo | Assunto |
|---------|---------|
| [01 - Estrutura Padrão Dos Exercícios](<03 - Exercícios/01 - Estrutura Padrão Dos Exercícios.md>) | Os 12 tipos de exercício e a autoavaliação |
| [02 - Exercícios Por Módulo](<03 - Exercícios/02 - Exercícios Por Módulo.md>) | Lista de exercícios de cada módulo |

### 04. Consulta

| Arquivo | Assunto |
|---------|---------|
| [01 - Checklist De Competências](<04 - Consulta/01 - Checklist De Competências.md>) | O que você deve saber fazer ao final |
| [02 - Referências](<04 - Consulta/02 - Referências.md>) | Documentação oficial de cada ferramenta e tecnologia da trilha |

O glossário, as referências gerais e o [catálogo de ferramentas de IA](<../01 - Trilha IA Geral/02 - Consulta/03 - Catálogo De Ferramentas De IA.md>) ficam na Trilha IA Geral.

## Cronograma sugerido (~16 semanas, depois da Trilha Geral)

| Fase | Semanas | Módulos | Entregável |
|------|---------|---------|------------|
| 1. Fluxo e ferramentas de IA | 1 a 4 | 01 a 03 + projeto (etapa 1) | Repositório e quadro do projeto prontos, regras no Cursor/Copilot, `CLAUDE.md` e uma Skill |
| 2. Construir software com IA | 5 a 10 | 04 + projeto (etapas 2 a 13) | Aplicação completa com testes, pipeline e deploy |
| 3. Construir com IA | 11 a 14 | 05 a 08 + projeto (etapas 14 e 15) | Funcionalidade com IA no projeto (API, MCP ou RAG) e uma automação |
| 4. Fechamento | 15 e 16 | Desafio final e portfólio | Projeto publicado e documentado |

> A quantidade de semanas pode ser ajustada. O importante é manter a ordem de dependência.

## Relação com as outras trilhas

- A [Trilha IA Geral](<../01 - Trilha IA Geral/README.md>) dá a base conceitual comum a todas as profissões.
- A [Trilha IA QA](<../02 - Trilha IA QA/README.md>) ensina a **testar** o que esta trilha ensina a **construir**. Os módulos 05 a 08 daqui têm um par do lado do teste: servidor MCP (QA 04), escolha de ferramenta medida com evals (QA 05 e 07), RAG e agentes (QA 08).

## Progresso geral

- [ ] Trilha IA Geral concluída
- [ ] Fase 1 concluída
- [ ] Fase 2 concluída
- [ ] Fase 3 concluída
- [ ] Fase 4 concluída
- [ ] Checklist de competências revisado

## Regras para evoluir este material

1. Não trocar conteúdo essencial por modismo, nem adicionar ferramenta só porque apareceu em anúncio.
2. Validar na documentação oficial: recursos, planos e limites mudam.
3. Não registrar preços; registrar o link oficial e a data da verificação.
4. Manter em todos os módulos: exercícios, comparação entre ferramentas e checklist.
5. Manter o projeto evolutivo como fio condutor.
6. Manter os pilares da trilha: Claude Code e Cursor/Copilot; front-end e back-end; QA manual e automação; Git, GitHub, Docker e CI/CD; Jira/Trello; MCP, RAG, agentes e n8n; documentação e pesquisa na fonte oficial.
7. Nunca registrar dados de cliente ou de empresa: o repositório é público.
