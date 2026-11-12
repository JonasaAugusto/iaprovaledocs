# IAprovale by Augustus: documentação

O IAprovale encontra concursos públicos abertos compatíveis com a formação da pessoa e entrega o link direto do portal oficial de inscrição.

Este repositório é público e documenta **o que o produto faz** (funcionalidades, decisões de produto e roadmap). O código do front e do back fica em repositórios privados. Aqui não há chaves, credenciais, dados de usuários nem detalhes de infraestrutura.

## Índice

- [Funcionalidades](docs/funcionalidades.md): o que já existia e o que foi acrescentado, com o estado de cada item. Pacote de avisos, prazos e e-mail com código (Novidades, alertas e acompanhamento): ainda não publicado; envio de e-mail desligado.
- [Rebranding (Rodada 1)](docs/rebranding-rodada-1.md): novo visual do app e da home.
- [Pedido de acesso pelo chat](docs/pedido-de-acesso.md): como o pedido e a janela de dúvidas funcionam.
- [Busca pelo perfil e nível](docs/busca-por-perfil.md): consulta sem IA, filtro por nível, cota e exclusão de avaliações.
- [Compatibilidade entre perfil e cargos — etapa 3](docs/compatibilidade.md): backend implementado, ainda não publicado; níveis por cargo, lacunas, cota, cache e recuperação de falhas. Tela depende de integração e revisão.
- [IAprovale Empresas — E1/E2](docs/empresas.md): currículo compactado, compatibilidade com vagas, explicação sob demanda, cota própria e privacidade; backend implementado, ainda não publicado e fora de produção.
- [Filtro de UF](docs/filtro-de-uf.md): com UFs escolhidas só voltam concursos delas e os nacionais; nacionais regionais marcados pela fonte tratados pela UF do texto; zero resultados avisa claramente. No ar (backend 2.11.0, site 3.10.0). UF do texto como filtro e `ufs` na API de parceiros: aguardando publicação do backend 2.12.0.
- [Stats do administrador](docs/stats-do-administrador.md): a aba Stats, só para administradores, com a evolução do uso. Atualização da estimativa de custo de IA: ainda não publicado.
- [Eventos de busca](docs/eventos-de-busca.md): o registro de cada busca (horário, custo e tipo, sem conteúdo) que alimenta o Stats por hora, com retenção de 90 dias e o texto para a Política de Privacidade.
- [Solicitações de acesso](docs/solicitacoes-de-acesso.md): como o administrador aprova ou recusa pedidos e como o login é entregue à pessoa.
- [Versão grátis](docs/versao-gratis.md): a versão publicada em produção. Cadastro pelo chat (confirmação do usuário, termos com botões, dúvidas), plano grátis de 17 buscas por dia e avaliação a cada 5 buscas. Cadastro com e-mail obrigatório quando o envio estiver configurado: ainda não publicado.
- [Configurações do usuário](docs/configuracoes-do-usuario.md): decisões da tela de configurações.
- [Roadmap](docs/roadmap.md): o que vem depois.
- [Preparação da publicação](docs/pre-deploy.md): migrações v3_17 a v3_22 e, para Empresas, v3_23 e pypdf antes do reinício, aceite `gratis-1.2` e e-mail desligado até a chave SMTP. Tudo ainda não publicado.
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

O pacote de avisos e prazos tem backend implementado, mas ainda depende da revisão do site e da publicação. Nenhuma dessas adições está em produção. Tudo que envolve e-mail só é habilitado com o serviço de envio configurado; hoje permanece desligado.

A etapa 3, os novos aceites `gratis-1.2`, a acentuação das mensagens e a correção de custo/cache do DeepSeek também estão implementados no backend e **ainda não publicados**. As tarifas documentam a referência de 11/11/2026; não representam cobrança à pessoa nem a fatura do provedor.

Endereço do produto: https://augustusai.com.br/iaprovale/

O que está no ar em https://augustusai.com.br/iaprovale/ é a versão grátis: a pessoa cria a própria conta pelo chat da página inicial. O modo por convite (cada login nasce de uma solicitação aprovada pelo responsável) continua existindo como alternativa de build do site, mas não é o publicado. O endereço antigo /iaprovale/gratis/ apenas redireciona para a raiz.

## Verificação local

`python3 -m unittest discover -s tests -v` verifica o contrato documentado do pacote, o estado de publicação e os links relativos, sem acessar serviços externos.

## Contato

Responsável pelo IAprovale: Jonas, da Augustus AI.

- E-mail: [jonasaugustosantosoliveira@gmail.com](mailto:jonasaugustosantosoliveira@gmail.com).
- Instagram da [Augustus AI](https://www.instagram.com/augustusaisolutions/).
- Instagram de [Jonas](https://www.instagram.com/jonasaaugusto/).
