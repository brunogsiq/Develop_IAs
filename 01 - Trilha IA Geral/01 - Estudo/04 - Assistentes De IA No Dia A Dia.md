# 04. Assistentes de IA no dia a dia

> Antes de testar ou programar com IA, use-a como ferramenta de análise e produtividade. Isso vale para qualquer papel: analisar documentos, pesquisar, escrever, preparar reuniões e desenhar fluxos. O módulo usa o Claude (claude.ai) como exemplo principal, mas os mesmos recursos existem, com outros nomes, nos demais assistentes.

> Recursos, nomes e planos mudam com frequência. Antes de estudar um recurso, confira a documentação oficial em [support.claude.com](https://support.claude.com) e [docs.claude.com](https://docs.claude.com).

## Objetivos

- Organizar o trabalho em projetos e manter o contexto certo.
- Usar um assistente para analisar documentos, pesquisar, escrever e preparar reuniões.
- Saber os limites: o que conferir sempre e o que nunca enviar.

## Recursos equivalentes entre assistentes

| Necessidade | Claude | ChatGPT | Gemini | Microsoft Copilot |
|-------------|--------|---------|--------|-------------------|
| Agrupar conversas e arquivos de um assunto | Projects | Projects | Gems / NotebookLM | Notebooks ⚠️ |
| Instruções fixas | Instruções do Project, Estilos | Custom instructions, GPTs | Gems | ⚠️ |
| Conteúdo editável ao lado do chat | Artifacts | Canvas | Canvas | Pages ⚠️ |
| Pesquisa profunda com fontes | Research | Deep research | Deep Research | ⚠️ |
| Ligar a ferramentas externas | Conectores e MCP | Conectores / apps | Extensões | Conectores do Microsoft 365 |

> ⚠️ = nome ou disponibilidade a confirmar na documentação oficial. O que importa é saber **o que procurar** em qualquer ferramenta, não decorar nomes.

## Recursos principais (exemplo: Claude)

| Recurso | Para que serve |
|---------|----------------|
| **Projects** | Agrupar conversas, arquivos e instruções de um mesmo assunto. Ex.: um Project por sistema ou cliente de estudo |
| **Instruções do Project** | Regras fixas para todas as conversas do Project (tom, formato, papel) |
| **Artifacts** | Conteúdo gerado em painel separado: documentos, código, diagramas, páginas e ferramentas interativas, que podem ser editados e compartilhados |
| **Estilos** | Ajustar o tom e o formato das respostas |
| **Memória** | Lembrar preferências e contexto entre conversas (conforme o plano e as configurações) |
| **Pesquisa (Research)** | Pesquisa mais profunda na web, com fontes |
| **Raciocínio estendido** | Respostas mais elaboradas em problemas difíceis |
| **Conectores e MCP** | Ligar o Claude a ferramentas externas (Drive, GitHub, Jira etc.), conforme disponibilidade |
| **Contexto longo** | Trabalhar com documentos grandes de uma vez |

## Casos de uso

### Análise de documentos

Entradas típicas: PDF, Word, Excel, PowerPoint, histórias de usuário, requisitos, RFC, Swagger/OpenAPI, diagramas UML e contratos.

Práticas:
- Resumir um documento e listar as decisões.
- Extrair requisitos e montar uma **matriz de rastreabilidade**.
- Encontrar ambiguidades, conflitos e inconsistências.
- Gerar perguntas para refinamento.
- Comparar duas versões de um documento.
- Criar checklist de revisão e documentação derivada.

### Pesquisa assistida por IA

Conteúdo: estratégias de pesquisa, pesquisa profunda, verificação e comparação de fontes, *fact checking*, avaliação de credibilidade e documentação oficial.

Práticas:
- Pesquisar uma tecnologia em pelo menos 5 fontes e comparar divergências.
- Validar uma afirmação feita pela IA na documentação oficial.
- Produzir um relatório técnico citando as fontes.

> Regra de ouro: a IA aponta o caminho; a **documentação oficial** confirma.

### Comunicação profissional

Conteúdo: e-mails, relatórios, atas, resumos, RFC, ADR (*Architecture Decision Record*), feedback técnico e comunicação com stakeholders.

Práticas:
- Escrever um e-mail profissional a partir de tópicos.
- Criar um relatório executivo e um relatório técnico sobre o mesmo assunto.
- Adaptar um texto técnico para o público executivo.
- Escrever um ADR para uma decisão de arquitetura.

### Preparação de reuniões

Conteúdo: refinamento, planning, daily, review, retrospectiva, agenda, checklist, ata e follow-up.

Práticas:
- Preparar a agenda e as perguntas de um refinamento a partir das histórias.
- Gerar a ata a partir de anotações, listando decisões e pendências.

### Análise de dados

Conteúdo: CSV, Excel, SQL, logs, KPIs, métricas e dashboards.

Práticas:
- Analisar uma planilha e identificar anomalias.
- Interpretar um log de erro e sugerir a causa provável.
- Definir KPIs para um time e gerar um relatório com insights.

### Geração de conteúdo técnico

Conteúdo: README, wiki, documentação de API (Swagger), tutoriais, guias, artigos e documentação funcional e técnica.

Práticas:
- Escrever um README completo para um projeto.
- Criar um guia de instalação e um tutorial.

### Fluxos de trabalho e diagramas

Conteúdo: Mermaid, BPMN, fluxogramas, UML, diagramas de sequência e arquitetura.

Práticas:
- Desenhar em Mermaid o fluxo de desenvolvimento, o fluxo de QA, um pipeline de CI/CD e a sequência de login.
- Desenhar a arquitetura da aplicação do projeto.

### Colaboração

Conteúdo: compartilhamento de conversas e Artifacts, revisão, versionamento de documentação e convenções de time.

Práticas:
- Revisar um documento produzido por outra pessoa.
- Definir convenções de prompts e de documentação para um time.

## Cuidados

- **Dados sensíveis:** nunca envie dados de clientes, senhas ou código proprietário para contas pessoais. Siga a política de IA da empresa ([02 - Uso Responsável E Privacidade](<02 - Uso Responsável E Privacidade.md>)).
- **Confira números e citações:** a IA pode errar valores e inventar referências.
- **Contexto demais atrapalha:** prefira enviar só o que é relevante para a tarefa.

## Práticas do módulo

1. Criar um projeto (Project) para um sistema de estudo, com instruções e documentos.
2. Criar um documento, um diagrama e uma ferramenta interativa simples no painel de conteúdo (Artifact/Canvas).
3. Revisar uma história de usuário e gerar perguntas de refinamento.
4. Aplicar à sua área: plano de testes (QA), revisão de um trecho de código (dev), comparação de duas arquiteturas (arquiteto) ou análise de um log de erro (DevOps).
5. Refatorar um documento existente (reorganizar, eliminar repetição, ajustar ao público) e gerar uma documentação técnica completa a partir dele.
6. Gerar uma proposta de arquitetura a partir de requisitos, pedindo premissas e riscos explícitos.
7. Preparar uma reunião e gerar a ata.
8. Comparar dois assistentes (por exemplo, Claude e ChatGPT) em uma tarefa real.

## Checklist de aprendizado

- [ ] Uso projetos para separar assuntos e manter o contexto
- [ ] Criei conteúdos de tipos diferentes no painel ao lado do chat
- [ ] Analisei um documento e extraí requisitos e ambiguidades
- [ ] Fiz uma pesquisa validando as fontes na documentação oficial
- [ ] Escrevi um relatório executivo e um técnico
- [ ] Desenhei um fluxo em Mermaid
- [ ] Sei o que nunca enviar para uma IA
