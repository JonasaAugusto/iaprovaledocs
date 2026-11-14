# Referência da API: administração e erros

Esta referência cobre as mudanças de segurança T4 e T3, implementadas e **ainda não publicadas em produção**. Não é um catálogo completo de rotas. Autenticação e respostas de sucesso mantêm seus contratos anteriores.

## Acesso administrativo

Estado de T4: **Ainda não publicado em produção**.

As rotas sob `/admin/` e as rotas administrativas `/auth/users` respondem **404** quando a chamada está sem credencial de sessão, com credencial inválida, expirada ou revogada, ou com sessão de usuário comum. A resposta é a mesma de uma rota inexistente: `{"detail":"Not Found"}`.

A regra inclui o uso de método incorreto: para esses acessos sem autorização administrativa, retorna 404 sem cabeçalho `Allow`, em vez de revelar os métodos disponíveis por um 405.

| Situação | Resposta |
| --- | --- |
| Sem credencial, credencial inválida ou sessão de usuário comum, inclusive com método incorreto | 404, sem cabeçalho `Allow` |
| Administrador com sessão válida e senha definitiva, método incorreto | 405, com cabeçalho `Allow` |
| Administrador com senha provisória, método aceito | 403, com `detail`: `senha_provisoria` |
| Administrador com senha provisória, método incorreto | 404, sem cabeçalho `Allow` |

Para o administrador autenticado com sessão válida e senha definitiva, o contrato de sucesso permanece e método incorreto continua respondendo 405. A exigência de trocar a senha provisória também permanece: com método aceito, o administrador nessa situação recebe 403 com `senha_provisoria`. Esta mudança não altera a autenticação das rotas comuns nem a credencial da API de parceiros.

## Erros de serviços externos

Estado de T3: **Ainda não publicado em produção**.

| Método e rota | Falha tratada | Resposta |
| --- | --- | --- |
| `POST /search` e `POST /v1/search` | Fonte de concursos indisponível ou resposta inválida | 502, com `detail`: “A fonte de concursos está indisponível no momento, tente novamente em instantes.” |
| `POST /v1/partner/wallet/topup` | Provedor recusa a abertura da recarga | 502, com `detail`: “Não foi possível iniciar a recarga agora. Tente novamente mais tarde.” |

Esses casos não devolvem o corpo bruto nem o texto interno de erro do fornecedor. Os contratos de sucesso e o código 502 permanecem. A tabela delimita as falhas corrigidas; outras validações e erros conservam suas mensagens e códigos próprios, inclusive o 503 quando o pagamento não está configurado.

Os diagnósticos dessas integrações e as limitações dos registros estão em [Privacidade e segurança](privacidade-e-seguranca.md#respostas-e-registros-de-diagnóstico).
