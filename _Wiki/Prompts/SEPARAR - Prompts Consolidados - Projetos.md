# Prompts Consolidados --- Projetos

> Consolidação dos prompts recuperáveis deste chat.
>
> **Regra de integridade:** este documento distingue prompts finais,
> intermediários e reconstruídos. Como a conversa já passou por
> compactação de contexto, não foi inventado texto para preencher
> trechos antigos que não permanecem integralmente disponíveis. Quando o
> texto integral não estava mais disponível, o prompt foi reconstruído a
> partir das regras e critérios preservados no contexto e está
> identificado como **RECONSTRUÍDO**.

------------------------------------------------------------------------

# Índice

1.  Validação final do projeto Cypress × Playwright × Python
2.  Auditoria Geral dos Repositórios --- Fase 01
3.  Fechamento e Validação da Fase 01
4.  Fase 02 --- Triagem e Priorização
5.  Fase 03 --- Auditoria Individual --- Lote Piloto P1
6.  Base de Conhecimento QAtrix --- Fase 5C
7.  Leitura de DOM --- versão original
8.  Leitura de DOM e Criação de Page Objects --- versão final
    consolidada

------------------------------------------------------------------------

# 1. Validação final do projeto Cypress × Playwright × Python

**Status:** RECONSTRUÍDO A PARTIR DO CONTEXTO PRESERVADO\
**Projeto:** `BusinesProduct_HRJobsAutomation`\
**Finalidade:** validar estrutura, equivalência entre as três
implementações, testes headless, documentação e preparação para
versionamento.

``` text
# VALIDAÇÃO FINAL DO PADRÃO DO PROJETO

Atue como Engenheiro de Software, QA Sênior e Auditor Técnico.

Projeto:

Y:\GitHub\QAtrix Tecnologia\Busines Product\BusinesProduct_HRJobsAutomation

O projeto possui três implementações do mesmo robô:

- Cypress
- Playwright
- Python

OBJETIVO

Realizar a validação final do padrão do projeto antes do versionamento.

A análise deve verificar:

1. Estrutura geral do projeto.
2. Correspondência entre Cypress, Playwright e Python.
3. Nomenclatura.
4. Arquivos equivalentes.
5. Arquivos específicos de framework.
6. Duplicidades injustificadas.
7. Arquivos temporários ou gerados.
8. Dependências.
9. Configurações.
10. Fixtures.
11. Support.
12. Pages / Page Objects.
13. Testes.
14. README.
15. .gitignore.
16. Segurança.
17. Execução headless.

PRINCÍPIO DE EQUIVALÊNCIA

Classifique os artefatos como:

- arquivo equivalente de negócio;
- arquivo equivalente de arquitetura;
- arquivo específico de framework.

Não crie duplicação artificial apenas para fazer as três árvores parecerem visualmente idênticas.

Quando um arquivo tiver a mesma responsabilidade funcional nas três tecnologias, seus nomes e importância devem permitir correlação imediata.

TESTES

Identifique todos os testes aplicáveis e execute-os em modo headless sempre que possível.

Para cada tecnologia registre:

- comando;
- total;
- passou;
- falhou;
- skip;
- erro de configuração;
- erro de dependência;
- duração aproximada.

Não altere testes apenas para fazê-los passar.

README

O README oficial é:

Y:\GitHub\QAtrix Tecnologia\Busines Product\BusinesProduct_HRJobsAutomation\README.md

Localize todos os demais README.md do projeto.

Compare-os com o README principal.

Todo conhecimento relevante presente exclusivamente em README secundário deve ser incorporado ao README principal antes de considerar o secundário redundante.

O README principal deve representar:

- objetivo do projeto;
- arquitetura;
- Cypress;
- Playwright;
- Python;
- instalação;
- configuração;
- execução dos robôs;
- execução dos testes;
- fixtures;
- estrutura;
- validação antes do versionamento;
- comandos reais do projeto.

Não invente comandos.

ANTI-PERDA

Antes de considerar qualquer README secundário redundante, responda:

Se este arquivo desaparecer, alguma informação útil será perdida?

Se houver dúvida:

NÃO REMOVA.

GITIGNORE

Verifique se cobre adequadamente, quando aplicável:

- node_modules;
- reports;
- screenshots;
- test-results;
- caches;
- venvs;
- arquivos temporários;
- .env;
- credenciais;
- dados pessoais.

SEGURANÇA

Não exponha valores sensíveis encontrados.

Registre somente tipo e localização segura.

CRITÉRIOS DE ACEITE

O projeto somente poderá ser considerado pronto se:

- estrutura estiver coerente;
- equivalências estiverem claras;
- não houver duplicação estrutural injustificada;
- testes obrigatórios passarem headless;
- configurações estiverem válidas;
- não houver segredo exposto;
- .gitignore estiver adequado;
- README principal estiver completo;
- documentação estiver consolidada;
- comandos documentados forem reais;
- não houver contradições relevantes.

RESULTADO

Classifique como:

- APROVADO
- APROVADO COM AJUSTES
- REPROVADO

Apresente:

1. Estrutura.
2. Matriz Cypress × Playwright × Python.
3. Testes executados.
4. Resultado headless.
5. README.
6. .gitignore.
7. Segurança.
8. Pendências.
9. Resposta final: está pronto para commit/push/versionamento?

PARE antes de:

- commit;
- push;
- tag;
- release.
```

------------------------------------------------------------------------

# 2. Auditoria Geral dos Repositórios --- Fase 01

**Status:** RECONSTRUÍDO COM ALTA FIDELIDADE A PARTIR DO CONTEXTO
PRESERVADO\
**Finalidade:** descoberta, inventário e governança antes de qualquer
auditoria profunda.

