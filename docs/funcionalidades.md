# Funcionalidades

## O que já existia

Estado: **No ar**.

| Área | Funcionalidade |
|---|---|
| Busca | Busca por texto com interpretação por IA (siglas expandidas, cargo e local) |
| Busca | Busca usando o perfil salvo |
| Busca | Opção de usar o currículo salvo como pista extra |
| Resultado | Cartão com cargos compatíveis com a formação, prazo de inscrição e localização |
| Resultado | Aviso de "formação futura" para quem ainda vai se formar |
| Resultado | Selo "Novo" para concursos que não apareceram em buscas anteriores |
| Resultado | Link da matéria do concurso e, quando a IA o encontra, link direto da inscrição |
| Informações | Painel por concurso: vagas, remuneração, taxa, datas importantes, cargos e links oficiais, com aviso de que os dados são extraídos automaticamente |
| PDF | Geração e visualização do PDF dos resultados |
| Perfil | Formação, cidade, estado e currículo |
| Administração | Criar usuário, gerar nova senha, renomear, desativar, reativar, excluir e ver informações de uso |
| Administração | O administrador não exclui nem desativa a própria conta |
| Ajuda | Guia "Como pesquisar" em abas (Começar, Onde buscar, Dicas e Entender o resultado), com exemplo ilustrado do cartão de resultado; cada aba, e cada abertura do guia, começa do alto |
| Aparência | Tema claro e escuro |
| Plataformas | App web e app desktop, ambos com o painel Informações |

Regra de produto: não há pesquisas de exemplo clicáveis, porque cada busca tem custo.

## C6a: equivalentes de cargo na busca

