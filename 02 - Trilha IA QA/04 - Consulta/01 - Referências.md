# Referências

> Conteúdos externos para aprofundar. Marque conforme for consumindo.

## Priorização: trilhas do Claude e do Copilot

Nem todo conteúdo de ferramenta agrega da mesma forma. Leve dessas trilhas os **conceitos**, que valem para qualquer modelo de IA, e a **prática com MCP**. Pode pular sem culpa a parte que só ensina botões e configurações.

| Tipo de conteúdo | Exemplo | Vale para o projeto? |
|---|---|---|
| **Conceito** (como a IA funciona e falha) | Tool calling, MCP, alucinação | ✅ Muito |
| **Prática com a ferramenta** | Gerar casos de teste com o Copilot | ✅ Médio (produtividade) |
| **Recurso específico do produto** | Atalhos, planos, configurações | ❌ Pouco |

Ordem sugerida:

| Ordem | O quê | Por quê |
|---|---|---|
| 1 | [Trilha IA Geral](<../../01 - Trilha IA Geral/README.md>) (módulos 01 e 06) e [04 - Testando MCP.md](<../01 - Estudo/04 - Testando MCP.md>) + curso **Introduction to Model Context Protocol** (Claude Academy) | Base conceitual. A Anthropic criou o MCP |
| 2 | **AI Fluency: Framework & Foundations** (Claude Academy) | Ajuda a pensar como avaliador de IA |
| 3 | Copilot no VS Code focado em **modo agente + MCP** ([laboratório](<../02 - Laboratório/README.md>)) | Prática do conceito na sua máquina |
| 4 | **Building with the Claude API** (Claude Academy), mesmo só lendo | Mostra tool calling e system prompt por dentro |
| 5 | **MCP: Advanced Topics** (Claude Academy) | Depois de dominar o básico |
| 6 | GitHub Copilot Fundamentals (Microsoft Learn); ver as [trilhas oficiais dos fornecedores](<../../01 - Trilha IA Geral/02 - Consulta/04 - Trilhas Oficiais Dos Fornecedores.md>) | Produtividade no dia a dia de QA |

Ganho indireto: **usar IA todo dia treina o seu olho para os erros dela.** Cada vez que o Copilot inventar uma função que não existe, você está vendo uma alucinação ao vivo.

## Base geral

Fundamentos de LLM, prompt, MCP, segurança e privacidade estão nas [referências da Trilha IA Geral](<../../01 - Trilha IA Geral/02 - Consulta/02 - Referências.md>). Aqui ficam só as referências específicas de QA.

## MCP para teste

- [ ] **DeepLearning.AI: "MCP: Build Rich-Context AI Apps with Anthropic"** (curso curto e gratuito).
- [ ] **MCP Inspector**: ferramenta oficial para testar servidores MCP.
  ```bash
  npx @modelcontextprotocol/inspector
  ```
- [ ] **Repositório de servidores MCP de exemplo**: github.com/modelcontextprotocol/servers

## Teste de IA e evals

- [ ] **promptfoo**: promptfoo.dev. Testes de LLM com YAML, inclusive red teaming.
- [ ] **DeepEval**: deepeval.com. Framework de avaliação em Python.
- [ ] **Ragas**: docs.ragas.io. Avaliação de sistemas RAG.
- [ ] **Langfuse**: langfuse.com. Traces, datasets e avaliações (open source).
- [ ] **Ollama**: ollama.com. Rodar modelos localmente e de graça, útil para estudar evals sem chave de API.
- [ ] **Playwright MCP**: github.com/microsoft/playwright-mcp. Servidor MCP que deixa o agente navegar num navegador (ver arquivo 09).
- [ ] **DeepLearning.AI**: buscar cursos curtos sobre "evaluating" e "red teaming LLM applications".

## Certificações

- [ ] **ISTQB CT-AI**: Certified Tester AI Testing. Testar sistemas baseados em IA.
- [ ] **ISTQB CT-GenAI**: Testing with Generative AI. Uso e teste de IA generativa.
  - No Brasil, ver BSTQB (bstqb.online) para disponibilidade em português.

## Domínio bancário e regulação

- [ ] **Banco Central do Brasil: cotações e PTAX** (bcb.gov.br) e **portal de dados abertos** (API da PTAX).
- [ ] **LGPD**: Lei 13.709/2018 (planalto.gov.br) e guias da ANPD (gov.br/anpd).
- [ ] **Lei Complementar 105/2001**: sigilo bancário.
- [ ] **Resolução CMN 4.893/2021**, com a alteração da **Resolução CMN 5.274/2025**: segurança cibernética e nuvem em instituições financeiras. Consulte o texto consolidado em bcb.gov.br (busca de normas).

## Prática recomendada

- [ ] Usar um assistente de IA no dia a dia e observar falhas
- [ ] Rodar o MCP Inspector num servidor MCP de exemplo
- [ ] Criar um projeto pequeno no promptfoo com 5 casos
- [ ] (Opcional) Seguir o quickstart oficial do MCP e criar um servidor "de brinquedo" com uma tool de câmbio usando a API pública da PTAX
