# 07. RAG e embeddings

> RAG (Retrieval-Augmented Generation) é buscar trechos relevantes dos **seus** documentos e colocá-los no contexto antes de o modelo responder. É a forma mais comum de fazer uma IA responder com base em manuais, políticas e bases de conhecimento, citando a fonte.

## Objetivos

- Entender embeddings e busca semântica.
- Montar um pipeline de RAG simples.
- Saber quando usar RAG, MCP, contexto longo ou fine-tuning.
- Avaliar a qualidade de um RAG.

## Como funciona

```text
Indexação (uma vez, ou quando os documentos mudam)
  Documentos → dividir em pedaços (chunks) → gerar embeddings → salvar no banco vetorial

Consulta (a cada pergunta)
  Pergunta → embedding da pergunta → buscar os chunks mais parecidos
          → montar o prompt (pergunta + chunks) → modelo responde citando a fonte
```

## Conceitos

| Conceito | O que é |
|----------|---------|
| **Embedding** | Vetor de números que representa o significado de um texto. Textos parecidos geram vetores próximos |
| **Chunking** | Dividir documentos em pedaços. Pedaço pequeno demais perde contexto; grande demais traz ruído |
| **Sobreposição** | Repetir um trecho entre chunks vizinhos para não cortar uma ideia ao meio |
| **Banco vetorial** | Armazena embeddings e busca por similaridade: pgvector (PostgreSQL), Chroma, Qdrant, entre outros |
| **Similaridade** | Medida de proximidade entre vetores, geralmente cosseno |
| **Busca híbrida** | Combina busca semântica com busca por palavra-chave (BM25), boa para códigos e nomes próprios |
| **Reranking** | Reordenar os resultados com um modelo mais preciso antes de mandar ao LLM |
| **Metadados** | Fonte, data, autor e permissão de cada chunk. Permitem filtrar e citar |

> A Anthropic não oferece modelo de embeddings próprio; a documentação dela recomenda provedores como a Voyage AI. Também há modelos abertos que rodam localmente.

## RAG, MCP, contexto longo ou fine-tuning?

| Abordagem | Use quando |
|-----------|------------|
| **Contexto longo** | Poucos documentos que cabem no contexto: envie tudo e use cache |
| **RAG** | Muitos documentos, conhecimento que muda, necessidade de citar a fonte |
| **MCP / tool calling** | Dados vivos e estruturados (saldo, cotação, status de pedido) consultados em sistemas |
| **Fine-tuning** | Ajustar estilo ou formato em uma tarefa muito específica; raramente é o primeiro passo |

Na prática, os três primeiros costumam ser combinados: uma tool de MCP pode ser justamente "buscar na base de conhecimento".

## Como avaliar um RAG

| Métrica | Pergunta |
|---------|----------|
| **Relevância do contexto** | Os chunks recuperados têm a ver com a pergunta? |
| **Recall do contexto** | A informação necessária estava entre os recuperados? |
| **Fidelidade** (*faithfulness*) | A resposta usa só o que está nos chunks, sem inventar? |
| **Relevância da resposta** | A resposta responde à pergunta? |
| **Citação** | A fonte citada contém mesmo a afirmação? |

Ferramentas: Ragas, DeepEval e promptfoo. A lógica é a mesma dos evals da Trilha IA QA: [05 - Como Testar IA](<../../02 - Trilha IA QA/01 - Estudo/05 - Como Testar IA.md>).

## Riscos

- **Documento desatualizado** gera resposta errada com aparência de certa.
- **Permissões:** o RAG não pode devolver trechos que o usuário não tem direito de ver. Filtre por metadados.
- **Injeção indireta:** um documento indexado pode conter instruções maliciosas.

## Práticas

1. Gerar embeddings de 10 frases e verificar quais ficam mais próximas.
2. Indexar a documentação de um projeto seu (ex.: os arquivos desta trilha) em um banco vetorial local.
3. Fazer perguntas e mostrar os chunks recuperados junto da resposta.
4. Testar tamanhos de chunk diferentes e comparar.
5. Criar 10 perguntas com resposta esperada e medir fidelidade e relevância.
6. Expor a busca como uma tool MCP.

## Checklist de aprendizado

- [ ] Sei explicar embeddings e busca semântica
- [ ] Montei um pipeline de RAG simples
- [ ] Sei escolher entre contexto longo, RAG, MCP e fine-tuning
- [ ] Medi a fidelidade das respostas
- [ ] Conheço os riscos de permissão e de injeção em RAG
