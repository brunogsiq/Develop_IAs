# Próximos passos depois da trilha

> Você concluiu a Trilha IA Geral e a Trilha IA QA. E agora? Este arquivo organiza o que estudar, quais ferramentas priorizar, quais certificações fazer e como mostrar o que você sabe, pensando em **empregabilidade**.

> É uma avaliação de mercado, não uma pesquisa. Use como direção e **confirme olhando vagas reais** da sua região e da sua área. Reveja este plano a cada seis meses.

## Dois perfis de "QA com IA"

| Perfil | O que faz | Valor no mercado |
|--------|-----------|------------------|
| **QA que usa IA** | Usa Copilot e Claude para gerar casos, massa de teste e automação mais rápido | Está virando **o mínimo esperado**. Em pouco tempo não diferencia, só elimina quem não sabe |
| **QA de sistemas com IA** | Testa chatbots, assistentes, RAG e agentes: evals, red teaming, MCP | **Diferencial raro**: pouca gente sabe, e a demanda cresce com cada empresa que lança IA |

As duas trilhas que você concluiu cobrem os dois perfis. O passo seguinte é tornar isso **demonstrável**.

## Ferramentas em ordem de prioridade

| Prioridade | Ferramenta | Por quê | Onde está no repositório |
|-----------|------------|---------|--------------------------|
| 1 | **GitHub Copilot no VS Code** | A IA de código mais comum nas empresas, porque costuma vir no pacote Microsoft/GitHub que elas já pagam. É onde você escreve a automação | [DEV 02](<../../03 - Trilha IA DEV/01 - Estudo/02 - IDEs Com IA Cursor E Copilot.md>), [laboratório](<../02 - Laboratório/README.md>) |
| 2 | **Playwright + Playwright MCP** | A ferramenta de automação web mais pedida hoje. Com o MCP, o agente navega e ajuda a gerar testes: a ponte entre automação clássica e IA | [QA 09](<../01 - Estudo/09 - IA Como Ferramenta Do QA.md>), [DEV 04](<../../03 - Trilha IA DEV/01 - Estudo/04 - Engenharia De Software Com IA.md>) |
| 3 | **Claude (chat e Claude Code)** | Forte para analisar requisitos, desenhar casos e fazer tarefas de automação com agente. Também é usado como modelo dentro de produtos que você vai testar | [Geral 04](<../../01 - Trilha IA Geral/01 - Estudo/04 - Assistentes De IA No Dia A Dia.md>), [DEV 03](<../../03 - Trilha IA DEV/01 - Estudo/03 - Claude Code.md>) |
| 4 | **promptfoo (ou DeepEval)** | O diferencial: provar que você mede a qualidade de uma IA com números. Pouquíssimos QAs têm isso no currículo | [QA 07](<../01 - Estudo/07 - Evals Na Prática Com Promptfoo.md>) |
| 5 | **Postman** | Teste de API continua essencial, e um servidor MCP é uma API | [DEV 04](<../../03 - Trilha IA DEV/01 - Estudo/04 - Engenharia De Software Com IA.md>) |
| Baixa | ChatGPT, Gemini, Cursor | Saber usar basta. Não vale estudar a fundo como QA | [Catálogo](<../../01 - Trilha IA Geral/02 - Consulta/03 - Catálogo De Ferramentas De IA.md>) |

## O que estudar da Trilha IA DEV

Você **não** precisa da Trilha DEV inteira: front, back e banco não são o foco. Faça nesta ordem:

| # | Módulo DEV | Por que um QA precisa |
|---|------------|-----------------------|
| 1 | [01 - Fluxo Profissional](<../../03 - Trilha IA DEV/01 - Estudo/01 - Fluxo Profissional Com IA.md>) | Git, PR e CI: automação vive em pipeline |
| 2 | [02 - IDEs Com IA](<../../03 - Trilha IA DEV/01 - Estudo/02 - IDEs Com IA Cursor E Copilot.md>) | Copilot a fundo, no dia a dia da automação |
| 3 | [04 - Engenharia De Software](<../../03 - Trilha IA DEV/01 - Estudo/04 - Engenharia De Software Com IA.md>), **só a seção "Testes e QA"** | Playwright, Postman e CI |
| 4 | [05 - API E Tool Calling](<../../03 - Trilha IA DEV/01 - Estudo/05 - API E Tool Calling.md>) | Entender por dentro o que você testa |
| 5 | [06 - MCP Para Desenvolvedores](<../../03 - Trilha IA DEV/01 - Estudo/06 - MCP Para Desenvolvedores.md>) | Construir um servidor pequeno: quem constrói testa melhor |
| 6 | [08 - Agentes E Automação](<../../03 - Trilha IA DEV/01 - Estudo/08 - Agentes E Automação.md>) | Testar agentes é a próxima fronteira |

