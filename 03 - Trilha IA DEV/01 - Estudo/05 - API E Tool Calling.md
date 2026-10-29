# 05. API e tool calling

> Até aqui você usou IA por meio de produtos. Agora você vai **construir** com ela: chamar um modelo pela API, definir instruções de sistema, deixar o modelo usar ferramentas suas e controlar custo. É a base para MCP, RAG e agentes.

> Os exemplos usam Python e o SDK oficial da Anthropic. A API muda com frequência: confira sempre [docs.claude.com](https://docs.claude.com).

## Objetivos

- Fazer uma chamada à API com system prompt.
- Entender o ciclo de tool calling: o modelo pede, seu código executa, o modelo responde.
- Usar streaming, contar tokens e reduzir custo com cache.
- Escolher o modelo certo para cada tarefa.

## Preparação

```bash
pip install anthropic
```

Crie uma chave de API no console da Anthropic e defina a variável de ambiente `ANTHROPIC_API_KEY`. **Nunca** coloque a chave no código nem faça commit dela.

## 1. Primeira chamada

```python
import anthropic

client = anthropic.Anthropic()  # lê ANTHROPIC_API_KEY do ambiente

resposta = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    system="Você é um assistente técnico. Responda em português, de forma objetiva.",
    messages=[{"role": "user", "content": "O que é um middleware em uma API REST?"}],
)

for bloco in resposta.content:
    if bloco.type == "text":
        print(bloco.text)

print(resposta.usage)  # tokens de entrada e de saída
```

- `system` são as instruções fixas, o "system prompt" que você estudou na Trilha IA Geral.
- `messages` é o histórico da conversa. A API **não guarda estado**: a cada chamada você reenvia o histórico.
- `resposta.content` é uma lista de blocos (texto, uso de ferramenta, raciocínio). Verifique o tipo antes de ler.

## 2. Tool calling

Você descreve ferramentas com **nome, descrição e schema**. O modelo decide se usa e com quais parâmetros. **Quem executa é o seu código.**

```python
import anthropic

client = anthropic.Anthropic()

ferramentas = [{
    "name": "consultar_cotacao",
    "description": "Retorna a cotação atual de uma moeda em reais. Use quando o usuário perguntar o valor de uma moeda.",
    "input_schema": {
        "type": "object",
        "properties": {"moeda": {"type": "string", "description": "Código ISO, ex.: USD, EUR"}},
        "required": ["moeda"],
    },
}]

def consultar_cotacao(moeda: str) -> str:
    cotacoes = {"USD": "5,43", "EUR": "5,91"}  # dados fictícios
    return cotacoes.get(moeda, "Moeda não encontrada")

mensagens = [{"role": "user", "content": "Quanto está o dólar?"}]

while True:
    resposta = client.messages.create(
        model="claude-opus-5-5", max_tokens=16000,
        tools=ferramentas, messages=mensagens,
    )
    mensagens.append({"role": "assistant", "content": resposta.content})

    if resposta.stop_reason != "tool_use":
        break  # o modelo terminou

    resultados = []
    for bloco in resposta.content:
        if bloco.type == "tool_use":
            saida = consultar_cotacao(**bloco.input)
            resultados.append({"type": "tool_result", "tool_use_id": bloco.id, "content": saida})
    mensagens.append({"role": "user", "content": resultados})

for bloco in resposta.content:
    if bloco.type == "text":
        print(bloco.text)
```

O ciclo:

```text
Pergunta → modelo responde com tool_use (nome + parâmetros)
        → seu código executa → devolve tool_result
        → modelo redige a resposta final (stop_reason = "end_turn")
```

Pontos de atenção:
- A **descrição** da ferramenta é o que o modelo lê para decidir. Descrição vaga, escolha errada.
- Valide os parâmetros recebidos antes de executar, como em qualquer entrada externa.
- Se a ferramenta falhar, devolva o erro no `tool_result` (com `"is_error": True`) em vez de omitir.
- O SDK também tem um *tool runner* que automatiza esse laço. Escrever o laço à mão uma vez ajuda a entender o que acontece por baixo.

## 3. Streaming

Para mostrar a resposta enquanto é gerada (como num chat):

```python
with client.messages.stream(
    model="claude-opus-5-5", max_tokens=64000,
    messages=[{"role": "user", "content": "Explique CI/CD em 5 parágrafos."}],
) as stream:
    for texto in stream.text_stream:
        print(texto, end="", flush=True)
```

Use streaming também para respostas longas, para evitar timeout.

## 4. Tokens e custo

- Você paga por **tokens de entrada** (tudo o que envia, inclusive o histórico) e **de saída**.
- Conte antes de enviar:

```python
contagem = client.messages.count_tokens(
    model="claude-opus-5-5",
    messages=[{"role": "user", "content": open("README.md", encoding="utf-8").read()}],
)
print(contagem.input_tokens)
```

- **Prompt caching:** partes que se repetem em toda chamada (system prompt longo, documentos) podem ser cacheadas e ficam bem mais baratas nas chamadas seguintes:

```python
system=[{
    "type": "text",
    "text": INSTRUCOES_LONGAS,
    "cache_control": {"type": "ephemeral"},
}]
```

- **Batches:** processamento em lote, assíncrono e mais barato, para tarefas que não precisam de resposta imediata.
- Preços mudam: consulte a página oficial de preços.

### Limites e erros

- **Rate limits:** a API limita requisições e tokens por minuto, conforme o nível da conta. Ao passar do limite, ela responde **HTTP 429**, com o cabeçalho `retry-after` indicando quanto esperar.
- **Sobrecarga:** em picos, a API pode responder **529** (overloaded). Também é temporário.
- **Retry com backoff:** os SDKs oficiais já repetem automaticamente alguns erros temporários (`max_retries`). No seu código, espere cada vez mais entre as tentativas e desista depois de um limite, com uma mensagem clara ao usuário.
- **Limites do modelo:** tamanho da janela de contexto e máximo de tokens de saída (`max_tokens`). Se a resposta parar no meio, confira o `stop_reason`: `max_tokens` indica que faltou espaço.

Os valores atuais de cada limite ficam na documentação oficial (seção "Rate limits"); não os copie para cá.

## 5. Escolhendo o modelo

| Modelo (família Claude 5) | Quando usar |
|---------------------------|-------------|
| **Opus 5.5** | Padrão para a maioria das tarefas: código, agentes, análise |
| **Sonnet 5.5** | Equilíbrio entre velocidade, custo e capacidade em grande volume |
| **Haiku 5.5** | Tarefas simples e rápidas: classificação, extração, alto volume |
| **Fable 5.1** | O mais capaz, para raciocínio muito difícil e tarefas longas |

Além do modelo, os modelos atuais têm um parâmetro de **esforço** (`effort`), que equilibra profundidade de raciocínio e custo. Compare na sua tarefa antes de decidir.

## Segurança

- Chave de API em variável de ambiente ou gerenciador de segredos, nunca no repositório.
- Trate a saída do modelo como **entrada não confiável**: valide antes de executar, salvar ou renderizar como HTML.
- Ferramentas que **alteram** dados precisam de confirmação e de permissão do usuário. Veja [06 - Segurança OWASP LLM](<../../02 - Trilha IA QA/01 - Estudo/06 - Segurança OWASP LLM.md>).

## Práticas

1. Fazer a primeira chamada com um system prompt e ler o `usage`.
2. Criar um chat simples no terminal que mantém o histórico.
3. Implementar uma ferramenta (cotação, clima ou busca em um CSV) com o laço de tool calling.
4. Trocar a descrição da ferramenta por algo vago e observar o efeito.
5. Adicionar streaming.
6. Medir tokens de uma conversa longa e aplicar cache no system prompt.
7. Rodar a mesma tarefa em dois modelos e comparar qualidade, tempo e custo.
8. Simular um erro 429 (ou disparar várias chamadas seguidas) e implementar retry com backoff e mensagem de erro amigável.

## Checklist de aprendizado

- [ ] Fiz chamadas à API com system prompt
- [ ] Sei que a API não guarda o histórico e por quê
- [ ] Implementei o laço de tool calling à mão
- [ ] Usei streaming
- [ ] Sei contar tokens e aplicar prompt caching
- [ ] Sei escolher entre Opus, Sonnet, Haiku e Fable
- [ ] Minha chave de API nunca foi para o Git
