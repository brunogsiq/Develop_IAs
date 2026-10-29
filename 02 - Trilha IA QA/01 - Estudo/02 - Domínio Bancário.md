# 02. Domínio bancário

> Para saber se a IA respondeu certo, você precisa saber o que é "certo" no negócio. Este arquivo cobre o mínimo para câmbio, crédito e regulação. Ele vem no início da trilha porque o laboratório, os cenários e o golden dataset usam esses conceitos. O caso é hipotético: serve para quem trabalha, ou vai trabalhar, em uma instituição financeira do ramo bancário, e o mesmo raciocínio vale para qualquer domínio.

## Câmbio

### Tipos de cotação

| Termo | O que é |
|-------|---------|
| **PTAX** | Taxa oficial calculada pelo Banco Central, média de consultas ao longo do dia. Referência para contratos |
| **Dólar comercial** | Usado em operações de empresas: comércio exterior, transferências |
| **Dólar turismo** | Para pessoa física comprar moeda em espécie/cartão; normalmente mais caro |
| **Taxa do banco** | Cotação praticada pela própria instituição, com spread |
| **Compra × venda** | Compra = quanto o banco paga; venda = quanto o banco cobra. A diferença é o **spread** |

### Por que isso importa no teste
"Quanto tá o dólar?" é ambígua. Defina com o time (e coloque no critério de aceite):
- Qual cotação é o padrão quando o gerente não especifica?
- A resposta deve informar **qual** cotação está mostrando?
- Mostra compra, venda ou as duas?

### Pontos de atenção
- **Horário:** cotação muda ao longo do dia. A resposta deve mostrar o horário/data.
- **Fim de semana e feriado:** não há PTAX. O correto é "última cotação de [data]".
- **Fechamento:** PTAX do dia só é definida no fim da tarde; antes disso existem "boletins" intermediários.
- **Casas decimais:** câmbio costuma usar 4 casas; confirme a regra de exibição.
- **Cache:** a cotação exibida pode estar desatualizada se houver cache. Qual a validade?

### Oráculo público
O Banco Central disponibiliza a PTAX publicamente (site e API de dados abertos). Útil para conferir valores quando a fonte for a PTAX.

## Crédito

| Termo | O que é |
|-------|---------|
| **Limite aprovado** | Total concedido ao cliente |
| **Limite disponível** | Aprovado menos o que já está em uso |
| **Pré-aprovado** | Oferta calculada, ainda não contratada |
| **Score / rating** | Avaliação de risco do cliente (normalmente informação restrita) |
| **Produto** | Cheque especial, cartão, consignado, capital de giro... cada um tem seu limite |

### Por que isso importa no teste
"O cliente tem crédito?" pode significar várias coisas:
- Tem limite disponível? Em qual produto?
- Tem pré-aprovado?
- Qual o valor? O gerente pode ver o valor ou só "sim/não"?
- O que a IA deve responder se o cliente estiver com restrição?

Cada uma dessas respostas é uma regra de negócio que deve estar nas histórias de usuário. Se não estiver, **pergunte**.

## Regulação e compliance

| Norma | Resumo | Impacto no teste |
|-------|--------|------------------|
| **LGPD (Lei 13.709/2018)** | Proteção de dados pessoais: finalidade, necessidade, segurança | Minimização de dados nas respostas, retenção do histórico de conversa, logs |
| **Sigilo bancário (LC 105/2001)** | Operações e dados de clientes são sigilosos | Acesso apenas por quem tem necessidade e permissão |
| **Resolução CMN 4.893/2021** (alterada pela **CMN 5.274/2025**) | Política de segurança cibernética e contratação de nuvem por instituições financeiras. A alteração de 2025 detalhou requisitos mínimos como autenticação, criptografia, detecção de intrusão e controle de acesso | Onde o modelo de IA roda, para onde os dados vão, rastreabilidade |
| **Normas de suitability (CVM/ANBIMA)** | Recomendação de investimento exige perfil do cliente e profissional habilitado | A IA não deve recomendar investimentos |

> Valide com o time de compliance do banco quais normas internas se aplicam. Esta lista é ponto de partida, não parecer jurídico.

### Perguntas de compliance para o time
- Os dados de clientes saem do ambiente do banco para o provedor do LLM? Há contrato e anonimização?
- Por quanto tempo o histórico de conversa fica armazenado?
- Existe trilha de auditoria de quem perguntou o quê sobre qual cliente?

## Checklist de aprendizado

- [ ] Sei a diferença entre PTAX, comercial, turismo, compra e venda
- [ ] Sei a regra do projeto para "quanto tá o dólar" sem especificação
- [ ] Sei diferenciar limite aprovado, disponível e pré-aprovado
- [ ] Sei o que o gerente pode e não pode ver
- [ ] Li um resumo da LGPD e do sigilo bancário
- [ ] Conversei com alguém de negócio/compliance sobre as regras
