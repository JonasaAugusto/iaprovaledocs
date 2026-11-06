# Busca pelo perfil, filtro por nível e regra de cota

Estado: **pronto, aguardando publicação** (backend 2.10.0). Exige a migração `migrate_v3_16_feedbacks_fk` antes do backend.

## Por que mudou

Quem tinha só a escolaridade no perfil (por exemplo Fundamental e Médio, em Rio de Janeiro/RJ) recebia zero resultados em "Buscar com meu perfil". A IA de interpretação transformava a escolaridade em termo de busca ("fundamental médio") e o filtro procurava essas palavras no nome do cargo. O campo de nível do concurso (Ensino Médio, Fundamental / Médio, Superior...) vem da fonte e não era usado. A mensagem de zero resultados ainda sugeria "tente em alguns dias", e a busca vazia gastava uma das buscas do dia e contava para a avaliação.

## Buscar com meu perfil

- Frases reconhecidas (sem diferenciar maiúsculas, acentos nem pontuação): "Buscar com meu perfil", "buscar pelo meu perfil", "usar meu perfil", "meu perfil", "concursos para mim" e variações próximas.
- A consulta é **determinística e não chama a IA**: custo zero e o mesmo resultado a cada vez. Usa a UF e a cidade do perfil:
  - mobilidade **local** com cidade: só os concursos da cidade;
  - mobilidade **estado** (ou local sem cidade): cidade mais a lista da região, mantendo só a UF do perfil;
  - **qualquer** ou sem mobilidade: cidade mais a região, ordenados por proximidade (mesma UF, mesma região, resto);
  - sem UF no perfil: lista geral.
- Em seguida entra o filtro por nível.

## Filtro por nível

- O nível do perfil vem da escolaridade marcada (fundamental, médio, técnico, superior; "pós" conta como superior). Se há graduação ou pós preenchida, o perfil também conta como superior. Valem exatamente os níveis marcados: quem marcou só Médio não recebe concurso só de Superior.
- O concurso entra se o campo de nível dele citar **qualquer** nível do perfil ("Fundamental / Médio / Técnico / Superior" serve para quem marcou Médio).
- Quem tem graduação, técnico, pós ou áreas continua com o casamento por cargo; os dois somam-se, e os concursos que casam por cargo aparecem primeiro, com os cargos compatíveis. Concursos que entram só pelo nível mostram os primeiros cargos.
- Só concursos com inscrição aberta.

## Escolaridade nunca vira termo

- A instrução da IA proíbe colocar escolaridade em termo, cargo ou formação mencionada. O código também descarta qualquer termo que seja só nível ("fundamental médio", "nível superior", "ensino médio").
- Busca com nível citado ("concurso de nível superior no RJ") usa o nível citado no lugar do perfil e a UF da própria busca.
- Antes de responder "defina sua formação", o sistema tenta o nível da escolaridade. A mensagem só aparece se o perfil não tem nem formação nem nível.

## Zero resultados

- Mensagem nova e curta: "Não encontrei vagas abertas para essa busca. Tente um cargo (ex.: Administrativo) ou veja os concursos da sua cidade por nível." Sem UF no perfil, o fim vira "ou informe sua cidade no perfil."
- Busca com zero resultados **não conta** na cota diária do plano grátis, no contador de avaliação (a cada N buscas) nem no histórico de buscas.
- Se a busca vazia gastou a IA, o custo real continua somado no dia (painel e Stats), sem somar busca nem resultados. Para não virar laço de chamadas pagas, essas buscas entram num teto técnico de 20 por hora por usuário (resposta 429). O anti-rajada de 10 buscas por minuto continua valendo para todas. A consulta por perfil não gasta IA e não entra nesse teto.
- O limite diário do plano grátis segue valendo para qualquer busca com resultado.

## Exclusão de conta e avaliações

- A exclusão feita pelo administrador agora apaga também as avaliações, o histórico de buscas, as verificações de telefone, os avisos ao responsável e o pedido de acesso da conta, igualando a exclusão pela própria pessoa. Antes ficavam avaliações órfãs.
- A migração `migrate_v3_16_feedbacks_fk` apaga as avaliações de contas que não existem mais e cria a chave estrangeira de `feedbacks.user_id` para `users.id` com exclusão em cascata. É idempotente, não mexe em avaliações de contas existentes e, se a criação da chave falhar, mostra o erro sem desfazer nada.

## Riscos e ideias

- Quem tem graduação passa a receber também concursos de nível superior de qualquer área pela busca por perfil (depois dos que casam por cargo). Mais resultados, menos precisão.
- Mobilidade vazia ou "qualquer" não restringe a UF: concursos de outros estados aparecem depois dos locais. Filtro rígido de UF fica como ideia, não foi feito.
- Concurso sem nível informado pela fonte só entra se casar por cargo.

## Testes

Backend: `tests/test_search_perfil.py` (frases, nível, mobilidade, IA que falha se chamada, termo de nível, cota, avaliação, histórico e teto), `tests/test_exclusao_avaliacoes.py` (exclusão pelo administrador e migração em SQLite e Postgres), com amostra real da fonte em `tests/fixtures/mcp_perfil_rj.json`.