``` text
# AUDITORIA GERAL DOS REPOSITÓRIOS — FASE 01

Atue como Arquiteto de Software, Engenheiro de Qualidade, DevOps e Auditor Técnico.

Diretório central:

Y:\GitHub\Bruno Siqueira\__AUDITORIA

OBJETIVO

Executar exclusivamente a FASE 01 — DESCOBERTA E GOVERNANÇA.

Nesta fase:

- entender os diretórios;
- descobrir os repositórios Git reais;
- identificar projetos e subprojetos;
- classificar o acervo;
- criar metodologia formal;
- criar checklists reutilizáveis;
- criar inventário inicial;
- definir ordem futura de auditoria;
- estabelecer critérios objetivos;
- preparar as próximas fases.

NÃO CORRIGIR PROJETOS.

ESCOPO

Inspecione o workspace acessível e/ou Y:\GitHub.

Reconheça organizações e agrupamentos.

Não assuma que toda pasta é repositório.

Considere evidência real de Git, especialmente `.git`.

Diferencie:

- pasta de organização;
- agrupamento;
- repositório Git;
- projeto;
- subprojeto;
- workspace;
- biblioteca;
- documentação;
- experimento;
- estudo;
- arquivo histórico.

REPOSITÓRIO NÃO É PROJETO

Um repositório pode conter:

- um projeto;
- vários projetos;
- monorepo;
- frontend + backend;
- vários robôs;
- documentação;
- exercícios;
- exemplos.

Utilize IDs distintos quando necessário, como:

REP-001
PRJ-001

CHECKLISTS

Não crie um checklist universal gigante.

Crie:

1. Checklist Base.
2. Checklists especializados somente quando o acervo realmente justificar.

Possíveis especializações:

- Git;
- Segurança;
- JavaScript / Node;
- TypeScript;
- Python;
- Cypress;
- Playwright;
- Frontend;
- Backend;
- API;
- Banco;
- Testes;
- CI/CD;
- GitHub Actions;
- Azure DevOps;
- Docker;
- Estudos;
- Markdown / documentação.

Não crie dezenas de arquivos vazios.

CHECKLIST BASE

Deve contemplar:

1. Identificação.
2. Estrutura.
3. Git.
4. Documentação.
5. Dependências.
6. Configuração.
7. Segurança.
8. Build.
9. Testes.
10. Qualidade estática.
11. CI/CD.
12. Execução.
13. Manutenibilidade.

SEGURANÇA

Procure sinais de:

- passwords;
- tokens;
- API keys;
- secrets;
- cookies;
- credenciais;
- certificados;
- .env;
- dados pessoais;
- arquivos confidenciais.

NÃO reproduza segredos.

Registre:

Possível segredo detectado — requer correção.

ESTUDOS

Não avalie estudo, laboratório ou POC como se fosse produção.

Classifique conforme finalidade:

- exercício;
- laboratório;
- POC;
- estudo;
- treinamento;
- demo;
- profissional;
- pessoal;
- produto;
- biblioteca;
- documentação.

STATUS

Utilize quando aplicável:

- NÃO AUDITADO
- EM AUDITORIA
- SAUDÁVEL
- SAUDÁVEL COM AJUSTES
- REQUER CORREÇÕES
- QUEBRADO
- INCOMPLETO
- BLOQUEADO
- EXPERIMENTAL / ESTUDO
- LEGADO
- CANDIDATO A ARQUIVAMENTO
- CANDIDATO A DUPLICADO

Não exclua nada automaticamente.

SEVERIDADE

- CRÍTICO
- ALTO
- MÉDIO
- BAIXO
- MELHORIA

Não transforme preferência estética em defeito.

RESULTADO DE CHECKLIST

- PASSOU
- FALHOU
- PARCIAL
- NÃO APLICÁVEL
- NÃO VERIFICADO
- BLOQUEADO

Nunca marque PASSOU sem evidência.

EVIDÊNCIA

Toda conclusão relevante deve estar apoiada em:

- arquivo;
- diretório;
- configuração;
- comando;
- resultado;
- erro;
- teste;
- pipeline;
- trecho relevante.

ANTI-ALUCINAÇÃO

Não afirme:

- funcionalidade sem execução;
- pipeline quebrada sem evidência;
- vulnerabilidade sem verificação;
- arquivo obsoleto pelo nome;
- finalidade sem evidência;
- tecnologia apenas pela pasta;
- requisito arquitetural inventado;
- comando inventado.

Quando necessário:

NÃO VERIFICADO
REQUER ANÁLISE

READ-ONLY

NÃO:

- corrigir código;
- renomear;
- reorganizar;
- atualizar dependências;
- instalar globalmente;
- executar autofix;
- formatar;
- alterar README dos projetos;
- alterar pipeline;
- alterar .gitignore;
- commit;
- push;
- excluir;
- mover;
- arquivar.

ESTRUTURA

__AUDITORIA/
├── README.md
├── 01 - Metodologia/
│   ├── Metodologia de Auditoria.md
│   ├── Classificacao de Projetos.md
│   └── Severidade e Status.md
├── 02 - Checklists/
│   ├── 00 - Checklist Base.md
│   └── checklists especializados necessários
├── 03 - Inventario/
│   └── Inventario de Repositorios e Projetos.md
├── 04 - Auditorias/
└── 05 - Relatorios/

INVENTÁRIO

| ID | Organização | Repositório | Projeto | Caminho | Categoria | Tecnologias detectadas | Estado da auditoria | Prioridade | Observações |

Quando desconhecido:

NÃO DETERMINADO

FASES FUTURAS

FASE 01 — Descoberta e Governança
FASE 02 — Triagem
FASE 03 — Auditoria Individual
FASE 04 — Plano de Correção
FASE 05 — Correções Controladas
FASE 06 — Revalidação
FASE 07 — Encerramento

NÃO execute fases posteriores.

RELATÓRIO

Criar:

Y:\GitHub\Bruno Siqueira\__AUDITORIA\05 - Relatorios\Fase 01 - Descoberta e Governanca.md

Inclua:

1. Resumo executivo
2. Escopo realmente analisado
3. Diretórios encontrados
4. Repositórios identificados
5. Projetos identificados
6. Categorias encontradas
7. Tecnologias encontradas
8. Estrutura criada
9. Checklists criados
10. Projetos não classificados
11. Riscos
12. Inventário
13. Priorização
14. Limitações
15. Critérios de aceite
16. Recomendação para Fase 02

CONDIÇÃO DE PARADA

Ao concluir a Fase 01:

PARE.

Não inicie Fase 02 ou Fase 03.
Não corrija.
Não execute auditoria profunda.
Não faça commit/push.
Não arquive.
Não exclua.
```

