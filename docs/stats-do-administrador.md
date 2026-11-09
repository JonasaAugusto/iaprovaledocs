# Stats (aba só do administrador)

Estado: **no ar**, incluindo buscas, custo e pessoas ativas por hora de **Hoje** (backend 2.10.1, site 3.9.0, migração v3_15 já aplicada; ver [Eventos de busca](eventos-de-busca.md)).

A aba **Stats** é o último item da barra de navegação (embaixo no celular, na lateral no computador) e só aparece para administradores. Quem não é administrador não vê a aba, não abre a tela e recebe 403 no endpoint. Serve para acompanhar a evolução do uso.

## O que a tela mostra

- **Período**, em um seletor com cinco opções: Hoje, Este mês, 7 dias (abre assim), 30 dias e 90 dias. Os dias valem no horário de Brasília. Hoje vai de 0h até agora; Este mês, do dia 1 até hoje (sem dias futuros); 7, 30 e 90 dias terminam hoje, inclusive.
- **Seis números:** cadastros no período (grátis e por convite), total de contas, buscas (com pessoas ativas, média por pessoa ativa e quantas contas chegaram ao limite diário), custo estimado em US$, nota média das avaliações e vagas restantes do teto de cadastros grátis. Total de contas e vagas restantes são sempre globais; os demais seguem o período.
- **Gráficos:** cadastros por dia (empilhado, grátis e convite), buscas por dia, custo estimado acumulado e distribuição das notas de 1 a 5. Em **Hoje**, os cadastros aparecem por hora (24 pontos). Com a tabela de eventos de busca (3.9.0), **Hoje** também mostra buscas por hora, custo por hora e pessoas ativas por hora (cada pessoa conta uma vez por hora). Sem ela, buscas e custo de hoje aparecem só como total do dia, com um aviso.
- **Tabela** com os mesmos números, em "Ver os números em tabela" (alternativa aos gráficos para leitor de tela).
- Estados claros de carregando, erro (com "Tentar de novo") e vazio. Os números são pedidos de novo toda vez que a aba é aberta.

Nenhum dado pessoal aparece: só contagens, somas e médias.

## Como funciona

- Endpoint `GET /admin/stats?periodo=hoje|mes|7|30|90` (só administrador; 401 sem login, 403 para os demais). Também aceita `dias` (1 a 180) no lugar de `periodo`.
- Cadastros vêm de `users` (data de criação e `origem_cadastro`), buscas, pessoas ativas e custo de `search_usage` (e, em Hoje por hora, de `search_events`), avaliações de `feedbacks`. Uma consulta agregada por série.
- Os gráficos são SVG desenhados pelo próprio app, sem biblioteca nem recurso externo, nos temas claro e escuro, com dica ao passar o mouse ou tocar, e rótulos para leitor de tela.
- Cores: plano grátis e por convite têm cores próprias e validadas para daltonismo (verde e ouro no claro; ouro e verde no escuro); séries únicas usam um tom neutro. Sem vermelho nem azul.

## Testes

Backend: `tests/test_stats.py`. Site: `e2e/stats-test.mjs` (aba oculta para quem não é admin, cinco períodos, estados, 390 e 1280 px, claro e escuro, acessibilidade, sem rolagem lateral, sem requisição externa).
