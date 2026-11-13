# Filtro rígido de UF

Estado: seleção de UFs **publicada em 09/11/2026** (backend 2.11.0, site 3.10.0, docs 1.12.0). A UF citada no texto como filtro rígido e o campo `ufs` em `POST /v1/search` estão **prontos, aguardando publicação do backend 2.12.0** (seção "UF citada no texto e API de parceiros").

## Como era

- A busca recebia só o texto (`query`) e o interruptor do currículo. Não existia campo de UF.
- A UF só entrava de três jeitos, nenhum rígido:
  - a IA tirava uma UF do texto ("enfermeiro em SP") e a repassava à fonte. Só vale para pesquisar por termo e por cargo; a fonte então devolve a UF e os nacionais, mas se a IA não preenchia a UF nada restringia;
  - perfil com mobilidade **local** ou **estado** injetava a UF do perfil na pesquisa por termo e por cargo;
  - perfil com UF e busca sem local só **ordenava** (mesma UF, mesma região, resto). Todos os estados apareciam.
- "Lista geral" (sem termo) só aceita região: trazia a região inteira, de vários estados. Mobilidade "qualquer" ou vazia, na busca pelo perfil, também só ordenava.
- Nenhum caminho aceitava várias UFs, e a busca pelo perfil (2.10.0) dispensava nacionais ao restringir pela UF do perfil.

## Como fica

- `POST /search` aceita `ufs`, lista opcional de siglas (`["SP", "RJ"]`). Maiúsculas ou minúsculas, sem repetição; sigla que não existe dá erro 422. Sem `ufs` (ausente ou vazia), a seleção não se aplica; na 2.11.0 nada mudava, e na 2.12.0 vale a UF citada no texto (ver abaixo).
- Com `ufs`, voltam só:
  - concursos de alguma das UFs escolhidas;
  - concursos **nacionais** (vagas no país todo).
  Nunca de outro estado, mesmo que a fonte devolva.
- A UF escolhida vale mais que a UF que a IA tirou do texto e mais que a mobilidade do perfil.
- Vale na busca com IA e em "Buscar com meu perfil" (nesta, as UFs escolhidas substituem o local do perfil).
- Na busca pelo perfil com mobilidade **local** ou **estado**, os nacionais também entram (uma consulta extra à lista geral da fonte).
- Ordem: concursos das UFs na ordem pedida, nacionais depois.
- Federais com sede em DF aparecem só para quem escolhe DF (decisão do dono); nacionais genuínos entram sempre.
- O resumo da busca mostra, por exemplo, "UF: SP, RJ (e nacionais)".

## UF citada no texto e API de parceiros (backend 2.12.0, aguardando publicação)

- **Texto da busca.** Quando o usuário não envia `ufs` (ausente ou lista vazia), a UF que a IA extrai do texto ("enfermeiro em SP", "nível médio em SP ou no RJ") passa a ser filtro rígido, com a mesma regra da seleção: só as UFs citadas e os nacionais, mesmo que a fonte devolva outro estado. Vale também para a busca só por nível e por cidade. A IA pode devolver várias UFs; siglas que não existem ou em formato errado são descartadas, sem derrubar a busca.
- **Prioridade.** `ufs` enviado vence a UF do texto e o perfil. Não são combinados.
- **O que não vira filtro.** A UF que a mobilidade do perfil injeta na pesquisa continua só restringindo a consulta à fonte, como antes. Uma região sem estados citados ("no Sul") também não vira lista de UFs.
- **Resumo e zero resultados.** O resumo da busca mostra "UF: SP (e nacionais)" e a mensagem de zero resultados é a do filtro de UF, como na seleção explícita. Se a pergunta for sobre terceiros, o pedido de reformulação continua igual.
- **Limitação.** Quem escreve uma cidade ou estado no texto passa a receber só aquele estado e os nacionais; a UF depende da leitura da IA. Quem quiser outro recorte pode enviar `ufs` ou remover o estado do texto.
- **`POST /v1/search`.** Aceita o campo opcional `ufs` com a mesma validação e prioridade de `POST /search`: até 27 siglas, maiúsculas ou minúsculas, sem repetição; sigla inválida, valor que não seja lista ou mais de 27 itens dão erro 422. Sem `ufs`, a resposta segue a regra do texto acima. Não há mudança de banco nem de outras rotas.

