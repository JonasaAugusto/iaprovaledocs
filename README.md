# IAprovale by Augustus: documentação

O IAprovale encontra concursos públicos abertos compatíveis com a formação da pessoa e entrega o link direto do portal oficial de inscrição. Desde 12/11/2026, o IAprovale Empresas também oferece currículo, compatibilidade, materiais por vaga e busca de vagas de empresas.

Este repositório é público e documenta **o que o produto faz** (funcionalidades, decisões de produto e roadmap). O código do front e do back fica em repositórios privados. Aqui não há chaves, credenciais, dados de usuários nem detalhes de infraestrutura.

## Índice

- [Privacidade do currículo na busca](docs/busca-por-perfil.md#privacidade-do-currículo-na-busca), ajuste **ainda não publicado em produção**: remoção de e-mails, telefones, links e CPF reconhecidos antes do corte de 6.000 caracteres e do envio ao DeepSeek, inclusive nas repetições, sem mudar o currículo salvo. Mantém nome e endereço; não anonimiza o currículo.
- C14, **ainda não publicado em produção**: [link de compartilhamento de busca](docs/funcionalidades.md#c14-link-de-compartilhamento-de-busca), só com títulos e links públicos, válido por 7 dias; [troca, revogação e privacidade](docs/configuracoes-do-usuario.md#c14-gerenciar-links-de-busca) e [migração v3.29 e proteção da credencial nos registros de acesso](docs/pre-deploy.md#c14-compartilhamento-e-proteção-do-link). Telas pendentes.
- [Funcionalidades](docs/funcionalidades.md): o que já existia e o que foi acrescentado, com o estado de cada item. Novidades, alertas e acompanhamento publicados; envio de e-mail ligado via Brevo desde 12/11/2026.
- Correções C1, **ainda não publicadas**: [erro de upload acima de 5 MB](docs/empresas.md#c1-erro-de-tamanho), [identificação da conexão](docs/versao-gratis.md#c1-identificação-da-conexão), [limites do PDF de concursos](docs/funcionalidades.md#c1-limites-do-pdf-de-concursos) e [validação de um único processo da API](docs/pre-deploy.md#c1-validação-antes-da-publicação).
- C4, **ainda não publicado**: [histórico enxuto](docs/configuracoes-do-usuario.md#c4-histórico-enxuto), com até 100 resultados por nova busca, só identificador, título e link; [retenção diretamente no banco e índice reversível](docs/pre-deploy.md#c4-histórico-e-retenção), preservando prazos e registros antigos.
- [Rebranding (Rodada 1)](docs/rebranding-rodada-1.md): novo visual do app e da home.
- [Pedido de acesso pelo chat](docs/pedido-de-acesso.md): como o pedido e a janela de dúvidas funcionam.
- C7, **ainda não publicado**: [ranking por relevância](docs/busca-por-perfil.md#c7-ranking-por-relevância), com prioridade geográfica, cargo e prazo, motivo da ordem e [selo conservador por cargo](docs/compatibilidade.md#c7-selo-na-resposta-da-busca), sem IA adicional.
- [Busca pelo perfil e nível](docs/busca-por-perfil.md): consulta sem IA, filtro por nível, cota e exclusão de avaliações.
- C3, **ainda não publicado em produção**: [inferência textual de UF e prazo no dia de Brasília](docs/filtro-de-uf.md#c3-inferência-textual-e-prazo), com siglas em contexto, capitais ambíguas e descarte de inscrições vencidas.
- C6b, **ainda não publicado em produção**: [pedidos para terceiros e nível dos cargos](docs/busca-por-perfil.md#c6b-terceiros-e-nível-dos-cargos), preservando menções narrativas e cargos sem requisito individual conhecido.
- C10, **ainda não publicado**: contrato previsto de [verificação segura de links e consulta por cidade](docs/busca-por-perfil.md#c10-verificação-de-links-e-cidade), com conexão ao IP público validado, grafia original antes da alternativa normalizada e cache da PCI preservado; [validações antes da publicação](docs/pre-deploy.md#c10-links-e-consulta-por-cidade).
- C9, **ainda não publicado**: [cache público da PCI](docs/busca-por-perfil.md#c9-cache-da-pci), por cinco minutos, com cópias independentes antes dos filtros pessoais; [conexões durante a compatibilidade](docs/compatibilidade.md#c9-conexões-durante-a-avaliação), preservando a trava contra avaliações duplicadas.
- C6a, **ainda não publicado**: [equivalentes de cargo com cache](docs/busca-por-perfil.md#c6a-equivalentes-de-cargo), até cinco por formação; cache de 30 dias, lista vazia por 24 horas e até três gerações paralelas por busca com teto de seis segundos de espera pelo modelo.
- [Compatibilidade entre perfil e cargos — etapa 3](docs/compatibilidade.md): publicada, acessível em Alertas > Acompanhando; níveis por cargo, lacunas, cota, cache e recuperação de falhas.
- [IAprovale Empresas — E1/E2](docs/empresas.md): no ar desde 12/11/2026; currículo compactado, compatibilidade com vagas, explicação sob demanda, cota própria e privacidade.
- [Busca de vagas — E5](docs/empresas-vagas.md): busca, panorama, prévia gratuita e cobertura do índice local.
- C11, **ainda não publicado**: [coleta incremental SmartRecruiters](docs/empresas-vagas.md#c11-coleta-incremental-smartrecruiters), com primeira coleta lenta e seguintes mais rápidas pelo reaproveitamento de texto e link das vagas sem alteração; limite por board, preservação das vagas conhecidas na coleta parcial e renovação periódica dos detalhes.
- [Navegação e Carreira](docs/navegacao.md): telas publicadas, barra, topo, home e endereços das abas.
- C8, **ainda não publicado**: [início agregado](docs/navegacao.md#c8-início-agregado), com cota do Empresas, acompanhados, perfil e contagem de não lidas em uma chamada; rotas individuais preservadas por uma versão, adaptação da interface separada.
- [Filtro de UF](docs/filtro-de-uf.md): com UFs escolhidas só voltam concursos delas e os nacionais; nacionais regionais marcados pela fonte tratados pela UF do texto; zero resultados avisa claramente. No ar (backend 2.11.0, site 3.10.0). UF do texto como filtro e `ufs` na API de parceiros: disponíveis desde o backend 2.12.0.
- [Stats do administrador](docs/stats-do-administrador.md): a aba Estatísticas, só para administradores, com a evolução do uso. Atualização da estimativa de custo de IA: no ar desde 12/11/2026, junto da etapa 3.
- [Eventos de busca](docs/eventos-de-busca.md): o registro de cada busca (horário, custo e tipo, sem conteúdo) que alimenta o Stats por hora, com retenção de 90 dias e o texto para a Política de Privacidade.
- [Solicitações de acesso](docs/solicitacoes-de-acesso.md): como o administrador aprova ou recusa pedidos e como o login é entregue à pessoa.
- [Versão grátis](docs/versao-gratis.md): a versão publicada em produção. Cadastro pelo chat (confirmação do usuário, termos com botões, dúvidas), plano grátis de 17 buscas por dia e avaliação a cada 5 buscas. E-mail opcional na conta; textos legais 1.3 do convite vigentes e variante grátis ainda não ativada.
- [Configurações do usuário](docs/configuracoes-do-usuario.md): decisões da tela de configurações.
- C13, **ainda não publicado em produção**: [checklist pessoal por acompanhado](docs/funcionalidades.md#c13-checklist-de-inscrição), até 30 itens, e [até 20 versões do perfil](docs/configuracoes-do-usuario.md#c13-versões-do-perfil), sem texto do currículo nas versões, apenas hash e tamanho; [migração v3.28 obrigatória antes do código novo e limites da eliminação](docs/pre-deploy.md#c13-checklist-e-versões-do-perfil). Interface e validação jurídica das cópias residuais pendentes.
- C12, **ainda não publicado em produção**: [calendário pessoal dos acompanhados](docs/funcionalidades.md#c12-calendário-dos-acompanhados), com assinatura `.ics`, [troca e revogação do link](docs/configuracoes-do-usuario.md#c12-link-pessoal-do-calendário), [contrato de alerta por termo e UFs](docs/funcionalidades.md#c12-contrato-de-alerta-por-busca) e [migração e proteção do token nos registros de acesso](docs/pre-deploy.md#c12-calendário-e-proteção-do-link); controles de interface pendentes.
- C5, **ainda não publicado**: [proteção das sessões por hash](docs/configuracoes-do-usuario.md#c5-proteção-das-sessões), com novo login na mudança, e [cuidados da migração e reversão](docs/pre-deploy.md#c5-migração-e-reversão).
- [Empresas: currículo ATS e entrevista](docs/empresas-e3-e4.md): no ar desde 12/11/2026; geração conservadora, cota e armazenamento. Gratuitos no teste, cobrança desligada; preços e meio de pagamento pendentes.
- [Roadmap](docs/roadmap.md): o que vem depois.
- [Preparação da publicação](docs/pre-deploy.md): dependências de migrações e pypdf, registro da publicação do Empresas e do e-mail e pendências legais. Esta documentação não executa nem atesta cada migração.
- [Decisões de produto](docs/decisoes.md): regras de produto que valem para todo o projeto.

## Legenda de estado

| Estado | Significado |
|---|---|
| **No ar** | Já está em uso. |
| **Ainda não publicado** | Descrito para uma próxima entrega; o texto distingue o que já está implementado do que segue o contrato previsto. |
| **Pronto, aguardando liberação** | Implementado e testado fora de produção. |
| **Em andamento** | Parte pronta, parte pendente. |
| **Decidido** | Definido, ainda não construído. |
| **Sugerido** | Ideia sem decisão final. |

Novidades, alertas, acompanhamento e compatibilidade por cargo estão publicados no site. O envio de e-mail está ligado em produção desde 12/11/2026, via Brevo. O e-mail é opcional nas Configurações e confirmado por código de 6 dígitos válido por 10 minutos. O resumo diário das 07:00 de São Paulo exige endereço verificado e preferência de avisos ativa; as cotas globais e falhas de entrega não impedem consultar Novidades no site.

O Empresas E1–E5 está em produção desde 12/11/2026 (backend ef7dc58 ou posterior; site 0ccfa9d ou posterior). A cobrança está desligada. Os textos legais 1.3 do modo por convite estão vigentes desde 12/11/2026, com e-mail opcional, Brevo e Carreira; a variante do plano grátis ainda não foi ativada. O aceite do plano grátis e a atualização da estimativa de custo/cache do DeepSeek mantêm os estados específicos das páginas correspondentes. As tarifas documentam a referência de 11/11/2026; não representam cobrança à pessoa nem a fatura do provedor.

Endereço do produto: https://augustusai.com.br/iaprovale/

O que está no ar em https://augustusai.com.br/iaprovale/ é a versão grátis: a pessoa cria a própria conta pelo chat da página inicial. O modo por convite (cada login nasce de uma solicitação aprovada pelo responsável) continua existindo como alternativa de build do site, mas não é o publicado. O endereço antigo /iaprovale/gratis/ apenas redireciona para a raiz.

## Verificação local

`python3 -m unittest discover -s tests -v` verifica o contrato documentado do pacote, o estado de publicação e os links relativos, sem acessar serviços externos.

## Contato

Responsável pelo IAprovale: Jonas, da Augustus AI.

- E-mail: [jonasaugustosantosoliveira@gmail.com](mailto:jonasaugustosantosoliveira@gmail.com).
- Instagram da [Augustus AI](https://www.instagram.com/augustusaisolutions/).
- Instagram de [Jonas](https://www.instagram.com/jonasaaugusto/).
