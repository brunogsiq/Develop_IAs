# Trilha de Estudo: IA Geral

> A base comum para qualquer profissão de tecnologia: desenvolvimento, arquitetura, QA, DevOps, produto ou gestão. Aqui você aprende o que é IA, como pedir bem, como um sistema com IA funciona, quais são os riscos e como usar com responsabilidade. Depois, cada profissão segue para a sua trilha.

## A ideia central

1. **A IA gera o texto mais provável, não necessariamente o verdadeiro.** Por isso ela alucina, e por isso você confere.
2. **A qualidade do resultado depende da clareza do pedido.** Pedir bem é escrever bons requisitos.
3. **Você continua responsável pelo resultado.** A IA ajuda; a decisão é sua.

## Como a trilha está organizada

```
01 - Trilha IA Geral/
├── 01 - Estudo/      01 a 09, na ordem de leitura
└── 02 - Consulta/    01 glossário · 02 referências · 03 catálogo de ferramentas · 04 trilhas oficiais
```

Cada módulo termina com um **"Checklist de aprendizado"**: troque `[ ]` por `[x]` e faça commit.

### 01. Estudo

| # | Módulo | Assunto |
|---|--------|---------|
| 01 | [Fundamentos De IA E LLM](<01 - Estudo/01 - Fundamentos De IA E LLM.md>) | IA, LLM, tokens, contexto, alucinação, famílias de modelos |
| 02 | [Uso Responsável E Privacidade](<01 - Estudo/02 - Uso Responsável E Privacidade.md>) | O que nunca colar numa IA, anonimização, LGPD, viés |
| 03 | [Engenharia De Prompt](<01 - Estudo/03 - Engenharia De Prompt.md>) | Elementos, técnicas, exemplo ruim/bom/excelente, o mesmo método por papel |
| 04 | [Assistentes De IA No Dia A Dia](<01 - Estudo/04 - Assistentes De IA No Dia A Dia.md>) | Projetos, documentos, pesquisa, comunicação, reuniões e diagramas |
| 05 | [Anatomia De Um Sistema Com IA](<01 - Estudo/05 - Anatomia De Um Sistema Com IA.md>) | O fluxo de uma pergunta, erros de decisão e de redação, quem cuida de cada camada |
| 06 | [MCP Conceitos](<01 - Estudo/06 - MCP Conceitos.md>) | O padrão que conecta IA a ferramentas: papéis, primitivas, transportes |
| 07 | [RAG E Agentes Conceitos](<01 - Estudo/07 - RAG E Agentes Conceitos.md>) | Responder com documentos e executar tarefas em várias etapas |
| 08 | [Riscos E Segurança Da IA](<01 - Estudo/08 - Riscos E Segurança Da IA.md>) | OWASP Top 10 para LLM, prompt injection, agência excessiva |
| 09 | [IA Por Papel Profissional](<01 - Estudo/09 - IA Por Papel Profissional.md>) | Dev, arquiteto, QA, DevOps, PO e gestão: uso, riscos e próximo passo |

### 02. Consulta

| Arquivo | Assunto |
|---------|---------|
| [01 - Glossário](<02 - Consulta/01 - Glossário.md>) | Termos das três trilhas |
| [02 - Referências](<02 - Consulta/02 - Referências.md>) | Cursos, documentações e normas que valem para todos |
| [03 - Catálogo De Ferramentas De IA](<02 - Consulta/03 - Catálogo De Ferramentas De IA.md>) | Ferramentas por categoria, critérios de escolha e ficha de avaliação |
| [04 - Trilhas Oficiais Dos Fornecedores](<02 - Consulta/04 - Trilhas Oficiais Dos Fornecedores.md>) | Cursos e certificações de Claude, Copilot, Cursor, AWS, Azure e Google, ligados aos módulos |

## Cronograma sugerido (~3 semanas)

| Semana | Módulos | Entregável |
|--------|---------|------------|
| 1 | 01 a 03 | Matriz comparativa de modelos, lista pessoal do que nunca colar numa IA e 5 prompts reutilizáveis da sua área |
| 2 | 04 a 06 | Um documento analisado com um assistente e o desenho do fluxo de um sistema com IA, com a camada que é sua |
| 3 | 07 a 09 | Quando usar RAG ou agente, riscos da sua função e exercício final por papel |

## Para onde seguir

| Se você é... | Siga para |
|--------------|-----------|
| QA, analista de testes, PO | [02 - Trilha IA QA](<../02 - Trilha IA QA/README.md>): testar sistemas com IA |
| Dev, arquiteto, DevOps / SRE | [03 - Trilha IA DEV](<../03 - Trilha IA DEV/README.md>): desenvolver com IA e construir aplicações com IA |
| Gestão | Os módulos 02, 08 e 09 desta trilha, e o README das outras duas para entender o que o time estuda |

## Progresso geral

- [ ] Semana 1 concluída
- [ ] Semana 2 concluída
- [ ] Semana 3 concluída
- [ ] Exercício final do módulo 09 feito

## Regras para evoluir este material

1. Manter os exemplos de prompt na progressão ruim → bom → excelente.
2. Manter tudo independente de profissão; o que for específico de teste vai para a Trilha IA QA, e o de construção para a Trilha IA DEV.
3. Validar na documentação oficial; não registrar preços, só o link oficial e a data da verificação.
4. Nunca registrar dados de cliente ou de empresa: o repositório é público. Exemplos de contexto real são sempre hipotéticos ("caso trabalhe em uma instituição financeira do ramo bancário...").
