# 02. Uso responsável e privacidade

> Usar IA no trabalho é também uma questão de **dados, responsabilidade e confiança**. Este módulo reúne as regras que valem para qualquer profissão. Ele não substitui a política de IA da sua empresa nem orientação jurídica: na dúvida, pergunte ao time de segurança ou de privacidade. Ele vem logo no início porque, a partir do próximo módulo, você vai colar textos, documentos e código em assistentes de IA.

## As cinco regras de bolso

1. **Você responde pelo resultado.** A IA ajuda; a entrega, a decisão e o erro são seus.
2. **Não cole o que não pode vazar.** Dados de cliente, dados pessoais, senhas, chaves, código e documentos internos só entram em ferramentas **aprovadas pela empresa**.
3. **Confira antes de usar.** Números, leis, citações, nomes de funções e comandos devem ser verificados na fonte oficial.
4. **Seja transparente.** Diga quando um conteúdo foi produzido com apoio de IA, se a política do time pedir.
5. **Na dúvida, não envie.** Anonimize ou use dados fictícios.

## Que dados nunca colar numa IA não aprovada

| Tipo | Exemplos |
|------|----------|
| Dados pessoais | Nome + CPF, endereço, telefone, e-mail de clientes ou colegas |
| Dados pessoais sensíveis (LGPD) | Saúde, religião, biometria, origem racial, opinião política |
| Dados financeiros e sigilosos | Saldo, limite, transações, dados protegidos por sigilo bancário |
| Credenciais | Senhas, tokens, chaves de API, arquivos `.env`, certificados |
| Propriedade da empresa | Código proprietário, arquitetura, contratos, estratégia, preços |
| Dados de clientes da empresa | Nome do cliente, projeto, prints, bugs e dados de teste reais |

### Como anonimizar antes de pedir ajuda
- Troque nomes por `Cliente A`, `Empresa X`, `Sistema 1`.
- Troque valores por números fictícios com o mesmo formato.
- Remova URLs, IPs, nomes de servidores e de tabelas reais.
- Reduza ao mínimo: cole só o trecho necessário para a pergunta.

## Ferramenta pessoal × ferramenta corporativa

| Pergunta | Por que importa |
|----------|-----------------|
| Os dados enviados são usados para treinar modelos? | Planos pessoais e corporativos costumam ter regras diferentes |
| Por quanto tempo as conversas ficam guardadas? | Retenção e direito de exclusão |
| Em que país os dados são processados? | Transferência internacional (LGPD) |
| A empresa aprovou essa ferramenta? | Uso de IA não aprovada ("shadow AI") é um risco de segurança e de compliance |

Confira sempre os termos atuais do fornecedor e a política interna.

## LGPD em uma página

A Lei 13.709/2018 vale para qualquer tratamento de dados pessoais, inclusive por IA.

| Princípio | Na prática com IA |
|-----------|-------------------|
| Finalidade | Usar o dado só para o objetivo informado |
| Necessidade (minimização) | A IA só recebe e só mostra o mínimo necessário |
| Segurança | Controle de acesso, logs sem dados sensíveis |
| Transparência | O titular tem direito de saber como seus dados são tratados |
| Revisão de decisões automatizadas | Decisões tomadas só por máquina que afetem a pessoa podem ser contestadas (art. 20) |

Referências: [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) e guias da ANPD ([gov.br/anpd](https://www.gov.br/anpd)).

## Outros cuidados

| Tema | Cuidado |
|------|---------|
| **Viés** | A IA pode reproduzir preconceitos dos dados de treino. Revise textos sobre pessoas, avaliações e seleção com atenção redobrada |
| **Direitos autorais e licenças** | Código e imagens gerados podem se parecer com material protegido. Siga a política da empresa sobre uso comercial e verifique licenças |
| **Decisões sobre pessoas** | Crédito, contratação, avaliação de desempenho: a IA pode apoiar, mas a decisão e a justificativa precisam ser humanas e explicáveis |
| **Excesso de confiança** | Quanto mais a IA acerta, menos se revisa. Mantenha a revisão proporcional ao risco |
| **Regulação** | A regulação de IA está em evolução no Brasil e no mundo (por exemplo, o AI Act na União Europeia). Acompanhe pela área jurídica da empresa |

## Este repositório como exemplo

Este repositório é público e segue a mesma regra: só conteúdo genérico de estudo. Veja a "Regra de ouro" no [README principal](<../../README.md>).

## Checklist de aprendizado

- [ ] Sei quais ferramentas de IA a minha empresa aprovou
- [ ] Sei listar o que nunca colar numa IA não aprovada
- [ ] Sei anonimizar um dado antes de pedir ajuda
- [ ] Sei os princípios da LGPD que mais impactam o uso de IA
- [ ] Reviso o resultado da IA proporcionalmente ao risco da tarefa
