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

## Busca por palavra e ordenação — C2

Estado: **Ainda não publicado**. A correção C2 está implementada no backend e aguarda revisão e publicação; o estado **No ar** acima se refere à busca E5 já publicada.

A busca passa a exigir **todos os termos** informados, procurando em título, descrição, empresa e área. A comparação usa **palavras completas**, em vez de aceitar qualquer pedaço de uma palavra: `Java` não encontra `JavaScript`, e `C` não equivale a `C++`. Acentos não impedem a comparação (`análise` e `analise` encontram o mesmo termo), e o texto original da vaga é preservado.

São aceitas equivalências limitadas, como `Go` e `golang`, sem confundir `Go` com `Google` ou `algoritmo`. Para evitar confusões, siglas curtas como `JS` e `RH` precisam aparecer em maiúsculas no anúncio; o nome `Go` também aceita a inicial maiúscula. Não há promessa de reconhecer qualquer sinônimo ou abreviação.

Na ordenação, cada termo encontrado no título soma um ponto: vagas com mais termos no título aparecem primeiro. Em caso de empate, a ordem é por empresa, título e identificador. Essa ordenação ocorre **antes da paginação**. Sem termo de busca, vale a ordem por empresa, título e identificador. Essa prioridade não é uma nota de compatibilidade com o currículo nem uma recomendação de contratação.

## Reutilização do índice — C2

Estado: **Ainda não publicado**, junto com a busca por palavra do C2.

O backend passa a usar um **cache**, uma cópia em memória do índice já lido e preparado para buscas. Enquanto o arquivo permanece igual, ele é reutilizado, inclusive entre consultas simultâneas. A mudança do arquivo, identificada pela data de modificação e outras marcas do próprio arquivo, faz com que seja recarregado na próxima consulta. Isso reduz leituras repetidas; não aumenta a frequência da coleta nem a cobertura das fontes.

Os textos para comparação são preparados durante a coleta. Índices antigos continuam aceitos e são preparados em memória na primeira leitura, sem migração. Essa preparação interna não aparece nos resultados da busca.

A validade continua sendo verificada **a cada consulta**, mesmo usando o cache: vagas com mais de 24 horas desde a coleta são marcadas como desatualizadas, e aquelas com mais de **72 horas** ficam fora dos resultados. Uma vaga também pode trazer a marca de desatualização da coleta. Se o arquivo estiver ausente ou inválido, o serviço retorna **503** e não usa a cópia anterior para ocultar a falha. Um índice válido sem vagas dentro da validade pode retornar uma lista vazia.

A prévia de compatibilidade localiza a vaga diretamente pelo identificador entre as vagas válidas do índice atual. Se ela não estiver mais nesse conjunto, a consulta responde **404** (vaga não encontrada); o cache não prolonga a disponibilidade da vaga.

## Índice e cobertura

- A atualização diária do índice é feita pelo timer **`iaprovale-empresas-vagas`**, às **06:00 de São Paulo** (`America/Sao_Paulo`). **Código de saída 2 = coleta parcial aceita**: algumas fontes podem falhar e a coleta ainda ser aproveitada. Isso não significa cobertura completa.
- `EMPRESAS_INDICE_PATH` seleciona o arquivo de índice local. Esta documentação não expõe o caminho usado em produção nem instruções de alteração do serviço.
- As vagas têm validade de **72 horas** no índice. A fonte pode encerrar uma vaga antes disso; confirme disponibilidade e requisitos no anúncio oficial.
- O catálogo reúne **176 empresas** em `data/empresas` no backend. Estar no catálogo não garante vagas abertas, coleta bem-sucedida ou participação de todas as empresas em cada atualização.
- A cobertura é restrita aos sistemas públicos **Greenhouse, Lever, Ashby, Workable e SmartRecruiters**, em fontes cuja coleta é permitida por **`robots.txt`**. Não há acesso a páginas privadas ou contorno de restrições. **Gupy não está implementado**; o catálogo não amplia a lista de fontes suportadas.

## Prévia de compatibilidade

A consulta `GET /empresas/vagas/{id}/compatibilidade` oferece uma **prévia gratuita, sem IA**, usando os requisitos disponíveis e comparação **por regras** com o perfil do currículo. Não consome chamadas de IA nem executa a extração e a explicação sob demanda de [E2](empresas.md#e2--compatibilidade-e-explicação).

É uma prévia limitada aos dados do índice e do perfil; requisitos ausentes ou incompletos reduzem o que pode ser comparado. O resultado **não é chance de contratação** nem garantia de elegibilidade. Para a análise de uma descrição ou link de vaga, veja o fluxo de E2 e sua cota própria; confirme sempre os requisitos na fonte oficial.
