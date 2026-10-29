Revisei o arquivo original por completo e consolidei com as melhorias propostas. Mantive os pontos essenciais que já estavam corretos: navegação real antes do Page Object, `read_page`, `run_playwright_code` + `page.evaluate()`, inspeção de widgets customizados via `outerHTML`, diferenciação entre dropdown e autocomplete, proibição de submissão durante o mapeamento, cuidado com dados reais e tratamento específico de campos `readonly`/datepicker.    

Também corrigi os pontos que deixavam o documento excessivamente acoplado ao Cypress/Copilot: agora existe **um único processo de descoberta do DOM → mapa neutro → geração correspondente para Cypress, Playwright e Python**. A versão abaixo pode substituir integralmente o conteúdo de `03 - Leitura de DOM e criação de Page Objects.md`.

````markdown
# PROJETO — LEITURA DE DOM E CRIAÇÃO DE PAGE OBJECTS

## Padrão reutilizável para Cypress, Playwright e Python

---

# 1. OBJETIVO

Antes de escrever qualquer teste, robô, comando ou Page Object para uma nova plataforma, realizar o mapeamento dos elementos reais da página utilizando o navegador e o DOM efetivamente renderizado.

O objetivo é evitar a criação de seletores baseada apenas em:

- prints;
- aparência visual;
- textos vistos na tela;
- posições;
- suposições;
- conhecimento prévio não confirmado da plataforma.

O processo deverá descobrir:

- quais elementos realmente existem;
- quais atributos possuem;
- o significado semântico de cada campo;
- quais componentes são HTML nativos;
- quais são widgets customizados;
- como cada componente deve ser manipulado;
- qual seletor é mais estável;
- quais elementos correspondem logicamente entre Cypress, Playwright e Python.

O fluxo obrigatório é:

```text
Navegação real
      ↓
Leitura estrutural/acessível
      ↓
Inspeção do DOM
      ↓
Mapeamento dos campos
      ↓
Classificação dos widgets
      ↓
Análise dos seletores
      ↓
Mapa neutro do formulário
      ↓
Validação
      ↓
├── Page Object Cypress
├── Page Object Playwright
└── Page Object Python
      ↓
Commands / Actions / Robô
```

A descoberta do DOM deve acontecer antes da criação dos Page Objects.

---

# 2. PRINCÍPIO CENTRAL

Os três projetos:

- Cypress;
- Playwright;
- Python;

representam implementações diferentes do mesmo robô.

Portanto:

> O conhecimento funcional sobre a página deve ser descoberto uma única vez e reutilizado conceitualmente pelas três tecnologias.

Não devem existir três interpretações diferentes do mesmo formulário sem necessidade.

O processo esperado é:

```text
1 descoberta do DOM
        ↓
1 mapa neutro
        ↓
3 implementações equivalentes
```

Nova descoberta somente será necessária se:

- o DOM tiver mudado;
- a plataforma tiver mudado;
- algum comportamento não tiver sido identificado;
- algum framework revelar comportamento não documentado;
- o mapa estiver incompleto.

---

# 3. PAPEL DO AGENTE

Atue como Engenheiro de Automação Sênior especializado em:

- automação web;
- inspeção de DOM;
- HTML;
- acessibilidade;
- Cypress;
- Playwright;
- Python;
- Selenium quando aplicável;
- Page Object Model;
- componentes web modernos;
- aplicações SPA;
- React;
- Angular;
- Vue;
- widgets customizados;
- automação de processos via navegador.

Nesta atividade, o objetivo NÃO é validar a aplicação.

O objetivo é:

> compreender tecnicamente a interface e criar um mapa confiável para automação.

---

# 4. DADOS DE ENTRADA

Antes de começar, considere:

```text
Plataforma: <NOME_DA_PLATAFORMA>

URL inicial:
<URL>

Objetivo da página:
<DESCRIÇÃO>

Necessita autenticação:
<SIM / NÃO>

Tecnologias consumidoras do mapeamento:
- Cypress
- Playwright
- Python
```

Adapte esses valores para cada novo projeto.

---

# 5. TECNOLOGIA DE INSPEÇÃO

O padrão conceitual utilizado é:

> navegador automatizado + inspeção do DOM real.

A ferramenta específica pode variar.

Exemplos:

- GitHub Copilot Agent;
- Codex;
- Claude Code;
- Playwright;
- MCP/browser tools;
- navegador controlado por agente;
- ferramenta equivalente com capacidade de executar JavaScript na página.

Quando disponíveis, podem ser utilizadas ferramentas como:

```text
open_browser_page
navigate_page
click_element
type_in_page
read_page
screenshot_page
run_playwright_code
```

Esses nomes NÃO fazem parte obrigatória da arquitetura.

São apenas ferramentas disponíveis em determinados ambientes.

O método deve continuar válido mesmo quando o agente ou ferramenta mudar.

---

# 6. PRÉ-REQUISITOS

Quando aplicável:

- VS Code;
- agente de IA com acesso ao projeto;
- navegador controlável pelo agente;
- ferramenta de leitura da página;
- capacidade de executar JavaScript no contexto da página;
- sessão autenticada válida quando necessária.