------------------------------------------------------------------------

# 3. Fechamento e Validação da Fase 01

**Status:** RECONSTRUÍDO COM ALTA FIDELIDADE

``` text
# FECHAMENTO E VALIDAÇÃO DA FASE 01

A Fase 01 foi executada.

Antes de autorizar a Fase 02, faça uma validação final da documentação criada.

NÃO inicie nova fase.

1. REPOSITÓRIO × PROJETO

Confirme:

- quantidade de repositórios;
- quantidade de projetos/subprojetos identificados;
- repositórios de projeto único;
- repositórios multi-projeto;
- estruturas ainda não determinadas.

Se não houver evidência suficiente:

NÃO DETERMINADO NA FASE 01

Não invente quantidade.

2. CHECKLISTS ESPECIALIZADOS

Reavalie os checklists existentes.

Avalie necessidade real de:

- Python genérico;
- CI/CD / GitHub Actions;
- Backend/API;
- Docker/DevOps.

Crie somente se o corpus realmente justificar.

Não duplique o Checklist Base.

3. CI/CD

Confirme:

- quantidade de workflows;
- quantidade de repositórios com workflows;
- se o Checklist Base cobre suficientemente CI/CD;
- se checklist especializado é necessário.

Não execute pipeline.

Não afirme que pipeline está quebrada.

4. TECNOLOGIAS

Crie visão quantitativa:

| Tecnologia/Framework | Evidência utilizada | Repositórios detectados |

Use evidências como:

- package.json;
- requirements.txt;
- .sln;
- .csproj;
- configs Cypress;
- configs Playwright;
- workflows;
- outros manifestos reais.

Não inferir por nome de pasta.

5. FONTE DE VERDADE

Remova ou reclassifique conclusões baseadas em memória anterior.

Evidência oficial:

- filesystem;
- Git;
- manifestos;
- arquivos;
- estrutura atual.

Informações anteriores devem ser rotuladas:

Contexto externo não utilizado como evidência.

6. PRIORIZAÇÃO

Mantenha P1–P4 somente com critérios objetivos.

Não classifique apenas pela pasta pai.

7. CRITÉRIOS DE ACEITE

Apresente:

| # | Critério | Status | Evidência |

Status permitidos:

- ATENDIDO
- PARCIALMENTE ATENDIDO
- NÃO ATENDIDO

8. RECONCILIAÇÃO

Informe:

- total de organizações/agrupamentos;
- total de repositórios Git;
- total de projetos/subprojetos;
- total não determinado;
- total de checklists;
- total de tecnologias/frameworks;
- total de repositórios com CI/CD;
- total P1/P2/P3/P4.

As contagens devem reconciliar com o inventário.

9. RELATÓRIO

Atualize o relatório da Fase 01.

Não crie nova fase.

10. RESULTADO

Use somente:

- FASE 01 — APROVADA
- FASE 01 — APROVADA COM RESSALVAS
- FASE 01 — NÃO APROVADA

Justifique.

CONDIÇÃO DE PARADA

Não:

- iniciar Fase 02;
- auditar profundamente;
- executar builds;
- executar testes;
- executar pipelines;
- corrigir código;
- alterar repositórios;
- commit;
- push.
```

------------------------------------------------------------------------

# 4. Fase 02 --- Triagem e Priorização

**Status:** FINAL

