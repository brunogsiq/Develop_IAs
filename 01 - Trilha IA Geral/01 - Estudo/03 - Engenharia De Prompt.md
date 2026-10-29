# 03. Engenharia de Prompt

> O módulo mais importante da trilha. A qualidade do que a IA entrega depende diretamente da clareza do que você pede. Engenharia de prompt é, no fundo, **escrever bons requisitos para uma IA**.

## Objetivos

- Formular instruções claras, sem ambiguidade.
- Estruturar contexto, restrições e formato de saída.
- Criar prompts reutilizáveis e avaliar a qualidade das respostas.
- Adaptar o mesmo prompt para ferramentas diferentes.

## Elementos de um prompt

| Elemento | Pergunta que responde | Exemplo |
|----------|----------------------|---------|
| **Papel / persona** | Quem a IA deve ser? | "Atue como QA Sênior" |
| **Objetivo** | O que deve ser entregue? | "Crie cenários de teste em BDD" |
| **Contexto** | Qual é a situação? | "Tela de login de um app bancário" |
| **Dados de entrada** | Sobre o que ela trabalha? | A história de usuário colada |
| **Restrições** | O que não pode fazer? | "Não invente regras não documentadas" |
| **Exemplos** | Como é um bom resultado? | Um cenário modelo |
| **Formato de saída** | Como entregar? | "Tabela com ID, cenário e resultado esperado" |
| **Critérios de qualidade** | Como saber se está bom? | "Cada cenário rastreável a um requisito" |
| **Revisão** | Ela deve se autoavaliar? | "Ao final, revise se algo foi assumido" |

## Como a IA lê o seu prompt

```text
Instruções do sistema (definidas pelo produto ou por você)
        ↓
Papel → Objetivo → Contexto → Restrições → Exemplos → Formato
        ↓
Resposta
```

Tudo o que não está escrito, a IA **preenche com suposições**. A principal habilidade aqui é perceber o que você sabe e ela não sabe.

## Técnicas

| Técnica | Quando usar |
|---------|-------------|
| **Zero-shot** | Tarefa simples, sem exemplo |
| **One-shot / few-shot** | Formato específico: dê 1 ou mais exemplos do resultado esperado |
| **Role prompting** | Definir o ponto de vista (QA, arquiteto, revisor) |
| **Context prompting / engenharia de contexto** | Fornecer documentos, código e regras relevantes, e só os relevantes |
| **Prompt chaining** | Quebrar uma tarefa grande em etapas: analisar → listar dúvidas → gerar → revisar |
| **Pedir raciocínio (chain of thought)** | Problemas com várias etapas lógicas. Modelos com raciocínio nativo já fazem isso sozinhos; pedir "pense passo a passo" ajuda menos neles |
| **Tree of thought / self-consistency** | Gerar várias soluções e comparar, ou pedir a mesma resposta várias vezes e ver se converge |
| **Prompt iterativo** | Melhorar o prompt a partir da resposta anterior |
| **Markdown / XML / JSON prompting** | Estruturar o prompt em seções. A Anthropic recomenda tags XML (`<documento>`, `<regras>`) para separar partes |
| **Templates reutilizáveis** | Prompts com lacunas (`{{historia}}`) para usar sempre |

