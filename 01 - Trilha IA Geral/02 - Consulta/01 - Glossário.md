# Glossário

> Termos usados nas três trilhas, em ordem alfabética.

| Termo | Definição curta |
|-------|-----------------|
| **Agente** | LLM que chama ferramentas em sequência e decide os próximos passos sozinho |
| **Alucinação** | Informação falsa gerada com aparência de verdadeira |
| **Anonimização** | Trocar dados reais por fictícios antes de enviar a uma IA |
| **Banco vetorial** | Banco que guarda embeddings e encontra os mais parecidos com uma pergunta |
| **Chunk** | Pedaço de documento indexado para busca num sistema de RAG |
| **Context window** | Quantidade máxima de texto que o modelo enxerga de uma vez |
| **Elicitation (MCP)** | Recurso em que o servidor MCP pede uma informação ou confirmação ao usuário |
| **Embedding** | Representação numérica do sentido de um texto, usada na busca por similaridade |
| **Esforço (effort)** | Parâmetro que regula quanto o modelo raciocina antes de responder, disponível nos modelos recentes da Anthropic |
| **Eval** | Conjunto de casos de teste executados contra a IA, gerando métricas |
| **Faithfulness (fidelidade)** | Métrica de RAG: a resposta está apoiada apenas nos trechos recuperados |
| **Fine-tuning** | Treinar mais um modelo pronto com dados próprios |
| **Golden dataset** | Base de perguntas com respostas/comportamentos esperados |
| **Guardrail** | Regra ou filtro que impede comportamentos indesejados |
| **Host (MCP)** | Aplicação que o usuário usa e que contém o cliente MCP |
| **Human in the loop** | Ponto do fluxo em que uma pessoa aprova antes de a IA continuar |
| **JSON-RPC** | Formato de requisição/resposta em JSON usado pelo MCP |
| **Knowledge cutoff** | Data limite do conhecimento do modelo |
| **LGPD** | Lei Geral de Proteção de Dados (Lei 13.709/2018) |
| **LLM** | Large Language Model, modelo de linguagem de grande porte |
| **LLM-as-a-judge** | Uso de uma IA para avaliar respostas de outra |
| **MCP Client** | Componente que conversa com um servidor MCP |
| **MCP Inspector** | Ferramenta oficial para inspecionar e testar servidores MCP |
| **MCP Server** | Componente que expõe tools, resources e prompts |
| **MCP** | Model Context Protocol, padrão aberto para conectar IA a ferramentas e dados |
| **Menor privilégio** | Dar à IA só as ferramentas e permissões necessárias para a tarefa |
| **Modelo de raciocínio** | Modelo que gera um raciocínio intermediário antes da resposta final |
| **OAuth 2.1** | Padrão de autorização usado por servidores MCP remotos |
| **Ollama** | Ferramenta para rodar modelos de linguagem localmente, sem chave de API |
| **Oráculo** | Fonte de verdade usada para saber se o resultado está correto |
| **OWASP LLM Top 10** | Lista dos 10 principais riscos de segurança em aplicações com LLM (LLM01 a LLM10) |
| **Prompt injection** | Ataque que tenta sobrescrever as instruções do modelo |
| **Prompt** | Texto de entrada enviado ao modelo |
| **promptfoo** | Ferramenta open source de evals e red teaming com casos em YAML |
| **RAG** | Retrieval-Augmented Generation: buscar documentos e usá-los na resposta |
| **Red teaming** | Testar ativamente formas de fazer o sistema se comportar mal |
| **Resource (MCP)** | Dado de leitura exposto por um servidor MCP |
| **Sampling (MCP)** | Recurso em que o servidor MCP pede ao LLM do host para gerar um texto |
| **Shadow AI** | Uso de ferramentas de IA não aprovadas pela empresa |
| **Streamable HTTP** | Transporte do MCP para servidores remotos |
| **Streaming** | Exibir a resposta conforme é gerada, palavra por palavra |
| **System prompt** | Instruções ocultas que definem papel e regras da IA |
| **Temperatura** | Parâmetro de geração que controla a variação das respostas (nem todo modelo permite ajustá-lo; ver Esforço) |
| **Token** | Unidade de texto processada pelo modelo |
| **Tool (MCP)** | Ação ou consulta que o LLM pode decidir chamar |
| **Tool calling** | Mecanismo pelo qual o LLM pede a execução de uma ferramenta |
| **Trace** | Registro detalhado de cada passo (tools chamadas, parâmetros, retornos) |
| **Trajetória** | Sequência de ferramentas chamadas por um agente para cumprir um pedido |

> Termos do domínio bancário (PTAX, spread) estão em [02 - Domínio Bancário](<../../02 - Trilha IA QA/01 - Estudo/02 - Domínio Bancário.md>).
