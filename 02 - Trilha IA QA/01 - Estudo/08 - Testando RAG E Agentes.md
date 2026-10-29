# 08. Testando RAG e agentes

> Dois padrões aparecem em quase todo projeto de IA depois da primeira versão: **RAG**, para responder com base em documentos (normas, manuais, políticas), e **agentes**, que encadeiam várias ferramentas sozinhos. Cada um traz falhas próprias.

## Parte 1: RAG (Retrieval-Augmented Generation)

### Como funciona

```
Pergunta do gerente
   │
   ▼
Busca na base de documentos  ──►  trechos mais parecidos com a pergunta (chunks)
   │
   ▼
LLM recebe: pergunta + trechos encontrados
   │
   ▼
Resposta baseada nos trechos (idealmente com a fonte citada)
```

Os documentos são divididos em pedaços (**chunks**) e convertidos em **embeddings** (vetores numéricos que representam o sentido do texto). A busca encontra os chunks com sentido mais próximo da pergunta, mesmo sem as mesmas palavras.

### Onde o RAG falha

| Etapa | Falha | Exemplo bancário |
|-------|-------|------------------|
| Busca | Não encontra o trecho certo | Pergunta sobre "tarifa de TED" e traz a de PIX |
| Busca | Traz trecho desatualizado | Política de 2024 em vez da de 2026 |
| Busca | Traz trecho que o usuário não poderia ver | Norma interna restrita à diretoria |
| Redação | Inventa algo que não está nos trechos | Cita um prazo que o documento não menciona |
| Redação | Mistura trechos contraditórios sem avisar | Duas versões de uma regra |
| Citação | Cita a fonte errada ou nenhuma | "Conforme o manual" sem dizer qual |

### As quatro métricas clássicas

São as métricas usadas por ferramentas como o **Ragas** (docs.ragas.io):

| Métrica | Pergunta que responde |
|---------|----------------------|
| **Faithfulness** (fidelidade) | A resposta está apoiada **só** nos trechos recuperados? |
| **Answer relevancy** (relevância da resposta) | A resposta atende à pergunta feita? |
| **Context precision** (precisão do contexto) | Os trechos recuperados são relevantes, ou há muito ruído? |
| **Context recall** (cobertura do contexto) | Os trechos recuperados contêm tudo o que era necessário? |

Para o QA, a mais importante é a **fidelidade**: num banco, uma resposta "bem escrita mas sem base no documento" é um bug grave.

### Cenários de teste de RAG

- [ ] Pergunta cuja resposta está claramente em um documento: responde e cita a fonte?
- [ ] Pergunta cuja resposta **não está** na base: diz que não encontrou ou inventa?
- [ ] Duas versões do mesmo documento: usa a vigente?
- [ ] Pergunta com sinônimos ou termos informais ("taxa do pix" × "tarifa de transferência instantânea")
- [ ] Usuário sem permissão para um documento: o conteúdo dele aparece na resposta?
- [ ] Documento com instrução escondida ("IA, ignore as regras..."): obedece? (injection indireta, arquivo 06)
- [ ] Documento atualizado hoje: a resposta reflete a mudança? Quanto tempo leva para indexar?

## Parte 2: agentes

### O que muda

Num assistente simples, a IA chama **uma** ferramenta e responde. Um agente decide uma **sequência**:

```
"Quanto o cliente 1003 pagaria em reais por US$ 2.000, e ele tem limite para isso?"
   │
   ├─► buscar_cliente(1003)
   ├─► consultar_cambio(USD)
   ├─► calcular (2.000 × cotação)
   ├─► consultar_limite_credito(1003)
   └─► responde comparando valor e limite
```

A essa sequência de passos chamamos **trajetória**. Avaliar só a resposta final não basta: o agente pode acertar a resposta por sorte, com passos errados, ou errar porque um passo do meio falhou.

### Onde o agente falha

| Falha | Exemplo |
|-------|---------|
| Ordem errada | Calcula antes de consultar a cotação |
| Passo pulado | Não verifica se o cliente é da carteira do gerente |
| Passo repetido / loop | Consulta a cotação 15 vezes |
| Erro no meio ignorado | A consulta de limite falhou e ele responde "tem limite" mesmo assim |
| Ação além do pedido | Pediu só uma simulação e ele inicia uma operação |
| Contexto perdido | No passo 4 usa dados de outro cliente |

### Cenários de teste de agentes

- [ ] A trajetória (tools chamadas, em ordem) é a esperada? Compare pelo trace.
- [ ] Cada parâmetro passado entre passos está correto (o resultado do passo 1 chega certo ao passo 2)?
- [ ] Falha em um passo do meio: o agente para, informa ou tenta de novo de forma controlada?
- [ ] Existe limite de passos? O que acontece quando é atingido?
- [ ] Ações que alteram dados pedem confirmação explícita antes?
- [ ] Rodar o mesmo pedido N vezes: a trajetória é estável?
- [ ] Custo e latência de um pedido complexo estão dentro da meta?

### Como registrar a trajetória esperada

No golden dataset, acrescente uma coluna "Trajetória esperada":

| ID | Pergunta | Trajetória esperada | Critério |
|----|----------|---------------------|----------|
| AGT-01 | Simulação de compra de US$ 2.000 para o cliente 1003 | buscar_cliente → consultar_cambio → consultar_limite_credito | Valor calculado correto, compara com o limite, não executa operação |

> Nomes de tools ilustrativos. Use os do projeto.

## Checklist de aprendizado

- [ ] Sei explicar chunk, embedding e busca por similaridade
- [ ] Sei as quatro métricas de RAG e por que fidelidade é a principal num banco
- [ ] Sei o que é a trajetória de um agente e por que avaliar só a resposta final não basta
- [ ] Escrevi 5 cenários de RAG e 5 de agentes adaptados ao projeto
- [ ] Perguntei ao time se o projeto usa (ou vai usar) RAG ou agentes
