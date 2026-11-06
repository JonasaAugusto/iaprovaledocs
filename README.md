# IAprovale by Augustus: documentação

O IAprovale encontra concursos públicos abertos compatíveis com a formação da pessoa e entrega o link direto do portal oficial de inscrição.

Este repositório é público e documenta **o que o produto faz** (funcionalidades, decisões de produto e roadmap). O código do front e do back fica em repositórios privados. Aqui não há chaves, credenciais, dados de usuários nem detalhes de infraestrutura.

## Índice

- [Funcionalidades](docs/funcionalidades.md): o que já existia e o que foi acrescentado, com o estado de cada item.
- [Rebranding (Rodada 1)](docs/rebranding-rodada-1.md): novo visual do app e da home.
- [Pedido de acesso pelo chat](docs/pedido-de-acesso.md): como o pedido e a janela de dúvidas funcionam.
- [Stats do administrador](docs/stats-do-administrador.md): a aba Stats, só para administradores, com a evolução do uso.
- [Eventos de busca](docs/eventos-de-busca.md): o registro de cada busca (horário, custo e tipo, sem conteúdo) que alimenta o Stats por hora, com retenção de 90 dias e o texto para a Política de Privacidade.
- [Solicitações de acesso](docs/solicitacoes-de-acesso.md): como o administrador aprova ou recusa pedidos e como o login é entregue à pessoa.
- [Versão grátis](docs/versao-gratis.md): a versão publicada em produção. Cadastro pelo chat (confirmação do usuário, termos com botões, dúvidas), plano grátis de 17 buscas por dia e avaliação a cada 5 buscas.
- [Configurações do usuário](docs/configuracoes-do-usuario.md): decisões da tela de configurações.
- [Roadmap](docs/roadmap.md): o que vem depois.
- [Decisões de produto](docs/decisoes.md): regras de produto que valem para todo o projeto.

## Legenda de estado

| Estado | Significado |
|---|---|
| **No ar** | Já está em uso. |
| **Pronto, aguardando liberação** | Implementado e testado fora de produção. |
| **Em andamento** | Parte pronta, parte pendente. |
| **Decidido** | Definido, ainda não construído. |
| **Sugerido** | Ideia sem decisão final. |

Endereço do produto: https://augustusai.com.br/iaprovale/

O que está no ar em https://augustusai.com.br/iaprovale/ é a versão grátis: a pessoa cria a própria conta pelo chat da página inicial. O modo por convite (cada login nasce de uma solicitação aprovada pelo responsável) continua existindo como alternativa de build do site, mas não é o publicado. O endereço antigo /iaprovale/gratis/ apenas redireciona para a raiz.
