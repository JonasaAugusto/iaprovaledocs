# Filtro rígido de UF

Estado: **pronto para revisão** (backend 2.11.0, branch `feat/filtro-uf`, sem tag, sem merge e sem publicação). O site ainda não tem onde escolher a UF na busca.

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
- Ordem: concursos das UFs na ordem pedida, nacionais depois.
- O resumo da busca mostra, por exemplo, "UF: SP, RJ (e nacionais)".

## Como o concurso nacional é identificado

A fonte (PCI Concursos) marca nacionais com `uf` vazio e `regiao` = NACIONAL (hoje, por exemplo, INB e Câmara dos Deputados). Só isso conta como nacional. Concurso sem UF **e** sem região nacional (dado ausente ou estranho) fica de fora quando há filtro.

## Zero resultados

Com o filtro ligado e nenhum concurso, a resposta diz isso: "Não encontrei concursos abertos em AM (nem concursos nacionais) para essa busca. O filtro de UF está ligado, então não mostrei concursos de outros estados. Remova ou troque a UF para ampliar a busca." Com várias UFs: "nas UFs AM, RR e AC". Continua sem contar na cota, no histórico nem na avaliação.

## Pendências de decisão

- O app ainda não tem seletor de UF na busca (a UF aparece só no perfil). Para o filtro aparecer para quem usa, é preciso desenhar o seletor (uma ou várias UFs) na tela de busca.
- Federais com sede em DF (UF = DF) contam como DF, não como nacionais: quem escolher SP não os recebe.
- Mobilidade do perfil (local, estado) e UF citada no texto continuam como na 2.10.0 (a fonte já inclui os nacionais na pesquisa por UF; na busca pelo perfil com mobilidade local ou estado os nacionais não entram). Só a UF escolhida no campo `ufs` é rígida.
- A API de parceiros (`/v1/search`) não ganhou o campo.

## Testes

`tests/test_search_filtro_uf.py` (backend): UF única, várias UFs, nacionais incluídos, sem UF, zero resultados, fonte que devolve outro estado, UF escolhida contra IA e mobilidade, busca pelo perfil, validação do campo e repasse pelo endpoint.
