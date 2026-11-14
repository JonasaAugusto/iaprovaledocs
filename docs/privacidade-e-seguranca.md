# Privacidade e segurança

Esta página descreve armazenamento no navegador e as mudanças T4, T3 e T6 implementadas, **ainda não publicadas em produção**. Não altera os textos legais vigentes nem anuncia um novo aceite. Veja os [Termos e a Política de Privacidade](versao-gratis.md#termos-de-uso-e-política-de-privacidade).

## Acesso à administração

Estado de T4: **Ainda não publicado em produção**. Sem credencial válida de administrador, as rotas administrativas respondem 404, como uma rota inexistente, inclusive quando se usa um método incorreto. O contrato do administrador autenticado permanece. Veja os detalhes na [referência da API](referencia-api.md#acesso-administrativo).

## Respostas e registros de diagnóstico

Estado de T3 e dos ajustes de logs de T6: **Ainda não publicado em produção**.

Falhas da fonte de concursos e da abertura de recarga usam mensagens fixas, sem repassar o corpo bruto de erro recebido do serviço externo. Os códigos e os contratos de sucesso permanecem; consulte as [rotas e mensagens](referencia-api.md#erros-de-serviços-externos).

Nos diagnósticos de falha tratados pelo webhook de pagamento e pelo cliente da busca, ficam somente o tipo do erro e o código HTTP, quando disponível, sem o corpo de terceiros. Isso reduz a exposição de conteúdo recebido dos fornecedores. Esta regra descreve esses diagnósticos específicos; não afirma que todos os logs do produto seguem o mesmo formato. Os registros de acesso da infraestrutura exigem conferência separada.

## Retenção e exclusão

Estado de T6: **Ainda não publicado em produção**. A rotina de limpeza foi implementada para execução diária, removendo identificadores e dados de acesso vencidos mesmo sem novos cadastros. Horário: **03:30, horário de Brasília**.

| Registro | Prazo e ação da limpeza |
| --- | --- |
| Hash de IP dos pedidos, inclusive aprovados | 30 dias desde a criação; remove só o hash, preservando o pedido aprovado |
| Falhas de login | 1 dia |
| Eventos do cadastro | 2 dias |
| Sessões do cadastro | Vencidas há mais de 1 dia ou criadas há 30 dias |
| Registros de envio de e-mail do cadastro | 24 horas |
| IP, data e versão do aceite dos termos | Enquanto a conta existir; os três são apagados com a conta |

O hash é um identificador protegido do IP; não é o IP em texto claro. O IP do aceite tem a retenção própria indicada na tabela e na [prova de consentimento](versao-gratis.md#registro-do-aceite-prova-de-consentimento).

Os prazos são critérios da limpeza diária, não garantia de remoção no segundo exato do vencimento. Há limite por execução para a limpeza dos identificadores de rede; um acúmulo pode exigir execuções seguintes. Falhas de login têm retenção de 1 dia; isso não muda a duração do bloqueio temporário de autenticação.

Pedidos pendentes ou recusados continuam sujeitos à retenção de 90 dias; pedidos aprovados permanecem enquanto a conta existir e saem com ela, mas seu hash de IP passa a seguir o prazo menor da tabela. Histórico e [eventos de busca](eventos-de-busca.md) continuam com retenção de 90 dias. As regras próprias de Novidades, currículo e materiais permanecem nas respectivas páginas.

A exclusão da conta apaga também o aceite completo dos termos: data, versão e IP. Data e versão não são mantidas separadamente como prova após a exclusão. Esta descrição não substitui a validação jurídica pendente dos textos legais.

## Armazenamento no navegador

O aplicativo usa `sessionStorage` para o token da sessão, os dados do usuário e a última atividade. Esses dados ficam na sessão da aba; sair da conta remove os três. Há também estados temporários de navegação e busca, conforme a [busca fora da URL](navegacao.md#busca-fora-da-url).

O `localStorage` guarda preferências como tema, tamanho do texto, menu e “usar currículo”, além de outros estados de interface. Essas preferências podem persistir depois de fechar o navegador; não são a credencial de login. Veja as [Configurações](configuracoes-do-usuario.md).

O backend não define cookies. O armazenamento descrito serve ao funcionamento e às preferências do aplicativo, sem rastreio publicitário ou ferramentas de acompanhamento de navegação. Isso não significa ausência de registros de segurança, de uso ou de busca: as finalidades e os prazos correspondentes continuam documentados acima e nas páginas vinculadas.