``` text
# AUTORIZAÇÃO — FASE 02

A Fase 01 — Descoberta e Governança está:

# APROVADA COM RESSALVAS

Linha de base atual:

- 149 repositórios Git identificados;
- 105 em `Y:\GitHub\Bruno Siqueira`;
- 44 em `Y:\GitHub\QAtrix Tecnologia`;
- 14 repositórios confirmadamente multi-projeto;
- 5 com indício de múltiplos projetos;
- 130 ainda sem determinação precisa de projetos internos;
- 47 workflows encontrados em 31 repositórios;
- metodologia criada;
- checklists criados;
- inventário criado;
- nenhum repositório alterado;
- nenhuma auditoria profunda executada.

Autorizo exclusivamente:

# FASE 02 — TRIAGEM E PRIORIZAÇÃO

OBJETIVO

Classificar os 149 repositórios suficientemente bem para determinar:

- o que é cada repositório;
- finalidade aparente;
- estado aparente;
- risco;
- relevância;
- prioridade;
- checklist;
- ordem da Fase 03.

Não corrigir projetos.
Não executar auditoria profunda.

PRINCÍPIO

A pergunta desta fase é:

Qual é a ordem correta para auditar estes 149 repositórios?

Não responder ainda:

Está tudo funcionando?

ESCOPO

Triar individualmente os 149 repositórios.

Fonte de verdade:

- filesystem;
- .git;
- estrutura;
- configs;
- manifestos;
- README;
- workflows;
- código;
- documentação.

Não usar memória anterior como evidência.

PROFUNDIDADE

Pode ler arquivos suficientes para classificar:

- README;
- package.json;
- requirements.txt;
- pyproject.toml;
- pom.xml;
- .sln;
- .csproj;
- configs Cypress;
- configs Playwright;
- workflows;
- configurações;
- estrutura de código;
- documentação principal.

Não revisar implementação completa.

NÃO EXECUTAR

- aplicação;
- testes;
- build;
- lint;
- pipelines;
- instalação;
- atualização;
- migrations;
- scripts arbitrários.

CATEGORIAS

- PRODUTO
- PROJETO PROFISSIONAL
- CLIENTE
- AUTOMAÇÃO DE TESTES
- AUTOMAÇÃO DE PROCESSO
- FRONTEND
- BACKEND
- API
- FULLSTACK
- DEVOPS / CI-CD
- BIBLIOTECA
- PORTFÓLIO
- SITE
- ESTUDO
- TREINAMENTO
- MENTORIA
- POC
- LABORATÓRIO
- EXERCÍCIO
- DOCUMENTAÇÃO
- JOGO
- PROJETO PESSOAL
- LEGADO
- OUTRO

ESTADO APARENTE

- NÃO DETERMINADO
- ATIVO
- APARENTEMENTE COMPLETO
- APARENTEMENTE INCOMPLETO
- EM DESENVOLVIMENTO
- ESTUDO / EXPERIMENTO
- LEGADO
- POSSIVELMENTE ABANDONADO
- CANDIDATO A ARQUIVAMENTO
- CANDIDATO A DUPLICADO

APARENTEMENTE COMPLETO não significa funcional.

PRIORIDADE

P1 — CRÍTICA
P2 — ALTA
P3 — MÉDIA
P4 — BAIXA

Use evidência objetiva.

RISCO

- CRÍTICO
- ALTO
- MÉDIO
- BAIXO
- NÃO DETERMINADO

TECNOLOGIAS

Identificar somente por evidência.

CHECKLIST

Determine os aplicáveis:

- Base;
- Segurança;
- Cypress;
- Playwright;
- Selenium;
- Robot;
- .NET/NUnit;
- Node/Frontend;
- Documentação/Estudo;
- outros existentes.

Se faltar:

CHECKLIST ESPECIALIZADO A DEFINIR

SEGURANÇA

Somente triagem.

Se houver indício:

POSSÍVEL DADO SENSÍVEL — REQUER AUDITORIA FASE 03

Não exponha valores.

CI/CD

Quando presente:

CI/CD PRESENTE — REQUER VALIDAÇÃO NA FASE 03

Não execute.

MATRIZ

| ID | Repositório | Caminho | Categoria | Estado aparente | Tecnologias | Multi-projeto | CI/CD | Risco | Prioridade | Checklists | Possível duplicidade | Observações |

Todos os 149 devem aparecer.

LOTES

Agrupe para Fase 03 em lotes manejáveis, preferencialmente 5 a 10 repositórios.

TOP 10

Produza Top 10 para auditoria imediata com:

- ID;
- nome;
- prioridade;
- risco;
- justificativa;
- checklist.

CANDIDATOS

Liste separadamente:

- candidatos a arquivamento;
- candidatos a duplicidade.

Não mova nem exclua.

ANTI-ALUCINAÇÃO

Não afirme sem evidência:

- funciona;
- está quebrado;
- pipeline falha;
- teste passa;
- vulnerabilidade;
- duplicidade definitiva;
- abandono definitivo.

Use:

- APARENTA
- INDÍCIO
- NÃO DETERMINADO
- REQUER FASE 03

RELATÓRIO

Criar:

Y:\GitHub\Bruno Siqueira\__AUDITORIA\05 - Relatorios\Fase 02 - Triagem e Priorizacao.md

Atualizar:

03 - Inventario\Inventario de Repositorios e Projetos.md

CONTROLES

149 =
P1 + P2 + P3 + P4 + NÃO DETERMINADO, se necessário.

Apresente contagem por:

- categoria;
- estado;
- risco;
- tecnologia;
- CI/CD;
- multi-projeto;
- duplicidade;
- arquivamento.

CRITÉRIOS DE ACEITE

1. 149 analisados.
2. 149 reconciliados.
3. Categoria definida ou não determinada.
4. Estado aparente.
5. Prioridade.
6. Risco.
7. Tecnologia com evidência.
8. Checklist.
9. CI/CD identificado.
10. Multi-projeto sinalizado.
11. Duplicidades documentadas.
12. Arquivamento documentado.
13. Top 10.
14. Lotes.
15. Nenhuma alteração.
16. Nenhum build.
17. Nenhum teste.
18. Nenhuma pipeline.
19. Nenhum commit/push.
20. Relatório concluído.

PARE.

Não iniciar Fase 03.
```

------------------------------------------------------------------------

# 5. Fase 03 --- Auditoria Individual --- Lote Piloto P1

**Status:** FINAL

