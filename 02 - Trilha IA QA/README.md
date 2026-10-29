# Trilha de Estudo: IA QA

> Trilha pessoal e profissional para sair do teste de aplicações tradicionais e chegar ao teste de sistemas com IA, LLM e MCP. O caso de uso de referência é um assistente bancário que usa MCP para consultar câmbio, crédito e dados de clientes.

**Pré-requisito:** [01 - Trilha IA Geral](<../01 - Trilha IA Geral/README.md>). Os conceitos (LLM, prompt, MCP, RAG, agentes, riscos) são explicados lá; aqui eles viram teste.

## A ideia central

Em um sistema com IA:

1. **A mesma pergunta pode gerar respostas diferentes** (não determinismo).
2. **O sistema pode responder algo errado com total confiança** (alucinação).

Quase tudo o que há para aprender nesta trilha vem dessas duas frases.

## Como a trilha está organizada

```
02 - Trilha IA QA/
├── 01 - Estudo/        01 a 09, na ordem de leitura
├── 02 - Laboratório/   prática na sua máquina: Copilot + MCP + servidor de câmbio
├── 03 - Templates/     01 cenários · 02 golden dataset · 03 registro · 04 perguntas · 05 estratégia
├── 04 - Consulta/      01 referências de QA
└── 05 - Carreira/      01 próximos passos: ferramentas, certificações, portfólio
```

Cada arquivo de estudo termina com um **"Checklist de aprendizado"**: marque os itens trocando `[ ]` por `[x]` e faça commit. O histórico do Git vira o registro do seu progresso. Comportamentos estranhos que você observar nos exercícios vão para a seção "Comportamentos observados" do [03 - Registro De Execução](<03 - Templates/03 - Registro De Execução.md>).

### 01. Estudo

| # | Arquivo | Assunto |
|---|---------|---------|
| 01 | [01 - Mapa Da Jornada.md](<01 - Estudo/01 - Mapa Da Jornada.md>) | O fluxo completo de uma pergunta no caso bancário e o tipo de teste de cada etapa |
| 02 | [02 - Domínio Bancário.md](<01 - Estudo/02 - Domínio Bancário.md>) | Câmbio, crédito e regulação (LGPD, sigilo bancário, CMN) |
| 03 | [03 - LLM Sob A Ótica Do Teste.md](<01 - Estudo/03 - LLM Sob A Ótica Do Teste.md>) | O que cada conceito de LLM muda no teste |
| 04 | [04 - Testando MCP.md](<01 - Estudo/04 - Testando MCP.md>) | O servidor MCP como API: anatomia da tool, JSON-RPC, checklist e Inspector |
| 05 | [05 - Como Testar IA.md](<01 - Estudo/05 - Como Testar IA.md>) | Evals, golden dataset, LLM-as-judge e observabilidade |
| 06 | [06 - Segurança OWASP LLM.md](<01 - Estudo/06 - Segurança OWASP LLM.md>) | Como testar os riscos do OWASP LLM Top 10: injection, vazamento, agência |
| 07 | [07 - Evals Na Prática Com Promptfoo.md](<01 - Estudo/07 - Evals Na Prática Com Promptfoo.md>) | Montar e rodar evals, testar o sistema real, red teaming automatizado |
| 08 | [08 - Testando RAG E Agentes.md](<01 - Estudo/08 - Testando RAG E Agentes.md>) | Fidelidade ao documento, trajetória de agentes e suas falhas |
| 09 | [09 - IA Como Ferramenta Do QA.md](<01 - Estudo/09 - IA Como Ferramenta Do QA.md>) | Usar IA para gerar casos, revisar critérios, apoiar automação e escrever bugs |

### 02. Laboratório

| Arquivo | Assunto |
|---------|---------|
| [02 - Laboratório/README.md](<02 - Laboratório/README.md>) | Copilot + MCP no VS Code: servidor `filesystem` com clientes fictícios e servidor de câmbio (PTAX) em Python |

### 03. Templates

| Arquivo | Para quê |
|---------|----------|
| [01 - Cenários De Teste.md](<03 - Templates/01 - Cenários De Teste.md>) | Cerca de 40 cenários prontos para adaptar (câmbio, crédito, contexto, segurança, escopo, front) |
| [02 - Golden Dataset.csv](<03 - Templates/02 - Golden Dataset.csv>) | Planilha do golden dataset, abre direto no Excel |
| [03 - Registro De Execução.md](<03 - Templates/03 - Registro De Execução.md>) | Comportamentos observados, evidência de execução e de bug de IA |
| [04 - Perguntas Para O Time.md](<03 - Templates/04 - Perguntas Para O Time.md>) | O que perguntar para preencher as lacunas do projeto |
| [05 - Estratégia De Teste.md](<03 - Templates/05 - Estratégia De Teste.md>) | Estratégia de teste por camada, metas, critérios de entrada e saída, riscos |

