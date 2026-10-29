# Estratégia de teste para sistemas com IA

> Modelo para o entregável da semana 4: a estratégia de teste por camada. Preencha uma cópia **nos canais do projeto**, não neste repositório. Os textos em _itálico_ são orientações; apague-os ao preencher.

## 1. Contexto

- **Sistema:** _o que é, quem usa, qual problema resolve_
- **Arquitetura resumida:** _front → backend → LLM → servidor MCP → APIs (ver 01 - Mapa Da Jornada)_
- **Modelo de IA e versão:** _
- **Fora do escopo desta estratégia:** _

## 2. Camadas e abordagem

| Camada | Natureza | Tipos de teste | Ferramentas | Responsável |
|--------|----------|----------------|-------------|-------------|
| Front (chat) | Determinística | Funcional, layout (Figma), acessibilidade, streaming | _ | _ |
| Backend / orquestrador | Determinística | API, integração, contrato | _ | _ |
| Servidor MCP | Determinística | API: `tools/list`, `tools/call`, schemas, erros, autorização | MCP Inspector, _ | _ |
| APIs de origem | Determinística | Integração, disponibilidade, massa | _ | _ |
| Comportamento da IA | **Não determinística** | Evals com golden dataset, robustez, multi-turno | promptfoo, _ | _ |
| Segurança | Mista | Red teaming, OWASP LLM Top 10, autorização | _ | _ |
| Não funcional | Mista | Latência, custo por conversa, carga | _ | _ |

## 3. Golden dataset

- **Tamanho inicial:** _ex.: 50 casos_
- **Distribuição por categoria:** _câmbio X%, crédito Y%, segurança Z%, escopo..._
- **Quem mantém e como cresce:** _ex.: todo bug de IA vira um caso novo_
- **Repetições por caso:** _ex.: 5_

## 4. Critérios de aceite e metas

| Métrica | Meta | Como medir |
|---------|------|------------|
| Taxa de acerto geral no golden dataset | _ex.: ≥ 95%_ | Eval automatizado |
| Casos críticos (segurança, dados de cliente) | _100%_ | Eval + execução manual |
| Exatidão numérica (câmbio, limites) | _100%_ | Comparação com o oráculo |
| Latência (resposta completa) | _ex.: ≤ 5 s no p95_ | Trace / promptfoo |
| Custo médio por conversa | _ | Trace |

## 5. Critérios de entrada e saída

**Entrada (podemos começar a testar quando):**
- [ ] Lista de tools com nome, descrição e schema disponível
- [ ] Ambiente de teste com massa fictícia e mocks de falha
- [ ] Acesso a traces/logs
- [ ] System prompt versionado e acessível ao QA

**Saída (podemos liberar quando):**
- [ ] Metas da seção 4 atingidas
- [ ] Nenhum bug crítico ou alto de segurança aberto
- [ ] Regressão do golden dataset executada na versão candidata

## 6. Regressão

- **Quando roda:** _a cada mudança de prompt, modelo, tool ou release_
- **Onde roda:** _pipeline / manual_
- **O que bloqueia o deploy:** _

## 7. Riscos e mitigação

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Alucinação de valores | _ | Alto | Comparação com oráculo em 100% dos casos numéricos |
| Acesso a cliente de outra carteira | _ | Crítico | Testes de autorização na camada MCP, não só no prompt |
| Mudança de versão do modelo pelo provedor | _ | Médio | Fixar versão; regressão completa a cada troca |
| _ | _ | _ | _ |

## 8. Evidências e rastreabilidade

- **Onde ficam as execuções:** _
- **Modelo de registro:** [03 - Registro De Execução](<03 - Registro De Execução.md>)
- **Como um bug de IA é aberto:** _campos obrigatórios_
