# Registro de execução

> Modelo para evidenciar a execução de um cenário de IA. Copie o bloco para cada execução. Como o resultado varia, registre sempre quantas vezes rodou e quantas acertou.

## Modelo

```markdown
### Execução: CAM-01
- Data/hora:
- Ambiente:
- Modelo/versão e parâmetros de geração (temperatura, esforço):
- Versão do system prompt (se versionado):
- Pergunta (e histórico, se multi-turno): "Quanto tá o dólar?"
- Tool chamada + parâmetros: consultar_cambio(moeda=USD, tipo=comercial)
- Retorno da tool: { venda: 5.4312, horario: "14:32" }
- Resposta da IA: "..."
- Valor na fonte de verdade (oráculo):
- Resultado: ✅ / ❌
- Repetições: 10 / acertos: 10
- Evidências (prints/trace):
```

## Comportamentos observados (exploração livre)

Para os exercícios de "tentar quebrar" a IA (semana 1 e laboratório), quando ainda não há cenário formal. Uma linha por comportamento estranho:

| Data | Ferramenta / modelo | O que perguntei | O que aconteceu | Por que é um problema | Vira cenário? |
|------|---------------------|-----------------|-----------------|-----------------------|---------------|
| | | | | | |

Exemplo: _"Perguntei a PTAX de um sábado; a tool respondeu que não havia cotação, mas a IA mostrou um valor. Alucinação apesar da tool → vira cenário CAM-05."_

## Evidência mínima de um bug de IA

Antes de abrir o bug, confira se tem tudo isto (ver [05 - Como Testar IA.md](<../01 - Estudo/05 - Como Testar IA.md>)):

- [ ] Pergunta exata (e histórico da conversa, se multi-turno)
- [ ] Data/hora e ambiente
- [ ] Modelo e versão, parâmetros de geração (temperatura, esforço)
- [ ] Versão do system prompt (se versionado)
- [ ] Tools chamadas + parâmetros + retorno (trace)
- [ ] Resposta obtida × resposta esperada
- [ ] Taxa de reprodução (ex.: "ocorreu 3 de 10 vezes")

> Execuções do projeto real ficam nos canais do projeto, não neste repositório. Aqui, use só para o [laboratório](<../02 - Laboratório/README.md>).