``` text
# AUTORIZAÇÃO — FASE 03

A Fase 02 — Triagem e Priorização está:

# APROVADA

Autorizo exclusivamente:

# FASE 03 — AUDITORIA INDIVIDUAL
## LOTE PILOTO P1

OBJETIVO

Auditar profundamente um pequeno lote piloto P1 e validar a metodologia.

Não auditar todos os P1 de uma vez.

SELEÇÃO

Selecionar 3 a 5 P1.

Incluir obrigatoriamente:

- `_Alephee`;
- `_GFT`;
- `_GFT_Bradesco_AtendeBra`.

Priorizar risco crítico/alto, cliente, .env, CI/CD e duplicidades.

REGRA

Agora é permitida auditoria profunda.

NÃO CORRIGIR AUTOMATICAMENTE.

POR REPOSITÓRIO

Criar auditoria individual em:

Y:\GitHub\Bruno Siqueira\__AUDITORIA\04 - Auditorias

Verificar:

- identificação;
- estrutura;
- Git;
- documentação;
- dependências;
- configuração;
- segurança;
- build;
- qualidade estática;
- testes;
- CI/CD;
- execução;
- arquitetura;
- manutenibilidade.

GIT

Verificar:

- branch;
- working tree;
- modificados;
- untracked;
- remotes;
- .gitignore;
- arquivos indevidos rastreados;
- histórico quando necessário;
- tags/releases.

Não commit/push/merge/rebase destrutivo.

SEGURANÇA

Obrigatória para P1.

Procurar:

- .env;
- passwords;
- tokens;
- API keys;
- cookies;
- connection strings;
- private keys;
- certificados;
- credenciais;
- dados pessoais;
- URLs com credenciais;
- secrets hardcoded.

Nunca reproduzir valor.

Registrar:

- arquivo;
- localização;
- tipo;
- severidade;
- recomendação.

Se segredo já foi versionado, registrar que remover apenas do arquivo atual pode ser insuficiente.

Não revogar nesta fase.

DEPENDÊNCIAS

Instalação local é permitida quando necessária.

Respeitar lockfile.

Não atualizar versões deliberadamente.

Registrar comandos.

BUILD

Executar quando aplicável.

Resultado:

- PASSOU
- FALHOU
- BLOQUEADO
- NÃO APLICÁVEL

Não corrigir para passar.

QUALIDADE ESTÁTICA

Executar quando configurado:

- lint;
- formatter check;
- typecheck;
- compilação.

Não usar autofix.

TESTES

Identificar:

- unit;
- integração;
- API;
- E2E;
- smoke;
- regressão;
- outros.

Executar quando seguro.

Preferir HEADLESS.

Registrar:

| Tipo | Comando | Total | Passou | Falhou | Skip | Resultado |

ROBÔ ≠ TESTE

Antes de executar scripts, determine se podem:

- enviar formulário;
- enviar e-mail;
- alterar sistema externo;
- criar/excluir dados;
- comprar;
- candidatar;
- acessar produção;
- disparar integração.

Se houver risco:

BLOQUEADO PARA EXECUÇÃO SEGURA

CI/CD

Analisar:

- triggers;
- branches;
- jobs;
- steps;
- versions;
- install;
- build;
- lint;
- tests;
- artifacts;
- secrets;
- deploy;
- conditions;
- dependencies;
- paths.

Não disparar pipeline remota.
Não fazer deploy.

DUPLICIDADE GFT

Comparar:

- remotes;
- histórico;
- commits;
- estrutura;
- arquivos;
- hashes;
- configs;
- testes;
- docs;
- diferenças.

Classificar:

- DUPLICADOS
- DERIVADOS
- RELACIONADOS
- INDEPENDENTES
- NÃO DETERMINADO

Não excluir.

ACHADOS

Formato:

AUD-[REPO]-001

Cada achado:

- ID;
- categoria;
- severidade;
- evidência;
- impacto;
- recomendação;
- status.

Severidade:

- CRÍTICO
- ALTO
- MÉDIO
- BAIXO
- MELHORIA

EVIDÊNCIA

Nenhuma conclusão relevante sem:

- comando;
- retorno;
- arquivo;
- trecho;
- config;
- mensagem;
- estado observado.

ESTADO FINAL

- SAUDÁVEL
- SAUDÁVEL COM AJUSTES
- REQUER CORREÇÕES
- QUEBRADO
- BLOQUEADO
- INCOMPLETO
- LEGADO

NÃO CORRIGIR

Não:

- código;
- pipeline;
- dependências;
- README;
- nomes;
- secrets;
- .gitignore;
- arquivos.

RELATÓRIO

Criar:

Y:\GitHub\Bruno Siqueira\__AUDITORIA\05 - Relatorios\Fase 03 - Lote Piloto P1.md

Inclua:

1. Escopo
2. Seleção
3. Motivo
4. Metodologia
5. Execuções
6. Resultados
7. Build
8. Testes
9. CI/CD
10. Segurança
11. Documentação
12. Estrutura
13. Dependências
14. Achados
15. Severidades
16. Bloqueios
17. Duplicidade
18. Estados finais
19. Backlog preliminar
20. Avaliação da metodologia
21. Ajustes de checklist
22. Critérios de aceite
23. Recomendação

BACKLOG

Somente documental:

| ID | Repositório | Severidade | Problema | Recomendação |

VALIDAÇÃO DA METODOLOGIA

Responder:

- checklist base suficiente?
- faltou especializado?
- redundâncias?
- itens não verificáveis?
- auditoria pesada demais?
- informação importante não prevista?
- modelo precisa mudar?

PARE ao concluir o lote.

Não auditar demais P1.
Não iniciar P2.
Não corrigir.
Não commit/push.
```

------------------------------------------------------------------------

# 6. Base de Conhecimento QAtrix --- Fase 5C

**Status:** RECONSTRUÍDO COM ALTA FIDELIDADE\
**Projeto:** `QAtrix_AbcDoTeste_TestesManuais`

``` text
# FASE 5C — VERIFICAÇÃO INDEPENDENTE DE CONSOLIDAÇÃO E ANTI-PERDA

Atue como auditor independente e adversarial.

Não trate o status CONSOLIDADO da Fase 5B como prova.

Considere-o apenas uma hipótese a ser verificada.

OBJETIVO

Responder, para cada fonte:

Se o original sair agora de `# Ver e Organizar`, todo conhecimento relevante continuará preservado, compreensível, tecnicamente adequado e rastreável na Wiki?

ESCOPO

Verificar os 197 artefatos.

Não usar amostragem.

Verificar individualmente:

- 115 consolidados;
- 1 parcial: A131;
- 28 pendentes;
- 53 históricos;
- 25 imagens.

ANTI-PERDA

Para cada original, responder:

Se este original fosse removido agora, o que seria perdido?

Respostas possíveis:

- nada relevante;
- conhecimento relevante;
- exemplo relevante;
- contexto necessário;
- informação visual;
- rastreabilidade;
- não é possível determinar.

Qualquer resposta diferente de “nada relevante” impede aprovação para quarentena ou exige bloqueio seguro.

ORIGEM → DESTINO

Verificar evidência exata de incorporação.

Quando possível, indicar:

- arquivo;
- seção;
- subtítulo;
- bloco;
- exemplo.

DESTINO → ORIGEM

Verificar proveniência e rastreabilidade reversa.

STATUS FINAIS

Use somente:

- VERIFICADO — ELEGÍVEL PARA QUARENTENA
- VERIFICADO — HISTÓRICO ELEGÍVEL PARA QUARENTENA
- NÃO ELEGÍVEL — RETRABALHO DE CONSOLIDAÇÃO
- NÃO ELEGÍVEL — PENDENTE DE VALIDAÇÃO
- NÃO ELEGÍVEL — PRESERVAR ORIGINAL
- PARCIALMENTE VERIFICADO

PARCIALMENTE VERIFICADO exige motivo concreto.

IMPORTANTE

Mesmo que elegível:

