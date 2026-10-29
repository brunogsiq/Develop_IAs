# Trilhas oficiais dos fornecedores

> Os fornecedores de IA mantêm cursos e certificações próprios. Este mapa não copia esse conteúdo, porque ele muda a cada poucos meses. Ele mostra **o que existe, em que ordem fazer e qual módulo deste repositório cada curso complementa**.

> [!IMPORTANT]
> Nomes de cursos, códigos de exame e catálogos mudam com frequência, e preços não são registrados aqui. Os itens marcados com ⚠️ foram confirmados só por fontes de terceiros. Antes de se inscrever, confira no site oficial e anote abaixo a data da sua verificação.

## Como usar

1. Faça primeiro o módulo correspondente deste repositório: ele dá o contexto e o espírito crítico.
2. Use a trilha oficial para aprofundar na ferramenta que você realmente usa no trabalho.
3. Certificação é opcional. Ela vale quando o mercado ou a empresa pede; o aprendizado vem da prática.

## Ferramentas de IA

### Claude (Anthropic)

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **Claude Academy** ([academy.claude.com](https://academy.claude.com)) ⚠️, que sucedeu a Anthropic Academy ([anthropic.skilljar.com](https://anthropic.skilljar.com)) | Cursos gratuitos, sem certificação formal | Ver abaixo |
| AI Fluency: Framework & Foundations | Usar IA com critério em qualquer função | Geral 01, 02 e 03 |
| Claude 101 | Recursos do Claude no dia a dia | Geral 04 |
| Introduction to Model Context Protocol / MCP: Advanced Topics | MCP do conceito à construção | Geral 06, QA 04, DEV 06 |
| Claude Code in Action | Desenvolver com o agente | DEV 03 |
| Building with the Claude API | API, tool calling, system prompt | DEV 05, QA 03 |
| Introduction to agent skills / subagents ⚠️ | Skills e subagentes | DEV 03 e 08 |
| Documentação oficial ([docs.claude.com](https://docs.claude.com)) | Referência de API e de Claude Code | DEV 03 e 05 |

### GitHub Copilot (Microsoft / GitHub)

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **Microsoft Learn**: GitHub Copilot Fundamentals, partes 1 e 2 | Trilha oficial gratuita | DEV 02, QA 09 |
| Documentação do Copilot ([docs.github.com/copilot](https://docs.github.com/copilot)) | Modo agente, instruções do repositório, MCP no VS Code | DEV 02, laboratório da QA |
| **Certificação GH-300: GitHub Copilot** | Exame que valida o uso do Copilot | Opcional |

### Cursor

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **Cursor Learn** ([cursor.com/learn](https://cursor.com/learn)) ⚠️ | Curso oficial gratuito: fundamentos de IA, programar com agentes, revisar e testar o código gerado. Tem versão em espanhol; não tem certificado | DEV 02 |
| Documentação ([docs.cursor.com](https://docs.cursor.com)) | Regras do projeto, modo agente, MCP | DEV 02 |

## Nuvens

As três grandes nuvens oferecem modelos de vários fornecedores (inclusive Claude) como serviço gerenciado. É por elas que muitas empresas usam IA em produção, então o tema interessa principalmente a **arquitetos, DevOps e desenvolvedores**.

### AWS

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **AWS Skill Builder** ([skillbuilder.aws](https://skillbuilder.aws)) | Planos de estudo e laboratórios, muitos gratuitos | Ver abaixo |
| **AWS Certified AI Practitioner (AIF-C01)** ⚠️ | Certificação de entrada: conceitos de IA e IA generativa na AWS. Também serve para quem não programa | Geral 01 a 08 |
| Amazon Bedrock (documentação e cursos no Skill Builder) | Usar modelos de vários fornecedores, RAG (Knowledge Bases), agentes e guardrails na AWS | DEV 05, 07 e 08 |
| **AWS Certified Generative AI Developer – Professional (AIP-C01)** | Certificação avançada para quem constrói aplicações com IA generativa. A AWS recomenda chegar com experiência e outras certificações | DEV 05 a 08 |

### Microsoft Azure

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **Microsoft Learn** ([learn.microsoft.com](https://learn.microsoft.com)) | Trilhas gratuitas de IA no Azure | Ver abaixo |
| **Azure AI Fundamentals**: exame AI-901, sucessor do AI-900 ⚠️ | Certificação de entrada em conceitos de IA no Azure | Geral 01 a 08 |
| Azure AI Foundry / Azure OpenAI (documentação) | Modelos, agentes e RAG no Azure | DEV 05 a 08 |
| **Azure AI App and Agent Developer Associate**: exame AI-103, sucessor do AI-102 ⚠️ | Certificação para quem constrói aplicações e agentes no Azure | DEV 05 a 08 |

> O AI-900 e o AI-102 foram aposentados em 30/06/2026. Quem já tinha as certificações continua com elas válidas.

### Google Cloud

| Onde | O que fazer | Complementa |
|------|-------------|-------------|
| **Google Skills** ([skills.google](https://www.skills.google), antigo Cloud Skills Boost) | Trilhas e laboratórios | Ver abaixo |
| **Generative AI Leader** (trilha gratuita de 5 cursos + certificação) | Visão de negócio e estratégia de IA generativa, para quem não é técnico: gestão, PO, liderança | Geral 01, 02, 05, 07 a 09 |
| Vertex AI (documentação e cursos) | Modelos, agentes e RAG no Google Cloud | DEV 05 a 08 |
| **Professional Machine Learning Engineer** ⚠️ | Certificação técnica de ML e IA no Google Cloud | DEV 05 a 08 |

## Por papel: por onde começar

| Papel | Primeira trilha oficial sugerida |
|-------|----------------------------------|
| Todos | Claude Academy: AI Fluency |
| QA | GitHub Copilot Fundamentals (gerar casos e automação) + Claude Academy: Building with the Claude API, para entender o que está testando |
| Dev | Copilot Fundamentals ou Cursor Learn (o editor que você usa) + Claude Code in Action |
| Arquiteto | A certificação de entrada da nuvem da empresa (AWS AI Practitioner, Azure AI Fundamentals ou Google Generative AI Leader), depois a trilha de construção da mesma nuvem |
| DevOps / SRE | A trilha de IA da nuvem da empresa, com foco em operação: custo, limites, segurança e observabilidade |
| Gestão / PO | Google Generative AI Leader ou AI Fluency |

> Escolha **uma** nuvem: a que a empresa usa. Fazer as três ao mesmo tempo dispersa o estudo.

## Registro das verificações

| Data | Fornecedor | O que mudou |
|------|------------|-------------|
| | | |