### 04. Consulta

| Arquivo | Assunto |
|---------|---------|
| [01 - Referências.md](<04 - Consulta/01 - Referências.md>) | Priorização de cursos, ferramentas de eval, certificações e regulação bancária |

O glossário, as referências gerais e o catálogo de ferramentas ficam na [Trilha IA Geral](<../01 - Trilha IA Geral/02 - Consulta/01 - Glossário.md>).

### 05. Carreira

| Arquivo | Assunto |
|---------|---------|
| [01 - Próximos Passos Depois Da Trilha.md](<05 - Carreira/01 - Próximos Passos Depois Da Trilha.md>) | O que fazer depois da trilha: ferramentas prioritárias, módulos da DEV, certificações, portfólio e posicionamento |

## Cronograma sugerido (~6 semanas, depois da Trilha Geral)

| Semana | Foco | Entregável |
|--------|------|------------|
| 1 | [Mapa da jornada](<01 - Estudo/01 - Mapa Da Jornada.md>), [domínio bancário](<01 - Estudo/02 - Domínio Bancário.md>) e [LLM sob a ótica do teste](<01 - Estudo/03 - LLM Sob A Ótica Do Teste.md>) | Tabela de [comportamentos observados](<03 - Templates/03 - Registro De Execução.md>), marcando o que vira cenário |
| 2 | [Testando MCP](<01 - Estudo/04 - Testando MCP.md>) + [laboratório](<02 - Laboratório/README.md>) | Desenho da arquitetura do projeto com perguntas validadas pelo time |
| 3 | [Teste de IA](<01 - Estudo/05 - Como Testar IA.md>) e [segurança](<01 - Estudo/06 - Segurança OWASP LLM.md>) | Rascunho do golden dataset (30 a 50 perguntas). Para acelerar, use a IA para sugerir perguntas ([09, seção 1](<01 - Estudo/09 - IA Como Ferramenta Do QA.md#1-gerar-casos-de-teste-a-partir-de-uma-história>)) e revise cada uma |
| 4 | Respostas às [perguntas para o time](<03 - Templates/04 - Perguntas Para O Time.md>) | [Estratégia de teste](<03 - Templates/05 - Estratégia De Teste.md>) por camada |
| 5 | [Evals com promptfoo](<01 - Estudo/07 - Evals Na Prática Com Promptfoo.md>) | Golden dataset rodando com taxa de acerto medida |
| 6 | [RAG e agentes](<01 - Estudo/08 - Testando RAG E Agentes.md>) + [IA como ferramenta do QA](<01 - Estudo/09 - IA Como Ferramenta Do QA.md>) (completo) | Casos de RAG/agentes (se aplicável) e automação apoiada por IA, revisada |

> As semanas 1 a 4 preparam você para o projeto. As semanas 5 e 6 aprofundam e podem acontecer em paralelo ao trabalho.

## A divisão que organiza todo o resto

| Camada | Natureza | Como testar |
|--------|----------|-------------|
| Front (chat, layout Figma) | Determinística | Como sempre: UI, usabilidade, acessibilidade |
| Servidor MCP e APIs do banco | Determinística | **Como API comum** (você já sabe fazer) |
| Comportamento da IA | **Não determinística** | **Evals e estatística** (a parte nova) |
| Segurança | Mista | Red teaming + checklist OWASP LLM |

## Progresso geral

- [ ] Trilha IA Geral concluída
- [ ] Semana 1 concluída
- [ ] Semana 2 concluída
- [ ] Semana 3 concluída
- [ ] Semana 4 concluída
- [ ] Semana 5 concluída
- [ ] Semana 6 concluída
- [ ] Golden dataset v1 pronto e rodando no promptfoo
- [ ] Estratégia de teste apresentada ao time
- [ ] Plano de [próximos passos](<05 - Carreira/01 - Próximos Passos Depois Da Trilha.md>) iniciado

## Próximo passo

Siga o plano de [próximos passos depois da trilha](<05 - Carreira/01 - Próximos Passos Depois Da Trilha.md>). Ele indica quais módulos da [03 - Trilha IA DEV](<../03 - Trilha IA DEV/README.md>) fazer (não é preciso a trilha inteira), quais ferramentas priorizar, quais certificações fazer e como montar o portfólio.

> Os nomes de tools e as regras de negócio dos exemplos são ilustrativos. Dados, respostas e bugs do projeto real ficam nos canais do projeto, nunca neste repositório.
