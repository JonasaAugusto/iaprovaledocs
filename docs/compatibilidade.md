# Compatibilidade entre perfil e cargos (etapa 3)

Estado: **No ar**, conforme a publicação informada em **12/11/2026**. A tela fica em **Alertas > Acompanhando**, com resultado por cargo, motivo e lacunas. Esta etapa complementa os [concursos acompanhados](funcionalidades.md#alertas-e-concursos-acompanhados). Veja a [navegação publicada](navegacao.md#alertas) e o registro da dependência da [migração v3_22](pre-deploy.md).

## Consulta e resposta

- Consulta autenticada: `GET /concursos/{id}/compatibilidade`, para um concurso da própria conta. Usa o link salvo na própria lista de acompanhados e reaproveita o cache de Informações do concurso. Não recebe um link arbitrário nessa consulta. Concurso não acompanhado pela pessoa retorna 404.
- A resposta traz `geral`, `cargos` e `gerado_em`. Cada cargo tem `nome`, `nivel`, `motivo` e `falta` (lista do que precisa ser comprovado ou esclarecido).

| Resultado | Onde aparece | Significado |
|---|---|---|
| `combina` | Cargo e geral | Formação e escolaridade informadas combinam com as exigências educacionais disponíveis. |
| `parcial` | Cargo e geral | Faltam dados ou há requisitos que precisam de confirmação no edital. |
| `nao_combina` | Cargo e geral | Há incompatibilidade explícita de formação ou escolaridade. |
| `sem_perfil` | Somente geral | O perfil não informa escolaridade, graduação, técnico nem pós; a lista de cargos vem vazia. |

O resultado geral é `combina` se pelo menos um cargo combina; é `nao_combina` se todos os cargos avaliados não combinam; nos demais casos é `parcial`, inclusive quando a leitura não traz cargos. `sem_perfil` não é um nível por cargo.

## C7: selo na resposta da busca

Estado: **Ainda não publicado**. A [resposta da busca](busca-por-perfil.md#c7-ranking-por-relevância) passa a incluir `compatibilidade_cargos`, calculada por regras locais, sem IA, sem chamadas adicionais e sem cobrança adicional por essa avaliação. Isso não torna a busca por texto inteira gratuita nem dispensa sua interpretação por IA.

Cada cargo recebe `nome`, `nivel`, `motivo` e `falta`. O contrato admite `combina`, `parcial` e `nao_combina`, mas a fonte da busca fornece nomes sem requisitos individuais; por isso, os selos atuais permanecem `parcial`, orientando a conferir as exigências. O nível global do concurso não é atribuído a todos os cargos, nem o nome do cargo permite inferir requisitos. A avaliação usa a formação concluída do perfil, mesmo se a busca mencionar outra formação ou houver correspondência com formação futura.

A correspondência textual em `cargos_compativeis` não comprova habilitação. O selo não garante elegibilidade: confirme no edital a formação exigida e os demais requisitos. Lista de cargos vazia produz lista de compatibilidade vazia.

Essa anotação na busca é distinta da consulta detalhada de **Alertas > Acompanhando**, descrita nesta página, que lê informações do concurso e tem cota e cache próprios conforme as regras abaixo. O C7 não anuncia a apresentação do selo na interface.

## Regras e papel da IA

- Regras em Python comparam a formação concluída e a escolaridade com exigências explícitas de cada cargo. Formação em andamento não equivale a diploma concluído. Escolaridade e requisitos gerais do concurso não são herdados por todos os cargos.
- Ausência de requisitos, alternativas ambíguas e condições não educacionais ficam para confirmação. Não se deduz formação pelo nome do cargo nem se declara equivalência entre cursos distintos.
- A IA nunca decide o nível: o DeepSeek só complementa o motivo e as lacunas dos casos `parcial`. Mesmo que o modelo sugira um nível, ele não é utilizado; as lacunas apontadas pelas regras são preservadas. A leitura automática das informações também pode usar IA.
- O resultado é uma ajuda para leitura, sem garantia de elegibilidade: confirme sempre no edital e no portal oficial, inclusive registro profissional, experiência e demais condições.

## Cota, cache e falhas

- O resultado fica em cache persistente por usuário, concurso e versão do perfil. Salvar o perfil cria uma nova versão, mesmo com o mesmo conteúdo. O acerto do cache de compatibilidade não consome nova busca, feedback ou chamada externa.
- Uma avaliação nova com cargos consome **uma busca normal** e incrementa o contador da avaliação do plano grátis, compartilhando as **17 buscas por dia** e a avaliação a cada **5 buscas**. Também conta quando a comparação é toda por regras. O cache de Informações não dispensa esse consumo: ele evita repetir a leitura, mas ainda pode haver uma avaliação nova do perfil.
- `sem_perfil` retorna sem chamadas externas e sem consumir cota. Leitura concluída sem cargos também não consome busca nem feedback, embora o custo de IA já realizado continue registrado.
- Há reserva durável antes de qualquer chamada externa, inclusive antes de ler a matéria ou extrair informações. A reserva respeita cota e avaliação pendente. Pedidos simultâneos para a mesma chave não executam a avaliação duas vezes: em processamento retorna 409; falha na leitura retorna 502.
- Após a reserva, qualquer exceção encerra a tentativa como falha. A falha não consome busca nem feedback; custos já informados pelo provedor são preservados. Resultado, busca consumida e feedback são confirmados juntos.
- Reservas abandonadas expiram e falhas permitem nova tentativa mais tarde, sem repetir custos já registrados. Uma execução ainda ativa não é sobreposta. Não há repetição automática da explicação pela IA na mesma tentativa. Se uma interrupção ocorrer antes de receber a telemetria do provedor, esse custo permanece desconhecido.
- A estimativa inclui a leitura e a explicação, mesmo se a extração que gastou tokens for inválida, conforme as [tarifas e a contagem de cache](stats-do-administrador.md#estimativa-de-custo-ainda-não-publicado).

## C9: conexões durante a avaliação

Estado: **Ainda não publicado**. O pool do banco, conjunto de conexões reutilizáveis pelo serviço, passa a admitir 12 conexões persistentes e até 12 extras por processo. O ajuste dá espaço às avaliações de compatibilidade enquanto aguardam o provedor de IA e às leituras concorrentes, como autenticação.

A transação de leitura continua encerrada antes da chamada de IA. Cada avaliação ativa mantém uma conexão para a trava que impede executar duas vezes a mesma combinação de pessoa, concurso e versão do perfil; encerrar a transação não significa liberar essa conexão. Um pedido duplicado em processamento continua retornando 409. As regras de cota, cache por perfil e contabilização de custos permanecem as descritas acima.

O cenário de validação usa 12 avaliações simultâneas com provedor fictício mantido em espera e outras leituras em paralelo, sem erro 500 por esgotamento do pool nesse cenário. Isso não é garantia de capacidade ilimitada nem de disponibilidade do provedor real. Mais processos multiplicam a demanda de conexões; a capacidade total depende também dos limites do banco. Este ajuste não muda a tela nem exige migração de dados.

## Dados e privacidade

O cache da própria pessoa entra na exportação de dados em `compatibilidades` e é apagado com a conta, tanto na exclusão pela pessoa quanto pelo administrador. O registro inclui a versão do perfil, o estado da tentativa, a data e a resposta, quando disponível.

Para explicar lacunas, o serviço envia ao DeepSeek os campos educacionais do perfil (escolaridade, graduação, técnico e pós) e os requisitos dos cargos parciais; não envia o currículo completo nesse pedido. Esses campos podem conter informações pessoais inseridas pela pessoa. A comparação não usa nome de usuário, telefone ou e-mail como critérios.

Avaliação nova com cargos gera um [evento de busca](eventos-de-busca.md) do tipo `normal`, sem guardar o conteúdo do perfil nesse evento. A retenção de 90 dias dos eventos e do histórico de buscas não define o prazo do cache de compatibilidade.
