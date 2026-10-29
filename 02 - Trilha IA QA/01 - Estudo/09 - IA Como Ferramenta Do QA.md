# 09. IA como ferramenta do QA

> Até aqui a IA foi o **objeto** do teste. Este arquivo trata da IA como **ferramenta** do seu trabalho: gerar casos, revisar critérios, apoiar a automação e escrever evidências. O mesmo olhar crítico dos arquivos anteriores vale aqui: tudo o que a IA produz precisa ser revisado.

## Antes de tudo: o que pode e o que não pode ir para uma IA

| Pode (em ferramenta aprovada pela empresa) | Não pode |
|--------------------------------------------|----------|
| Histórias de usuário e critérios de aceite, se a política da empresa permitir | Dados reais de clientes (nome, CPF, conta, saldo) |
| Código de automação do projeto, no assistente corporativo (ex.: Copilot da empresa) | Credenciais, tokens, URLs internas em ferramentas pessoais |
| Massa de teste fictícia | Prints com dados reais |
| Estrutura de telas e HTML de ambiente de teste | Documentos classificados como confidenciais |

**Regra:** use a ferramenta de IA **aprovada pelo cliente/empresa** para material do projeto. Ferramentas pessoais (incluindo contas gratuitas) só com conteúdo genérico.

## 1. Gerar casos de teste a partir de uma história

Prompt base (adapte):

```text
Você é um analista de QA sênior. A partir da história de usuário e dos critérios de aceite abaixo,
gere casos de teste em tabela com as colunas: ID, Cenário, Pré-condição, Passos, Resultado esperado, Tipo
(positivo, negativo, borda, segurança).

Regras:
- Cubra cada critério de aceite com pelo menos um caso positivo e um negativo.
- Inclua casos de borda (valores limite, campos vazios, formatos inválidos).
- Se algum critério for ambíguo, NÃO invente a regra: liste a ambiguidade numa seção "Dúvidas para o PO".

História:
<cole aqui>

Critérios de aceite:
<cole aqui>
```

O que revisar no resultado:
- [ ] Cada critério de aceite tem cobertura? (a IA costuma pular os menos óbvios)
- [ ] Algum caso testa uma regra que **não existe** na história? (alucinação)
- [ ] A seção "Dúvidas para o PO" trouxe algo útil? Frequentemente é a parte mais valiosa.

## 2. Revisar critérios de aceite

Peça para a IA encontrar ambiguidades, conflitos e lacunas:

```text
Analise os critérios de aceite abaixo como um QA. Aponte: termos ambíguos, regras conflitantes,
cenários não cobertos (erro, vazio, permissão, limite) e critérios que não são testáveis.
Não reescreva a história; só liste os problemas com uma pergunta sugerida para cada um.
```

Num projeto de IA, peça também: "quais critérios exigem avaliação estatística (eval) em vez de passou/falhou?"

## 3. Gerar massa de teste fictícia

```text
Gere 20 clientes fictícios em CSV (código, nome, CPF fictício válido no dígito verificador,
carteira, limite disponível). Inclua de propósito: 3 nomes duplicados, 2 clientes sem limite,
1 nome com acento e apóstrofo, 1 nome muito longo.
```

Confira os dígitos verificadores com um validador. A IA erra cálculos com frequência.

## 4. Apoio à automação (Cypress, Playwright, API)

| Tarefa | Como a IA ajuda | Cuidado |
|--------|-----------------|---------|
| Page Objects | Ler o DOM e propor seletores e métodos | Seletores inventados ou frágeis; valide na página real. Veja o prompt [02 - Leitura De DOM E Page Objects](<../../_Wiki/01 - Prompts/02 - Leitura De DOM E Page Objects.md>) |
| Testes de API | Gerar casos a partir do contrato OpenAPI/Swagger | Conferir status, schemas e cenários negativos |
| Refatoração | Remover duplicação, padronizar nomes | Rodar a suíte antes e depois |
| Diagnóstico de falha | Explicar stack trace e log | A explicação pode soar certa e estar errada |

### Playwright MCP

A Microsoft mantém um servidor MCP do Playwright (`@playwright/mcp`) que deixa o agente do VS Code **navegar de verdade** num navegador: abrir a página, clicar, ler a árvore de acessibilidade. É útil para explorar uma tela e gerar o rascunho de um teste. Experimente no mesmo esquema do [laboratório](<../02 - Laboratório/README.md>), adicionando ao `mcp.json`:

```json
"playwright": {
  "type": "stdio",
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

Use só em ambientes de teste, nunca logado com usuário real em produção.

## 5. Escrever bugs e evidências

```text
Reescreva o relato abaixo como um bug report com: título objetivo, ambiente, passos para reproduzir,
resultado obtido, resultado esperado, severidade sugerida e evidências necessárias.
Não invente informações que não estão no relato; marque o que faltar com [PREENCHER].
```

Para bugs de IA, use o checklist de evidência mínima do [03 - Registro De Execução](<../03 - Templates/03 - Registro De Execução.md>).

## Riscos de usar IA no trabalho de QA

- **Ilusão de cobertura:** 50 casos gerados em segundos parecem completos, mas podem repetir o óbvio e esquecer o crítico.
- **Viés de confirmação:** a IA tende a gerar casos que **passam**. Peça explicitamente casos negativos e de ataque.
- **Automação frágil:** seletores e esperas gerados sem critério quebram na primeira mudança de layout.
- **Dependência:** use a IA para acelerar, não para substituir o seu entendimento do negócio.

## Checklist de aprendizado

- [ ] Sei o que pode e o que não pode ser enviado a uma IA no contexto do projeto
- [ ] Gerei casos de teste de uma história e revisei o resultado criticamente
- [ ] Usei a IA para encontrar ambiguidades em critérios de aceite
- [ ] Gerei massa fictícia e validei os dados
- [ ] Testei o Playwright MCP ou outro apoio de automação num ambiente de estudo
