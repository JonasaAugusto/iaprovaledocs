# Anunciantes (cursos preparatórios)

Estado: implementado em branches (`anunciantes` no backend 2.7.0 e no docs, `anunciantes-front` no site 3.7.0). Ainda não publicado nem ativado.

## Modelo comercial
- Mensalidade: R$ 1.000 por anunciante, com uma posição inicial: a **vitrine de cursos na busca (posição 3)**. Rodízio por perfil da busca fica para depois e é configurável.
- Comissão: **5% sobre o valor da matrícula** de cada aluno que veio pelo site, paga **quinzenalmente** (quinzenas 1 a 15 e 16 ao fim do mês).
- Contrato mínimo de **6 meses**; cancelar antes custa **2 mensalidades** (R$ 2.000).
- **Sem estorno**: comissão paga não volta se o aluno pedir reembolso depois. Matrícula cancelada antes do pagamento da matrícula não gera comissão. A opção `estorna_comissao` (por anunciante, padrão desligada) existe só para uma negociação futura.
- Tudo é dado em tabela: mensalidade, comissão, multa, janela do clique, início e fim mínimo por anunciante. Não há código por anunciante.

## Como o IAprovale prova que o aluno veio do site
Vale a venda se UMA das duas formas apontar para o IAprovale; a mesma matrícula nunca é paga duas vezes (unicidade por anunciante e matrícula).

1. **Cupom**: exclusivo, no formato `IAPROVALE-NOMEDOCURSO`. O aluno usa na matrícula; o contratante registra o cupom na lista que envia.
2. **Código do clique**: cada clique no anúncio (`GET /r/{id}`) gera um código aleatório de 10 caracteres e leva o aluno ao site do curso com `?utm_source=iaprovale&utm_medium=anuncio&utm_campaign=<id>&iaprovale_clique=<código>`. O contratante guarda o parâmetro e informa o código na matrícula. Vale por 30 dias (configurável) entre o clique e a matrícula.

Se as duas batem, o critério é "ambos" e a comissão é paga uma vez. Clique fora da janela, sem cupom válido, vira **contestada**, para conferência. Sem cupom nem clique válido, fica em **não atribuídas** (pode virar atribuída se uma nova lista trouxer a prova).

## Privacidade
O clique guarda só código, anúncio e data e hora. Não há IP, user agent, usuário ou telefone. Sem cookie. O limite contra cliques inflados é um contador por anúncio e por minuto em memória. O anunciante não recebe dado de usuário. Retenção prevista dos cliques: 12 meses. Os textos legais ainda não foram alterados: os trechos prontos estão em `entrega/anunciantes/trechos-privacidade-termos.md` (para a versão 1.2).

## Fechar um novo anunciante em 5 comandos
Com a ficha preenchida (`docs/anunciantes-ficha.md` do backend):

```
python -m scripts.migrate_v3_14_anuncios          # uma única vez, na primeira ativação
python -m scripts.anunciantes novo --nome "Curso X" --razao-social "..." --cnpj "..." --contato "..." --titulo "Curso X" --descricao "..." --url https://cursox.com.br/oferta --area saude --uf SP,MG
python -m scripts.anunciantes listar              # confere status, cupom e link de rastreio
python -m scripts.anunciantes importar-vendas matriculas.csv --anunciante 1   # a cada quinzena, com a lista do contratante
python -m scripts.anunciantes fechamento --quinzena 2026-11-1 --md            # relatório e valor a cobrar
```
O `novo` imprime o resumo, o **link de rastreio** (`<API>/r/<id>`) e o texto pronto para o contratante (como usar o cupom e o parâmetro `iaprovale_clique`). Outros comandos: `pausar [--retomar]` e `encerrar` (calcula a multa de 2 mensalidades se antes de 6 meses).

## Quinzena e relatório
- Identificador `AAAA-MM-1` (dias 1 a 15) ou `AAAA-MM-2` (16 ao fim do mês). Vale a data da matrícula.
- O contratante envia a lista até o dia 17 (1ª quinzena) e até o dia 2 do mês seguinte (2ª quinzena): CSV com `matricula_id, data, valor, cupom, codigo_clique` (cupom e código opcionais; aceita `;` ou `,` e valor como `1.299,90`).
- Importação: CLI `importar-vendas` ou `POST /admin/anuncios/vendas/importar` (CSV ou JSON, só admin). A resposta separa importadas, contestáveis, não atribuídas, duplicadas e inválidas.
- Fechamento: `GET /admin/anuncios/relatorio?anunciante=&quinzena=` (JSON) e `/admin/anuncios/relatorio.md`. Traz cliques, matrículas atribuídas, valor das matrículas, comissão devida, mensalidade do período (metade do mês em cada quinzena), total a pagar e não atribuídas.
- Status de cada venda: pendente (a pagar), aprovada, contestada, paga, estornada. `PATCH /admin/anuncios/vendas/{id}` muda o status.

## Vitrine no site
O app tenta `GET <API>/anuncios?posicao=vitrine`. Com itens, mostra esses cartões, com link sempre via `/r/` da API (conta o clique). Sem resposta, com erro ou lista vazia, usa `App/data/cursos.json`; sem ele, mostra o cartão "Anuncie aqui!". O visual não mudou. A política de segurança do app já permitia a API em `connect-src`.

## Pendências do responsável
- Preencher os dados do IAprovale nas cláusulas (razão social, CNPJ, foro, prazo de pagamento) e revisar com assessoria jurídica.
- Aplicar os trechos de privacidade e termos (versão 1.2) antes de ativar o primeiro anunciante e avisar os usuários.
- Definir PIX ou nota fiscal e o dia do pagamento.
- Criar a rotina que apaga cliques com mais de 12 meses (ainda não implementada).
