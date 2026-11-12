# Changelog da documentação do IAprovale

Versões [SemVer](https://semver.org/lang/pt-BR/) alinhadas ao que a documentação descreve: maior = mudança de produto,
menor = funcionalidade documentada, correção = ajuste de texto.

## [1.16.0] - Não publicado
- Corrigido o nome da aba para **Estatísticas** (barra, título e acessibilidade; o endereço continua `#stats`). Documentados o uso do currículo do Perfil na Carreira, o botão Preencher com currículo, os avisos `role="alert"` sempre presentes para leitor de tela e o app sem scripts de CDN (site de 12/11/2026).
- Registrado o [envio de e-mail ligado em produção desde 12/11/2026](docs/funcionalidades.md#avisos-e-prazos-publicados-e-mail-ligado), via Brevo SMTP, remetente IAprovale <avisos@augustusai.com.br>. E-mail opcional nas Configurações, código de 6 dígitos válido por 10 minutos, boas-vindas e resumo diário das 07:00 de São Paulo somente com endereço verificado e preferência de avisos ativa para resumos.
- Preservadas as cotas globais de 200 códigos e 100 avisos por dia, com uso da sobra dos avisos somente pelos códigos. Sem cota no cadastro com endereço informado, conta criada com e-mail pendente; boas-vindas adiada e Novidades disponível como alternativa sem entrega.
- Documentada a Brevo (Sendinblue SAS, França) como operador e a transferência internacional. [Textos legais 1.3 do convite](docs/versao-gratis.md#termos-de-uso-e-política-de-privacidade) vigentes em 12/11/2026, com e-mail opcional, Brevo e Carreira; variante grátis em `scripts/legal-gratis/v1_3.py` ainda não ativada, sem presumir aceite novo. Validação jurídica pendente.
- README, configurações, navegação, roadmap, decisões e [pré-deploy](docs/pre-deploy.md) alinhados; regressões locais atualizadas para estado de produção, provedor, distinção legal e links. Esta entrada ainda não publica as docs, não altera a versão do produto e preserva as entradas históricas abaixo.

## [1.15.0] - Não publicado
- Estado do [Empresas E1–E5](docs/empresas.md) atualizado para **no ar desde 12/11/2026** (backend ef7dc58 ou posterior; site 0ccfa9d ou posterior). Esta entrada registra a atualização das docs, ainda não publicada, sem atribuir uma nova versão ao produto em produção.
- Documentada a [busca de vagas E5](docs/empresas-vagas.md): filtros, paginação, panorama, prévia gratuita sem IA, índice local diário às 06:00 de São Paulo, coleta parcial aceita, indisponibilidade 503 sem índice, validade de 72 horas, catálogo de 176 empresas e cobertura pública limitada por `robots.txt`.
- Documentadas as [telas e a navegação](docs/navegacao.md): Carreira condicionada à resposta de `/empresas/cota`, Currículo e vaga, Buscar vagas, nota com régua e explicação, materiais por vaga em PDF/Word/copiar e roteiro de entrevista. Compatibilidade por cargo publicada em Alertas > Acompanhando; barra, topo, seção Empresas na home, menu no celular e fragmentos das abas descritos.
- Correção de currículo longo documentada: teto de resposta de 3.500 tokens e contrato `perfil-2`, preservando os limites de entrada e os avisos de corte.
- Incorporada a entrada antes sem SemVer de [E3/E4](docs/empresas-e3-e4.md), preservando geração conservadora, cota e armazenamento. Retirados da tabela vigente os valores antes previstos (R$ 1,49 e R$ 2,99): preços e meio de pagamento seguem pendentes, cobrança desligada e produtos gratuitos no teste, com cota compartilhada de 17 chamadas ou US$ 0,01 por conta/dia, o que vier primeiro.
- Índice, funcionalidades, configurações, referências de cota/eventos, roadmap, decisões e preparação da publicação alinhados ao estado publicado. E-mail continua desligado e revisão jurídica pendente. Acrescentadas regressões locais para publicação, E5, navegação, currículo longo e pendências comerciais; as entradas anteriores preservam o estado histórico da documentação.

## [1.14.0] - Não publicado
- Documentado o [IAprovale Empresas E1/E2](docs/empresas.md), implementado no backend 2.15.0 e ainda não publicado: endpoints autenticados, currículo e original opcional compactados, compatibilidade calculada em Python, explicação sob demanda e cache. Cota própria de 17 chamadas ou US$ 0,01 por dia (o que vier primeiro), exportação/exclusão, envio ao DeepSeek com remoção de contatos antes do perfil e limites dessa remoção, transferência internacional e revisão dos textos legais. Índice, funcionalidades, configurações, decisões, roadmap e dependências v3_23/pypdf alinhados; regressões locais incluídas, sem anunciar nova versão ou publicação.
- Documentada a [compatibilidade entre perfil e cargos (etapa 3)](docs/compatibilidade.md), implementada no backend e ainda não publicada: consulta autenticada sobre acompanhados, níveis conservadores por cargo, IA só para explicar lacunas, cache por versão do perfil, reserva antes de chamadas externas, cota e feedback compartilhados e recuperação de falhas. Exportação e exclusão abrangem o cache; índice, funcionalidades, decisões, roadmap e referências de cota e eventos alinhados.
- Registrado o aceite `gratis-1.2` já implementado para novos cadastros, preservando versões anteriores, e a correção de acentos nas mensagens, sem alterar campos ou botões. Tudo ainda não publicado. Ver [Versão grátis](docs/versao-gratis.md).
- Explicitadas as tarifas DeepSeek de 11/11/2026 por milhão de tokens (fora de pico: US$ 0,003/0,15/0,60; pico: US$ 0,006/0,30/1,20 para entrada com cache, sem cache e saída), a estimativa sempre de pico e a correção de cache zero/ausente/nulo e retentativas, preservando o histórico. Ainda não publicado; ver [Stats](docs/stats-do-administrador.md).
- Documentadas as [migrações v3_17 a v3_22 e a ordem da publicação](docs/pre-deploy.md), todas antes do reinício, incluindo a reexecução da v3_18 quando necessária e o e-mail desligado até a chave SMTP. Acrescentadas regressões locais do contrato, tarifas, estado de publicação e ordem das migrações.

## [1.13.0] - Não publicado
- Documentado o pacote de avisos e prazos, ainda não publicado: cadastro com e-mail obrigatório quando o envio estiver configurado, confirmação por código de 6 dígitos e conta com e-mail pendente quando não houver cota. Endereço pendente não reserva o e-mail. Cotas globais diárias de 200 códigos e 100 avisos, com aproveitamento da sobra de avisos apenas pelos códigos. Hoje o envio permanece desligado. Ver [Versão grátis](docs/versao-gratis.md) e [Configurações](docs/configuracoes-do-usuario.md).
- Caixa de Novidades, até 10 alertas por perfil/termo/UFs e até 50 concursos acompanhados com lembretes D-3/D-1 de inscrição, isenção e prova. Alertas criam linha de base ao criar/reativar e avisam só concursos futuros, até 10 avisos por alerta por dia. Rotina às 07:00 de Brasília, modelos de e-mail em HTML e texto e boas-vindas após confirmar o endereço; sem cota, adiado para a manhã seguinte com prioridade. Novidades lidas são apagadas após 6 meses (183 dias desde a criação); não lidas ficam. Tudo ainda não publicado. Ver [Funcionalidades](docs/funcionalidades.md).
- Atualização ainda não publicada da estimativa de custo de IA com preços atuais da DeepSeek e correção da contagem de cache; histórico preservado e estimativa conservadora, sem equivalência à fatura. Ver [Stats](docs/stats-do-administrador.md). Adicionada verificação local em Python para o contrato documentado e os links relativos.
- Exportação e exclusão da conta passam a incluir esses dados. Termos de Uso e Política de Privacidade previstos na versão 1.2, ainda não publicada; preservado o registro da versão 1.1 em vigor. Ver [Versão grátis](docs/versao-gratis.md). Índice, decisões e roadmap alinhados ao escopo gratuito.

## [1.12.2] - Não publicado
- Adicionada seção de contato no [README](README.md), com o e-mail do responsável e os perfis de Instagram da Augustus AI e de Jonas.

## [1.12.1] - 2026-11-09
- Documentado o que o backend 2.12.0 traz (no ar desde 2026-11-09): a UF extraída do texto da busca vira filtro rígido quando o usuário não envia `ufs`, e `POST /v1/search` aceita `ufs` com a mesma validação e prioridade. Ver `docs/filtro-de-uf.md`.

## [1.12.0] - 2026-11-09
- Filtro rígido de UF (backend 2.11.0): com UFs escolhidas só voltam concursos delas e os nacionais, mensagem própria de zero resultados e como o nacional é identificado. Seletor de estados na busca (site 3.10.0), com várias UFs e vazio = Brasil todo; busca pelo perfil com mobilidade local ou estado inclui os nacionais. Ver `docs/filtro-de-uf.md`. Aguardando revisão e publicação.

## [1.11.2] - 2026-11-09
- Estado de Stats e dos eventos de busca atualizado para no ar (backend 2.10.1, site 3.9.0, migração v3_15 já aplicada). Confirmada a publicação da exclusão de avaliações com a conta pelo administrador (migração v3_16).

## [1.11.1] - 2026-11-07
- Resumo diário do Telegram (19h) só é enviado se houve novidade no dia: cadastro novo, busca ou avaliação nova (backend 2.10.1). Sem novidade, o dia é registrado e nada é enviado.

## [1.11.0] - 2026-11-06
- Busca pelo perfil sem IA, filtro por nível de escolaridade, escolaridade nunca vira termo, regra de cota para buscas sem resultado, mensagem nova de zero resultados e exclusão de conta apagando avaliações (backend 2.10.0). Ver `docs/busca-por-perfil.md`. No ar; migração v3_16 já aplicada.

## [1.10.0] - 2026-11-06
- Tabela de eventos de busca (backend 2.9.0, site 3.9.0, migração v3_15): Stats em Hoje com buscas, custo e pessoas ativas por hora. Retenção de 90 dias, exclusão com a conta, inclusão na exportação de dados e trecho proposto para a Política de Privacidade do plano grátis (versão 1.2). Ver `docs/eventos-de-busca.md`. No ar; migração v3_15 já aplicada.

## [1.9.0] - 2026-11-06
- Aba Stats do administrador (backend 2.8.0, site 3.8.0): períodos Hoje, Este mês, 7, 30 e 90 dias, números-resumo e gráficos de uso. Ver `docs/stats-do-administrador.md`. No ar: backend v2.8.0 e site v3.8.0.

## [1.8.2] - 2026-11-06
- Aviso de fase de teste encurtado para "Plataforma em fase de teste" (site v3.6.2); `preparo-comercial.md` atualizado.

## [1.8.1] - 2026-11-06
- O botão Mostrar da senha usa um campo espelho em vez de trocar o tipo do campo (compatibilidade com Safari/iOS). Site 3.6.1. No ar.

## [1.8.0] - 2026-11-06
- Preparo para uso comercial: descrição e título da home para o plano grátis, prévia de link (og/twitter e imagem 1200x630), canonical, robots, sitemap, JSON-LD, página 404, aviso de fase de teste na home e no app, aviso de dados sensíveis no currículo; exportação de feedbacks em markdown e custo no resumo do Telegram. Ver `docs/preparo-comercial.md`.

## [1.7.1] - 2026-11-06
- Espaços "Anuncie aqui!" (faixa na home e cartão na vitrine vazia do app) e o fluxo de contato de anunciantes. Decisão 28. No ar.

## [1.7.0] - 2026-11-06
- Registro do aceite dos Termos e da Política no cadastro do plano grátis (data e hora, IP e versão aceita), com finalidade, retenção e exclusão com a conta. Termos e Política do plano grátis na versão 1.1. No ar (backend 2.5.0, site 3.5.1). Botão "Mostrar" da senha ajustado para Safari/iOS.

## [1.6.2] - 2026-11-06
- Resumo diário de cadastros no Telegram do responsável, às 19h de São Paulo (cadastros do dia, grátis e por convite, e total de contas). No ar.

## [1.6.1] - 2026-11-06
- Versão grátis agora é a publicada, servida na raiz https://augustusai.com.br/iaprovale/; /iaprovale/gratis/ só redireciona. A versão por convite passa a ser modo de build alternativo. Decisões 1, 25, 26 e 27 atualizadas. Chat de cadastro revisado e limites novos (1.6.0) já no ar.
- Resumo diário de cadastros no Telegram do responsável, às 19h de São Paulo (cadastros do dia, grátis e por convite, e total de contas).

## [1.6.0] - 2026-11-06
- Chat do plano grátis revisado: confirmação do usuário, alertas em pop-up, termos com botões (Aceito/Recuso, Sim/Sair), botão "Entrar" ao concluir, dúvidas respondidas pela IA só com uma ficha fixa, limite de 10 dúvidas por conversa.
- Plano grátis com 17 buscas por dia e etiqueta no cabeçalho; uma conta por dia por conexão; teto total de 1000 cadastros no lugar dos limites diários; sem limite de avaliações por dia. Termos de Uso e Política de Privacidade do plano grátis. Decisões 26 e 27.

## [1.5.1] - 2026-11-05
- Cadastro grátis feito dentro do chat da página inicial, não em página separada.

## [1.5.0] - 2026-11-05
- Versão grátis no ar: cadastro pelo chat, plano grátis com limite diário, avaliação a cada 5 buscas e decisão 25.

## [1.4.1] - 2026-11-05
- Teste de segurança externo autorizado: sem falha crítica ou alta. Mensagens de erro de validação não devolvem mais o que foi enviado, e salvar o perfil preserva campos não enviados. Limite de tentativas de login confirmado em funcionamento.

## [1.4.0] - 2026-11-05
- Aprovação sem envio automático: caixa de login com "Copiar mensagem" e "Abrir no WhatsApp".
- Troca obrigatória da senha provisória no primeiro acesso, com tela de nova senha.
- Exclusão da conta pedida ao responsável pelo Telegram, em dois passos, enquanto o WhatsApp está desligado.
- Login com bloqueio por origem e por usuário, sem números internos.
- Decisões 22 a 24.

## [1.3.0] - 2026-11-05
- Acessibilidade verificada por script e por testes, sem auditoria com leitor de tela real: melhorias no ar e o que ainda não foi confirmado.
- Decisões novas: tempo do chat de dúvidas é limite de custo, sem prorrogação; texto da home esmaece de propósito na rolagem lenta.
- Confirmação do telefone por código registrada como desligada por enquanto, até haver WhatsApp para o produto.

## [1.2.0] - 2026-11-05
- Sessões de 30 dias, intervalo de 15 dias do telefone, avisos e aprovação de pedidos pelo Telegram, login entregue pelo responsável, verificação por código desligada por enquanto.

## [1.1.0] - 2026-11-05
- Exclusão de conta em duas etapas, retenção de 90 dias, exportação de dados, privacidade e termos.

## [1.0.0] - 2026-11-05
- Rodada 1 no ar: Solicitações de acesso, Configurações, endereço `/iaprovale/`, login.

## [0.1.0] - 2026-11-04
- Primeira versão: funcionalidades, rebranding, roadmap e decisões.
