# Preparação da publicação: e-mail, textos legais 1.3, etapa 3 e Empresas

Estado: **Publicado com envio de e-mail**, ligado em produção desde **12/11/2026**, via Brevo SMTP, além de avisos no site, compatibilidade por cargo e Empresas. Este documento preserva as dependências e a ordem de validação para novas instalações; não é um atestado da execução de cada migração. A distinção entre [textos legais 1.3 do convite e variante grátis](versao-gratis.md#termos-de-uso-e-política-de-privacidade) e o estado da [estimativa de custos de IA](stats-do-administrador.md) estão nas páginas correspondentes.

## Migrações necessárias

Aplicar as versões v3_17 a v3_22 na ordem abaixo, antes do reinício. Os scripts são idempotentes e executados separadamente do servidor; o servidor web não executa migrações automaticamente. A v3_20 ajusta a unicidade de e-mail, preservando os endereços e as verificações existentes. A documentação pública lista os arquivos e seus efeitos, sem comandos de acesso ao ambiente ou credenciais.

| Arquivo no backend | Finalidade |
|---|---|
| `scripts/migrate_v3_17_email_novidades.py` | E-mail na conta, verificação, preferência e caixa de Novidades. |
| `scripts/migrate_v3_18_alertas_acompanhamento.py` | Alertas, acompanhados, controle de avisos repetidos, resumos e estado da linha de base/processamento dos alertas. |
| `scripts/migrate_v3_19_email_cadastro_cotas.py` | Verificação de e-mail no cadastro e cotas globais diárias por categoria. |
| `scripts/migrate_v3_20_email_pendente.py` | Unicidade só para e-mails verificados; pendência não reserva endereço. |
| `scripts/migrate_v3_21_boas_vindas.py` | Registro de boas-vindas por conta, sem envio retroativo. |
| `scripts/migrate_v3_22_compatibilidade.py` | Cache persistente da etapa 3, com reserva por usuário, concurso e versão do perfil e exclusão em cascata com a conta. |

É necessário reexecutar a v3_18 em bases que receberam uma versão anterior dela, para acrescentar o estado da linha de base e do processamento. As tabelas são necessárias mesmo com a rotina diária desligada: a exportação e a exclusão de contas também as consultam. Desligar o e-mail não elimina a necessidade dessas migrações.

## Empresas em produção

Estado: **No ar** desde **12/11/2026**. O [Empresas](empresas.md) E1–E5 está em produção (backend ef7dc58 ou posterior; site 0ccfa9d ou posterior), com cobrança desligada. Em uma instalação que ainda não tenha E1/E2, acrescentar às dependências anteriores a migração aditiva e idempotente `scripts/migrate_v3_23_empresas.py` (v3_23), **antes do reinício**, e a dependência de leitura de PDF `pypdf==6.21.4` do backend. A migração cria o armazenamento compactado, requisitos de vagas, explicações e uso diário de IA; este registro de dependência não substitui a conferência da base pelo operador.

Conferir os textos legais do site para currículo compactado, original opcional, materiais de E3/E4, exportação/exclusão, envio ao DeepSeek, limites da remoção de contatos e transferência internacional; a validação por advogado continua pendente. E3/E4 estão gratuitos no teste; preços e meio de pagamento pendentes. Para E5, conferir índice disponível, atualização diária e comportamento com coleta parcial, conforme [Busca de vagas](empresas-vagas.md). Em novas liberações, validar cota, exportação/exclusão e integração das telas em recursos descartáveis. Execução e publicação continuam a cargo de Claude/serviço, pelo botão do dono.

## C1: validação antes da publicação

Estado: **Ainda não publicado**.

O lote C1 acrescenta [erro claro de upload acima de 5 MB](empresas.md#c1-erro-de-tamanho), [identificação confiável da conexão](versao-gratis.md#c1-identificação-da-conexão) e [limites do PDF de concursos](funcionalidades.md#c1-limites-do-pdf-de-concursos). Os estados de produção anteriores desta página não comprovam a publicação de C1.

A configuração de referência da API declara **`--workers 1`**, ou seja, **um processo** de atendimento. Parte dos limites de proteção e dos caches fica na **memória** desse processo: esses dados **não são compartilhados** entre processos. Aumentar esse número exige antes uma solução compartilhada e decisão do dono. Um teste verifica que a referência mantém exatamente um processo; ele não comprova a configuração ativa.

A referência **não foi instalada** pelo lote C1. Antes de liberar, Claude/serviço deve comparar a configuração ativa com a referência, conferir a confiança no intermediário de conexão e fazer revisão cruzada do código e das docs. Em recursos descartáveis, validar upload no limite e acima dele, resposta JSON 413 e sua apresentação no site, recusa 422 do PDF fora dos limites e preservação das proteções de login e cadastro. Esta documentação não executa instalação nem reinício; a publicação segue pelo botão **[Publicar]** do dono.

## C4: histórico e retenção

Estado: **Ainda não publicado**. O lote C4 implementa o [histórico enxuto para novas buscas](configuracoes-do-usuario.md#c4-histórico-enxuto) e muda a forma de executar a limpeza, preservando os prazos e as contagens de registros removidos.

A poda mantém no máximo as últimas 10 buscas por conta e remove as de mais de 90 dias. A poda e a limpeza diária passam a usar `DELETE` com condições em SQL: o próprio banco seleciona e apaga os registros vencidos, sem carregar cada registro na aplicação para apagá-lo individualmente. Isso reduz o trabalho de limpeza sem criar um novo prazo de retenção.

Na limpeza diária, continuam protegidos os pedidos aprovados e as exclusões e verificações pendentes. Sessões revogadas são removidas depois de mais de 30 dias da revogação, mesmo que seu último uso seja antigo. Para as demais sessões, a regra continua sendo 30 dias de inatividade para expirar e mais 30 dias de retenção antes de remover o registro; sem data de último uso, vale a data de criação. Remover esse registro não exclui a conta. Eventos de busca mantêm 90 dias; Novidades lidas mantêm sua regra própria de mais de 183 dias desde a criação, e não lidas permanecem.

A migração `scripts/migrate_v3_25_history_index.py`, após a v3_24, cria o índice `search_history(user_id, created_at)`: uma estrutura auxiliar para localizar o histórico por conta e data com mais eficiência. É idempotente e reversível; a reversão com `--downgrade` remove somente esse índice. Aplicação e reversão preservam os registros, sem reescrever resultados antigos. O backend usa scripts próprios de migração, não usa Alembic.

Antes de liberar C4, Claude/serviço deve fazer revisão cruzada do código e destas docs, validar em recursos descartáveis a criação e a remoção do índice, os limites do histórico, a exportação e as regras de limpeza. A migração deve ser aplicada e conferida antes do reinício. Esta página não comprova aplicação da migração nem publicação de C4; ambas dependem da operação autorizada e a publicação segue pelo botão **[Publicar]** do dono.

## Ordem da publicação

Referência para futuras instalações ou liberações; os passos abaixo não são comandos para repetir a publicação já informada.

1. Revisar e validar as docs e a integração das telas; conferir os textos legais 1.3 do convite, vigentes desde 12/11/2026, e o alinhamento entre textos apresentados e aceite do plano grátis, sem presumir ativação da sua variante 1.3; preparar backup antes de alterar a base.
2. Aplicar e conferir as migrações v3_17 a v3_22 antes de reiniciar o backend, incluindo a reexecução da v3_18 quando necessária; para Empresas, incluir também a v3_23 e conferir a dependência pypdf e os textos legais acima.
3. Reiniciar o backend e validar o funcionamento básico em recursos de teste: conta sem e-mail, confirmação por código, conta criada com e-mail pendente sem cota, aceite correspondente ao texto apresentado, preservação dos aceites antigos, Novidades, alertas, acompanhados, compatibilidade, exportação e exclusão.
4. Conferir a rotina diária de avisos das 07:00 de São Paulo com e-mail ligado via Brevo: endereço verificado e preferência ativa para resumos, boas-vindas após confirmação, cotas e Novidades como alternativa sem entrega.
5. Publicar o site alinhado à variante legal aprovada e às rotas disponíveis, mantendo a variante grátis 1.3 ainda não ativada até liberação específica, após revisão das telas e validação das etapas anteriores; se houver falha, interromper a publicação e avaliar a recuperação.

Produção, backup, migrações, reinício e publicação cabem ao responsável pela operação (Claude/serviço), após autorização explícita do dono; a publicação depende do botão **[Publicar]**. Esta tarefa altera somente documentação e testes locais.

## E-mail ligado em produção

O envio está ligado desde **12/11/2026**, via **Brevo SMTP**, remetente **IAprovale <avisos@augustusai.com.br>**. O e-mail é opcional nas Configurações, confirmado por código de 6 dígitos válido por 10 minutos. As cotas globais são 200 códigos e 100 avisos por dia; códigos usam a sobra dos avisos, nunca o contrário. Sem cota no cadastro com endereço informado, a conta é criada com e-mail pendente para confirmação posterior; Novidades segue acessível no site. Boas-vindas só após confirmar; sem cota, fica para a manhã seguinte, antes dos resumos. Não há fila retroativa do período anterior à ativação. Veja as [condições completas de envio](funcionalidades.md#cotas-de-e-mail).

Brevo (Sendinblue SAS, França) é operador, com transferência internacional. Os textos legais 1.3 do convite estão vigentes desde 12/11/2026 e incluem e-mail opcional, Brevo e Carreira; a variante grátis em `scripts/legal-gratis/v1_3.py` está **ainda não ativada**. Conferir o texto efetivamente apresentado e seu aceite antes de qualquer ativação dessa variante. Credenciais ficam fora desta documentação. A validação por advogado continua pendente.