## Como o concurso nacional é identificado

A fonte (PCI Concursos) marca nacionais com `uf` vazio e `regiao` = NACIONAL. Mas ela também marca assim concursos que são regionais (por exemplo, a MGS, empresa de Minas Gerais, e os Comandos de Distrito Naval da Marinha). Por isso a regra é em duas partes:

1. Concurso marcado NACIONAL pela fonte **só é nacional se o título ou o órgão não indicar estado nem região**.
2. Se indicar, vale a UF indicada, como se a fonte tivesse dado essa UF. O texto indica UF quando traz: nome de estado ("Minas Gerais"), "Distrito Federal", nome de capital ("Manaus"), sigla de UF em maiúsculas ("SP/RJ") ou Nordeste, Sudeste, Centro-Oeste. "Pará" só conta com P maiúsculo (para não confundir com a preposição "para"). Se citar mais de um estado, vale para todos.

Distritos Navais seguem uma tabela pequena, pela **sede oficial** do comando:

| Distrito Naval | Sede | UF |
|---|---|---|
| 1º DN | Rio de Janeiro | RJ |
| 2º DN | Salvador | BA |
| 3º DN | Natal | RN |
| 4º DN | Belém | PA |
| 5º DN | Rio Grande | RS |
| 6º DN | Ladário | MS |
| 7º DN | Brasília | DF |
| 8º DN | São Paulo | SP |
| 9º DN | Manaus | AM |

Não há lista de exceções por concurso: só essas duas regras. Concurso sem UF **e** sem região nacional (dado ausente ou estranho) fica de fora quando há filtro.

**Limitações conhecidas**

- INB, Câmara dos Deputados e TRF3 (Tribunal Regional Federal da 3ª Região) não trazem estado no título: continuam nacionais pela regra da fonte e aparecem para qualquer UF, mesmo que a vaga seja só em Brasília ou em outra sede. Não inventamos lotação. O site avisa que "nacionais" são os que a fonte marca assim.
- Distrito Naval vale para a UF da sede; a jurisdição pode cobrir outros estados (o 1º DN, por exemplo, também atende Minas Gerais), e quem escolhe só esse outro estado não o vê.
- Um concurso nacional que cita uma cidade ou estado só de passagem no título seria tratado como regional. Hoje isso não aconteceu nos dados lidos.

## Como a busca consulta a fonte

- **Busca pelo perfil com UFs:** usa `pesquisar_concursos` com `uf` (a fonte devolve a UF e os nacionais), com os termos do perfil (graduação, técnico, pós, áreas) e depois termos genéricos de cargo (`analista`, `técnico`, `assistente`, `prefeitura`, `professor`), porque a fonte não aceita busca sem termo. `listar_concursos` (no máximo 30 por chamada) fica só como complemento (lista geral), sem repetir concursos. Antes, só a lista era usada e estados pequenos (AM, AP, RR) ficavam sem resultado.
- **Teto de chamadas:** até 3 termos por UF e no máximo 10 pesquisas no total. Com muitas UFs escolhidas, usa 1 termo por UF e a cobertura é menor (limitação conhecida; escolher poucas UFs traz mais resultados).
- **Em paralelo:** as consultas por UF rodam ao mesmo tempo (até 12 por vez, 10 s de limite cada). Se a fonte falhar para uma UF, a falha é registrada (só ferramenta e UF, nunca o texto da busca) e as outras UFs seguem; se todas falharem, a busca informa indisponibilidade como antes. A ordem do resultado não depende de qual resposta chega primeiro.
- **Tempos medidos ao vivo na fonte (09/11/2026):** 1 UF cerca de 0,5 a 1,7 s; 5 UFs cerca de 1,0 a 1,8 s; 27 UFs cerca de 0,8 a 2,0 s (a fonte oscila; era cerca de 13 s com 27 UFs em fila).