Se a aplicação exigir:

- login;
- MFA;
- CAPTCHA;
- credencial;
- autorização humana;

não tente contornar a proteção.

Solicite intervenção quando necessário.

---

# 7. PROMPT REUTILIZÁVEL

Utilize o prompt abaixo sempre que precisar mapear uma nova página.

```text
Preciso mapear tecnicamente a página da plataforma:

<NOME_DA_PLATAFORMA>

URL:

<URL_DA_PAGINA>

O objetivo é criar posteriormente Page Objects equivalentes para Cypress, Playwright e Python.

IMPORTANTE:

Nesta etapa NÃO quero que você implemente o robô nem crie os Page Objects imediatamente.

Primeiro faça somente a descoberta técnica da página real.

Execute obrigatoriamente este fluxo:

1. Abra a URL no navegador.

2. Aguarde todos os redirecionamentos necessários e registre:
   - URL inicial;
   - URL final;
   - redirecionamentos observados;
   - plataforma identificada.

3. Se houver autenticação:
   - utilize uma sessão já autorizada quando disponível;
   - caso necessite credenciais ou intervenção humana, pare e solicite;
   - não tente contornar CAPTCHA, MFA ou proteção anti-bot.

4. Navegue até a tela real que deverá ser automatizada.

5. Leia primeiro a estrutura da página usando `read_page`, accessibility tree ou recurso equivalente.

6. Identifique:
   - seções;
   - headings;
   - labels;
   - campos;
   - botões;
   - formulários;
   - grupos;
   - abas;
   - diálogos;
   - elementos condicionais.

7. Depois execute JavaScript no contexto real da página, preferencialmente por:
   `run_playwright_code` + `page.evaluate()`
   ou mecanismo equivalente.

8. Extraia os atributos reais dos componentes, incluindo quando disponíveis:
   - tag;
   - type;
   - id;
   - name;
   - label;
   - placeholder;
   - role;
   - aria-label;
   - aria-labelledby;
   - data-testid;
   - data-test;
   - data-cy;
   - autocomplete;
   - required;
   - disabled;
   - readonly;
   - contenteditable;
   - href;
   - className;
   - texto visível relevante.

9. NÃO extraia nem registre valores pessoais existentes nos campos.

10. Para cada elemento, determine o significado semântico real do campo.

11. Classifique o tipo de widget:
    - input simples;
    - textarea;
    - select nativo;
    - dropdown;
    - combobox;
    - autocomplete;
    - multiselect;
    - checkbox;
    - radio;
    - toggle;
    - file upload;
    - date input;
    - datepicker;
    - contenteditable;
    - botão;
    - link;
    - desconhecido.

12. Diferencie obrigatoriamente:
    - dropdown de clique;
    - autocomplete;
    - combobox pesquisável;
    - select HTML nativo.

13. Quando o elemento for customizado e não puder ser compreendido apenas pelo input:
    - encontre o container correspondente;
    - inspecione o `outerHTML`;
    - identifique roles, aria attributes, elementos internos e comportamento;
    - identifique indícios do framework utilizado quando possível.

14. Verifique se existem:
    - campos condicionais;
    - modais;
    - iframes;
    - dialogs;
    - novas abas;
    - Shadow DOM;
    - portais;
    - overlays.

15. Para cada seletor candidato:
    - indique estratégia;
    - justifique a escolha;
    - classifique estabilidade como ALTA, MÉDIA ou BAIXA.

16. Não escolha seletores apenas porque funcionaram uma vez.

17. Evite classes dinâmicas, posições e seletores estruturais frágeis.

18. Gere primeiro um MAPA NEUTRO do formulário, independente de Cypress, Playwright ou Python.

19. Apresente uma tabela contendo:
    campo | label | HTML/role | widget | seletor recomendado | estratégia | estabilidade | observações.

20. Liste separadamente:
    - seletores frágeis;
    - campos não compreendidos;
    - componentes customizados;
    - campos condicionais;
    - possíveis riscos de automação.

21. NÃO clique em:
    - Enviar;
    - Salvar;
    - Candidatar;
    - Confirmar;
    - Excluir;
    ou qualquer botão que possa persistir dados reais.

22. NÃO invente dados pessoais ou profissionais.

23. NÃO crie ainda os Page Objects.

24. Ao finalizar o mapa neutro, PARE e aguarde minha aprovação.

Somente depois da minha confirmação serão criados os Page Objects Cypress, Playwright e Python.
```

---

# 8. LEITURA ESTRUTURAL DA PÁGINA

Antes da leitura do DOM bruto, utilize:

```text
read_page
```

ou recurso equivalente.

A accessibility tree pode revelar:

- títulos;
- seções;
- labels;
- nomes acessíveis;
- botões;
- grupos;
- roles;
- hierarquia;
- relacionamentos semânticos.

Ela é extremamente útil para compreender:

> o que cada elemento significa.

Entretanto:

> a accessibility tree sozinha não é suficiente para selecionar elementos robustamente.

Ela pode não revelar:

