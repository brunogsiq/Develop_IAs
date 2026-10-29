# 08. Agentes e automação

> Um agente é um modelo que usa ferramentas em sequência e decide os próximos passos sozinho até cumprir um objetivo. Automação é colocar a IA dentro de um fluxo que roda sem você: um gatilho dispara, a IA processa, o resultado vai para outro sistema.

## Objetivos

- Entender os padrões de agentes e quando **não** usar um.
- Construir automações com n8n.
- Organizar uma base de conhecimento pessoal com Obsidian.
- Conectar a IA a ferramentas externas com segurança.

## Agentes

| Conceito | O que é |
|----------|---------|
| **Tool use** | O modelo chama ferramentas ([05 - API E Tool Calling](<05 - API E Tool Calling.md>)) |
| **Memória** | O que o agente guarda entre etapas e sessões |
| **Workflow** | Sequência definida pelo código: você controla a ordem |
| **Agente** | O modelo decide a ordem e quando parar |
| **Planner → Executor** | Um agente planeja, outro executa |
| **Supervisor → Workers** | Um agente distribui tarefas para agentes especializados |
| **Single × multi-agent** | Um agente com várias ferramentas ou vários agentes cooperando |
| **Orquestração** | Quem coordena, e como os resultados são combinados |
| **Observabilidade** | Traces de cada passo: qual ferramenta, com quais parâmetros e qual resultado |

### Quando usar um agente

Comece pela opção mais simples: **uma chamada → um workflow → um agente**. Use agente só quando:
- a tarefa tem muitos passos e não dá para prever a ordem;
- o resultado compensa mais custo e tempo;
- os erros podem ser detectados e corrigidos (testes, revisão, rollback).

### Frameworks

| Ferramenta | Destaque |
|------------|----------|
| Claude Agent SDK | O "motor" do Claude Code como biblioteca: ferramentas de arquivo, terminal, MCP e subagentes prontos |
| OpenAI Agents SDK | SDK de agentes da OpenAI |
| LangChain / LangGraph | Componentes para LLM e grafos de agentes com estado |
| CrewAI | Equipes de agentes com papéis |
| AutoGen | Multiagente da Microsoft (a Microsoft vem unificando AutoGen e Semantic Kernel no Microsoft Agent Framework; confira o status) |

Estude um framework quando o problema pedir, não antes. Entender o laço de tool calling à mão vale mais do que decorar um framework.

## Automação com n8n

n8n é uma plataforma de automação visual, com versão open source auto-hospedada e versão em nuvem paga.

Conteúdo: nodes, triggers, workflows, webhooks, chamadas de API, credenciais, nodes de IA (modelos, agente, MCP), tratamento de erros e logs.

Projeto de referência:

```text
Nova User Story (Jira ou webhook)
   ↓
n8n
   ↓
Claude (análise)
   ↓
Pontos de atenção + cenários iniciais
   ↓
Documentação (Confluence, Notion ou arquivo)
```

Práticas: workflow simples, workflow com Claude, gerador de documentação, analisador de requisitos, classificador de bugs, gerador de relatórios e automação de user story.

Alternativas: Zapier e Make (mais simples, sem auto-hospedagem). Veja o [catálogo](<../../01 - Trilha IA Geral/02 - Consulta/03 - Catálogo De Ferramentas De IA.md>).

## Base de conhecimento com Obsidian

Obsidian guarda notas em Markdown local, com links, backlinks, tags e templates. Combinado com IA, vira uma base pessoal consultável.

Prática: criar um vault com notas de IA, engenharia de prompt, Claude, Cursor, front-end, back-end, QA, DevOps e arquitetura, ligadas entre si. Depois, usar o Claude Code ou um servidor MCP para consultar e resumir o vault.

## Integrações externas

Conforme disponibilidade oficial: GitHub, Gmail, Slack, Notion, Google Drive, Jira, Trello, bancos de dados, APIs e CRM. Podem ser feitas por conectores do Claude, servidores MCP, n8n ou código próprio.

> Antes de integrar, confira permissões, limites, plano e **quais dados saem** para o provedor de IA.

## Computer use

Recurso da API em que o modelo controla um computador (tela, mouse e teclado) a partir de screenshots. Útil para sistemas sem API, porém mais lento, mais caro e mais arriscado do que tools ou MCP. Use em ambiente isolado e com supervisão.

## Segurança

- Agentes ampliam o impacto de um prompt injection: limite as ferramentas e as permissões.
- Ações irreversíveis exigem confirmação humana.
- Registre traces para auditar o que o agente fez.
- Defina limites de passos e de custo.

## Práticas

1. Criar um agente de documentação que lê um repositório e gera o README.
2. Criar um agente de code review com critérios definidos.
3. Criar um agente de QA que recebe uma história e devolve cenários BDD.
4. Implementar um fluxo Planner → Executor.
5. Comparar agente único e multiagente na mesma tarefa: qualidade, custo e tempo.
6. Montar o projeto de referência no n8n.

## Checklist de aprendizado

- [ ] Sei diferenciar workflow de agente
- [ ] Sei quando um agente não é a melhor escolha
- [ ] Construí um agente com tool calling
- [ ] Montei uma automação no n8n com IA
- [ ] Criei uma base de conhecimento no Obsidian
- [ ] Defini limites e confirmações para ações irreversíveis
