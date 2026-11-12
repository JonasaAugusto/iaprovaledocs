# IAprovale Empresas: currículo e compatibilidade (E1/E2)

Estado: **Ainda não publicado**. E1 e E2 estão implementados na versão principal do backend 2.15.0, mas **não estão em produção**. Esta documentação descreve o contrato implementado, sem anunciar disponibilidade das rotas ou das telas. A publicação depende da revisão da integração, dos textos legais e das dependências em [Preparação da publicação](pre-deploy.md#empresas-e1e2-ainda-não-publicado).

O Empresas ajuda a comparar o currículo com uma vaga de empresa. É um fluxo próprio, separado da [compatibilidade educacional de concursos](compatibilidade.md). E3 (currículo para ATS), E4 (entrevista) e E5 (busca de vagas e panorama) são etapas futuras, fora desta entrega; não há candidatura automática.

## Endpoints (ainda não publicado)

Todas as rotas são autenticadas e usam a conta da pessoa. Os caminhos abaixo são relativos à API do backend.

| Método e caminho | Entrada e comportamento |
|---|---|
| `POST /empresas/curriculo` | Arquivo diretamente no corpo, com o `Content-Type` correspondente; não é formulário multipart. `guardar_original=true` na consulta permite guardar também o original; `X-Nome-Arquivo` é opcional. Salva o currículo e tenta gerar o perfil. |
| `GET /empresas/curriculo` | Retorna texto extraído, perfil e metadados da própria conta; 404 se não houver currículo. |
| `GET /empresas/curriculo/original` | Baixa o arquivo original, somente se tiver sido guardado; caso contrário, 404. |
| `POST /empresas/curriculo/perfil` | Sem corpo; tenta gerar o perfil pendente. Perfil válido já pronto é reaproveitado. |
| `DELETE /empresas/curriculo` | Apaga currículo, original, perfil e explicações da conta; retorna 204, inclusive se já não houver currículo. |
| `POST /empresas/compatibilidade` | JSON com `texto` ou `url`, exatamente um dos dois. Retorna nota e requisitos avaliados. |
| `POST /empresas/compatibilidade/explicacao` | JSON com `vaga_id` devolvido pela compatibilidade. Retorna `resumo`, `requisitos_citados` e `cache`. |
| `GET /empresas/cota` | Consulta o uso e os limites de IA da conta no dia, sem chamar IA. |

As respostas de currículo incluem `versao`, `enviado_em`, `atualizado_em`, `perfil_status` (`pronto` ou `pendente`), `perfil`, `perfil_parcial`, `texto`, `texto_truncado`, `original`, `armazenamento` e `aviso`. `original` contém só metadados quando guardado; o download usa a rota própria. `armazenamento` informa codec e tamanhos do JSON e do conteúdo compactado. Um `aviso` pode informar que o texto foi salvo, mas o perfil ficou pendente.

## E1 — currículo (ainda não publicado)

- Aceita **PDF, DOCX ou TXT**, até **5 MB**, com tipo declarado correspondente ao conteúdo: `application/pdf`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document` ou `text/plain`.
- A extração local não usa IA. PDF precisa ter camada de texto, sem senha e com até **15 páginas**; sem OCR. Arquivos sem texto legível suficiente são recusados. Formato não aceito ou tipo divergente retorna 415; tamanho excedido, 413; PDF protegido, páginas demais ou conteúdo inválido, 422.
- Guarda até **40.000 caracteres** de texto extraído; `texto_truncado` indica corte. A entrada para gerar o perfil usa até **12.000 caracteres** após remover contatos; `perfil_parcial` indica esse corte. Texto incompleto pode reduzir a qualidade da comparação.
- Uma chamada curta ao DeepSeek organiza cargos, competências, ferramentas, experiências, formação, idiomas e conquistas com números. Anos de experiência são calculados em Python, sem somar duas vezes períodos simultâneos; ferramentas e números passam por checagens contra o texto. Essas checagens não garantem que todos os fatos estejam corretos: revise o perfil.
- Reenviar o mesmo texto extraído com perfil válido reaproveita o resultado, sem nova chamada. Texto diferente cria nova versão e invalida as explicações anteriores.
- Se a cota acabar ou a IA falhar, o texto é salvo e o perfil fica `pendente`, com aviso. Use `POST /empresas/curriculo/perfil` para tentar novamente quando houver disponibilidade; a compatibilidade depende de um perfil pronto.

## E2 — compatibilidade e explicação (ainda não publicado)

A pessoa cola a descrição da vaga em `texto` (até 30.000 caracteres) ou informa um link público em `url`. A descrição precisa ter pelo menos 80 caracteres após normalização. Sem currículo ou com perfil pendente, a compatibilidade retorna 409 antes de buscar a vaga ou chamar IA.

Os links aceitos são de **Greenhouse, Lever, Ashby, Workable e SmartRecruiters**, consultados pelas APIs públicas de vagas. O backend não aceita links arbitrários; **Gupy não está implementado nesta entrega**, embora constasse do plano inicial. Um link não aceito retorna 400; indisponibilidade da fonte retorna 502. É possível colar o texto em vez do link.

Os requisitos da vaga são extraídos pelo DeepSeek e reaproveitados em **cache global**, identificado pelo conteúdo e pela versão do extrator. São guardados título, fonte e requisitos, sem o texto completo da vaga; não é um cache de currículos. A primeira extração consome a cota de quem a solicitou; reutilizar requisitos já válidos não chama IA. A extração usa até 9.000 caracteres; `vaga_parcial` sinaliza corte.

A nota de **0 a 10**, os pontos fortes e as lacunas são **calculados em Python**. A resposta inclui `vaga_id`, `titulo`, `fonte`, `nota`, `dados_insuficientes`, `peso_avaliado`, `componentes`, `nao_avaliados`, `pontos_fortes`, `lacunas`, `requisitos`, `vaga_parcial`, `rubrica`, `cache` e `aviso`. `cache` indica reaproveitamento dos requisitos da vaga; a nota é recalculada com o currículo atual, sem IA.

A rubrica considera requisitos (peso 65), função (10) e anos de experiência (10), quando há dados; requisito obrigatório crítico tem peso 5, obrigatório comum 3 e desejável 1. Componentes sem dados ficam em `nao_avaliados`, fora do denominador; localização, senioridade e remuneração não são avaliadas nesta entrega. Sem requisitos suficientes, retorna `nota: null` e `dados_insuficientes: true`, em vez de inventar uma nota. A nota **não é chance de contratação**; confira a descrição oficial e as evidências do currículo.

“Por que essa nota?” é uma explicação **sob demanda**, em uma chamada curta com as contribuições já calculadas, **sem enviar o currículo**. A IA não decide nem muda a nota. O resultado é privado e reaproveitado por conta, versão do currículo e vaga; acerto desse cache não chama IA. Sem requisitos suficientes, a explicação informa a limitação sem chamada externa. Uma falha de IA retorna 502 e não vira resultado válido em cache.

## Cota diária de IA (ainda não publicado)

Limites por conta e por dia, renovados à meia-noite de **Brasília**:

| Limite | Valor |
|---|---|
| Chamadas de IA | 17 |
| Custo estimado em US$ | 0,01 |

Vale **o que vier primeiro**. Esta cota é **separada da cota de buscas de concursos** e do contador de avaliação a cada 5 buscas. É controle de uso do serviço, **não é cobrança** à pessoa nem promessa de 17 operações completas por dia.

Geração do perfil, extração inédita de requisitos e explicação inédita compartilham esses limites. Conta **cada tentativa** ao provedor, inclusive falhas e a possível repetição por JSON inválido (no máximo uma, se ainda houver orçamento). Os acertos de cache não consomem chamadas nem custo; extração local, cálculo da nota, consulta, download, exportação e exclusão também não chamam IA.

Há **reserva pelo custo máximo antes** de cada chamada, seguida de ajuste pelo uso retornado, com tarifa estimada de pico. A chamada pode ser recusada com **429 mesmo sem atingir os dois limites**, se o saldo não comportar essa reserva. Sem resposta do provedor, a tentativa continua contando, mas a reserva de custo é devolvida. O que já estiver em cache continua disponível com a cota esgotada.

`GET /empresas/cota` retorna `dia`, `chamadas`, `limite_chamadas`, `custo_usd`, `limite_usd`, `chamadas_restantes` e `esgotada`. `chamadas_restantes` é saldo de tentativas, não de análises garantidas. `esgotada` indica que um teto já foi atingido; não garante que uma próxima reserva caiba no orçamento.

## Armazenamento (ainda não publicado)

No Empresas, o **texto extraído e o perfil** são guardados **somente compactados**, em um documento JSON versionado com **zstd ou gzip**. A compactação reduz espaço; **não é criptografia** nem anonimização. A leitura autenticada e a exportação devolvem o conteúdo descompactado à própria pessoa.

O **original não é guardado por padrão**. A opção explícita `guardar_original=true` guarda o arquivo **também compactado**, com nome, tipo e tamanho para download e exportação. Reenviar sem essa opção remove o original antes guardado, mesmo quando o texto permite reaproveitar o perfil.

O currículo fica salvo **até a pessoa apagar**, substituir o conteúdo ou excluir a conta. O prazo de 90 dias do histórico de buscas não se aplica automaticamente ao currículo do Empresas. Este armazenamento é próprio do Empresas; não altera o contrato do currículo já usado no Perfil de concursos.

## Exportação e exclusão (ainda não publicado)

`GET /me/exportar` inclui o bloco `empresas`, com `curriculo`, `explicacoes` e `uso_ia` da própria conta. Texto e perfil vão **descompactados**, com versão, datas, estado e metadados de armazenamento; se o original foi guardado, o arquivo vai em **base64**, com nome, tipo e tamanho. As explicações incluem resumo, vaga, versão do currículo e data; o uso inclui dia, chamadas e custo estimado. Sem dados, o bloco contém currículo nulo e listas vazias.

`DELETE /empresas/curriculo` remove texto, perfil, original e explicações da conta, mas **não zera a cota** nem apaga o registro diário de uso. Excluir a conta apaga também esses registros de uso: **ambos os fluxos** de exclusão (pedido da pessoa ou exclusão pelo administrador) abrangem os dados privados do Empresas. Permanecem as confirmações do [fluxo de exclusão da conta](configuracoes-do-usuario.md#dados-e-privacidade).

O **cache global de requisitos de vagas permanece**, pois é compartilhado e não contém o currículo da pessoa. Apagar o currículo ou a conta no IAprovale não constitui garantia sobre a retenção do provedor externo; os textos legais precisam descrever esse tratamento antes da liberação.

## Privacidade e textos legais (ainda não publicado)

- As chamadas de IA do Empresas enviam dados **somente ao DeepSeek**, sem encaminhar a outro provedor de IA. Na extração do perfil, **e-mail, telefone, links e CPF** reconhecidos são substituídos por marcadores **antes de gerar o perfil**. Essa remoção não modifica o texto guardado para a pessoa e **não garante anonimização**: nomes e informações profissionais podem identificar alguém, e formatos não reconhecidos podem permanecer.
- Para os requisitos, o DeepSeek recebe o texto da vaga; para a explicação, apenas as contribuições calculadas, sem o currículo completo. Não cole contatos ou informações pessoais na descrição da vaga. Currículo e perfil **não são enviados aos ATS**: a consulta de link apenas lê a vaga pública, sem candidatura ou envio de documento a empregadores.
- O processamento pelo DeepSeek envolve **transferência internacional** dos dados encaminhados. A Política de Privacidade e os Termos devem informar finalidade, destinatário, transferência internacional, retenção e direitos, alinhados ao armazenamento compactado e à exportação/exclusão descritos aqui. Esta documentação não comprova mecanismos jurídicos de transferência nem promete prazos de exclusão no provedor.
- Ao enviar currículo, **não inclua dados sensíveis** (como saúde, religião, origem, opinião política ou filiação) nem informações desnecessárias de terceiros. Revise o conteúdo antes do envio; a remoção automática de contatos não substitui esse cuidado.

Os **textos legais** do site precisam incorporar o Empresas e ser revisados antes da publicação; a validação por advogado continua pendente. Não se declara nova versão legal nem novo aceite em vigor nesta tarefa. Todo o escopo E1/E2 permanece **ainda não publicado**. Veja também [Versão grátis](versao-gratis.md#termos-de-uso-e-política-de-privacidade) e [Dados e privacidade](configuracoes-do-usuario.md#dados-e-privacidade).