- `id`;
- `name`;
- classes;
- atributos `data-*`;
- estrutura interna de componentes;
- HTML dos widgets customizados.

Por isso, a leitura estrutural deve ser complementada com inspeção do DOM.

---

# 9. DESCOBRIR A FERRAMENTA DE EXECUÇÃO DE JAVASCRIPT

Quando `run_playwright_code` não estiver disponível diretamente no agente, procure ferramenta equivalente.

Exemplo conceitual de busca:

```text
evaluate javascript on page
execute playwright code
get html outerHTML
inspect DOM
page.evaluate
```

No ambiente em que exista `tool_search`, pode ser utilizado algo semelhante a:

```text
tool_search:
"evaluate javascript on page get html outerHTML execute script"
```

Não dependa deste nome específico para manter a portabilidade.

---

# 10. SCRIPT PRINCIPAL — EXTRAÇÃO DOS ELEMENTOS

Quando possível, execute via:

```text
run_playwright_code
```

utilizando:

```javascript
page.evaluate()
```

Script recomendado:

```javascript
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

  const elements = Array.from(
    root.querySelectorAll(selector)
  );

  function getLabel(el) {

    if (el.labels && el.labels.length) {
      return Array.from(el.labels)
        .map(label => label.innerText?.trim())
        .filter(Boolean)
        .join(' | ');
    }

    const ariaLabel =
      el.getAttribute('aria-label');

    if (ariaLabel) {
      return ariaLabel;
    }

    const labelledBy =
      el.getAttribute('aria-labelledby');

    if (labelledBy) {
      return labelledBy
        .split(/\s+/)
        .map(id =>
          document
            .getElementById(id)
            ?.innerText
            ?.trim()
        )
        .filter(Boolean)
        .join(' | ');
    }

    if (el.id) {
      const explicitLabel =
        document.querySelector(
          `label[for="${CSS.escape(el.id)}"]`
        );

      if (explicitLabel) {
        return explicitLabel
          .innerText
          ?.trim() || null;
      }
    }

    return null;
  }

  return elements.map((el, index) => ({

    index,

    tag:
      el.tagName?.toLowerCase() || null,

    type:
      el.getAttribute('type'),

    id:
      el.id || null,

    name:
      el.getAttribute('name'),

    label:
      getLabel(el),

    placeholder:
      el.getAttribute('placeholder'),

    role:
      el.getAttribute('role'),

    ariaLabel:
      el.getAttribute('aria-label'),

    ariaLabelledBy:
      el.getAttribute('aria-labelledby'),

    ariaDescribedBy:
      el.getAttribute('aria-describedby'),

    ariaExpanded:
      el.getAttribute('aria-expanded'),

    ariaControls:
      el.getAttribute('aria-controls'),

    ariaHasPopup:
      el.getAttribute('aria-haspopup'),

    dataTestId:
      el.getAttribute('data-testid'),

    dataTest:
      el.getAttribute('data-test'),

    dataCy:
      el.getAttribute('data-cy'),

    autocomplete:
      el.getAttribute('autocomplete'),

    required:
      el.required === true ||
      el.getAttribute('aria-required') === 'true',

    disabled:
      el.disabled === true ||
      el.getAttribute('aria-disabled') === 'true',

    readOnly:
      el.readOnly === true ||
      el.hasAttribute('readonly'),

    contentEditable:
      el.getAttribute('contenteditable'),

    multiple:
      el.multiple === true,

    accept:
      el.getAttribute('accept'),

    href:
      el.getAttribute('href'),

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
```

---

# 11. POR QUE NÃO EXTRAIR `value`

Evite incluir valores digitados no dump do DOM.

O objetivo é mapear:

- estrutura;
- semântica;
- atributos;
- comportamento.

Não dados pessoais.

Isso reduz risco de registrar:

- CPF;
- RG;
- e-mail;
- telefone;
- endereço;
- salário;
- datas pessoais;
- informações profissionais.

---

# 12. IDENTIFICAÇÃO SEMÂNTICA

Encontrar um `<input>` não é suficiente.

Para cada elemento, descubra:

> O que este campo representa?

Utilize como evidência, aproximadamente nesta ordem:

1. `<label>` explicitamente associado;
2. accessible name;
3. `aria-label`;
4. `aria-labelledby`;
5. `name`;
6. `id`;
7. `placeholder`;
8. texto próximo;
9. `role`;
10. tipo HTML;
11. opções disponíveis;
12. contexto da seção;
13. relacionamento com outros componentes.

Não deduza o significado apenas pela posição.

---

# 13. CLASSIFICAÇÃO DOS WIDGETS

Utilize uma taxonomia neutra.

```text
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
```

Esta classificação representa comportamento, não framework.

---

# 14. SELECT NATIVO

Exemplo:

```html
<select name="estado">
```

Classificação:

```text
SELECT_NATIVE
```

Comportamento conceitual:

```text
localizar
→ selecionar option
```

---

# 15. DROPDOWN DE CLIQUE

Exemplo funcional:

```text
Sexo
Tipo de documento
Estado civil
```

