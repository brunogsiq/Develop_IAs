# 08. Riscos e segurança da IA

> Um sistema com IA herda todos os riscos de um sistema comum e ganha novos: a IA pode ser convencida por texto, pode vazar o que viu e pode agir além do que deveria. A referência do mercado é o **OWASP Top 10 for LLM Applications** ([genai.owasp.org](https://genai.owasp.org)). Como testar cada risco está na [Trilha IA QA](<../../02 - Trilha IA QA/01 - Estudo/06 - Segurança OWASP LLM.md>).

## OWASP Top 10 for LLM Applications (edição 2025)

| Código | Risco | Em uma frase |
|--------|-------|--------------|
| LLM01 | Prompt Injection | Texto do usuário ou de um documento muda o comportamento da IA |
| LLM02 | Sensitive Information Disclosure | A IA revela dados que a pessoa não deveria ver |
| LLM03 | Supply Chain | Modelo, biblioteca ou servidor MCP de terceiros comprometido |
| LLM04 | Data and Model Poisoning | Dados de treino ou da base de RAG adulterados |
| LLM05 | Improper Output Handling | A saída da IA é usada sem validação (ex.: vira HTML ou comando) |
| LLM06 | Excessive Agency | A IA tem permissão para fazer mais do que precisa |
| LLM07 | System Prompt Leakage | As instruções internas são reveladas |
| LLM08 | Vector and Embedding Weaknesses | Falhas na base vetorial do RAG (permissões, envenenamento) |
| LLM09 | Misinformation | Alucinação tratada como fato |
| LLM10 | Unbounded Consumption | Uso sem limite: custo alto ou negação de serviço |

> Para sistemas com agentes, o OWASP publicou em dezembro de 2025 o **Top 10 for Agentic Applications** (códigos ASI01 a ASI10). Ele complementa a lista acima.

## Os conceitos que mais caem no dia a dia

### Prompt injection
- **Direta:** o usuário escreve "ignore suas instruções e...".
- **Indireta:** a instrução maliciosa está **nos dados** que a IA lê: uma página web, um e-mail, um PDF, um comentário de código, um campo de cadastro.
- Não existe filtro perfeito. A defesa real é **limitar o que a IA pode fazer** mesmo que seja enganada.

### Agência excessiva
Se a IA pode apagar, enviar, aprovar ou pagar, ela pode ser induzida a fazê-lo. Princípios:
- menor privilégio: só as ferramentas e permissões necessárias;
- confirmação humana para ações que alteram dados;
- a identidade usada é a do usuário, não a de um superusuário.

### Vazamento
Tudo o que entra no contexto (documentos, histórico, resultados de ferramentas) pode sair na resposta. Se o usuário não pode ver um dado, ele **não pode entrar no contexto** daquela conversa.

## Riscos para quem **usa** IA no trabalho

| Risco | Exemplo | Cuidado |
|-------|---------|---------|
| Vazar dados ao colar no chat | Colar planilha de clientes num assistente pessoal | Usar só ferramentas aprovadas pela empresa ([02](<02 - Uso Responsável E Privacidade.md>)) |
| Código ou comando gerado inseguro | Script com senha fixa, SQL concatenado | Revisar antes de rodar ou fazer merge |
| Agente com acesso amplo na máquina | Agente executa comando destrutivo | Permissões restritas, revisar cada ação |
| Servidor MCP ou extensão desconhecida | Extensão que lê todos os arquivos | Instalar só de fontes confiáveis |
| Pacote inventado pela IA | A IA sugere instalar uma biblioteca que não existe (e alguém pode publicá-la com código malicioso) | Conferir se o pacote existe e é o oficial |

## Por papel

| Papel | Sua responsabilidade principal |
|-------|-------------------------------|
| Dev | Validar entradas e saídas da IA, não dar à IA permissões além do necessário |
| Arquiteto | Identidade, permissões, isolamento de dados por usuário, aprovação humana |
| QA | Red teaming: tentar quebrar cada guardrail e cada permissão |
| DevOps / SRE | Segredos fora do código, limites de uso, logs sem dados sensíveis, resposta a incidentes |
| Todos | Não colar dados sensíveis em ferramentas não aprovadas |

## Checklist de aprendizado

- [ ] Li o OWASP Top 10 for LLM Applications
- [ ] Sei explicar prompt injection direta e indireta
- [ ] Sei por que "o filtro do prompt" não é controle de segurança suficiente
- [ ] Sei aplicar menor privilégio e confirmação humana a uma IA com ferramentas
- [ ] Sei os riscos de segurança de usar IA no meu próprio trabalho
