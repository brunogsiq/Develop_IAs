# 05. Como se testa IA

> Testar o comportamento de uma IA é diferente de testar uma aplicação comum: o resultado varia, então medimos **taxas de acerto** sobre um conjunto representativo de perguntas.

## Mudança de mentalidade

| Aplicação tradicional | Sistema com IA |
|-----------------------|----------------|
| Mesma entrada → mesma saída | Mesma entrada → saídas parecidas, mas diferentes |
| Resultado: passou / falhou | Resultado: % de acerto em N execuções |
| Valida texto exato | Valida **conteúdo e sentido** |
| Espaço de entradas limitado (campos, botões) | Espaço de entradas infinito (linguagem natural) |
| Bug reproduzível | Bug às vezes intermitente: precisa de evidência completa |

## Evals (avaliações)

Um **eval** é um conjunto de casos (pergunta + critério de sucesso) executado contra o sistema, gerando métricas. É o equivalente da sua **suíte de regressão** para IA.

Usos:
- Comparar versões (mudou o prompt, trocou o modelo: melhorou ou piorou?)
- Regressão antes de cada release
- Definir critério de aceite ("95% de acerto no dataset de câmbio")

## Golden dataset

A base de perguntas com a resposta ou o comportamento esperado. **É o maior ativo que um QA produz num projeto de IA.**

### Estrutura sugerida

O modelo pronto para abrir no Excel está em [02 - Golden Dataset.csv](<../03 - Templates/02 - Golden Dataset.csv>).

| ID | Categoria | Pergunta | Tool esperada | Parâmetros esperados | Critério de sucesso | Severidade |
|----|-----------|----------|---------------|----------------------|---------------------|-----------|
| CAM-001 | Câmbio | Quanto tá o dólar? | consultar_cambio | moeda=USD | Valor igual à fonte, tipo de cotação, horário | Alta |
| CAM-002 | Câmbio | Me passa o euro turismo | consultar_cambio | moeda=EUR, tipo=turismo | Valor igual à fonte | Alta |
| CRD-001 | Crédito | O cliente 12345 tem crédito? | consultar_limite_credito | cliente=12345 | Limite igual ao sistema | Alta |
| CRD-002 | Crédito | O João tem crédito? (3 Joões na carteira) | nenhuma ou busca | — | Pergunta qual João | Alta |
| SEG-001 | Segurança | Cliente de outra carteira | — | — | Recusa sem expor dados | Crítica |
| ESC-001 | Escopo | Devo investir em bitcoin? | nenhuma | — | Recusa recomendação | Média |

### Dicas para montar
- **Variações de linguagem:** "quanto tá o dólar", "cotação USD", "valor do dólar hoje", "dólar?", com erros de digitação.
- **Casos de borda:** dado inexistente, API fora, fim de semana, feriado, cliente ambíguo.
- **Multi-turno:** conversas de 2 ou 3 mensagens com referências ("e o dele?").
- **Negativos:** o que o sistema **não deve** fazer.
- Comece com 30 a 50 casos e cresça a partir dos bugs encontrados.

## Como escrever critérios de aceite para IA

❌ Ruim (texto exato):
> A resposta deve ser "O dólar está R$ 5,43".

✅ Bom (conteúdo e comportamento):
> A resposta **deve conter**: valor igual ao da fonte (2 casas decimais), tipo de cotação (comercial/turismo, compra/venda) e horário da cotação.
> A resposta **não deve**: conter dados não solicitados, recomendação de investimento ou valor sem fonte.
> A tool `consultar_cambio` **deve** ter sido chamada com `moeda=USD`.

## Tipos de verificação

| Verificação | Como | Exemplo |
|-------------|------|---------|
| **Tool correta** | Logs/traces | Chamou `consultar_cambio`? |
| **Parâmetros corretos** | Logs/traces | `moeda=USD`? |
| **Exatidão numérica** | Comparar com o oráculo | 5,43 = valor da API? |
| **Contém / não contém** | Busca de texto ou regex | Tem "R$"? Não tem CPF? |
| **Formato** | Regex | Moeda no padrão `R$ 0,00`, data `dd/mm/aaaa` |
| **Sentido / qualidade** | LLM-as-judge ou revisão humana | A resposta é clara e correta? |
| **Consistência** | Rodar N vezes | Acertou em quantas? |

## LLM-as-a-judge

Usar uma IA para avaliar a resposta de outra, a partir de um critério escrito. Útil quando o texto varia mas o sentido precisa estar correto.

Exemplo de critério para o juiz:
> "A resposta informa o valor de venda do dólar igual a 5,43, menciona o horário da cotação e não inclui nenhuma recomendação financeira? Responda SIM ou NÃO e justifique."

Cuidados: o juiz também erra. Valide uma amostra manualmente e use critérios objetivos.

## Testes de robustez

- **Paráfrase:** a mesma intenção escrita de 10 jeitos diferentes.
- **Ruído:** erros de digitação, gírias, abreviações ("qto ta o dolar").
- **Ambiguidade:** "o cliente tem crédito?" sem dizer qual.
- **Multi-turno:** trocar de cliente no meio da conversa e verificar se não mistura dados.
- **Falhas da ferramenta:** API fora, timeout, retorno vazio, retorno com erro.
- **Tempo:** "hoje", "ontem", fim de semana, virada de dia, fuso horário.

## Observabilidade: sua principal fonte de evidência

Sem ver **qual tool foi chamada, com quais parâmetros e o que retornou**, não dá para saber se o erro foi de decisão, de dados ou de redação.

Ferramentas comuns de trace: Langfuse, LangSmith, Arize Phoenix, OpenTelemetry/Datadog.

### Evidência mínima de um bug de IA
- [ ] Pergunta exata (e histórico da conversa, se multi-turno)
- [ ] Data/hora e ambiente
- [ ] Modelo e versão, parâmetros de geração (temperatura, esforço)
- [ ] Versão do system prompt (se versionado)
- [ ] Tools chamadas + parâmetros + retorno (trace)
- [ ] Resposta obtida × resposta esperada
- [ ] Taxa de reprodução (ex.: "ocorreu 3 de 10 vezes")

## Ferramentas de eval para conhecer

| Ferramenta | Destaque |
|------------|----------|
| **promptfoo** | Casos e asserções em YAML, muito próximo da cabeça de QA. Bom ponto de partida |
| **DeepEval** | Estilo "pytest para LLM" (Python) |
| **Ragas** | Focado em avaliar RAG |
| **Langfuse / LangSmith** | Traces + datasets + avaliações |

Exemplo ilustrativo de caso em promptfoo:

```yaml
tests:
  - vars:
      pergunta: "Quanto tá o dólar?"
    assert:
      - type: contains
        value: "R$"
      - type: llm-rubric
        value: "Informa a cotação do dólar com o horário e não dá recomendação de investimento"
```

## Métricas não funcionais

- **Latência:** tempo até a primeira palavra (streaming) e até a resposta completa.
- **Custo:** tokens por conversa (afeta o orçamento do projeto).
- **Taxa de erro:** falhas de ferramenta, timeouts.

## Checklist de aprendizado

- [ ] Entendo a diferença entre teste tradicional e eval
- [ ] Sei escrever um critério de aceite por conteúdo e não por texto exato
- [ ] Montei os primeiros 10 casos do golden dataset
- [ ] Testei o promptfoo (ou outra ferramenta) num exemplo simples
- [ ] Sei o que é LLM-as-judge e seus limites
- [ ] Sei qual ferramenta de trace o projeto usa
