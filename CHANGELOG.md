# Changelog da documentação do IAprovale

Versões [SemVer](https://semver.org/lang/pt-BR/) alinhadas ao que a documentação descreve: maior = mudança de produto,
menor = funcionalidade documentada, correção = ajuste de texto.

## [1.9.0] - não publicada
- Aba Stats do administrador (backend 2.8.0, site 3.8.0): períodos Hoje, Este mês, 7, 30 e 90 dias, números-resumo e gráficos de uso. Ver `docs/stats-do-administrador.md`.

## [1.8.1] - 2026-11-06
- O botão Mostrar da senha usa um campo espelho em vez de trocar o tipo do campo (compatibilidade com Safari/iOS). Site 3.6.1. No ar.

## [1.8.0] - 2026-11-06
- Preparo para uso comercial: descrição e título da home para o plano grátis, prévia de link (og/twitter e imagem 1200x630), canonical, robots, sitemap, JSON-LD, página 404, aviso de fase de teste na home e no app, aviso de dados sensíveis no currículo; exportação de feedbacks em markdown e custo no resumo do Telegram. Ver `docs/preparo-comercial.md`.

## [1.7.1] - 2026-11-06
- Espaços "Anuncie aqui!" (faixa na home e cartão na vitrine vazia do app) e o fluxo de contato de anunciantes. Decisão 28. No ar.

## [1.7.0] - 2026-11-06
- Registro do aceite dos Termos e da Política no cadastro do plano grátis (data e hora, IP e versão aceita), com finalidade, retenção e exclusão com a conta. Termos e Política do plano grátis na versão 1.1. No ar (backend 2.5.0, site 3.5.1). Botão "Mostrar" da senha ajustado para Safari/iOS.

## [1.6.2] - 2026-11-06
- Resumo diário de cadastros no Telegram do responsável, às 19h de São Paulo (cadastros do dia, grátis e por convite, e total de contas). No ar.

## [1.6.1] - 2026-11-06
- Versão grátis agora é a publicada, servida na raiz https://augustusai.com.br/iaprovale/; /iaprovale/gratis/ só redireciona. A versão por convite passa a ser modo de build alternativo. Decisões 1, 25, 26 e 27 atualizadas. Chat de cadastro revisado e limites novos (1.6.0) já no ar.
- Resumo diário de cadastros no Telegram do responsável, às 19h de São Paulo (cadastros do dia, grátis e por convite, e total de contas).

## [1.6.0] - 2026-11-06
- Chat do plano grátis revisado: confirmação do usuário, alertas em pop-up, termos com botões (Aceito/Recuso, Sim/Sair), botão "Entrar" ao concluir, dúvidas respondidas pela IA só com uma ficha fixa, limite de 10 dúvidas por conversa.
- Plano grátis com 17 buscas por dia e etiqueta no cabeçalho; uma conta por dia por conexão; teto total de 1000 cadastros no lugar dos limites diários; sem limite de avaliações por dia. Termos de Uso e Política de Privacidade do plano grátis. Decisões 26 e 27.

## [1.5.1] - 2026-11-05
- Cadastro grátis feito dentro do chat da página inicial, não em página separada.

## [1.5.0] - 2026-11-05
- Versão grátis no ar: cadastro pelo chat, plano grátis com limite diário, avaliação a cada 5 buscas e decisão 25.

## [1.4.1] - 2026-11-05
- Teste de segurança externo autorizado: sem falha crítica ou alta. Mensagens de erro de validação não devolvem mais o que foi enviado, e salvar o perfil preserva campos não enviados. Limite de tentativas de login confirmado em funcionamento.

## [1.4.0] - 2026-11-05
- Aprovação sem envio automático: caixa de login com "Copiar mensagem" e "Abrir no WhatsApp".
- Troca obrigatória da senha provisória no primeiro acesso, com tela de nova senha.
- Exclusão da conta pedida ao responsável pelo Telegram, em dois passos, enquanto o WhatsApp está desligado.
- Login com bloqueio por origem e por usuário, sem números internos.
- Decisões 22 a 24.

## [1.3.0] - 2026-11-05
- Acessibilidade verificada por script e por testes, sem auditoria com leitor de tela real: melhorias no ar e o que ainda não foi confirmado.
- Decisões novas: tempo do chat de dúvidas é limite de custo, sem prorrogação; texto da home esmaece de propósito na rolagem lenta.
- Confirmação do telefone por código registrada como desligada por enquanto, até haver WhatsApp para o produto.

## [1.2.0] - 2026-11-05
- Sessões de 30 dias, intervalo de 15 dias do telefone, avisos e aprovação de pedidos pelo Telegram, login entregue pelo responsável, verificação por código desligada por enquanto.

## [1.1.0] - 2026-11-05
- Exclusão de conta em duas etapas, retenção de 90 dias, exportação de dados, privacidade e termos.

## [1.0.0] - 2026-11-05
- Rodada 1 no ar: Solicitações de acesso, Configurações, endereço `/iaprovale/`, login.

## [0.1.0] - 2026-11-04
- Primeira versão: funcionalidades, rebranding, roadmap e decisões.