## Certificações, nesta ordem

| # | Certificação | Quando faz sentido |
|---|--------------|--------------------|
| 1 | **ISTQB CTFL** (Foundation) | Se ainda não tiver: é a base que muitos recrutadores filtram |
| 2 | **ISTQB CT-GenAI** ou **CT-AI** | Casam com a Trilha IA QA. No Brasil, ver disponibilidade no BSTQB |
| 3 | **GH-300 (GitHub Copilot)** | Rápida e prática; reforça a ferramenta nº 1 |
| 4 | Nuvem: AWS AI Practitioner, Azure AI Fundamentals ou Google Generative AI Leader | **Só se** a empresa ou as vagas que você quer pedirem. Escolha uma |

Detalhes e links: [trilhas oficiais dos fornecedores](<../../01 - Trilha IA Geral/02 - Consulta/04 - Trilhas Oficiais Dos Fornecedores.md>) e [referências de QA](<../04 - Consulta/01 - Referências.md>).

> Certificado abre a porta da triagem; o que convence na entrevista é o portfólio.

## Portfólio: o que publicar

Um repositório público, separado deste, com **dados fictícios**:

- [ ] **Automação web:** suíte Playwright com Page Objects, rodando no GitHub Actions, com relatório
- [ ] **Teste de API:** collection Postman (ou testes Playwright de API) rodando no pipeline
- [ ] **Eval de IA:** golden dataset no promptfoo contra um chatbot de exemplo (pode ser um modelo local via Ollama), com taxa de acerto e red teaming
- [ ] **MCP:** o servidor do [laboratório](<../02 - Laboratório/README.md>) com testes de API e uma seção de segurança (identidade, permissões, minimização de dados)
- [ ] **README** explicando a estratégia de teste por camada ([template](<../03 - Templates/05 - Estratégia De Teste.md>)) e onde a IA ajudou ou errou

Isso responde com algo concreto à pergunta de entrevista que mais separa candidatos: **"como você testa uma IA?"**

> Nunca use dados, nomes, prints ou bugs de projetos reais, nem caso trabalhe em uma instituição financeira do ramo bancário: tudo no portfólio deve ser fictício.

## Posicionamento

- **Título no LinkedIn e no currículo:** "QA com foco em qualidade de sistemas com IA (LLM, RAG, MCP, agentes)", e não só "uso IA no trabalho".
- **Experiências:** descreva resultados mensuráveis ("golden dataset com 50 casos, taxa de acerto de X% → Y%"), sem citar cliente.
- **Conteúdo:** um artigo curto sobre "como testar um assistente com IA" mostra domínio do assunto.

## Plano sugerido (~12 semanas, depois das trilhas)

| Semanas | Foco | Entregável |
|---------|------|------------|
| 1 a 3 | DEV 01 e 02 + Copilot a fundo | Repositório de portfólio criado, com CI |
| 4 a 6 | Playwright e Postman (DEV 04, seção de testes) | Suítes web e de API rodando no pipeline |
| 7 a 8 | promptfoo aplicado ao portfólio | Eval publicado com taxa de acerto e red teaming |
| 9 a 10 | DEV 05 e 06 | Servidor MCP próprio, testado |
| 11 a 12 | Certificação (CTFL ou CT-GenAI) + LinkedIn | Certificação marcada e perfil atualizado |

## Checklist

- [ ] Sei em qual dos dois perfis estou e qual quero alcançar
- [ ] Domino as ferramentas de prioridade 1 a 3
- [ ] Concluí os módulos da Trilha IA DEV indicados acima
- [ ] Tenho pelo menos uma certificação relevante ou uma prova marcada
- [ ] Publiquei o portfólio com automação, API, eval de IA e MCP
- [ ] Atualizei LinkedIn e currículo com o posicionamento
- [ ] Revi este plano olhando vagas reais nos últimos seis meses