> Nomes de técnicas mudam. Valide a terminologia no guia oficial: [docs.claude.com](https://docs.claude.com) (seção de prompt engineering).

## Exemplo: ruim, bom e excelente

### Ruim

```text
Faça casos de teste para login.
```

Problemas: não define contexto, objetivo, formato, papel, requisitos nem restrições. Resultado: resposta genérica.

### Bom

```text
Atue como um QA Sênior.

Crie casos de teste em BDD para uma tela de login contendo os campos E-mail e Senha.

Considere cenários positivos e negativos.
```

Melhorias: papel, objetivo, contexto mínimo, formato e escopo definidos.

### Excelente

```text
Atue como um QA Sênior especializado em Engenharia de Software,
Análise de Requisitos e Planejamento de Testes Manuais.

Analise exclusivamente a documentação fornecida.

Não invente regras, fluxos, mensagens, validações, permissões,
persistências ou comportamentos que não estejam documentados.

Caso exista alguma lacuna ou ambiguidade, registre-a como
"Ponto de Atenção".

Elabore cenários de teste em BDD utilizando:

Dado
E
Quando
Então
E

Inclua somente cenários suportados pela documentação fornecida.

Considere:

- Cenários positivos;
- Cenários negativos;
- Regras de negócio;
- Critérios de aceite;
- Obrigatoriedades documentadas;
- Navegação documentada;
- Mensagens documentadas;
- Limites documentados;
- Rastreabilidade entre requisito e cenário.

Ao final, revise todos os cenários para garantir que nenhum
comportamento não documentado tenha sido assumido.
```

### Exercício

Execute os três prompts no mesmo modelo, com a mesma história de usuário. Compare precisão, nível de detalhe, aderência ao requisito, quantidade de suposições e capacidade de reutilização. Depois repita no ChatGPT e no Gemini.

## O mesmo método em papéis diferentes

O exemplo acima é de QA, mas a estrutura (papel, objetivo, contexto, restrições, formato, revisão) vale para qualquer profissão:

| Papel | Pedido "ruim" | Pedido estruturado (resumo) |
|-------|---------------|-----------------------------|
| Desenvolvedor | "Faz uma API de usuários" | Papel de dev back-end; stack definida; endpoints e regras listados; "não adicione bibliotecas novas"; saída: código + testes + explicação |
| Arquiteto | "Qual a melhor arquitetura?" | Contexto (volume, equipe, restrições, nuvem); 2 ou 3 alternativas; critérios (custo, risco, operação); saída: tabela de trade-offs + recomendação + premissas assumidas |
| DevOps / SRE | "Arruma meu pipeline" | Log do erro colado; arquivo do workflow; "explique a causa antes de propor a correção"; saída: diagnóstico + diff mínimo |
| PO / Analista | "Escreve as histórias" | Objetivo de negócio; persona; regras conhecidas; "liste dúvidas em vez de inventar"; saída: histórias com critérios de aceite |
| Gestor | "Resume a reunião" | Anotações coladas; público do resumo; saída: decisões, pendências com responsável e prazo |

## Prompts de produtividade

Além de código e testes, crie prompts para o dia a dia:

| Categoria | Exemplo de uso |
|-----------|----------------|
| Resumo | Resumir um documento em 5 pontos com as decisões |
| Pesquisa | Comparar duas tecnologias com fontes |
| Documentação | Gerar README a partir do código |
| Programação | Implementar uma função com testes |
| Revisão | Revisar código ou texto com critérios explícitos |
| Brainstorming | Listar alternativas de solução com prós e contras |
| Tomada de decisão | Montar matriz de decisão |
| Entrevistas | Simular entrevista técnica |
| Arquitetura | Avaliar um desenho de arquitetura e seus riscos |

## Biblioteca pessoal de prompts

Monte uma biblioteca com pelo menos 20 prompts reutilizáveis, um por arquivo, registrando **quando usar** cada um. Categorias sugeridas: QA, Front-end, Back-end, SQL, Git, GitHub, Docker, DevOps, Documentação, Arquitetura, Automação, Code Review, Debug e Pesquisa.

Os prompts prontos deste repositório ficam na [wiki de prompts](<../../_Wiki/README.md>).

## Práticas

1. Criar um prompt ruim, melhorá-lo duas vezes e chegar a uma versão profissional.
2. Transformar a versão profissional em template reutilizável.
3. Reescrever o mesmo prompt em Markdown, em XML e em JSON. Comparar os resultados.
4. Adaptar o prompt para Claude, Cursor/Copilot e ChatGPT.
5. Criar a biblioteca com 20 prompts e registrar quando usar cada um.

## Checklist de aprendizado

- [ ] Sei listar os elementos de um bom prompt
- [ ] Sei quando usar zero-shot, few-shot e prompt chaining
- [ ] Executei e comparei os prompts ruim, bom e excelente
- [ ] Estruturei um prompt com tags XML
- [ ] Tenho pelo menos 20 prompts reutilizáveis na minha biblioteca