Comportamento:

```text
clicar no widget
→ abrir menu
→ selecionar opção
```

Classificação:

```text
DROPDOWN_CLICK
```

Não confundir com autocomplete.

---

# 16. AUTOCOMPLETE

Exemplos frequentes:

```text
Cidade
Localização
Empresa
Cargo
Curso
```

Comportamento:

```text
clicar/focar
→ digitar parte do texto
→ aguardar resultados
→ selecionar sugestão
```

Classificação:

```text
AUTOCOMPLETE
```

Quando o componente exigir seleção:

> apenas digitar o texto NÃO conclui o preenchimento.

É necessário selecionar a opção válida.

---

# 17. COMBOBOX PESQUISÁVEL

Alguns componentes misturam dropdown e busca.

Fluxo:

```text
abrir
→ digitar
→ filtrar
→ selecionar
```

Classificação:

```text
COMBOBOX
```

ou, quando múltiplos valores forem aceitos:

```text
MULTISELECT
```

---

# 18. INSPEÇÃO DE WIDGETS CUSTOMIZADOS

Frameworks modernos frequentemente não utilizam:

```html
<select>
```

Podem renderizar:

```html
<div role="combobox">
```

ou estruturas compostas.

Procure:

```text
role="combobox"
role="listbox"
role="option"

aria-expanded
aria-controls
aria-activedescendant
aria-haspopup
```

Também investigue:

- input interno;
- menu;
- overlay;
- portal;
- container;
- item selecionado;
- área de resultados.

---

# 19. SCRIPT PARA INSPECIONAR O CONTAINER

Quando precisar compreender um componente específico, obtenha o `outerHTML` do bloco relevante.

Exemplo:

```javascript
return await page.evaluate((labelText) => {

  function findAssociatedBlock(text) {

    const candidates = Array.from(
      document.querySelectorAll(
        'label, span, div, p'
      )
    );

    const label = candidates.find(el =>
      el.textContent?.trim() === text
    );

    if (!label) {
      return {
        found: false,
        label: text
      };
    }

    let current = label;

    for (
      let depth = 0;
      depth < 6 && current;
      depth++
    ) {

      const interactive =
        current.querySelector?.(
          [
            'input',
            'select',
            'textarea',
            '[role="combobox"]',
            '[role="listbox"]',
            '[role="checkbox"]',
            '[role="radio"]',
            '[contenteditable="true"]'
          ].join(',')
        );

      if (interactive) {

        return {
          found: true,
          depth,
          html:
            current.outerHTML
              .slice(0, 5000)
        };

      }

      current =
        current.parentElement;
    }

    return {
      found: true,
      html:
        label.parentElement
          ?.outerHTML
          .slice(0, 5000)
    };

  }

  return findAssociatedBlock(labelText);

}, 'RÓTULO EXATO DO CAMPO');
```

A saída deve ser usada para compreender o componente.

Não copie seletor automaticamente a partir da primeira classe encontrada.

---

# 20. IDENTIFICAÇÃO DO FRAMEWORK

Se houver evidência, registre indícios de:

- Semantic UI;
- Material UI;
- Ant Design;
- React Select;
- react-dropdown-select;
- Bootstrap;
- Angular Material;
- PrimeReact;
- Chakra UI;
- Headless UI;
- outros.

Exemplo:

```text
ui selection dropdown
```

pode sugerir Semantic UI.

Mas:

> o framework serve para explicar comportamento, não para definir sozinho o seletor.

---

# 21. PRIORIDADE DOS SELETORES

Utilize esta hierarquia como referência.

## Prioridade 1 — atributos específicos e estáveis para automação

```text
data-testid
data-test
data-cy
```

Somente quando forem semanticamente estáveis.

---

## Prioridade 2 — identidade estável

```text
id
name
```

---

## Prioridade 3 — acessibilidade

```text
label
role + accessible name
aria-label
aria-labelledby
```

---

## Prioridade 4 — atributos semânticos

Quando suficientemente específicos:

```text
type
autocomplete
href
value
```

---

## Prioridade 5 — placeholder

Pode ser útil, mas é texto de interface e pode mudar.

---

## Prioridade 6 — relação estrutural semântica

Exemplo:

```text
container identificado por label
→ input pertencente ao container
```

---

## Prioridade 7 — classe estável

Somente quando houver evidência de que a classe:

- é intencional;
- representa o componente;
- não é gerada dinamicamente.

---

## Prioridade 8 — posição

Exemplo:

```text
:nth-child(...)
.eq(...)
```

Use somente como último recurso.

Marque como:

```text
SELETOR FRÁGIL
```

---

# 22. SELETORES QUE DEVEM GERAR ALERTA

Tenha cautela com:

```text
:nth-child(4)

:eq(3)

div > div > div > input

css-1bhxif7

sc-cwHptR

sc-aXZVg

MuiBox-root-123
```

Classes provenientes de:

- styled-components;
- CSS Modules;
- CSS-in-JS;
- geração automática;
- hashes;

podem mudar entre builds.

---

# 23. ESTABILIDADE DOS SELETORES

