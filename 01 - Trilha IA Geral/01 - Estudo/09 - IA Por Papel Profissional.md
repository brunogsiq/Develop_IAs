# 09. IA por papel profissional

> Os módulos anteriores valem para todos. Este fecha a trilha mostrando como cada profissão usa IA no dia a dia, quais riscos são típicos de cada uma e para onde seguir depois.

## Visão geral

| Papel | IA como ferramenta de trabalho | IA como parte do produto | Próximo passo |
|-------|--------------------------------|--------------------------|---------------|
| **QA** | Gerar e revisar casos, massa de teste, apoio à automação | Testar respostas não determinísticas, evals, red teaming | [Trilha IA QA](<../../02 - Trilha IA QA/README.md>) |
| **Dev** | Programar com agentes, revisar código, documentar | Integrar modelos por API, tool calling, MCP, RAG, agentes | [Trilha IA DEV](<../../03 - Trilha IA DEV/README.md>) |
| **Arquiteto** | Comparar alternativas, revisar desenhos, escrever ADRs | Escolher modelo e fornecedor, desenhar identidade, dados e custo | Trilha IA DEV (módulos 05 a 08) + este módulo |
| **DevOps / SRE** | Escrever e depurar pipelines, IaC, analisar logs | Operar e observar aplicações com IA: custo, latência, limites, segredos | Trilha IA DEV (módulos 01, 04 e 06) |
| **PO / Analista** | Escrever histórias, achar lacunas, preparar refinamentos | Definir comportamento esperado e critérios de aceite da IA | Trilha IA QA (módulos 01, 02, 05 e template de cenários) |
| **Gestão** | Resumos, relatórios, preparação de reuniões | Avaliar riscos, custos, política de uso e capacitação do time | Módulos 02 e 08 desta trilha |

## QA

- **Usa IA para:** gerar cenários a partir de histórias, revisar critérios de aceite, criar massa de teste fictícia, apoiar a escrita de automação.
- **Testa IA:** a mesma pergunta pode dar respostas diferentes, então o resultado vira **taxa de acerto**.
- **Risco típico:** aceitar cenários gerados sem conferir se seguem a documentação.

## Desenvolvedor

- **Usa IA para:** implementar com Cursor, Copilot ou Claude Code; explicar código legado; gerar testes; revisar PRs.
- **Constrói com IA:** chamadas de API, ferramentas, servidores MCP, RAG e agentes.
- **Risco típico:** fazer merge de código que não entendeu; aceitar bibliotecas ou funções inventadas.

## Arquiteto

- **Usa IA para:** comparar alternativas com trade-offs explícitos, revisar diagramas, escrever ADRs, levantar riscos.
- **Decide sobre IA:**
  - qual modelo e fornecedor, e por onde os dados trafegam;
  - RAG, tool calling ou agente para cada necessidade ([07](<07 - RAG E Agentes Conceitos.md>));
  - identidade e permissões das ferramentas ([05](<05 - Anatomia De Um Sistema Com IA.md>));
  - custo por requisição, latência e plano de contingência quando o modelo falha.
- **Risco típico:** aceitar uma recomendação de arquitetura sem as premissas por trás dela.

## DevOps / SRE

- **Usa IA para:** escrever e depurar pipelines e Dockerfiles, Infraestrutura como Código, investigar logs e incidentes, escrever runbooks.
- **Opera IA:**
  - segredos e chaves de API fora do código;
  - limites de uso e alertas de custo;
  - observabilidade: traces de prompt, ferramentas chamadas, tokens, latência e erros;
  - logs sem dados sensíveis;
  - versionamento de prompts e modelos como parte do deploy.
- **Risco típico:** dar a um agente acesso a produção ou rodar comando gerado sem ler.

## PO / Analista de negócio

- **Usa IA para:** transformar anotações em histórias, encontrar ambiguidades, preparar perguntas de refinamento.
- **Especifica IA:** o que a IA pode e não pode responder, o tom, o que fazer quando não sabe, e o critério de aceite em forma de taxa ("acerta 95% das perguntas de câmbio").
- **Risco típico:** escrever histórias de IA sem exemplos de pergunta e resposta esperada.

## Gestão

- **Usa IA para:** resumos, relatórios executivos, preparação de reuniões.
- **Decide sobre IA:** ferramentas aprovadas, política de uso, capacitação do time, onde a IA traz ganho real e onde traz risco.
- **Risco típico:** medir adoção de IA pelo uso, e não pelo resultado e pela qualidade.

## Exercício final da trilha

Escolha o seu papel e escreva uma página respondendo:

1. Em quais três tarefas da minha semana a IA economiza tempo, e como eu confiro o resultado?
2. Qual dado do meu trabalho eu nunca posso colar numa IA não aprovada?
3. Se o meu time construísse um produto com IA, qual camada seria minha responsabilidade e qual a primeira pergunta que eu faria?

## Checklist de aprendizado

- [ ] Identifiquei como a IA aparece no meu papel: como ferramenta e como produto
- [ ] Conheço o risco típico da minha função
- [ ] Fiz o exercício final
- [ ] Escolhi a próxima trilha
