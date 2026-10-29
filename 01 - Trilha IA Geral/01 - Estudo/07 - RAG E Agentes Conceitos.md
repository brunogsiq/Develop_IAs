# 07. RAG e agentes: conceitos

> Duas técnicas aparecem em quase todo produto com IA: **RAG**, para responder com base nos documentos da empresa, e **agentes**, para executar tarefas em várias etapas. Aqui está o que todo profissional precisa entender. O teste está na [Trilha IA QA](<../../02 - Trilha IA QA/01 - Estudo/08 - Testando RAG E Agentes.md>) e a construção na [Trilha IA DEV](<../../03 - Trilha IA DEV/01 - Estudo/07 - RAG E Embeddings.md>).

## RAG (Retrieval-Augmented Generation)

O modelo não conhece os documentos internos da empresa. O RAG resolve isso **buscando** os trechos relevantes e colocando-os no contexto antes da resposta.

```text
Documentos → divididos em pedaços (chunks) → transformados em embeddings → guardados num banco vetorial
                                                                                │
Pergunta → embedding da pergunta → busca dos trechos mais parecidos ────────────┘
        → LLM responde usando só esses trechos (e cita a fonte)
```

| Conceito | O que é |
|----------|---------|
| **Chunk** | Pedaço de documento indexado |
| **Embedding** | Vetor numérico que representa o significado do texto; textos parecidos têm vetores próximos |
| **Banco vetorial** | Banco que encontra os vetores mais próximos de uma pergunta |
| **Fidelidade** | A resposta está apoiada só nos trechos recuperados, sem inventar |

### Onde o RAG falha

| Falha | Exemplo |
|-------|---------|
| Buscou o trecho errado | Pergunta sobre tarifa de 2026 traz a tabela de 2024 |
| Não buscou nada útil e o modelo inventou | Resposta confiante sem fonte |
| Documento desatualizado ou adulterado na base | A IA repete a informação errada com convicção |
| Ignorou permissões | Usuário recebe trecho de documento que não poderia abrir |

**RAG ou fine-tuning?** Para "a IA precisa saber o conteúdo dos nossos documentos", quase sempre é RAG: é mais barato, atualiza na hora e permite citar a fonte.

## Agentes

Um agente é um LLM que **escolhe e chama ferramentas em sequência** até cumprir um objetivo, decidindo sozinho o próximo passo.

```text
Objetivo → pensar → chamar ferramenta → observar o resultado → pensar → ... → resposta
```

| Conceito | O que é |
|----------|---------|
| **Trajetória** | A sequência de ferramentas que o agente chamou |
| **Autonomia** | Quanto o agente pode fazer sem pedir confirmação |
| **Human in the loop** | Pontos em que uma pessoa aprova antes de continuar |
| **Multiagente** | Vários agentes com papéis diferentes (planejador, executor, revisor) |

Exemplos que você já pode estar usando: Copilot e Cursor em modo agente, Claude Code, automações no n8n.

### Onde agentes falham

- Escolhem a ferramenta errada ou repetem a mesma em loop.
- Acertam a resposta final por um caminho errado (e vão errar na próxima vez).
- Executam uma ação que alteraria dados sem confirmação.
- Custo e tempo crescem a cada passo.

> Quanto mais autonomia, mais importante ter **logs de cada passo, limites de ação e aprovação humana** para o que altera dados.

## Quando usar o quê

| Necessidade | Solução típica |
|-------------|----------------|
| Responder com base em documentos internos | RAG |
| Consultar um dado atual (cotação, saldo, status) | Tool calling / MCP |
| Executar uma tarefa com várias etapas | Agente |
| Mudar o tom ou o formato das respostas | Prompt (não fine-tuning) |

## Checklist de aprendizado

- [ ] Sei explicar RAG em uma frase e desenhar o fluxo
- [ ] Sei o que é embedding e chunk
- [ ] Sei citar três formas de o RAG falhar
- [ ] Sei explicar o que é um agente e uma trajetória
- [ ] Sei por que ações que alteram dados precisam de aprovação humana
