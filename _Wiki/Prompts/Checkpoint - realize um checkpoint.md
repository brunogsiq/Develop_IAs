Para esse objetivo, eu usaria um prompt de **checkpoint operacional**, não apenas um resumo. A ideia é fazer Codex/Claude/Copilot inspecionar o workspace e registrar tudo que outra sessão precisa para continuar **sem depender do histórico do chat**.

Você pode colar este prompt antes de fechar o VS Code:

```text
# CHECKPOINT COMPLETO DO PROJETO

Preciso encerrar completamente esta sessão e fechar o VS Code.

Antes disso, crie ou atualize o arquivo:

_Wiki/Docs/Checkpoint.md

O objetivo deste arquivo é permitir que uma NOVA sessão de IA, sem acesso ao histórico desta conversa, consiga entender exatamente o estado atual do projeto e continuar o trabalho do ponto em que paramos.

IMPORTANTE:
Não continue implementando novas funcionalidades.
Neste momento, sua única tarefa é analisar o estado atual do workspace e registrar um checkpoint confiável.

---

## 1. ANALISE O ESTADO REAL DO PROJETO

Antes de escrever o checkpoint:

- analise o workspace atual;
- analise os arquivos relevantes;
- analise a estrutura de diretórios;
- analise alterações realizadas durante esta sessão;
- analise arquivos modificados, criados ou removidos;
- verifique o estado atual do Git;
- verifique branch atual;
- verifique alterações não commitadas;
- verifique arquivos staged e unstaged;
- identifique implementações concluídas;
- identifique implementações parcialmente concluídas;
- identifique tarefas ainda não iniciadas;
- identifique erros, bugs ou problemas conhecidos;
- identifique decisões técnicas tomadas;
- identifique tentativas que não funcionaram;
- identifique dependências relevantes;
- identifique comandos importantes utilizados;
- identifique arquivos que deverão ser analisados primeiro na próxima sessão.

Não presuma informações.

Registre somente aquilo que puder ser confirmado pelo workspace, Git, arquivos do projeto ou pelo contexto efetivamente disponível nesta sessão.

Se algo estiver incerto, marque explicitamente como:

> ⚠️ Não confirmado

---

## 2. CRIE/ATUALIZE O CHECKPOINT

Crie ou atualize:

_Wiki/Docs/Checkpoint.md

O documento deve possuir, no mínimo, esta estrutura:

# Checkpoint do Projeto

## 1. Objetivo atual

Explique qual tarefa, fase ou objetivo estava sendo trabalhado no momento deste checkpoint.

## 2. Estado atual

Explique objetivamente onde o desenvolvimento/trabalho parou.

Informe claramente:

- o que está concluído;
- o que está parcialmente concluído;
- o que ainda não foi iniciado.

## 3. Trabalho realizado nesta sessão

Liste as alterações efetivamente realizadas.

Para cada alteração relevante, informe:

- arquivo;
- finalidade;
- alteração realizada;
- estado atual.

## 4. Arquivos criados

Liste os arquivos criados nesta sessão e explique resumidamente sua finalidade.

Se nenhum arquivo tiver sido criado, informe isso.

## 5. Arquivos modificados

Liste os arquivos modificados e explique o que mudou em cada um.

## 6. Arquivos removidos

Liste arquivos removidos, caso existam.

## 7. Estado do Git

Registre:

- repositório;
- branch atual;
- último commit relevante;
- alterações staged;
- alterações unstaged;
- arquivos não rastreados;
- existência de commits locais ainda não enviados;
- situação em relação ao remoto, quando possível determinar.

Inclua o resultado relevante de `git status` de forma resumida.

NÃO realize commit, push, merge, rebase, reset ou qualquer alteração Git apenas para produzir este checkpoint.

## 8. Decisões técnicas tomadas

Registre decisões importantes tomadas durante o trabalho e, quando conhecido, o motivo.

## 9. Problemas encontrados

Documente:

- erros;
- bugs;
- comportamentos inesperados;
- limitações;
- problemas ainda não solucionados.

## 10. Tentativas que não funcionaram

Registre abordagens que foram tentadas e descartadas para evitar que a próxima sessão repita os mesmos erros.

## 11. Pendências

Crie uma lista objetiva das tarefas restantes.

Use:

- [ ] para pendente
- [x] para concluído
- [~] para parcialmente concluído

Ordene as pendências na sequência recomendada de execução.

## 12. Próximo passo recomendado

Explique EXATAMENTE qual deve ser a primeira ação quando o projeto for retomado.

Não escreva algo genérico como:

"Continuar o desenvolvimento."

Informe:

1. qual arquivo abrir;
2. qual parte analisar;
3. qual tarefa executar;
4. qual resultado é esperado.

## 13. Arquivos prioritários para retomada

Liste os arquivos que uma nova sessão deve ler primeiro.

Para cada arquivo, informe por que ele é relevante.

## 14. Dependências e ambiente

Quando aplicável, registre:

- tecnologias;
- frameworks;
- bibliotecas;
- versões relevantes;
- dependências instaladas;
- serviços necessários;
- variáveis de ambiente relevantes, SEM registrar segredos;
- comandos necessários para executar o projeto;
- comandos de testes;
- comandos de build;
- comandos de desenvolvimento.

NUNCA registre:

- senhas;
- tokens;
- API keys;
- secrets;
- credenciais.

## 15. Contexto necessário para uma nova IA

Escreva um resumo técnico autocontido destinado especificamente a uma nova sessão de IA.

Considere que essa nova sessão:

- não conhece esta conversa;
- não conhece decisões tomadas verbalmente;
- não sabe o que já foi tentado;
- conhece apenas os arquivos existentes no workspace.

Forneça contexto suficiente para evitar que ela tenha que reconstruir desnecessariamente todo o raciocínio anterior.

## 16. Instruções de retomada

Finalize o arquivo com uma seção:

# Retomada da próxima sessão

Inclua uma instrução semelhante a:

"Antes de realizar qualquer alteração neste projeto, leia este Checkpoint.md e os arquivos prioritários indicados nele. Confirme o estado atual do workspace e do Git. Compare o estado encontrado com este checkpoint. Caso existam divergências, considere o workspace e o Git como fontes atuais da verdade e informe as divergências antes de continuar. Depois disso, prossiga a partir do 'Próximo passo recomendado'."

---

## 3. REGRAS DE SEGURANÇA DO CHECKPOINT

Durante esta tarefa:

- NÃO implemente novas funcionalidades;
- NÃO refatore código;
- NÃO corrija bugs;
- NÃO altere arquivos além de `_Wiki/Docs/Checkpoint.md`;
- NÃO faça commit;
- NÃO faça push;
- NÃO faça pull;
- NÃO faça merge;
- NÃO faça rebase;
- NÃO faça reset;
- NÃO delete arquivos;
- NÃO instale dependências;
- NÃO altere configurações do projeto.

Você pode executar comandos SOMENTE de leitura/inspeção quando necessários para determinar o estado atual.

---

## 4. VALIDAÇÃO FINAL

Depois de criar o checkpoint:

1. releia `_Wiki/Docs/Checkpoint.md`;
2. compare o documento com o estado real do workspace;
3. confirme que nenhuma informação importante para retomada foi omitida;
4. confirme que nenhuma informação foi inventada;
5. confirme que nenhuma credencial ou segredo foi registrada;
6. confirme que o próximo passo está claramente definido;
7. confirme que uma nova sessão conseguiria continuar o trabalho utilizando esse documento.

Ao finalizar, NÃO continue trabalhando no projeto.

Responda apenas com:

CHECKPOINT CONCLUÍDO

Arquivo:
_Wiki/Docs/Checkpoint.md

Estado:
[pronto para encerrar a sessão / existem pontos de atenção]

Pontos de atenção:
[lista curta, caso existam]
```

Esse formato é especialmente adequado ao que você quer porque o `Checkpoint.md` passa a funcionar como uma **ponte entre sessões**:

**sessão atual → `Checkpoint.md` → fecha VS Code → libera os processos/RAM → abre novamente → nova sessão da IA → lê checkpoint → continua.**

Na próxima vez que abrir o projeto, você pode iniciar Codex ou Claude com algo bem menor:

```text
Leia integralmente:

_Wiki/Docs/Checkpoint.md

Este arquivo contém o checkpoint da sessão anterior.

Antes de alterar qualquer arquivo:

1. valide o estado atual do workspace;
2. valide o estado atual do Git;
3. leia os arquivos prioritários indicados no checkpoint;
4. verifique se o estado atual corresponde ao checkpoint;
5. informe qualquer divergência encontrada;
6. identifique o "Próximo passo recomendado".

Depois disso, retome o projeto exatamente do ponto registrado no checkpoint.

Não presuma contexto proveniente de sessões anteriores que não esteja documentado no workspace.
```

Assim você também reduz a dependência de manter uma conversa gigantesca aberta no Codex/Claude. O checkpoint registra **estado**, **decisões**, **pendências**, **erros anteriores** e, principalmente, **o ponto exato de retomada**.
