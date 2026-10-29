# 01. Fundamentos de IA e LLM

> Antes de usar, testar ou construir com IA, entenda o que ela é e onde ela erra. Quem conhece as limitações de um LLM escreve pedidos melhores, revisa o resultado com mais critério e escolhe a ferramenta certa, seja qual for a profissão.

## Objetivos

- Entender IA, IA generativa e LLM, e como eles se relacionam.
- Entender como um modelo processa contexto e por que ele "esquece" ou "inventa".
- Conhecer as principais famílias de modelos e saber compará-las.

## Do geral para o específico

| Conceito | O que é |
|----------|---------|
| **Inteligência Artificial** | Campo amplo: sistemas que executam tarefas que exigiriam inteligência humana |
| **Machine Learning** | Subárea em que o sistema aprende padrões a partir de dados, em vez de regras escritas à mão |
| **Deep Learning** | Machine Learning com redes neurais de muitas camadas |
| **IA Generativa** | Modelos que **geram** conteúdo novo: texto, imagem, áudio, vídeo, código |
| **LLM** (Large Language Model) | Modelo generativo de texto treinado em enormes volumes de dados para prever o próximo token |

Uma linha do tempo resumida: sistemas especialistas (anos 1980) → Machine Learning estatístico (anos 2000) → Deep Learning (2012 em diante) → arquitetura Transformer (2017) → LLMs de uso geral e assistentes de chat (2022 em diante) → modelos com uso de ferramentas e agentes (2024 em diante).

Um LLM é treinado para prever a próxima palavra de uma sequência. Dessa capacidade simples surgem conversa, resumo, tradução, código e uso de ferramentas. E dela também vêm as falhas: o modelo gera o texto **mais provável**, não necessariamente o **verdadeiro**.

## Conceitos essenciais

| Conceito | O que é | Por que importa no trabalho |
|----------|---------|------------------------------|
| **Token** | Pedaço de texto que o modelo processa (em português, ~3 a 4 caracteres) | Custo, velocidade e limites são medidos em tokens |
| **Janela de contexto** | Quanto texto o modelo enxerga de uma vez: instruções + histórico + documentos + pergunta | Conversas longas e arquivos grandes disputam o mesmo espaço; o começo pode ser "esquecido" |
| **Não determinismo** | A mesma pergunta pode gerar respostas diferentes | Um teste não basta; uma resposta boa não garante a próxima |
| **Parâmetros de geração** | Ajustes como temperatura (variação) e esforço de raciocínio | Nem todo modelo expõe os mesmos: nos modelos recentes da Anthropic, a API não aceita mais `temperature`, e o ajuste disponível é o esforço (`effort`) |
| **Alucinação** | Resposta falsa com aparência de verdadeira: números, nomes, leis, funções de código | O maior risco no uso profissional. Confira sempre na fonte |
| **Data de corte** | Até quando o modelo conhece o mundo | Versões, preços, leis e APIs novas podem ser desconhecidas |
| **System prompt** | Instruções que definem papel, tom e regras do assistente | Num produto com IA, é parte da especificação |
| **Raciocínio (thinking)** | O modelo "pensa" antes de responder | Melhora tarefas com várias etapas, com mais tempo e custo |
| **Tool calling** | O modelo pede para executar uma ferramenta (consulta, cálculo, API) e usa o resultado | É assim que a IA acessa dados reais ([05](<05 - Anatomia De Um Sistema Com IA.md>)) |
| **Embeddings** | Representação numérica do significado de um texto | Base da busca semântica e do RAG ([07](<07 - RAG E Agentes Conceitos.md>)) |
| **RAG** | Buscar documentos relevantes e colocá-los no contexto antes de responder | Respostas baseadas em dados próprios, com fonte |
| **Agente** | Modelo que usa ferramentas em sequência, decidindo os próximos passos | Copilot e Claude Code em modo agente, automações ([07](<07 - RAG E Agentes Conceitos.md>)) |
| **Fine-tuning** | Treinar mais um modelo pronto com dados próprios | Raramente é o primeiro passo; prompt, contexto e RAG resolvem a maioria dos casos |
| **Memória** | O que persiste entre conversas (instruções fixas, memória do produto) | Sem memória, cada sessão começa do zero |
| **Guardrails** | Regras e filtros que impedem respostas proibidas | Cada guardrail é um requisito, e pode ser burlado ([08](<08 - Riscos E Segurança Da IA.md>)) |

> Cada trilha aprofunda esses conceitos sob um ângulo: a [Trilha IA QA](<../../02 - Trilha IA QA/01 - Estudo/03 - LLM Sob A Ótica Do Teste.md>) mostra como testá-los; a [Trilha IA DEV](<../../03 - Trilha IA DEV/01 - Estudo/05 - API E Tool Calling.md>) mostra como usá-los por API.

## Famílias de modelos para comparar

| Assistente | Empresa | Destaque |
|------------|---------|----------|
| Claude | Anthropic | Análise, escrita, código, documentos longos |
| ChatGPT | OpenAI | Uso geral, ecossistema amplo |
| Gemini | Google | Integração com o ecossistema Google, multimodal |
| Copilot | Microsoft / GitHub | Integração com Office, VS Code e GitHub |
| DeepSeek | DeepSeek | Modelos de pesos abertos |
| Perplexity | Perplexity | Pesquisa na web com fontes citadas |

> Modelos e versões mudam a cada poucos meses. Em vez de decorar "qual é o melhor", aprenda a **comparar com a sua tarefa**. Na Anthropic, a família atual é a Claude 5 (Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable 5.1): confira em [docs.claude.com](https://docs.claude.com).

## Práticas

1. **Tente quebrar um chat de IA** por 30 minutos e anote o que acontecer:
   - Faça a mesma pergunta 5 vezes. As respostas mudam?
   - Pergunte sobre algo que não existe ("qual o CNPJ da empresa Xyzabc Ltda?"). Ele inventa?
   - Pergunte a cotação do dólar hoje. Ele admite que não sabe ou chuta?
   - Converse por muito tempo e depois pergunte algo do início. Ele lembra?
   - Peça para ele ignorar as instruções dele. O que acontece?
2. Explique o que é um LLM para uma criança de 10 anos, para um gestor e para um colega técnico. Compare como a linguagem muda.
3. Faça a mesma pergunta da sua área para Claude, ChatGPT e Gemini e registre as diferenças. Repita com três tipos de tarefa (por exemplo: teste/QA, programação e documentação) e descubra qual responde melhor em cada uma.
4. Pesquise as limitações declaradas por cada fornecedor (data de corte, tamanho de contexto, política de dados).
5. Monte uma **matriz comparativa** com: qualidade, precisão, velocidade, clareza e alucinações.
6. **Desafio:** resolva o mesmo problema em cinco IAs diferentes e escreva um relatório de uma página com as conclusões, recomendando qual usar para cada tipo de tarefa, com evidências.

## Checklist de aprendizado

- [ ] Assisti ao vídeo "Intro to Large Language Models" (Andrej Karpathy)
- [ ] Sei diferenciar IA, Machine Learning, Deep Learning, IA generativa e LLM
- [ ] Sei explicar token, contexto, não determinismo e alucinação com minhas palavras
- [ ] Sei por que um modelo pode inventar um dado que não existe
- [ ] Fiz o exercício de "quebrar" um chat e anotei os comportamentos
- [ ] Comparei pelo menos três modelos na mesma tarefa
- [ ] Escrevi o relatório recomendando um modelo por tipo de tarefa