Classifique cada seletor:

```text
ALTA
MÉDIA
BAIXA
```

Exemplo:

| Campo | Estratégia | Estabilidade |
|---|---|---|
| Nome | `name="fullName"` | ALTA |
| Cidade | `role=combobox + accessible name` | ALTA |
| Telefone | placeholder | MÉDIA |
| Campo X | classe dinâmica | BAIXA |
| Campo Y | `nth-child` | BAIXA |

Não classifique um seletor como estável apenas porque funcionou uma vez.

---

# 24. MAPA NEUTRO DO DOM

Antes dos Page Objects, gere um modelo independente de framework.

Exemplo:

```json
{
  "nomeCompleto": {
    "semanticName": "nomeCompleto",
    "label": "Nome completo",
    "widget": "TEXT",
    "required": true,
    "selectorStrategy": "name",
    "selectorValue": "fullName",
    "stability": "HIGH",
    "conditional": false
  },

  "cidade": {
    "semanticName": "cidade",
    "label": "Cidade",
    "widget": "AUTOCOMPLETE",
    "required": true,
    "selectorStrategy": "role+accessibleName",
    "role": "combobox",
    "accessibleName": "Cidade",
    "stability": "HIGH",
    "conditional": false,
    "interaction": [
      "focus",
      "type",
      "waitSuggestions",
      "selectSuggestion"
    ]
  },

  "curriculo": {
    "semanticName": "curriculo",
    "label": "Currículo",
    "widget": "FILE_UPLOAD",
    "selectorStrategy": "type",
    "selectorValue": "file",
    "stability": "MEDIUM",
    "conditional": false
  }
}
```

Este mapa deve funcionar como:

> fonte técnica comum para as três implementações.

---

# 25. TABELA OBRIGATÓRIA DO MAPEAMENTO

Produza:

| Campo | Label | HTML / Role | Widget | Seletor recomendado | Estratégia | Estabilidade | Condicional | Observação |
|---|---|---|---|---|---|---|---|---|

Exemplo:

| Campo | Label | Widget | Estratégia |
|---|---|---|---|
| nome | Nome completo | TEXT | preencher |
| tipoDocumento | Tipo de documento | DROPDOWN_CLICK | abrir → opção |
| cidade | Cidade | AUTOCOMPLETE | digitar → sugestão |
| currículo | Currículo | FILE_UPLOAD | upload |
| nascimento | Data de nascimento | DATEPICKER | abrir → selecionar |

---

# 26. CAMPOS CONDICIONAIS

Alguns componentes só aparecem após:

- selecionar opção;
- marcar checkbox;
- clicar botão;
- responder pergunta;
- avançar etapa;
- preencher campo anterior.

Registre:

```text
Campo condicional: SIM

Dependência:
<campo ou ação>

Ação que revela:
<ação>
```

Depois da ação:

> leia novamente o DOM.

Não assuma que a estrutura do formulário permanece estática.

---

# 27. FORMULÁRIOS MULTIETAPA

Se o formulário possuir:

```text
Etapa 1
Etapa 2
Etapa 3
...
```

cada etapa deve ser mapeada separadamente.

Antes de clicar em:

```text
Próximo
Continuar
Avançar
```

confirme que:

- a ação não envia definitivamente;
- não produz efeito irreversível;
- não cria candidatura real prematuramente.

Se houver dúvida:

PARE.

---

# 28. IFRAMES

Detecte:

```html
<iframe>
```

Elementos dentro de iframe possuem contexto diferente.

Registre:

```text
Iframe: SIM
Origem:
Finalidade:
Campos internos:
```

Não crie seletor do documento principal para elemento que está dentro de iframe.

---

# 29. MODAIS E DIALOGS

Identifique:

```text
role="dialog"
modal
overlay
popup
```

Registre:

- como abre;
- como fecha;
- quais campos contém;
- se é necessário para preenchimento.

---

# 30. NOVAS ABAS E POPUPS

Se uma ação abrir:

- nova aba;
- popup;
- janela;

registre explicitamente.

Não presuma que a navegação permanece no mesmo `page`.

---

# 31. SHADOW DOM

Quando houver Web Components ou Shadow DOM:

registre:

```text
Shadow DOM: SIM
```

e investigue a estratégia adequada.

Não confunda elemento invisível na árvore principal com elemento inexistente.

---

# 32. FILE UPLOAD

Para uploads, identifique:

```html
<input type="file">
```

e registre:

- `accept`;
- `multiple`;
- se está oculto;
- botão visual relacionado;
- label;
- comportamento.

Exemplo:

```text
Widget:
FILE_UPLOAD

accept:
.pdf,.doc,.docx

multiple:
false
```

Não faça upload real durante a descoberta sem necessidade.

---

# 33. CHECKBOX

Verifique:

- label;
- estado;
- valor;
- required;
- grupo;
- relação semântica.

Classificação:

```text
CHECKBOX
```

Checkbox normalmente permite seleções independentes.

---

# 34. RADIO

Verifique:

- nome do grupo;
- opções;
- label;
- valor.

Classificação:

```text
RADIO
```