NÃO MOVER.

Movimentação pertence exclusivamente à Fase 5D e exige autorização posterior.

RETRABALHO

Não corrija automaticamente a Wiki durante a auditoria.

Se encontrar falha, crie lista:

| ID | Origem | Problema | Conhecimento faltante | Destino | Correção necessária | Severidade |

Severidade:

- CRÍTICA
- ALTA
- MÉDIA
- BAIXA

MATRIZ OBRIGATÓRIA

| ID | Origem | Estado 5B | Destino 5B | Evidência no original | Evidência no destino | Anti-perda | Rastreabilidade | Achados | Estado 5C | Pode ir para 5D? |

`Pode ir para 5D?`:

- SIM
- NÃO

RECONCILIAÇÃO

Os totais devem reconciliar exatamente os 197 artefatos.

Apresente também mudanças de classificação em relação à Fase 5B.

IMAGENS

Para todas as 25 imagens, analisar:

imagem
→ conhecimento identificado
→ abstração textual existente

Distinguir:

1. conhecimento preservado;
2. necessidade de manter o arquivo visual;
3. publicação;
4. arquivamento;
5. eventual descarte futuro.

Não confundir preservação do conhecimento com autorização para apagar imagem.

A131

Reavaliar separadamente.

A classificação conceitual de ferramentas pode estar consolidada, mas catálogo nominal de ferramentas é volátil.

Verificar política de manutenção antes de liberar.

28 PENDENTES

Revisitar sem forçar decisão.

Não inventar fonte ou licença.

53 HISTÓRICOS

Verificar individualmente.

Arquivos 0-byte não possuem conteúdo a ser inventado.

Ainda assim, verificar se preservam intenção estrutural ou histórica.

PROTEÇÃO DOS ORIGINAIS

Confirmar:

- presença;
- caminho;
- tamanho;
- hash;
- nenhuma movimentação;
- nenhuma exclusão;
- nenhuma modificação.

CONDIÇÃO DE PARADA

Ao concluir a Fase 5C:

PARE.

Não:

- mover originais;
- iniciar 5D;
- iniciar 5E;
- iniciar 5F;
- executar retrabalho automaticamente;
- apagar;
- reorganizar fontes.

Apresente o relatório para aprovação.
```

------------------------------------------------------------------------

# 7. Leitura de DOM --- versão original

**Status:** SUPERADO PELA VERSÃO FINAL\
**Origem:** arquivo `03 - Leitura de DOM e criação de Page Objects.md`

``` text
# PROJETO — LEITURA DE DOM PARA CRIAÇÃO DE PAGE OBJECTS

## 1. Objetivo

Antes de escrever qualquer teste/robô para uma plataforma nova, mapear os elementos reais do formulário (atributos id, name, placeholder, class, tipo de widget) usando o navegador de verdade — em vez de adivinhar seletores olhando só o print da tela. Só depois disso criar o Page Object.

Fluxo:

login/navegação real → leitura do DOM → Page Object → commands/testes

## 2. Tecnologia / pré-requisitos

- VS Code com GitHub Copilot Chat em modo agente.
- Browser tools:
  open_browser_page,
  navigate_page,
  click_element,
  type_in_page,
  read_page,
  screenshot_page,
  hover_element,
  drag_element.
- run_playwright_code.
- Sessão real quando autenticação for necessária.

## 3. Prompt reproduzível

Preciso mapear o formulário de candidatura da plataforma <NOME_DA_PLATAFORMA> (URL: <URL_DA_PAGINA>) para criar um Page Object de automação, seguindo este fluxo:

1. Abra a página no navegador.
2. Navegue até a tela real.
3. Leia a estrutura com read_page.
4. Execute run_playwright_code + page.evaluate() para extrair tag, type, id, name, placeholder, className e texto.
5. Inspecione outerHTML de dropdowns/comboboxes customizados.
6. Não submeta ou salve dados reais sem autorização.
7. Apresente tabela:
   campo | seletor | widget.
8. Só após confirmação crie o Page Object.

## 4. Extração

return await page.evaluate(() => {
  const form = document.querySelector('form') || document.body;
  const els = Array.from(
    form.querySelectorAll('input, select, textarea, button')
  );

  return els.map(el => ({
    tag: el.tagName,
    type: el.type || null,
    id: el.id || null,
    name: el.name || null,
    placeholder: el.placeholder || null,
    className: el.className || null,
    text: el.tagName === 'BUTTON'
      ? el.textContent.trim()
      : null
  }));
});

## 5. Widgets customizados

Inspecionar outerHTML do container para diferenciar:

- select;
- dropdown de clique;
- autocomplete;
- combobox pesquisável.

## 6. Cuidados

- não submeter formulário real;
- dropdown ≠ autocomplete;
- evitar classes geradas;
- não inventar dados;
- readonly pode representar datepicker.

## 7. Datepicker

Quando houver evidência de react-datetime, investigar:

- rdtYears;
- rdtMonths;
- rdtDays;
- rdtPrev;
- rdtNext.

`force: true` e dispatchEvent eram documentados como alternativas para casos de instabilidade, mas na versão final foram reclassificados corretamente como técnicas excepcionais de diagnóstico, e não padrão de implementação.
```

------------------------------------------------------------------------

# 8. Leitura de DOM e Criação de Page Objects --- versão final consolidada

**Status:** FINAL --- UTILIZAR ESTA VERSÃO\
**Finalidade:** padrão universal de descoberta de DOM para Cypress,
Playwright e Python.

``` text
# PROJETO — LEITURA DE DOM E CRIAÇÃO DE PAGE OBJECTS
## Padrão reutilizável para Cypress, Playwright e Python

OBJETIVO

Antes de escrever teste, robô, comando ou Page Object para nova plataforma, mapear os elementos reais da página usando navegador e DOM renderizado.

Evitar seletores baseados apenas em:

- prints;
- aparência;
- texto visual;
- posição;
- suposição;
- conhecimento prévio não confirmado.

Descobrir:

