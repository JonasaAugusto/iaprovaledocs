# Empresas: busca de vagas e panorama (E5)

Estado: **No ar** desde **12/11/2026**, na opção **Buscar vagas** da aba [Carreira](navegacao.md#carreira). A busca consulta um índice local de vagas públicas; não faz candidatura automática nem garante cobertura de todo o mercado.

## Consulta

As rotas são autenticadas. Os caminhos são relativos à API do backend.

| Método e caminho | Comportamento |
|---|---|
| `GET /empresas/vagas` | Pesquisa as vagas do índice, com filtros e paginação abaixo. |
| `GET /empresas/panorama` | Consulta o panorama das vagas disponíveis no índice local. |
| `GET /empresas/vagas/{id}/compatibilidade` | Prévia gratuita por regras para a vaga identificada na busca. |

Parâmetros de consulta de `GET /empresas/vagas`:

| Parâmetro | Uso |
|---|---|
| `termo` | Termo para pesquisar vagas. |
| `uf` | Filtro por unidade da federação. |
| `remoto` | Filtro de trabalho remoto. |
| `empresa` | Filtro por empresa. |
| `ats` | Filtro pelo sistema público de vagas da empresa. |
| `limite` | Quantidade de itens da página. |
| `offset` | Deslocamento para consultar as próximas páginas. |

Enquanto **não há índice**, o serviço responde **503**: indisponibilidade não significa ausência de vagas. Os resultados e o panorama representam a base local disponível, não uma consulta completa aos sites no momento da busca.

## Índice e cobertura

- A atualização diária do índice é feita pelo timer **`iaprovale-empresas-vagas`**, às **06:00 de São Paulo** (`America/Sao_Paulo`). **Código de saída 2 = coleta parcial aceita**: algumas fontes podem falhar e a coleta ainda ser aproveitada. Isso não significa cobertura completa.
- `EMPRESAS_INDICE_PATH` seleciona o arquivo de índice local. Esta documentação não expõe o caminho usado em produção nem instruções de alteração do serviço.
- As vagas têm validade de **72 horas** no índice. A fonte pode encerrar uma vaga antes disso; confirme disponibilidade e requisitos no anúncio oficial.
- O catálogo reúne **176 empresas** em `data/empresas` no backend. Estar no catálogo não garante vagas abertas, coleta bem-sucedida ou participação de todas as empresas em cada atualização.
- A cobertura é restrita aos sistemas públicos **Greenhouse, Lever, Ashby, Workable e SmartRecruiters**, em fontes cuja coleta é permitida por **`robots.txt`**. Não há acesso a páginas privadas ou contorno de restrições. **Gupy não está implementado**; o catálogo não amplia a lista de fontes suportadas.

## Prévia de compatibilidade

A consulta `GET /empresas/vagas/{id}/compatibilidade` oferece uma **prévia gratuita, sem IA**, usando os requisitos disponíveis e comparação **por regras** com o perfil do currículo. Não consome chamadas de IA nem executa a extração e a explicação sob demanda de [E2](empresas.md#e2--compatibilidade-e-explicação).

É uma prévia limitada aos dados do índice e do perfil; requisitos ausentes ou incompletos reduzem o que pode ser comparado. O resultado **não é chance de contratação** nem garantia de elegibilidade. Para a análise de uma descrição ou link de vaga, veja o fluxo de E2 e sua cota própria; confirme sempre os requisitos na fonte oficial.