## Zero resultados

Com o filtro ligado e nenhum concurso, a resposta diz isso: "Não encontrei concursos abertos em AM (nem concursos nacionais) para essa busca. O filtro de UF está ligado, então não mostrei concursos de outros estados. Remova ou troque a UF para ampliar a busca." Com várias UFs: "nas UFs AM, RR e AC". Continua sem contar na cota, no histórico nem na avaliação.

## Seletor na tela de busca (site 3.10.0)

- Abaixo do campo de busca há o botão **Onde**, que mostra o resumo ("Brasil todo", "BA, MG, SP" ou "5 estados") e abre os 27 estados em chips agrupados por região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul). Pode marcar vários; vazio = Brasil todo.
- A escolha vai no pedido de busca como `ufs`. Na versão anterior, fica na URL como `&uf=SP,RJ`. **Publicado em 13/11/2026**, o front **3.13.0** passa a guardar as UFs no histórico do navegador (`history.state`), fora da URL; recarregar e voltar/avançar mantêm o filtro. Sem estados, o pedido é igual ao de antes. Veja [Busca fora da URL](navegacao.md#busca-fora-da-url).
- O seletor recolhe ao buscar. "Nova busca" limpa os estados junto com o texto.
- Resultados mostram "Só BA, MG, SP e concursos nacionais (os marcados assim pela fonte)." O texto de ajuda do seletor diz o mesmo e avisa que a vaga pode ser em uma sede específica, como Brasília. Se a busca com estados não acha nada, a tela diz que os estados continuam valendo e oferece **Buscar no Brasil todo**.
- Acessível: cada chip é um botão com estado marcado/desmarcado, nome completo do estado para leitores de tela, alvo de 44 px, marcado = preenchido (não depende só de cor). Claro e escuro, sem vermelho nem azul.

## Decisões do dono (09/11/2026)

1. Seletor de UF na tela de busca, com várias UFs e vazio = Brasil todo (feito, site 3.10.0).
2. Federais com sede em DF (`uf` = DF) continuam contando como DF, não como nacionais: quem escolhe SP não os recebe. Nacionais genuínos entram sempre.
3. Busca pelo perfil com mobilidade local ou estado inclui os nacionais (feito, backend 2.11.0).

## Pendências

- Até a publicação do backend 2.12.0, a UF citada no texto da busca ("enfermeiro em SP") segue como antes: a fonte já devolve a UF e os nacionais, mas sem filtro final no servidor, e `POST /v1/search` ainda não aceita `ufs`.

## Testes

Site: verificação em navegador (desktop e celular, claro e escuro, API simulada). Backend: `tests/test_search_filtro_uf.py` (UF única, várias UFs, nacionais, sem UF, zero resultados, fonte que devolve outro estado, UF escolhida contra IA e mobilidade, busca pelo perfil, validação e endpoint) e `tests/test_search_filtro_uf_nacionais.py` com registros reais da PCI como fixtures (MGS, Marinha, INB, Câmara, TRF3), detecção por texto, paralelismo com limite, ordem determinística, falha parcial, timeout e busca pelo perfil via `pesquisar_concursos`. Backend 2.12.0 (pronto, não publicado): os mesmos arquivos de teste e `tests/test_partner_search.py` cobrem UF extraída em cargo, pesquisa e cidade, várias UFs, prioridade de `ufs`, siglas inválidas vindas da IA, busca por nível, zero resultados e repasse e validação de `ufs` no `/v1/search`. Teste ao vivo contra a fonte (2.11.0): nenhum concurso de estado não escolhido apareceu, e MGS e distritos navais só aparecem para a UF certa.
