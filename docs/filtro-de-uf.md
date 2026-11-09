# Filtro rígido de UF

Estado: **pronto para revisão** (backend 2.11.0 e site 3.10.0, branches `feat/filtro-uf`, sem tag, sem merge e sem publicação).

## Como era

- A busca recebia só o texto (`query`) e o interruptor do currículo. Não existia campo de UF.
- A UF só entrava de três jeitos, nenhum rígido:
  - a IA tirava uma UF do texto ("enfermeiro em SP") e a repassava à fonte. Só vale para pesquisar por termo e por cargo; a fonte então devolve a UF e os nacionais, mas se a IA não preenchia a UF nada restringia;
  - perfil com mobilidade **local** ou **estado** injetava a UF do perfil na pesquisa por termo e por cargo;
  - perfil com UF e busca sem local só **ordenava** (mesma UF, mesma região, resto). Todos os estados apareciam.
- "Lista geral" (sem termo) só aceita região: trazia a região inteira, de vários estados. Mobilidade "qualquer" ou vazia, na busca pelo perfil, também só ordenava.
- Nenhum caminho aceitava várias UFs, e a busca pelo perfil (2.10.0) dispensava nacionais ao restringir pela UF do perfil.

## Como fica

- `POST /search` aceita `ufs`, lista opcional de siglas (`["SP", "RJ"]`). Maiúsculas ou minúsculas, sem repetição; sigla que não existe dá erro 422. Sem `ufs` (ausente ou vazia) **nada muda**.
- Com `ufs`, voltam só:
  - concursos de alguma das UFs escolhidas;
  - concursos **nacionais** (vagas no país todo).
  Nunca de outro estado, mesmo que a fonte devolva.
- A UF escolhida vale mais que a UF que a IA tirou do texto e mais que a mobilidade do perfil.
- Vale na busca com IA e em "Buscar com meu perfil" (nesta, as UFs escolhidas substituem o local do perfil).
- Na busca pelo perfil com mobilidade **local** ou **estado**, os nacionais também entram (uma consulta extra à lista geral da fonte).
- Ordem: concursos das UFs na ordem pedida, nacionais depois.
- O resumo da busca mostra, por exemplo, "UF: SP, RJ (e nacionais)".

## Como o concurso nacional é identificado

A fonte (PCI Concursos) marca nacionais com `uf` vazio e `regiao` = NACIONAL (hoje, por exemplo, INB e Câmara dos Deputados). Só isso conta como nacional. Concurso sem UF **e** sem região nacional (dado ausente ou estranho) fica de fora quando há filtro.

## Zero resultados

Com o filtro ligado e nenhum concurso, a resposta diz isso: "Não encontrei concursos abertos em AM (nem concursos nacionais) para essa busca. O filtro de UF está ligado, então não mostrei concursos de outros estados. Remova ou troque a UF para ampliar a busca." Com várias UFs: "nas UFs AM, RR e AC". Continua sem contar na cota, no histórico nem na avaliação.

## Seletor na tela de busca (site 3.10.0)

- Abaixo do campo de busca há o botão **Onde**, que mostra o resumo ("Brasil todo", "BA, MG, SP" ou "5 estados") e abre os 27 estados em chips agrupados por região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul). Pode marcar vários; vazio = Brasil todo.
- A escolha vai no pedido de busca como `ufs` e na URL como `&uf=SP,RJ`: recarregar e voltar/avançar mantêm o filtro. Sem estados, o pedido é igual ao de antes.
- O seletor recolhe ao buscar. "Nova busca" limpa os estados junto com o texto.
- Resultados mostram "Só BA, MG, SP e concursos nacionais." Se a busca com estados não acha nada, a tela diz que os estados continuam valendo e oferece **Buscar no Brasil todo**.
- Acessível: cada chip é um botão com estado marcado/desmarcado, nome completo do estado para leitores de tela, alvo de 44 px, marcado = preenchido (não depende só de cor). Claro e escuro, sem vermelho nem azul.

## Decisões do dono (09/11/2026)

1. Seletor de UF na tela de busca, com várias UFs e vazio = Brasil todo (feito, site 3.10.0).
2. Federais com sede em DF (`uf` = DF) continuam contando como DF, não como nacionais: quem escolhe SP não os recebe.
3. Busca pelo perfil com mobilidade local ou estado inclui os nacionais (feito, backend 2.11.0).

## Pendências

- A UF citada no texto da busca ("enfermeiro em SP") segue como antes: a fonte já devolve a UF e os nacionais, mas sem filtro final no servidor. Só a UF enviada em `ufs` é rígida.
- A API de parceiros (`/v1/search`) não ganhou o campo.

## Testes

Site: verificação em navegador (desktop e celular, claro e escuro, 68 verificações com a API simulada). Backend, `tests/test_search_filtro_uf.py`: UF única, várias UFs, nacionais incluídos, sem UF, zero resultados, fonte que devolve outro estado, UF escolhida contra IA e mobilidade, busca pelo perfil, validação do campo e repasse pelo endpoint.
