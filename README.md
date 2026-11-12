# IAprovale by Augustus: documentação

O IAprovale encontra concursos públicos abertos compatíveis com a formação da pessoa e entrega o link direto do portal oficial de inscrição. Desde 12/11/2026, o IAprovale Empresas também oferece currículo, compatibilidade, materiais por vaga e busca de vagas de empresas.

Este repositório é público e documenta **o que o produto faz** (funcionalidades, decisões de produto e roadmap). O código do front e do back fica em repositórios privados. Aqui não há chaves, credenciais, dados de usuários nem detalhes de infraestrutura.

## Índice

- [Funcionalidades](docs/funcionalidades.md): o que já existia e o que foi acrescentado, com o estado de cada item. Novidades, alertas e acompanhamento publicados; envio de e-mail ligado via Brevo desde 12/11/2026.
- [Rebranding (Rodada 1)](docs/rebranding-rodada-1.md): novo visual do app e da home.
- [Pedido de acesso pelo chat](docs/pedido-de-acesso.md): como o pedido e a janela de dúvidas funcionam.
- [Busca pelo perfil e nível](docs/busca-por-perfil.md): consulta sem IA, filtro por nível, cota e exclusão de avaliações.
- [Compatibilidade entre perfil e cargos — etapa 3](docs/compatibilidade.md): publicada, acessível em Alertas > Acompanhando; níveis por cargo, lacunas, cota, cache e recuperação de falhas.
- [IAprovale Empresas — E1/E2](docs/empresas.md): no ar desde 12/11/2026; currículo compactado, compatibilidade com vagas, explicação sob demanda, cota própria e privacidade.
- [Busca de vagas — E5](docs/empresas-vagas.md): busca, panorama, prévia gratuita e cobertura do índice local.
- [Navegação e Carreira](docs/navegacao.md): telas publicadas, barra, topo, home e endereços das abas.
- [Filtro de UF](docs/filtro-de-uf.md): com UFs escolhidas só voltam concursos delas e os nacionais; nacionais regionais marcados pela fonte tratados pela UF do texto; zero resultados avisa claramente. No ar (backend 2.11.0, site 3.10.0). UF do texto como filtro e `ufs` na API de parceiros: aguardando publicação do backend 2.12.0.
- [Stats do administrador](docs/stats-do-administrador.md): a aba Stats, só para administradores, com a evolução do uso. Atualização da estimativa de custo de IA: ainda não publicado.
- [Eventos de busca](docs/eventos-de-busca.md): o registro de cada busca (horário, custo e tipo, sem conteúdo) que alimenta o Stats por hora, com retenção de 90 dias e o texto para a Política de Privacidade.
- [Solicitações de acesso](docs/solicitacoes-de-acesso.md): como o administrador aprova ou recusa pedidos e como o login é entregue à pessoa.
- [Versão grátis](docs/versao-gratis.md): a versão publicada em produção. Cadastro pelo chat (confirmação do usuário, termos com botões, dúvidas), plano grátis de 17 buscas por dia e avaliação a cada 5 buscas. E-mail opcional na conta; textos legais 1.3 do convite vigentes e variante grátis ainda não ativada.
- [Configurações do usuário](docs/configuracoes-do-usuario.md): decisões da tela de configurações.
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