Não trate radio como checkbox.

---

# 35. TOGGLE / SWITCH

Pode ser implementado como:

```text
role="switch"
```

ou checkbox customizado.

Classificação:

```text
TOGGLE
```

Registre seu estado e significado.

---

# 36. CAMPOS READONLY

Ao encontrar:

```html
readonly
```

NÃO tente automaticamente:

```text
type()
fill()
```

Primeiro descubra a função do campo.

Ele pode representar:

- datepicker;
- autocomplete controlado;
- campo calculado;
- campo informativo;
- modal de seleção;
- componente customizado.

---

# 37. DATEPICKER

Campos de data devem ser classificados como:

```text
DATE_NATIVE

DATEPICKER

UNKNOWN_DATE_WIDGET
```

Para `DATEPICKER`, investigue:

- elemento que abre o calendário;
- overlay/modal;
- mês;
- ano;
- navegação;
- dias;
- estados desabilitados;
- formato exibido;
- formato persistido, quando observável sem salvar.

Não assuma implementação específica.

---

# 38. CASO ESPECÍFICO — REACT-DATETIME

Quando houver evidência concreta de `react-datetime`, podem aparecer classes como:

```text
rdtYears
rdtMonths
rdtDays
rdtPrev
rdtNext
rdtYear
rdtMonth
rdtDay
```

Nesse caso, o fluxo pode envolver:

```text
abrir campo
→ selecionar ano
→ selecionar mês
→ selecionar dia
```

Exemplo de seletor observado em algumas implementações:

```text
td.rdtYear[data-value="1986"]

td.rdtMonth[data-value="10"]

td.rdtDay[data-value="1"]:not(.rdtOld):not(.rdtNew)
```

Observação:

```text
data-value do mês pode utilizar índice iniciado em 0.
```

Isso NÃO deve ser aplicado a outros calendários sem confirmação do DOM.

---

# 39. ELEMENTO INSTÁVEL NO PLAYWRIGHT

Durante a investigação, o Playwright pode retornar mensagens como:

```text
waiting for element to be stable
```

Antes de contornar, investigue:

- animação;
- transição;
- overlay;
- elemento errado;
- carregamento;
- rerender;
- mudança contínua de layout.

Não transforme o workaround em implementação automaticamente.

---

# 40. `force: true`

No Cypress:

```javascript
click({ force: true })
```

pode contornar verificações de actionability.

Porém:

> NÃO utilize `force: true` como padrão.

Primeiro descubra por que o elemento não está acionável.

Só utilize se houver justificativa técnica.

Documente o motivo.

---

# 41. `dispatchEvent()`

Em investigações excepcionais, quando a ferramenta de inspeção não conseguir clicar devido a animação/estabilidade, pode ser útil disparar eventos manualmente apenas para descobrir o comportamento.

Exemplo diagnóstico:

```javascript
function clickEl(el) {

  el.dispatchEvent(
    new MouseEvent(
      'mousedown',
      { bubbles: true }
    )
  );

  el.dispatchEvent(
    new MouseEvent(
      'mouseup',
      { bubbles: true }
    )
  );

  el.dispatchEvent(
    new MouseEvent(
      'click',
      { bubbles: true }
    )
  );

}
```

Uso conceitual:

```javascript
await page.evaluate((selector) => {

  const el =
    document.querySelector(selector);

  if (!el) {
    return false;
  }

  el.dispatchEvent(
    new MouseEvent(
      'mousedown',
      { bubbles: true }
    )
  );

  el.dispatchEvent(
    new MouseEvent(
      'mouseup',
      { bubbles: true }
    )
  );

  el.dispatchEvent(
    new MouseEvent(
      'click',
      { bubbles: true }
    )
  );

  return true;

}, 'SELETOR');
```

IMPORTANTE:

Isso é:

```text
TÉCNICA DE DIAGNÓSTICO
```

e não padrão de automação.

Não copie automaticamente esse comportamento para Cypress, Playwright ou Python.

---

# 42. SEGURANÇA DURANTE O MAPEAMENTO

Durante a descoberta:

NÃO clicar em ações que possam gerar efeitos reais.

Exemplos:

```text
Enviar

Salvar

Confirmar

Candidatar

Finalizar

Excluir

Remover

Publicar
```

Se não for possível saber se determinado botão persiste dados:

> NÃO clique.

Peça autorização.

---

# 43. DADOS REAIS

Não invente dados pessoais ou profissionais.

Exemplos:

- CPF;
- RG;
- telefone;
- endereço;
- nascimento;
- salário;
- experiência;
- cargo;
- formação;
- certificações;
- disponibilidade;
- autorização de trabalho;
- LinkedIn;
- GitHub;
- respostas profissionais.

Dados fictícios podem ser utilizados apenas quando:

- forem necessários para revelar comportamento;
- não forem persistidos;
- não provocarem efeito externo.

---

# 44. FIXTURES

Dados de fixtures utilizados apenas para exploração podem ser fictícios.

Dados utilizados para:

```text
preencher
+
salvar
+
submeter
```