Estado: **Ainda não publicado**. Buscas em linguagem natural passam a usar até cinco equivalentes de cargo por formação, com palavras inteiras. Direito encontra Advogado entre os cargos já retornados. O cache global vale 30 dias para equivalentes e 24 horas para lista vazia. Cada busca gera no máximo três formações novas em paralelo, com teto conjunto de seis segundos de espera pelo modelo; falhas do provedor ou cache preservam a busca. “Buscar com meu perfil” continua sem IA; a tabela curta de siglas fica para C17. Veja [alcance, privacidade, falhas e custo estimado](busca-por-perfil.md#c6a-equivalentes-de-cargo) e a [migração reversível](pre-deploy.md#c6a-cache-de-equivalentes-de-cargo). Confira sempre os requisitos no edital.

## C7: ranking e selo por cargo

Estado do C7: **Ainda não publicado**. O [ranking por relevância](busca-por-perfil.md#c7-ranking-por-relevância) preserva a prioridade geográfica e ordena por cargo exato, parcial e prazo, com pontuação e motivo na resposta. A [compatibilidade por cargo na busca](compatibilidade.md#c7-selo-na-resposta-da-busca) usa regras sem IA adicional; sem requisitos individuais, o selo permanece parcial e exige confirmação no edital. A apresentação na interface não é anunciada nesta entrega; a consulta detalhada em Acompanhando mantém suas regras.

## C8: início agregado

Estado do C8: **Ainda não publicado**. `GET /me/inicio` reúne cota do Empresas, concursos acompanhados, Perfil de concursos e total de novidades não lidas da própria conta em uma chamada, sem consumir IA nem marcar avisos como lidos. As rotas individuais continuam disponíveis por uma versão como alternativa de recuperação. A adaptação da interface segue separada. Veja [campos, autenticação, falhas e compatibilidade](navegacao.md#c8-início-agregado).

## C9: cache da fonte e conexões da compatibilidade

Estado do C9: **Ainda não publicado**. O [cache público da PCI](busca-por-perfil.md#c9-cache-da-pci) reutiliza consultas iguais por cinco minutos, com até 500 entradas por processo e cópias independentes antes dos filtros pessoais. Falhas e respostas com avisos não são guardadas; as cotas permanecem iguais. O [pool da compatibilidade](compatibilidade.md#c9-conexões-durante-a-avaliação) ganha margem para avaliações simultâneas e leituras concorrentes, preservando a trava contra execução duplicada e sem prometer capacidade ilimitada.

## C10: links e cidade

Estado do C10: **Ainda não publicado**. O contrato previsto da [verificação de links e consulta por cidade](busca-por-perfil.md#c10-verificação-de-links-e-cidade) conecta ao IP público validado e revalida cada redirecionamento, preservando a identidade HTTPS do destino. Na cidade, tenta a grafia original e só consulta a alternativa normalizada após resposta vazia, no máximo duas chamadas; aceita “Salvador - BA”/“Salvador/BA” e variações “Ilhéus”/“Ilheus” nos dois sentidos, mantendo o cache da PCI. A mudança não garante resultados nem comprova a legitimidade de um concurso. Veja a [validação antes da publicação](pre-deploy.md#c10-links-e-consulta-por-cidade).

## Busca fora da URL

Estado: **Publicado em 13/11/2026**, front **3.13.0**. O texto da busca fica fora da URL da página: texto, modo de busca, uso do currículo e UFs ficam no histórico do navegador (`history.state`). Os botões voltar e avançar e a ação de recarregar preservam o estado da busca, sem depender de `?q=` ou `uf=` na URL.

Um link antigo com `?q=` abre a busca uma vez e a URL é limpa. Copiar o endereço da página não compartilha a busca; quem recebe o link precisa informar os critérios. Esse histórico de navegação é diferente do [histórico de buscas da conta](configuracoes-do-usuario.md#c4-histórico-enxuto), que tem retenção própria no serviço. A mudança na URL da página não significa que o texto deixou de ser enviado à API para executar a busca.

## C1: limites do PDF de concursos

Estado: **Ainda não publicado**. O lote C1 valida os dados enviados à rota autenticada `POST /pdf` antes de gerar o PDF dos resultados de concursos. O PDF continua disponível; a correção acrescenta os limites abaixo ao pedido de geração. Cada nome entre crases identifica um campo da integração.

| Campo | Máximo | Unidade ou significado |
|---|---|---|
| `results` | 100 | Resultados por PDF |
| `query` | 500 | Caracteres da busca |
| `extracted_summary` | 2000 | Caracteres do resumo |
| `titulo` | 500 | Caracteres por título |
| `cargos` | 100 | Itens por lista de cargos de cada resultado |
| `cargos_compativeis` | 100 | Itens por lista de cargos compatíveis de cada resultado |
| `cargos[]` | 200 | Caracteres por nome de cargo |
| `cargos_compativeis[]` | 200 | Caracteres por nome de cargo compatível |
| `uf` | 32 | Caracteres da UF |
| `regiao` | 100 | Caracteres da região |
| `datas.fim` | 100 | Caracteres do prazo de inscrição |
| `data_formacao_futura` | 7 | Caracteres da data de formação futura |
| `noticia.link` | 2048 | Caracteres do endereço da matéria |

Os campos de título até link pertencem a cada resultado. São aceitos até **100 links**, **um por resultado**, somente endereços válidos com **HTTP ou HTTPS**. O link pode estar ausente ou vazio. Campo acima do limite ou link inválido retorna **422** (dados não aceitos), sem gerar o PDF; a integração precisa corrigir o pedido. A mesma validação protege chamadas diretas ao gerador, e metadados extras não usados no documento são descartados.

Esse contrato não altera o limite de **15 páginas** do PDF enviado como currículo ao [Empresas](empresas.md#e1--currículo), nem os materiais PDF de E3/E4. Veja também a [validação antes da publicação](pre-deploy.md#c1-validação-antes-da-publicação).

## Acrescentado na Rodada 1 (novembro de 2026)

Estado: **No ar**, em https://augustusai.com.br/iaprovale/ (versão grátis na raiz; o modo por convite é build alternativo).

| Funcionalidade | Estado |
|---|---|
| Novo sistema visual (paleta, fontes, forma e espaçamento) | **No ar** |
| Navegação lateral no computador e barra inferior no celular | **No ar** |
| Barra lateral recolhível no computador, com a escolha lembrada | **No ar** |
| Busca com rótulo visível, validação e estados claros (inicial, carregando, resultados, vazio, erro) | **No ar** |
| Estado da busca: na versão anterior, guardado na URL; no front 3.13.0, no histórico do navegador, com recarga preservada (veja [Busca fora da URL](#busca-fora-da-url)) | **Publicado em 13/11/2026** (3.13.0) |
| Área de cursos patrocinados, visível só antes de uma pesquisa e sempre marcada como "Patrocinado" | **No ar** |
| Espaços "Anuncie aqui!" para cursinhos e instituições: faixa na home (entre "Como funciona" e "O que você recebe") e cartão na vitrine do app quando não há curso configurado. Só espaço reservado, marcado como "Publicidade", sem anúncio de terceiro | Pronto, aguardando publicação |
| Cartão de resultado com prazo em evidência e um botão principal ("Ir para a inscrição" ou "Ver o concurso") | **No ar** |
| Checklist para completar o perfil | **No ar** |
| Administração com abas (Usuários e Solicitações), blocos, rótulos visíveis e ações sensíveis separadas | **No ar** |
| Tela de login no novo visual, com suporte ao gerenciador de senhas do aparelho (veja [Decisões](decisoes.md)) | **No ar** |
| Home pública nova com demonstração do produto e movimento ao rolar a página | **No ar** |
| Chamada principal da home com Pedir acesso e Ver como funciona, e Login no cabeçalho | **No ar** |
| Marca "IAprovale by Augustus" em duas linhas, igual em todas as telas | **No ar** |
| Ícone do IAprovale (ramo com o nome embaixo) ao adicionar o site à tela de início do celular | **No ar** |
| Pedido de acesso por chat, com verificação do nome de usuário em tempo real (veja [Pedido de acesso](pedido-de-acesso.md)) | **No ar** |
| Janela de 5 minutos de dúvidas com IA depois do pedido, contada no servidor | **No ar** |
| Aviso ao responsável, no Telegram, quando chega um pedido novo | **No ar** |
| Aprovar ou recusar o pedido pelos botões do Telegram, com botão que abre o WhatsApp com o login pronto | **No ar** |
| Aprovar sem enviar: o sistema devolve usuário, senha provisória e mensagem prontos; caixa com "Copiar mensagem" e "Abrir no WhatsApp" | No ar |
| Troca obrigatória da senha provisória no primeiro acesso, com tela própria | No ar |
| Limite de 8 perguntas ou 5 minutos de dúvidas depois do pedido, o que vier primeiro | **No ar** |
| Aba Solicitações na Administração: aprovar ou recusar pedidos (veja [Solicitações de acesso](solicitacoes-de-acesso.md)) | **No ar** |
| Login mostrado uma única vez ao aprovar, com botão de copiar, para o responsável enviar à pessoa | **No ar** |
| Páginas de privacidade e termos de uso | **No ar** |
| Testes automatizados de interface e de acessibilidade: home, chat de pedido de acesso, app, administração, solicitações, configurações e login | **No ar** (todos passando) |
| Melhorias de acessibilidade: bordas dos campos com contraste maior, foco visível e nunca coberto por cabeçalho ou menu, diálogos que deixam o resto da tela inerte, nomes específicos para botões e links, links externos que avisam "abre em nova aba", Perfil com rótulos, preenchimento automático e erros anunciados, título da página por seção, suporte a cores forçadas e aviso de 1 minuto restante no chat de dúvidas | **No ar** |
| Acessibilidade ainda não confirmada: falta auditoria com leitor de tela e tecnologia assistiva reais (2 critérios) e há 1 critério pendente por decisão de produto. Não declaramos conformidade nem certificação (veja [Decisões](decisoes.md)) | Pendente |

## Configurações do usuário

Estado: **No ar**. Detalhes em [Configurações do usuário](configuracoes-do-usuario.md).

| Funcionalidade | Estado |
|---|---|
| Tela de Configurações, separada do Perfil, igual para administrador e usuário | **No ar** |
| Troca de senha, de usuário e de telefone, sempre pedindo a senha atual | **No ar** |
| Telefone com formatação automática enquanto se digita | **No ar** |
| Tema claro, escuro ou automático e tamanho do texto em 3 níveis | **No ar** |
| Preferência "usar o meu currículo" por padrão na busca (vale neste aparelho) | **No ar** |
| Histórico das últimas 10 buscas, com os resultados de cada uma e botão de apagar | **No ar** |
| Baixar os próprios dados, apagar o currículo e "Sair de todos os aparelhos" | **No ar** |
| Excluir a própria conta em duas etapas: senha na tela e resposta "SIM" no WhatsApp | Temporariamente indisponível: o WhatsApp da empresa está fora do ar |
| Excluir a própria conta com o WhatsApp desligado: pedido enviado ao responsável pelo Telegram, que confirma em dois passos | No ar |
| Aviso ao responsável quando o usuário troca o telefone | **No ar** |
| Contato com a equipe pelo WhatsApp, em Ajuda | **No ar** |
| Bloco de saldo e uso de buscas ("em breve") | **No ar** (aviso de que chega em breve) |

## Privacidade e retenção (novembro de 2026)

| Funcionalidade | Estado |
|---|---|
| Páginas de Privacidade e Termos revisadas contra o que o serviço faz hoje (LGPD), com controlador, encarregado, direitos, retenção e transferência internacional | **No ar** (a validação por advogado segue pendente) |
| Registro do aceite dos Termos e da Política no cadastro grátis: data e hora, IP e versão aceita, guardados enquanto a conta existir e apagados com ela | Pronto, aguardando publicação |
| Limpeza automática diária: pedidos de acesso pendentes ou recusados, avisos ao responsável, exclusões já decididas e buscas do histórico com mais de 90 dias (e, a partir da 2.9.0, eventos de busca com mais de 90 dias) | **No ar** |
| Resumo diário no Telegram do responsável, às 19h (horário de São Paulo): cadastros do dia (grátis e por convite) e total de contas, buscas e custo do dia e do mês. Só envia se houve novidade no dia (cadastro novo, busca ou avaliação nova); sem novidade não manda nada | No ar desde 6 de novembro de 2026 (só com novidade desde a v2.10.1) |
| Quem é usuário do IAprovale nunca recebe prospecção da empresa | **No ar** |
| Redefinir a senha de alguém, na Administração, encerra as sessões dela | **No ar** |
| C5: [sessões guardadas apenas como hash](configuracoes-do-usuario.md#c5-proteção-das-sessões); migração exige entrar novamente uma vez | **Ainda não publicado** (implementado; cuidados antes da publicação em [pré-deploy](pre-deploy.md#c5-migração-e-reversão)) |
| Proteção contra tentativas repetidas de senha também com tentativas simultâneas | **No ar** |
| Bloqueio de login por origem e por usuário: quem erra muito é barrado sem tirar o dono da conta do ar | No ar |
| Proteções contra uso abusivo do pedido de acesso e do pedido de exclusão de conta | **No ar** |

## Stats do administrador

Estado: **no ar**. Detalhes em [Stats](stats-do-administrador.md).

| Funcionalidade | Estado |
|---|---|
| Stats em **Hoje** com buscas, custo e pessoas ativas por hora, a partir de um registro de eventos de busca (horário, custo e tipo, sem conteúdo; apagado em 90 dias e com a conta; migração v3_15 já aplicada) | **No ar** |
| Aba **Estatísticas** (antes Stats), só para administradores, no fim da barra de navegação: seletor Hoje, Este mês, 7, 30 e 90 dias, seis números-resumo e gráficos de cadastros, buscas, custo acumulado e notas, com tabela alternativa | **No ar** |

## Avisos e prazos publicados; e-mail ligado

Estado: **No ar**, com envio de e-mail ligado em produção desde **12/11/2026**, além de Novidades, alertas e acompanhamento dentro do site. Os recursos são gratuitos para todas as contas, com os limites abaixo, sem depender de plano pago. O e-mail é opcional na conta e pode ser adicionado em Configurações. Novidades continua disponível como alternativa quando não houver e-mail verificado, a preferência estiver desligada ou faltar cota ou entrega.

### Cadastro e e-mail na conta

- O e-mail é **opcional**, com confirmação por **código de 6 dígitos**, válido por **10 minutos**, em Configurações. No cadastro com endereço informado, se a cota global do dia acabar, a conta é criada com e-mail pendente, para confirmar depois em Configurações, sem impedir o acesso. Um endereço não confirmado não reserva o e-mail. Endereço e código não são enviados à IA. Veja [Cadastro e confirmação](versao-gratis.md#cadastro-com-e-mail).
- E-mail na conta com preferência para receber avisos. A troca só vale após confirmar o endereço novo; é possível remover o endereço e desligar os avisos. Detalhes em [Configurações](configuracoes-do-usuario.md).

### Cotas de e-mail

- Cotas **globais por dia**, compartilhadas por todas as contas: **200 envios de códigos** e **100 envios de avisos**, renovadas à meia-noite de Brasília. Códigos podem usar a sobra da cota de avisos; avisos nunca usam a cota de códigos. Assim, os códigos podem ocupar até os 300 envios do dia, reduzindo o que resta para avisos.
- O e-mail de boas-vindas usa a categoria de códigos e compartilha essa cota. Sem cota, a confirmação fica para depois e o serviço informa quando é possível pedir outro código. O cadastro pode terminar com e-mail pendente, como descrito acima.

### Caixa de Novidades

- Caixa de Novidades dentro do site, com avisos de concursos novos, prazos e mensagens do sistema. Cada item tem título, texto, data e estado de leitura; pode trazer o concurso e seu link.
- A pessoa pode filtrar as não lidas e marcar os itens como lidos individualmente ou todos de uma vez. O contador de não lidas considera o total da conta, independentemente do filtro e do limite da lista. Desligar o e-mail mantém as Novidades no site.
- Novidades lidas são apagadas após **6 meses (mais de 183 dias desde a criação)**, na limpeza diária. As não lidas são mantidas até serem lidas e atingirem esse prazo, ou até a exclusão da conta.

### Alertas e concursos acompanhados

- Até **10 alertas por conta**, com nome, uso do perfil e/ou termo de busca e uma lista de UFs. É necessário informar um termo ou usar o perfil. A lista de UFs segue as mesmas regras do [filtro de UF](filtro-de-uf.md); vazia não impõe UFs explícitas, permitindo inferência pelo termo da busca. É possível criar, editar, pausar, reativar e excluir alertas.
- Ao criar ou reativar um alerta, a primeira busca bem-sucedida registra os concursos encontrados como **linha de base**, sem avisá-los. Os alertas avisam só concursos que aparecerem daí para a frente, com até **10 avisos por alerta por dia** na rotina prevista de uma execução diária; excedentes ficam pendentes para os próximos dias. Um concurso não gera avisos repetidos para a mesma conta, mesmo se combinar com mais de um alerta.
- Acompanhar até **50 concursos por conta**, guardando título e link da matéria do concurso. A lista é ordenada pela próxima data. Acompanhar de novo o mesmo concurso não duplica o item; é possível deixar de acompanhar.
- As datas vêm da leitura automática das informações do concurso: fim das inscrições, fim do pedido de isenção e data da prova. Se a leitura falhar, o acompanhamento continua salvo; datas podem ficar indisponíveis até uma atualização posterior.
- Lembretes em **D-3 e D-1** (três dias e um dia antes) de cada uma dessas datas aparecem em Novidades e no resumo por e-mail, quando habilitado. Dependem de uma data disponível. Os dados podem estar incompletos ou desatualizados: confirme sempre no edital e no site oficial do concurso.

### Rotina diária e modelos de e-mail

- Execução diária às **07:00, horário de Brasília** (São Paulo, `America/Sao_Paulo`). Consulta alertas ativos, sem consumir a cota de buscas da pessoa e sem gravar buscas no histórico, respeitando a linha de base e os limites acima.
- Atualiza as datas dos concursos acompanhados no máximo uma vez por dia e cria os lembretes de prazo. Repetir a rotina não duplica os avisos no mesmo dia.
- Modelos de código de confirmação, boas-vindas e resumo diário em **HTML e texto**, enviados via **Brevo SMTP**, com remetente **IAprovale <avisos@augustusai.com.br>**. O resumo reúne concursos novos e lembretes de prazo, traz um link para o aplicativo e orienta como desligar os avisos nas Configurações.
- Boas-vindas só depois de confirmar o e-mail e de a conta existir, inclusive quando a confirmação ocorrer depois em Configurações. Sem cota, fica para a manhã seguinte, com prioridade **antes dos resumos**; se a cota continuar esgotada, permanece pendente. Não há fila retroativa de boas-vindas para o período anterior à ativação do envio.
- No máximo **um e-mail-resumo por pessoa por dia**, somente com conta ativa, e-mail verificado, preferência de avisos ativada e envio disponível; sem novidades, não há resumo. A fila prioriza quem recebeu há mais tempo e inclui os avisos adiados por falta de cota. O primeiro resumo considera somente as Novidades do dia, sem carregar todo o histórico.
- Se houver falha ou interrupção com entrega incerta, o e-mail não é reenviado automaticamente: a mensagem pode não chegar, mas os avisos continuam em Novidades no site.
- E-mail, preferência, Novidades, alertas e concursos acompanhados entram na exportação e são apagados com a conta. A Brevo (Sendinblue SAS, França) atua como operador no envio, com transferência internacional de dados. Veja [Dados e privacidade](configuracoes-do-usuario.md) e o estado dos [textos legais 1.3](versao-gratis.md#termos-de-uso-e-política-de-privacidade).

A atualização da [estimativa de custo de IA](stats-do-administrador.md#estimativa-de-custo) está **no ar desde 12/11/2026**, junto da etapa 3, sem recalcular o histórico.

## C12: calendário dos acompanhados

Estado: **Ainda não publicado em produção**. Implementado no backend; o botão de calendário ainda depende da interface. Não altera o estado dos alertas e acompanhados já publicados.

Cada pessoa poderá gerar um link pessoal `.ics` com os concursos que acompanha, para assinar no Google Agenda, Apple Calendário ou Outlook. O link é uma credencial de leitura: compartilhe somente com o aplicativo escolhido. Veja [geração, troca e revogação](configuracoes-do-usuario.md#c12-link-pessoal-do-calendário).

Cada data conhecida de fim das inscrições, fim da isenção e prova gera um evento de dia inteiro. As datas ausentes não geram eventos; sem datas, o calendário é válido e vazio. Inclui datas passadas. Usa só as datas armazenadas, sem consulta externa, sem IA e sem consumir cota. Confirme os prazos no edital: o calendário não garante que as informações estejam completas ou atualizadas.

O arquivo se chama `acompanhados.ics`, com nome de calendário “Concursos acompanhados”, títulos, links públicos e prazos; não exporta nome nem e-mail da pessoa. Os títulos são tratados para não quebrar o arquivo, com escape de texto, remoção de caracteres de controle e divisão de linhas preservando os acentos.

Correções de data preservam o identificador do evento; deixar de acompanhar remove o concurso do calendário fornecido pelo link. A importação é uma fotografia do arquivo naquele momento. Para acompanhar mudanças, use a assinatura do link; a atualização e a remoção no aplicativo escolhido dependem da frequência de sincronização dele. Revogar o link impede novas leituras, mas não apaga cópias já importadas.

A leitura tem limite de 30 consultas por endereço IPv4 ou rede IPv6 /64 em 60 segundos, inclusive tentativas com credencial inválida. Excesso retorna HTTP 429 e orienta aguardar 60 segundos; pessoas na mesma rede podem compartilhar esse limite. Limitação conhecida: o controle é por processo e em memória, reinicia com o processo e não é compartilhado entre instâncias. Não é uma cota persistente global.

A liberação depende da [migração e proteção do link nos registros de acesso](pre-deploy.md#c12-calendário-e-proteção-do-link).

## C12: contrato de alerta por busca

Estado da documentação C12: **Ainda não publicado em produção**. O contrato de alerta por `termo` + `ufs` já existe no backend, sem exigir perfil; o atalho visual para usar a busca atual ainda depende da interface. Os alertas publicados e suas regras de linha de base e avisos continuam descritos acima.

Para integrações autenticadas da própria conta, `POST /me/alertas` aceita, por exemplo:

```json
{"nome": "Professor em SP", "termo": "professor", "ufs": ["SP"], "usar_perfil": false}
```

É necessária sessão autenticada; não é o token do calendário nem uma credencial da API de parceiros. A criação retorna 201, com `id`, `nome`, `termo`, `ufs`, `usar_perfil`, `ativo`, `criado_em` e `ultimo_envio_em`.

- `nome` é obrigatório, de 1 a 60 caracteres; `termo` aceita até 200 caracteres e é obrigatório quando `usar_perfil` é falso. Nome e termo têm espaços das extremidades removidos.
- `ufs` aceita até 27 siglas válidas, normaliza maiúsculas e espaços e remove duplicatas. Lista vazia não impõe UFs explícitas: permite inferência pelo termo da busca, conforme o [filtro de UF](filtro-de-uf.md).
- `usar_perfil` assume falso e `ativo` assume verdadeiro quando omitidos. São até dez alertas por conta; exceder retorna 409. Repetir o pedido cria outro alerta: não deduplica.
- `GET /me/alertas` lista os alertas da conta; `PATCH /me/alertas/{id}` edita e `DELETE /me/alertas/{id}` exclui. Um alerta de outra conta retorna 404, sem permitir leitura ou alteração.

## Compatibilidade entre perfil e cargos — etapa 3

Estado: **No ar**, conforme a publicação informada em 12/11/2026, em **Alertas > Acompanhando**. A consulta autenticada `GET /concursos/{id}/compatibilidade` usa o link da própria lista de acompanhados e o cache de Informações. Cada cargo recebe `combina`, `parcial` ou `nao_combina`, com motivo e lacunas; sem formação/escolaridade no perfil, o resultado geral é `sem_perfil`, sem chamadas externas ou cota.

As regras decidem a compatibilidade educacional; a IA só explica lacunas dos casos parciais, sem decidir o nível. Uma avaliação nova com cargos consome uma busca e conta para o feedback do plano grátis; acerto do cache de compatibilidade não cobra novamente. Há reserva durável antes de chamadas externas, e qualquer exceção encerra a tentativa como falha. O cache entra na exportação e é apagado com a conta. Veja [Compatibilidade](compatibilidade.md) para limites e recuperação de falhas; confirme sempre os requisitos no edital.

O envio de e-mail já está ligado. Os registros de dependências e a distinção entre textos legais 1.3 do convite e variante grátis ainda não ativada estão em [Preparação da publicação](pre-deploy.md).

## IAprovale Empresas — E1–E5

Estado: **No ar** desde **12/11/2026** (backend ef7dc58 ou posterior; site 0ccfa9d ou posterior). [Empresas](empresas.md) descreve upload PDF/DOCX/TXT até 5 MB e perfil, currículo e original opcional compactados, nota de compatibilidade calculada em Python e explicação sob demanda. O perfil de currículo longo usa contrato `perfil-2` e teto de resposta de 3.500 tokens. A cota própria é de 17 chamadas de IA ou US$ 0,01 por conta/dia, o que vier primeiro; acertos de cache não consomem.

Texto, perfil, original guardado, explicações, materiais gerados e uso entram na exportação; excluir a conta apaga os dados privados do Empresas. As chamadas de IA vão somente ao DeepSeek; contatos reconhecidos são removidos antes da geração do perfil, sem garantia de anonimização. Os textos legais devem refletir a transferência internacional; a validação jurídica continua pendente.

[E3/E4](empresas-e3-e4.md) entregam currículo ATS em PDF/Word/copiar e roteiro de entrevista por vaga, gratuitos no teste, com cobrança desligada; preços e meio de pagamento pendentes. [E5](empresas-vagas.md) oferece busca, panorama e prévia gratuita sem IA no índice local. A [aba Carreira e a navegação](navegacao.md) estão publicadas; Carreira aparece somente quando `/empresas/cota` responde. Veja as dependências em [Preparação da publicação](pre-deploy.md#empresas-em-produção).

**Ainda não publicado — C2:** a [busca por palavra e ordenação](empresas-vagas.md#busca-por-palavra-e-ordenação--c2) exige todos os termos como palavras completas, preserva a comparação sem acentos e prioriza termos no título antes da paginação. O [cache do índice](empresas-vagas.md#reutilização-do-índice--c2) reutiliza a leitura enquanto o arquivo não muda, mantendo a verificação de validade de 72 horas a cada consulta e a indisponibilidade quando o arquivo está ausente ou inválido.

## Ainda por construir

| Funcionalidade | Estado |
|---|---|
| Verificação do telefone por código enviado por WhatsApp, para provar que o número é da própria pessoa | Pronto, desligado por enquanto: depende do WhatsApp da empresa. Até lá, o número troca direto com a senha atual |
| Login expira após 30 dias sem uso | **No ar** |
| WhatsApp só pode ser trocado uma vez a cada 15 dias | **No ar** |
| Cobrança, planos e regras de reembolso | **Decidido** (adiado) |
