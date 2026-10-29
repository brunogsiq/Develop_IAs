# Develop_IAs

Meu repositório de estudo sobre Inteligência Artificial: uma trilha geral, comum a qualquer profissão de tecnologia, e duas trilhas específicas (testar e construir sistemas com IA), com laboratório prático e prompts reutilizáveis.

**Tudo é numerado: siga os números.** Pastas e arquivos aparecem no VS Code e no GitHub na ordem em que devem ser lidos.

## Comece aqui

| Passo | Abra | Para quem |
|-------|------|-----------|
| 1 | [01 - Trilha IA Geral](<01 - Trilha IA Geral/README.md>) | **Todos**: dev, arquiteto, QA, DevOps, PO, gestão. Fundamentos, prompt, como um sistema com IA funciona, riscos e uso responsável (~3 semanas) |
| 2a | [02 - Trilha IA QA](<02 - Trilha IA QA/README.md>) | QA, analista de testes, PO: testar sistemas com IA, LLM e MCP, com laboratório e templates (~6 semanas). Ao final, o [plano de carreira](<02 - Trilha IA QA/05 - Carreira/01 - Próximos Passos Depois Da Trilha.md>) indica o que vem depois |
| 2b | [03 - Trilha IA DEV](<03 - Trilha IA DEV/README.md>) | Dev, arquiteto, DevOps / SRE: desenvolver com IA e construir aplicações com IA, com projeto de portfólio (~16 semanas) |

Não sabe qual seguir depois da Geral? O módulo [09 - IA Por Papel Profissional](<01 - Trilha IA Geral/01 - Estudo/09 - IA Por Papel Profissional.md>) responde.

Quando precisar de algo pontual, consulte o [glossário](<01 - Trilha IA Geral/02 - Consulta/01 - Glossário.md>), as [referências](<01 - Trilha IA Geral/02 - Consulta/02 - Referências.md>), o [catálogo de ferramentas](<01 - Trilha IA Geral/02 - Consulta/03 - Catálogo De Ferramentas De IA.md>) as [trilhas oficiais dos fornecedores](<01 - Trilha IA Geral/02 - Consulta/04 - Trilhas Oficiais Dos Fornecedores.md>) (Claude, Copilot, Cursor, AWS, Azure, Google) ou a [wiki de prompts](_Wiki/README.md).

## Estrutura

```
Develop_IAs/
├── 01 - Trilha IA Geral/       ★ COMECE AQUI: a base para qualquer profissão
│   ├── 01 - Estudo/              01 a 09: fundamentos, prompt, sistemas com IA, MCP, RAG, riscos, privacidade, papéis
│   └── 02 - Consulta/            glossário, referências, catálogo de ferramentas e trilhas oficiais
├── 02 - Trilha IA QA/          testar sistemas com IA, LLM e MCP
│   ├── 01 - Estudo/              01 a 09, do mapa da jornada aos evals
│   ├── 02 - Laboratório/         prática: Copilot + MCP + servidor de câmbio
│   ├── 03 - Templates/           cenários, golden dataset, registro, perguntas, estratégia
│   ├── 04 - Consulta/            referências de QA
│   └── 05 - Carreira/            próximos passos: ferramentas, certificações e portfólio
├── 03 - Trilha IA DEV/         desenvolver com IA e construir com IA
│   ├── 01 - Estudo/              01 a 08, das IDEs com IA aos agentes
│   ├── 02 - Projeto/
│   ├── 03 - Exercícios/
│   └── 04 - Consulta/            checklist de competências
└── _Wiki/                      prompts reutilizáveis
```

| Pasta | O que tem | Status |
|-------|-----------|--------|
| [01 - Trilha IA Geral](<01 - Trilha IA Geral/README.md>) | O que é IA, como pedir bem, como funciona, riscos e uso responsável | Base |
| [02 - Trilha IA QA](<02 - Trilha IA QA/README.md>) | Como testar sistemas com IA, do conceito ao laboratório | Em andamento |
| [03 - Trilha IA DEV](<03 - Trilha IA DEV/README.md>) | Como desenvolver e construir com IA, da IDE ao agente | Próxima |
| [_Wiki](_Wiki/README.md) | Prompts prontos para reutilizar | Consulta |

### Como as trilhas se conectam

| Tema | Trilha IA Geral (entender) | Trilha IA QA (testar) | Trilha IA DEV (construir) |
|------|----------------------------|------------------------|---------------------------|
| LLM | O que é, por que varia e alucina | Taxa de acerto, oráculo | Chamar o modelo por API |
| Sistema com IA | Fluxo, camadas e quem cuida de cada uma | Tipo de teste por etapa | Laço de tool calling |
| MCP | Papéis, primitivas e transportes | Testar o servidor como API | Construir um servidor |
| RAG e agentes | Quando usar cada um e como falham | Fidelidade e trajetória | Indexar documentos e orquestrar ferramentas |
| Segurança | OWASP LLM e uso responsável | Red teaming | Validar entradas, saídas e permissões |
| IA no dia a dia | Assistentes e prompts | Gerar casos e apoiar automação | Programar com Cursor, Copilot e Claude Code |

## Como estudar no VS Code

- Em cada pasta, abra primeiro o `README.md`: ele explica o que tem ali e por onde seguir.
- `Ctrl+Shift+V` abre a visualização formatada do markdown. Os links entre arquivos funcionam no preview e no GitHub.
- Para ver os diagramas Mermaid, instale a extensão **Markdown Preview Mermaid Support**.
- Checklists: troque `- [ ]` por `- [x]` conforme avançar e faça commit. O histórico do Git vira o registro do seu progresso.

### Padrão de nomes

- Pastas e arquivos de conteúdo: `01 - Nome Do Arquivo`, número com dois dígitos, palavras iniciando com maiúscula, sem hífen entre as palavras.
- Arquivos que são executados (código, configuração, massa de dados do laboratório) mantêm o nome técnico, porque outros arquivos dependem dele: `servidor_cambio.py`, `requirements.txt`, `.vscode/mcp.json`, `dados/`.
- `README.md` e `LICENSE` mantêm o nome padrão do GitHub.
- Links para arquivos com espaço no nome usam `<>`, por exemplo: `[texto](<01 - Pasta/02 - Arquivo.md>)`.

## Regra de ouro deste repositório

Este repositório é **público**. Ele guarda só conteúdo de estudo, genérico e reaproveitável. **Nunca** entra aqui:

- nome de cliente, banco ou projeto;
- nomes reais de tools, endpoints, system prompts ou arquiteturas de clientes;
- respostas preenchidas das perguntas para o time, prints, bugs ou dados de teste reais;
- tokens, senhas, chaves ou arquivos `.env`.

## Licença

[MIT](LICENSE).