em formulário real devem ser fornecidos pelo responsável pela conta.

Nunca crie informações pessoais falsas para concluir candidatura real.

---

# 45. NÃO GERAR O PAGE OBJECT AUTOMATICAMENTE

Após a descoberta:

PARE.

Apresente primeiro:

- mapa neutro;
- tabela;
- widgets;
- seletores;
- estabilidade;
- componentes desconhecidos;
- riscos.

Somente depois de aprovação explícita:

```text
GERAR PAGE OBJECTS
```

---

# 46. PAGE OBJECT — CYPRESS

Após autorização, adapte ao padrão arquitetural do projeto.

Exemplo conceitual:

```javascript
export class PlataformaFormulario {

  nomeCompleto() {
    return cy.get(
      'input[name="fullName"]'
    );
  }

  cidade() {
    return cy.get(
      '[role="combobox"][name="city"]'
    );
  }

}
```

Quando o projeto utilizar getters, preserve o padrão existente.

Exemplo:

```javascript
export class PlataformaFormulario {

  get nomeCompleto() {
    return cy.get(
      'input[name="fullName"]'
    );
  }

}
```

Não imponha um estilo diferente se o projeto já possuir convenção.

---

# 47. PAGE OBJECT — PLAYWRIGHT JAVASCRIPT

Prefira locators semânticos quando forem confiáveis.

Exemplo:

```javascript
export class PlataformaFormulario {

  constructor(page) {

    this.page = page;

    this.nomeCompleto =
      page.getByLabel(
        'Nome completo'
      );

    this.cidade =
      page.getByRole(
        'combobox',
        { name: 'Cidade' }
      );

  }

}
```

---

# 48. PAGE OBJECT — PYTHON COM PLAYWRIGHT

Quando o projeto Python utilizar Playwright:

```python
class PlataformaFormulario:

    def __init__(self, page):

        self.page = page

        self.nome_completo = (
            page.get_by_label(
                "Nome completo"
            )
        )

        self.cidade = (
            page.get_by_role(
                "combobox",
                name="Cidade"
            )
        )
```

---

# 49. PAGE OBJECT — PYTHON COM SELENIUM

Se o projeto Python utilizar Selenium:

> não altere a tecnologia apenas para padronizar com Playwright.

Utilize o framework existente.

Exemplo conceitual:

```python
from selenium.webdriver.common.by import By


class PlataformaFormulario:

    NOME_COMPLETO = (
        By.NAME,
        "fullName"
    )

    CIDADE = (
        By.CSS_SELECTOR,
        '[role="combobox"][name="city"]'
    )
```

---

# 50. CORRESPONDÊNCIA ENTRE OS TRÊS ROBÔS

A responsabilidade funcional deve permanecer equivalente.

Exemplo:

```text
Cypress:
nomeCompleto

Playwright:
nomeCompleto

Python:
nome_completo
```

Apesar da convenção linguística diferente, os três representam:

```text
Nome completo
```

Outro exemplo:

```text
cidadeAutocomplete
```

deve possuir o mesmo significado lógico nos três robôs.

---

# 51. NOMENCLATURA

Use nomes baseados no significado funcional.

Preferir:

```text
nomeCompleto
cidade
tipoDocumento
dataNascimento
curriculo
pretensaoSalarial
```

Evitar:

```text
input1
campo2
elementoA
divX
dropdown3
```

---

# 52. SEPARAÇÃO PAGE OBJECT × AÇÃO

O Page Object deve representar:

> elementos e componentes da página.

A interação complexa pode pertencer a:

```text
commands
actions
services
helpers
flows
```

conforme a arquitetura existente.

Exemplo:

```text
Page Object:
cidadeAutocomplete

Command:
selecionarCidade("Rio de Janeiro")
```

Não coloque toda a lógica de negócio em seletores.

---

# 53. EXEMPLO — DROPDOWN

Mapa:

```json
{
  "tipoDocumento": {
    "widget": "DROPDOWN_CLICK",
    "interaction": [
      "click",
      "selectOption"
    ]
  }
}
```

Possível ação Cypress:

```javascript
selecionarTipoDocumento(tipo) {

  pagina.tipoDocumento
    .click();

  pagina.opcaoTipoDocumento(tipo)
    .click();

}
```

---

# 54. EXEMPLO — AUTOCOMPLETE

Mapa:

```json
{
  "cidade": {
    "widget": "AUTOCOMPLETE",
    "interaction": [
      "focus",
      "type",
      "waitSuggestions",
      "selectSuggestion"
    ]
  }
}
```

O comportamento não deve ser reduzido a:

```text
type("Rio de Janeiro")
```

se o componente exigir seleção da sugestão.

---

# 55. CAMPOS NÃO COMPREENDIDOS

Se não for possível determinar o comportamento:

registre:

```text
Campo:
<nome>

Status:
NÃO DETERMINADO

Motivo:
<explicação>

Próxima investigação:
<ação necessária>
```

Não invente comportamento.

---

# 56. ANTI-ALUCINAÇÃO

Nunca afirmar:

```text
Este campo é dropdown.
```

sem confirmação.