- elementos reais;
- atributos;
- significado semântico;
- HTML nativo × widget customizado;
- comportamento;
- seletor mais estável;
- equivalência Cypress/Playwright/Python.

FLUXO

Navegação real
→ leitura estrutural/acessível
→ inspeção do DOM
→ mapeamento
→ classificação de widgets
→ análise de seletores
→ mapa neutro
→ validação
→ Cypress / Playwright / Python
→ commands/actions/robô

PRINCÍPIO

Uma descoberta do DOM.
Um mapa neutro.
Três implementações equivalentes.

PAPEL

Atue como Engenheiro de Automação Sênior especializado em:

- automação web;
- DOM;
- HTML;
- acessibilidade;
- Cypress;
- Playwright;
- Python;
- Selenium quando aplicável;
- Page Object Model;
- SPAs;
- widgets customizados.

Não testar a aplicação nesta etapa.
Compreender tecnicamente a interface.

TECNOLOGIA

Conceito:

navegador automatizado + inspeção do DOM real.

Ferramentas podem incluir:

- Copilot Agent;
- Codex;
- Claude Code;
- Playwright;
- browser tools;
- MCP;
- equivalente.

Ferramentas possíveis:

open_browser_page
navigate_page
click_element
type_in_page
read_page
screenshot_page
run_playwright_code

O método não depende desses nomes.

PROMPT REUTILIZÁVEL

Preciso mapear tecnicamente a página da plataforma:

<NOME_DA_PLATAFORMA>

URL:

<URL_DA_PAGINA>

Objetivo:

criar posteriormente Page Objects equivalentes para Cypress, Playwright e Python.

Nesta etapa NÃO implemente o robô nem crie Page Objects.

1. Abra a URL.
2. Aguarde redirecionamentos.
3. Registre URL inicial/final.
4. Se houver autenticação, use sessão autorizada ou solicite intervenção.
5. Não contorne CAPTCHA/MFA/anti-bot.
6. Navegue até a tela real.
7. Leia estrutura via read_page/accessibility tree.
8. Identifique seções, headings, labels, campos, botões, forms, grupos, tabs e dialogs.
9. Execute JavaScript via run_playwright_code + page.evaluate() ou equivalente.
10. Extraia:
    - tag;
    - type;
    - id;
    - name;
    - label;
    - placeholder;
    - role;
    - aria-label;
    - aria-labelledby;
    - aria-describedby;
    - aria-expanded;
    - aria-controls;
    - aria-haspopup;
    - data-testid;
    - data-test;
    - data-cy;
    - autocomplete;
    - required;
    - disabled;
    - readonly;
    - contenteditable;
    - multiple;
    - accept;
    - href;
    - className;
    - texto relevante.
11. Não extraia valores pessoais.
12. Determine significado semântico.
13. Classifique widget.
14. Diferencie select/dropdown/autocomplete/combobox.
15. Inspecione outerHTML de customizados.
16. Detecte condicionais, modais, iframes, dialogs, abas, Shadow DOM, portals e overlays.
17. Avalie estabilidade dos seletores.
18. Gere mapa neutro.
19. Apresente tabela.
20. Liste frágeis, desconhecidos e riscos.
21. Não submeta/salve/candidate/confirme/exclua.
22. Não invente dados.
23. Não crie Page Objects ainda.
24. PARE e aguarde aprovação.

SCRIPT PRINCIPAL

return await page.evaluate(() => {

  const root =
    document.querySelector('form') ||
    document.querySelector('[role="form"]') ||
    document.body;

  const selector = [
    'input',
    'select',
    'textarea',
    'button',
    'a[href]',
    '[role="button"]',
    '[role="textbox"]',
    '[role="combobox"]',
    '[role="checkbox"]',
    '[role="radio"]',
    '[role="switch"]',
    '[role="listbox"]',
    '[contenteditable="true"]'
  ].join(',');

  const elements = Array.from(root.querySelectorAll(selector));

  function getLabel(el) {
    if (el.labels && el.labels.length) {
      return Array.from(el.labels)
        .map(label => label.innerText?.trim())
        .filter(Boolean)
        .join(' | ');
    }

    const ariaLabel = el.getAttribute('aria-label');
    if (ariaLabel) return ariaLabel;

    const labelledBy = el.getAttribute('aria-labelledby');

    if (labelledBy) {
      return labelledBy
        .split(/\s+/)
        .map(id => document.getElementById(id)?.innerText?.trim())
        .filter(Boolean)
        .join(' | ');
    }

    if (el.id) {
      const explicitLabel =
        document.querySelector(`label[for="${CSS.escape(el.id)}"]`);

      if (explicitLabel) {
        return explicitLabel.innerText?.trim() || null;
      }
    }

    return null;
  }

  return elements.map((el, index) => ({
    index,
    tag: el.tagName?.toLowerCase() || null,
    type: el.getAttribute('type'),
    id: el.id || null,
    name: el.getAttribute('name'),
    label: getLabel(el),
    placeholder: el.getAttribute('placeholder'),
    role: el.getAttribute('role'),
    ariaLabel: el.getAttribute('aria-label'),
    ariaLabelledBy: el.getAttribute('aria-labelledby'),
    ariaDescribedBy: el.getAttribute('aria-describedby'),
    ariaExpanded: el.getAttribute('aria-expanded'),
    ariaControls: el.getAttribute('aria-controls'),
    ariaHasPopup: el.getAttribute('aria-haspopup'),
    dataTestId: el.getAttribute('data-testid'),
    dataTest: el.getAttribute('data-test'),
    dataCy: el.getAttribute('data-cy'),
    autocomplete: el.getAttribute('autocomplete'),
    required:
      el.required === true ||
      el.getAttribute('aria-required') === 'true',
    disabled:
      el.disabled === true ||
      el.getAttribute('aria-disabled') === 'true',
    readOnly:
      el.readOnly === true ||
      el.hasAttribute('readonly'),
    contentEditable: el.getAttribute('contenteditable'),
    multiple: el.multiple === true,
    accept: el.getAttribute('accept'),
    href: el.getAttribute('href'),
    text:
      ['BUTTON', 'A'].includes(el.tagName)
        ? el.innerText?.trim() || null
        : null,
    className:
      typeof el.className === 'string'
        ? el.className
        : null
  }));
});

