# Eventos de busca (tabela `search_events`)

Estado: **pronto, aguardando publicação** (backend 2.9.0, site 3.9.0). **Exige migração** (`scripts/migrate_v3_15_eventos_busca.py`), aditiva e idempotente.

## Para que serve

`search_usage` guarda o uso de buscas só por dia. Para a aba Stats mostrar, em **Hoje**, buscas, custo e pessoas ativas **por hora**, cada busca concluída com sucesso grava um evento com o horário. É a única finalidade dessa tabela.

## O que é guardado

| Campo | Conteúdo |
|---|---|
| `id` | número do evento |
| `user_id` | a conta (chave estrangeira para `users`, com exclusão em cascata) |
| `criado_em` | data e hora da busca (UTC, exibida no horário de Brasília) |
| `custo_usd` | custo estimado da busca em US$ |
| `origem` | `normal` ou `curriculo` (busca com o toggle de currículo) |

Não são guardados: o texto da busca, os resultados, o IP nem qualquer dado pessoal além do `user_id`. Índices em `criado_em` e em (`user_id`, `criado_em`).

## Quando o evento é gravado

No mesmo ponto em que `search_usage` é atualizado: depois de uma busca que respondeu com sucesso e conta como uso e custo (a administradora e o administrador também contam, como em `search_usage`). Busca com falha (502) não grava nada. Se a gravação do evento falhar (por exemplo, a tabela ainda não existe), a busca segue normalmente e o erro vai para o log em uma linha, sem conteúdo.

## Retenção e privacidade

- **90 dias.** A limpeza diária (`scripts/purge_retencao.py`) apaga os eventos com mais de 90 dias, como o histórico de buscas.
- **Exclusão da conta.** Os eventos saem junto com a conta (exclusão explícita no código e `ON DELETE CASCADE` no banco).
- **Exportação de dados** (`/conta/exportar`): inclui `eventos_de_busca`, com o horário, o tipo e o custo de cada busca dos últimos 90 dias.

## Como a aba Stats usa

- **Hoje:** buscas, custo e pessoas ativas por hora (24 pontos, horas sem busca valem 0, hora de São Paulo) vêm de `search_events`. Cada pessoa conta uma vez por hora.
- **Este mês, 7, 30 e 90 dias:** continuam em `search_usage`. Os dois nunca são misturados no mesmo gráfico.
- O campo `buscas_por_hora_disponivel` da resposta de `GET /admin/stats` diz ao site se mostra os gráficos por hora (tabela existe) ou o aviso de "só total do dia" (tabela ausente ou backend antigo). No dia da migração, buscas anteriores à tabela ficam só no total do dia; o campo `buscas_por_hora_parcial` faz a tela avisar que a soma por hora fica abaixo do total.
- Os totais do período (cartões) seguem sempre de `search_usage`.

## Ordem de publicação

1. Backup do banco. 2. Migração. 3. Backend 2.9.0. 4. Site 3.9.0. O backend funciona antes da migração (formato antigo de `/admin/stats`, sem erro nas buscas), e o site funciona com o backend antigo (mantém o aviso).

## Texto para a Política de Privacidade do plano grátis (versão 1.2)

Sugestão de trecho, para aplicar na versão 1.2 dos textos legais (seção de dados coletados, e a retenção na seção correspondente):

> **Registro de eventos de busca.** A cada busca concluída, guardamos o horário, o custo estimado da busca e o tipo (normal ou com currículo), associados à sua conta. Não guardamos o conteúdo da sua pergunta nesse registro, nem os resultados, nem o seu IP. Usamos essas informações para medir o uso do serviço e o custo de operá-lo (base legal: legítimo interesse, LGPD, art. 7º, IX). Esses registros são apagados automaticamente depois de 90 dias e junto com a sua conta, e constam do arquivo de exportação dos seus dados.

Observação: o histórico das últimas buscas (com o texto), já descrito na Política, é um registro separado e continua com as regras próprias.