Nunca afirmar:

```text
Este campo aceita texto livre.
```

sem verificar.

Nunca afirmar:

```text
Este seletor é estável.
```

sem evidência.

Nunca afirmar:

```text
Este botão apenas avança.
```

sem confirmar.

Nunca afirmar:

```text
O campo está preenchido.
```

apenas porque existe texto visual.

Quando a evidência não for suficiente:

```text
NÃO DETERMINADO
```

---

# 57. SAÍDA OBRIGATÓRIA DA DESCOBERTA

Produza nesta ordem:

## 1. Resumo da página

## 2. URL inicial

## 3. URL final

## 4. Redirecionamentos observados

## 5. Estrutura da página

## 6. Formulários encontrados

## 7. Campos encontrados

## 8. Widgets identificados

## 9. Componentes customizados

## 10. Campos condicionais

## 11. Formulários multietapa

## 12. Iframes

## 13. Modais / dialogs

## 14. Novas abas / popups

## 15. File uploads

## 16. Campos readonly

## 17. Datepickers

## 18. Mapa neutro do DOM

## 19. Tabela de seletores

## 20. Classificação de estabilidade

## 21. Seletores frágeis

## 22. Campos não determinados

## 23. Riscos

## 24. Recomendações

## 25. Status final

Utilize somente:

```text
MAPEAMENTO COMPLETO

MAPEAMENTO PARCIAL

BLOQUEADO
```

---

# 58. CRITÉRIOS DE ACEITE

O mapeamento somente poderá ser considerado completo se:

1. a página real tiver sido aberta;

2. a URL final tiver sido identificada;

3. redirecionamentos relevantes tiverem sido observados;

4. a estrutura da página tiver sido lida;

5. o DOM real tiver sido inspecionado;

6. campos relevantes tiverem sido identificados;

7. labels tiverem sido correlacionados;

8. significado semântico dos campos tiver sido determinado quando possível;

9. widgets tiverem sido classificados;

10. dropdown e autocomplete tiverem sido diferenciados;

11. select nativo e componente customizado tiverem sido diferenciados;

12. atributos de acessibilidade tiverem sido considerados;

13. atributos específicos de automação tiverem sido considerados;

14. campos readonly tiverem sido investigados;

15. datepickers tiverem sido classificados;

16. file uploads tiverem sido identificados;

17. checkbox, radio e toggle tiverem sido diferenciados;

18. componentes customizados relevantes tiverem sido investigados;

19. campos condicionais tiverem sido registrados;

20. iframes/modais/popups tiverem sido identificados quando existirem;

21. cada seletor recomendado tiver justificativa;

22. cada seletor possuir classificação de estabilidade;

23. seletores frágeis estiverem explicitamente marcados;

24. mapa neutro tiver sido criado;

25. correspondência conceitual entre as três tecnologias estiver preservada;

26. campos desconhecidos estiverem explicitamente registrados;

27. nenhuma submissão real tiver sido realizada;

28. nenhuma ação irreversível tiver sido executada;

29. nenhum dado pessoal tiver sido inventado;

30. valores pessoais existentes não tiverem sido expostos no dump;

31. nenhum seletor tiver sido definido apenas por suposição;

32. Page Objects ainda não tiverem sido criados sem aprovação.

---

# 59. CONDIÇÃO DE PARADA — FASE DE DESCOBERTA

Ao finalizar:

# PARE.

NÃO:

- crie Page Object;
- crie command;
- implemente fluxo;
- altere teste;
- submeta formulário;
- salve candidatura;
- faça refatoração não solicitada.

Apresente:

```text
MAPA NEUTRO
+
TABELA DE ELEMENTOS
+
WIDGETS
+
SELETORES
+
ESTABILIDADE
+
PENDÊNCIAS
```

e aguarde aprovação.

---

# 60. SEGUNDA AUTORIZAÇÃO — GERAÇÃO DOS PAGE OBJECTS

Somente quando eu disser explicitamente algo equivalente a:

```text
Mapeamento aprovado.
Pode gerar os Page Objects.
```

prossiga.

Nesse momento:

1. leia o padrão já existente no projeto;

2. não invente nova arquitetura se já existir uma;

3. gere equivalência para:
   - Cypress;
   - Playwright;
   - Python;

4. preserve os mesmos nomes conceituais;

5. adapte apenas a sintaxe necessária de cada tecnologia;

6. não implemente ainda o fluxo completo do robô sem autorização.

---

# 61. PRINCÍPIO FINAL

O Page Object não deve ser a origem do conhecimento da página.

A origem deve ser:

```text
DOM REAL
    ↓
MAPA NEUTRO VALIDADO
    ↓
PAGE OBJECTS
```

Assim:

- Cypress;
- Playwright;
- Python;

utilizam a mesma interpretação da interface.

Isso reduz:

- duplicação;
- divergências;
- seletores inventados;
- manutenção desnecessária;
- comportamento inconsistente entre os três robôs.

E aumenta:

- rastreabilidade;
- reutilização;
- estabilidade;
- padronização;
- manutenção;
- confiança na automação.
````