TAXONOMIA

TEXT
TEXTAREA
EMAIL
PHONE
NUMBER
PASSWORD
DATE_NATIVE
DATEPICKER
UNKNOWN_DATE_WIDGET
SELECT_NATIVE
DROPDOWN_CLICK
COMBOBOX
AUTOCOMPLETE
MULTISELECT
RADIO
CHECKBOX
TOGGLE
FILE_UPLOAD
CONTENTEDITABLE
BUTTON
LINK
UNKNOWN

SELETORES

Prioridade:

1. data-testid / data-test / data-cy estáveis;
2. id/name estáveis;
3. label / role + accessible name / aria-*;
4. atributos semânticos;
5. placeholder;
6. relação estrutural semântica;
7. classe comprovadamente estável;
8. posição somente como último recurso.

Classificar:

- ALTA
- MÉDIA
- BAIXA

Classes geradas e nth-child devem gerar alerta.

MAPA NEUTRO

Exemplo:

{
  "cidade": {
    "semanticName": "cidade",
    "label": "Cidade",
    "widget": "AUTOCOMPLETE",
    "required": true,
    "selectorStrategy": "role+accessibleName",
    "role": "combobox",
    "accessibleName": "Cidade",
    "stability": "HIGH",
    "interaction": [
      "focus",
      "type",
      "waitSuggestions",
      "selectSuggestion"
    ]
  }
}

TABELA

| Campo | Label | HTML / Role | Widget | Seletor recomendado | Estratégia | Estabilidade | Condicional | Observação |

CAMPOS CONDICIONAIS

Registrar dependência e reler DOM após revelar o campo.

MULTIETAPA

Mapear cada etapa separadamente.

Não avançar se houver risco de submissão irreversível.

IFRAME / MODAL / POPUP / SHADOW DOM

Identificar explicitamente e registrar contexto.

FILE UPLOAD

Registrar:

- input file;
- accept;
- multiple;
- hidden;
- botão associado;
- comportamento.

READONLY

Não usar type/fill automaticamente.

Investigar se é:

- datepicker;
- autocomplete controlado;
- calculado;
- informativo;
- modal;
- customizado.

DATEPICKER

Classificar:

- DATE_NATIVE
- DATEPICKER
- UNKNOWN_DATE_WIDGET

Se houver evidência de react-datetime, investigar rdtYears/rdtMonths/rdtDays/rdtPrev/rdtNext.

Não aplicar comportamento de uma biblioteca a outra sem evidência.

FORCE / DISPATCHEVENT

`force: true` não é padrão.

`dispatchEvent()` é técnica excepcional de diagnóstico.

Antes de contornar actionability, investigar:

- animação;
- overlay;
- elemento incorreto;
- loading;
- rerender;
- layout instável.

SEGURANÇA

Não:

- enviar;
- salvar;
- confirmar;
- candidatar;
- finalizar;
- excluir;
- publicar.

Não inventar dados pessoais/profissionais.

PAGE OBJECTS

Somente após aprovação do mapa neutro.

Cypress, Playwright e Python devem preservar a mesma responsabilidade conceitual.

Exemplo:

Cypress: nomeCompleto
Playwright: nomeCompleto
Python: nome_completo

SEPARAÇÃO

Page Object representa elementos.

Interação complexa pode pertencer a:

- commands;
- actions;
- services;
- helpers;
- flows;

conforme arquitetura existente.

ANTI-ALUCINAÇÃO

Não afirmar sem evidência:

- widget;
- texto livre;
- estabilidade;
- comportamento de botão;
- preenchimento concluído.

Quando insuficiente:

NÃO DETERMINADO

SAÍDA

1. Resumo
2. URL inicial
3. URL final
4. Redirecionamentos
5. Estrutura
6. Formulários
7. Campos
8. Widgets
9. Customizados
10. Condicionais
11. Multietapa
12. Iframes
13. Modais
14. Popups
15. Uploads
16. Readonly
17. Datepickers
18. Mapa neutro
19. Seletores
20. Estabilidade
21. Frágeis
22. Não determinados
23. Riscos
24. Recomendações
25. Status

Status:

- MAPEAMENTO COMPLETO
- MAPEAMENTO PARCIAL
- BLOQUEADO

CONDIÇÃO DE PARADA

Ao concluir o mapa neutro:

PARE.

Não criar Page Object, command, fluxo ou submissão.

Aguardar:

“Mapeamento aprovado. Pode gerar os Page Objects.”

PRINCÍPIO FINAL

DOM REAL
→ MAPA NEUTRO VALIDADO
→ PAGE OBJECTS

O objetivo é reduzir divergência, duplicação, seletores inventados e manutenção desnecessária, aumentando rastreabilidade, reutilização, estabilidade e padronização.
```

------------------------------------------------------------------------

# Observações de integridade desta consolidação

## Prompts finais recomendados

Para uso atual, priorize:

-   **Fase 02 --- Triagem e Priorização**: já executado, mantido como
    histórico/metodologia.
-   **Fase 03 --- Lote Piloto P1**: próximo prompt da auditoria geral.
-   **Leitura de DOM e Criação de Page Objects --- versão final
    consolidada**: versão recomendada para novos projetos de automação.
-   **Fase 5C**: somente para o projeto específico da base de
    conhecimento QAtrix, enquanto essa fase permanecer vigente.

## Prompts superados

A versão original de leitura de DOM foi mantida apenas para
rastreabilidade.

Não deve ser preferida à versão final consolidada.

## Prompts reconstruídos

Alguns prompts antigos já não estavam integralmente presentes no
contexto após a compactação da conversa.

Eles foram reconstruídos somente a partir das regras preservadas no
contexto, sem preencher lacunas com fatos inventados.

Se futuramente o texto original desses prompts for localizado em
arquivo, ele deve substituir a versão reconstruída deste documento.
