# Perguntas para o time

> Estas perguntas preenchem as lacunas do projeto e já viram insumo para a estratégia de teste.

> [!WARNING]
> Este repositório é público. **Não preencha as respostas aqui.** Copie o arquivo para os canais do projeto (Confluence, SharePoint, OneDrive corporativo) e anote lá. As respostas descrevem a arquitetura e a segurança do cliente.

## Modelo de IA

- [ ] Qual LLM e qual versão?
  - Resposta:
- [ ] Quais parâmetros de geração são usados (temperatura, nível de esforço/raciocínio)? Ficam fixos nos ambientes de teste?
  - Resposta:
- [ ] Posso ler o system prompt? Ele é versionado?
  - Resposta:
- [ ] Onde o modelo roda (nuvem do provedor, nuvem do banco, on-premise)?
  - Resposta:

## MCP e ferramentas

- [ ] Quais tools o MCP expõe? Posso ver nome, descrição e schema?
  - Resposta:
- [ ] O MCP só **lê** ou também **executa ações**?
  - Resposta:
- [ ] Qual transporte (stdio ou HTTP)? Posso acessar via MCP Inspector em ambiente de teste?
  - Resposta:
- [ ] Qual é a fonte de verdade de cada dado (qual API de câmbio, qual sistema de crédito)?
  - Resposta:

## Segurança e permissões

- [ ] As chamadas ao MCP usam o token do **gerente logado** ou um **usuário de serviço**?
  - Resposta:
- [ ] Como é garantido que o gerente só vê clientes da carteira dele?
  - Resposta:
- [ ] Existem guardrails além do prompt (filtros, validações em código)?
  - Resposta:

## Comportamento esperado

- [ ] Qual cotação é a padrão quando o gerente não especifica?
  - Resposta:
- [ ] O que fazer quando o cliente é ambíguo?
  - Resposta:
- [ ] O que fazer quando uma API falha ou não há dado?
  - Resposta:
- [ ] Quais assuntos estão fora de escopo?
  - Resposta:
- [ ] Idioma das respostas?
  - Resposta:

## Ambiente e dados de teste

- [ ] Existe massa de teste (clientes fictícios, carteiras, limites)?
  - Resposta:
- [ ] Existem mocks das APIs (para simular falhas, fim de semana etc.)?
  - Resposta:
- [ ] Quais ambientes existem (dev, QA, homologação)?
  - Resposta:

## Observabilidade e evidência

- [ ] Terei acesso a logs/traces das chamadas de tool? Em qual ferramenta?
  - Resposta:
- [ ] Os logs registram dados sensíveis? Como são mascarados?
  - Resposta:

## Qualidade e critérios

- [ ] Existe meta de acerto (ex.: 95% no golden dataset)?
  - Resposta:
- [ ] Existe meta de latência?
  - Resposta:
- [ ] Haverá ferramenta de eval automatizada? Quem mantém o dataset?
  - Resposta:

## Compliance

- [ ] Dados de clientes saem do ambiente do banco para o provedor do LLM?
  - Resposta:
- [ ] Por quanto tempo o histórico de conversa é armazenado?
  - Resposta:
- [ ] Existe trilha de auditoria (quem perguntou o quê, sobre qual cliente)?
  - Resposta:
