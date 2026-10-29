# Catálogo de ferramentas de IA

> Catálogo de IAs e ferramentas, por categoria, com o que cada uma faz e onde encontrar. Serve para consulta e para o exercício de comparação dos módulos. As ferramentas marcadas com ★ fazem parte do caminho principal da trilha; as demais são opcionais.

> [!IMPORTANT]
> Preços, planos e limites mudam com frequência e **não** são registrados aqui. A coluna "Acesso" indica apenas o tipo de oferta, e mesmo ela deve ser conferida no site oficial antes de usar. Registre a data da sua verificação.

## Legenda de acesso

| Marca | Significado |
|-------|-------------|
| 🟢 Grátis | Uso gratuito relevante |
| 🟡 Freemium | Plano gratuito com limites |
| 🔵 Open source | Código ou modelo disponível para rodar por conta própria |
| 🟠 Trial | Só período de avaliação |
| 🔴 Pago | Sem opção gratuita relevante |
| ⚠️ Verificar | Condição atual ainda precisa ser confirmada |

## 1. Assistentes e modelos

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| ★ Claude | Análise, escrita, código, documentos longos | 🟡 | [claude.ai](https://claude.ai) |
| ★ ChatGPT | Uso geral, conteúdo, código, análise | 🟡 | [chatgpt.com](https://chatgpt.com) |
| ★ Gemini | Pesquisa, conteúdo, ecossistema Google | 🟡 | [gemini.google.com](https://gemini.google.com) |
| DeepSeek | Modelos de pesos abertos | 🟡 🔵 | [deepseek.com](https://www.deepseek.com) |
| Grok | Assistente da xAI | 🟡 | [grok.com](https://grok.com) |
| Meta AI | Assistente da Meta | 🟢 ⚠️ | [meta.ai](https://www.meta.ai) |

## 2. Pesquisa e estudo

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| ★ Perplexity | Pesquisa na web com fontes citadas, assuntos atuais | 🟡 | [perplexity.ai](https://www.perplexity.ai) |
| ★ NotebookLM | Estudar PDFs e documentos, perguntas sobre as fontes enviadas, consolidar e estudar documentação técnica, materiais de estudo | 🟡 | [notebooklm.google.com](https://notebooklm.google.com) |
| Obsidian | Base de conhecimento em Markdown local, com links e backlinks | 🟢 | [obsidian.md](https://obsidian.md) |

## 3. Desenvolvimento

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| ★ Claude Code | Agente de desenvolvimento: analisa repositórios, implementa, depura, documenta | 🔴 (plano pago ou API) | [claude.com/product/claude-code](https://www.claude.com/product/claude-code) |
| ★ GitHub Copilot | Autocompletar, chat e agente no VS Code e no GitHub; testes, documentação e análise de projeto | 🟡 | [github.com/features/copilot](https://github.com/features/copilot) |
| ★ Cursor | Editor com IA: agente, regras, indexação do projeto | 🟡 | [cursor.com](https://cursor.com) |
| Visual Studio Code | Editor base, com extensões de IA | 🟢 | [code.visualstudio.com](https://code.visualstudio.com) |
| OpenAI Codex | Agente de desenvolvimento da OpenAI: implementar, investigar bugs, revisar | ⚠️ (incluído em planos do ChatGPT) | [openai.com/codex](https://openai.com/codex) |
| Windsurf | Editor com IA | 🟡 | [windsurf.com](https://windsurf.com) |

### Geradores de aplicação

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Lovable | Criar aplicações e protótipos a partir de descrição | 🟡 | [lovable.dev](https://lovable.dev) |
| Bolt.new | Criar aplicações web no navegador | 🟡 | [bolt.new](https://bolt.new) |
| v0 | Gerar interfaces e aplicações (Vercel) | 🟡 | [v0.app](https://v0.app) |
| Replit | Ambiente de desenvolvimento na nuvem com agente | 🟡 | [replit.com](https://replit.com) |
| Manus | Agente de uso geral que executa tarefas | ⚠️ | [manus.im](https://manus.im) |

Exercício sugerido: criar o mesmo sistema num gerador de aplicação e no Cursor/Claude Code. Comparar a qualidade do código e refatorar o resultado.

### Modelos locais e roteadores

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Ollama | Rodar modelos abertos localmente | 🔵 | [ollama.com](https://ollama.com) |
| LM Studio | Interface para rodar modelos locais | 🟢 | [lmstudio.ai](https://lmstudio.ai) |
| OpenRouter | Uma API para acessar muitos modelos | 🟡 (pago por uso, alguns modelos grátis) | [openrouter.ai](https://openrouter.ai) |

### APIs e testes de API

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Swagger / OpenAPI | Especificar e documentar APIs | 🔵 | [swagger.io](https://swagger.io) |
| Postman | Testar APIs, collections, automação com Newman | 🟡 | [postman.com](https://www.postman.com) |
| Insomnia | Cliente de API | 🟡 | [insomnia.rest](https://insomnia.rest) |
| AssemblyAI | API de transcrição de áudio (speech-to-text) | 🟡 | [assemblyai.com](https://www.assemblyai.com) |

## 4. QA e testes

| Ferramenta | Para que serve |
|------------|----------------|
| Claude / ChatGPT / Gemini | Planejamento de testes, BDD/Gherkin, análise de requisitos, brainstorming de cenários, documentação |
| Claude Code / Copilot / Codex | Automação com Cypress, Playwright, Selenium e Robot Framework, testes de API, Page Objects, fixtures, análise de DOM, manutenção de automações |
| promptfoo, DeepEval, Ragas | Avaliação de aplicações com IA (ver Trilha IA QA) |

> A IA deve apoiar a análise, não inventar requisitos inexistentes.

## 5. Agentes e automação

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| ★ n8n | Automação visual com nodes de IA, auto-hospedável | 🔵 + nuvem paga | [n8n.io](https://n8n.io) |
| Zapier | Conectar aplicações e automatizar processos | 🟡 | [zapier.com](https://zapier.com) |
| Make | Workflows visuais entre serviços e APIs | 🟡 | [make.com](https://www.make.com) |
| Composio | Integrações prontas para agentes | ⚠️ | [composio.dev](https://composio.dev) |
| Claude Agent SDK | Construir agentes com o motor do Claude Code | API paga | [docs.claude.com](https://docs.claude.com) |
| LangChain / LangGraph | Frameworks para aplicações e agentes com LLM | 🔵 | [langchain.com](https://www.langchain.com) |
| CrewAI | Equipes de agentes com papéis | 🔵 | [crewai.com](https://www.crewai.com) |
| AutoGen | Multiagente da Microsoft (ver status do Microsoft Agent Framework) | 🔵 | [github.com/microsoft/autogen](https://github.com/microsoft/autogen) |
| MCP | Protocolo para conectar IA a ferramentas | 🔵 | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

## 6. Gestão, DevOps e observabilidade

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| GitHub | Repositório, PRs, Projects, Actions | 🟡 | [github.com](https://github.com) |
| Jira | Gestão ágil (Scrum, Kanban) | 🟡 | [atlassian.com/software/jira](https://www.atlassian.com/software/jira) |
| Trello | Kanban simples | 🟡 | [trello.com](https://trello.com) |
| Docker | Containers | 🟡 | [docker.com](https://www.docker.com) |
| Vercel | Deploy de front-end | 🟡 | [vercel.com](https://vercel.com) |
| Render | Deploy de back-end e bancos | 🟡 | [render.com](https://render.com) |
| Grafana / Prometheus | Dashboards e métricas | 🔵 | [grafana.com](https://grafana.com) |
| Playwright | Automação de testes web | 🔵 | [playwright.dev](https://playwright.dev) |
| Cypress | Automação de testes web | 🔵 | [cypress.io](https://www.cypress.io) |

## 7. Conteúdo, apresentações, documentos e carreira

> Os assistentes da seção 1 (Claude, ChatGPT, Gemini) cobrem a criação de conteúdo em texto: roteiros, artigos, posts, resumos, planejamento e ideias. As ferramentas abaixo cuidam do formato final.

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Gamma | Apresentações, documentos e páginas a partir de prompt | 🟡 | [gamma.app](https://gamma.app) |
| Canva | Apresentações, posts, currículos, diagramas, banners, thumbnails e materiais de identidade visual (com Looka) | 🟡 | [canva.com](https://www.canva.com) |
| Prezi | Apresentações visuais e não lineares, com foco em storytelling | 🟡 | [prezi.com](https://prezi.com) |
| Kickresume | Currículo e carta de apresentação | 🟡 | [kickresume.com](https://www.kickresume.com) |
| Promind | Criação de conteúdo | ⚠️ | ⚠️ confirmar site e disponibilidade |

## 8. Imagem e design

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Microsoft Designer / Image Creator | Gerar imagens a partir de prompts | 🟡 | [designer.microsoft.com](https://designer.microsoft.com) |
| Adobe Firefly | Imagem e edição generativa | 🟡 | [firefly.adobe.com](https://firefly.adobe.com) |
| Leonardo AI | Geração de imagens | 🟡 | [leonardo.ai](https://leonardo.ai) |
| Midjourney | Artes e conceitos visuais | 🔴 | [midjourney.com](https://www.midjourney.com) |
| AutoDraw | Transformar rabiscos em ilustrações | 🟢 | [autodraw.com](https://www.autodraw.com) |
| Freepik | Banco de imagens, vetores, PSD e mockups, com ferramentas de IA | 🟡 | [freepik.com](https://www.freepik.com) |
| Photopea | Editor de imagens online com camadas, compatível com PSD, alternativa a editores desktop (não é IA) | 🟢 | [photopea.com](https://www.photopea.com) |
| Looka | Logotipo e identidade visual | ⚠️ | [looka.com](https://looka.com) |

## 9. Vídeo

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Runway | Geração e edição de vídeo | 🟡 (créditos) | [runwayml.com](https://runwayml.com) |
| Veo | Geração de vídeo (Google) | ⚠️ | [deepmind.google/models/veo](https://deepmind.google/models/veo) |
| Sora | Geração de vídeo (OpenAI) | ⚠️ | [openai.com/sora](https://openai.com/sora) |
| Kling | Geração de vídeo | 🟡 | [klingai.com](https://klingai.com) |
| Pika | Geração de vídeo | 🟡 | [pika.art](https://pika.art) |
| InVideo | Roteiro → narração → clipes → vídeo | 🟡 | [invideo.io](https://invideo.io) |
| Synthesia | Vídeos com avatares | 🟡 | [synthesia.io](https://www.synthesia.io) |
| HeyGen | Vídeos com avatares | 🟡 | [heygen.com](https://www.heygen.com) |
| D-ID | Apresentadores virtuais | ⚠️ | [d-id.com](https://www.d-id.com) |
| Steve AI | Texto → vídeo e animação | 🟡 | [steve.ai](https://www.steve.ai) |
| Descript | Edição de vídeo e áudio pelo texto | 🟡 | [descript.com](https://www.descript.com) |

## 10. Voz

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| ElevenLabs | Texto para voz, narração, vozes | 🟡 | [elevenlabs.io](https://elevenlabs.io) |
| Speechify | Ouvir textos narrados | 🟡 | [speechify.com](https://speechify.com) |
| Murf | Voice-over | 🟡 | [murf.ai](https://murf.ai) |
| Lovo AI | Voz e vídeo | 🟡 | [lovo.ai](https://lovo.ai) |

## 11. Sites e produtos digitais

| Ferramenta | Para que serve | Acesso | Site |
|------------|----------------|--------|------|
| Durable | Criar sites e páginas comerciais rapidamente com IA | ⚠️ | [durable.co](https://durable.co) |
| Wix | Criar e publicar sites | 🟡 | [wix.com](https://www.wix.com) |
| HeroSpark | Páginas, produtos digitais e área de membros (não é IA) | ⚠️ | [herospark.com](https://herospark.com) |
| Printful | Impressão sob demanda e envio, integrado a lojas online (não é IA) | Paga por pedido | [printful.com](https://www.printful.com) |

## Fluxos combinando ferramentas

| Objetivo | Fluxo |
|----------|-------|
| Desenvolvimento | Requisito → Claude/ChatGPT → Claude Code/Copilot/Codex → código → testes → Git/GitHub |
| Apresentação | Claude/ChatGPT (estrutura) → Gamma (slides) → Canva → revisão → exportação |
| Conteúdo em vídeo | Claude/ChatGPT (roteiro) → ElevenLabs/Speechify (narração) → InVideo/Runway → Canva → publicação |
| Currículo | Descrição da vaga → IA revisa experiências, melhora descrições, resume competências, identifica palavras-chave da vaga e revisa português e inglês → Kickresume/Canva → **revisão humana** |
| Site | Claude/ChatGPT (conteúdo) → Durable/Wix → Canva ou gerador de imagens → publicação |
| Estampas | Gerador de imagem → Photopea/Canva (fundo, tamanho, resolução) → Printful |
| Automação de rotina | Gmail (novo e-mail) → Zapier/Make → Google Sheets (registro) → Slack (aviso) |
| Documentação | ChatGPT/Claude (README, guias, procedimentos) → NotebookLM (estudar e consolidar a documentação existente) → revisão |

## Como escolher uma ferramenta

Antes de adotar, verifique:

1. Tem plano gratuito permanente ou só período de teste?
2. Exige cartão de crédito?
3. Tem limite de créditos? Eles renovam?
4. Permite exportar no plano gratuito? Coloca marca d'água?
5. Permite uso comercial?
6. Como os dados enviados são usados (treinamento, retenção)?
7. Há limite de tamanho de arquivo ou mensal?
8. A ferramenta ainda está ativa e mantida?

### Ficha de ferramenta

Para cada ferramenta estudada a fundo, preencha:

```text
Ferramenta:
Categoria:
Objetivo:
Plano gratuito:
Plano pago:
Qualidade:
Maturidade (ativa, mantida, versão):
Pontos fortes:
Limitações:
Privacidade:
Integrações:
Quando usar:
Quando não usar:
Alternativas:
Documentação oficial:
Data da verificação:
```

> Regras: não adotar ferramenta só porque apareceu em anúncio; validar na documentação oficial; preferir aprender a **classificar e escolher** a decorar listas.
