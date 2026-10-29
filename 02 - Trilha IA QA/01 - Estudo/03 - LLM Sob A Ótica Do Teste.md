# 03. LLM sob a ótica do teste

> Os conceitos (token, contexto, temperatura, alucinação, tool calling) estão explicados em [01 - Fundamentos De IA E LLM](<../../01 - Trilha IA Geral/01 - Estudo/01 - Fundamentos De IA E LLM.md>), na Trilha IA Geral. Aqui está o que cada um muda no seu trabalho de QA.

## Conceito → impacto no teste

### Token e janela de contexto
- Custo e limite de tamanho são medidos em tokens.
- Conversas longas podem fazer o modelo "esquecer" o começo ou misturar informações.
- **Teste:** conversas longas, troca de assunto e troca de cliente no meio da conversa.

### Não determinismo e parâmetros de geração
- A mesma pergunta pode gerar respostas diferentes, mesmo com temperatura 0.
- Nem todo modelo expõe os mesmos parâmetros: nos modelos recentes da Anthropic a API não aceita mais `temperature`, e o ajuste disponível é o esforço de raciocínio (`effort`).
- **Teste:** o resultado deixa de ser só "passou/falhou" e passa a ser **taxa de acerto** ("acertou 19 de 20 execuções"). Rode o mesmo cenário várias vezes e pergunte ao time: **quais parâmetros de geração o projeto usa e eles ficam fixos nos testes?**

### Alucinação
- É o risco número 1 num contexto bancário.
- **Teste:** compare sempre os números com a **fonte de verdade** (oráculo). Teste cenários em que o dado **não existe** ou a API **falhou**: o certo é dizer "não encontrei/não consegui", nunca inventar.

### Data de corte do conhecimento
- Se a ferramenta de câmbio não for chamada, o modelo pode "chutar" uma cotação antiga.
- **Teste:** verifique nos logs se a ferramenta foi realmente chamada.

### System prompt
- Exemplo: *"Você é um assistente para gerentes do Banco X. Nunca forneça recomendação de investimento. Sempre informe o horário da cotação."*
- **Teste:** o system prompt **é parte da especificação**. Peça para ler e transforme cada regra em casos de teste.

### Tool calling
- É o coração do sistema.
- **Teste:** a ferramenta certa é escolhida? Com os parâmetros certos? A resposta reflete fielmente o resultado?

### Agentes
- Quanto mais passos, mais pontos de falha.
- **Teste:** exija logs/traces de cada passo ([08 - Testando RAG E Agentes](<08 - Testando RAG E Agentes.md>)).

### Modelos de raciocínio
- Tendem a errar menos em perguntas com várias etapas (ex.: conversão de moeda), mas são mais lentos e mais caros.
- **Teste:** inclua latência e custo nos critérios. O raciocínio exibido também pode conter dados sensíveis.

### RAG
- **Teste:** a resposta é **fiel ao documento** e cita a fonte? ([08](<08 - Testando RAG E Agentes.md>))

### Guardrails
- **Teste:** cada guardrail é um requisito testável, inclusive tentando burlá-lo ([06 - Segurança OWASP LLM](<06 - Segurança OWASP LLM.md>)).

## Exercício prático (Semana 1)

Se ainda não fez, faça o exercício "tente quebrar um chat de IA" do [módulo 01 da Trilha Geral](<../../01 - Trilha IA Geral/01 - Estudo/01 - Fundamentos De IA E LLM.md>) e registre cada comportamento estranho na tabela "Comportamentos observados" do [03 - Registro De Execução](<../03 - Templates/03 - Registro De Execução.md>). Para cada linha, responda: **isso viraria um cenário de teste no projeto?**

## Checklist de aprendizado

- [ ] Sei explicar o impacto no teste de cada conceito acima
- [ ] Sei por que o resultado de um teste de IA é uma taxa, não um sim/não
- [ ] Sei perguntar ao time quais parâmetros de geração são usados
- [ ] Registrei os comportamentos observados e marquei quais viram cenário
