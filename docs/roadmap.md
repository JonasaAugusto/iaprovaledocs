# Roadmap

## Rodada 1 (no ar)

Rebranding do app web e da home, tela de login, páginas de privacidade e termos, pedido de acesso por chat, aba Solicitações na Administração, login enviado por WhatsApp e Configurações completas. Veja [Rebranding](rebranding-rodada-1.md), [Solicitações de acesso](solicitacoes-de-acesso.md) e [Configurações](configuracoes-do-usuario.md).

## Em seguida

- Validação das páginas de Privacidade e Termos por um advogado.

## Pacote de avisos, prazos e e-mail (ainda não publicado)

- Etapas 1 e 2: backend implementado, revisão do site e publicação pendentes. Cadastro com e-mail obrigatório quando o envio estiver configurado, confirmação por código de 6 dígitos e preferência de avisos; sem cota no dia, conta com e-mail pendente para confirmar depois em Configurações. Endereço pendente não reserva o e-mail. Hoje o envio segue desligado, e o cadastro não pede e-mail.
- Até 10 alertas por perfil/termo/UFs, com linha de base ao criar/reativar e até 10 avisos por alerta por dia só para concursos futuros; até 50 concursos acompanhados, com lembretes D-3/D-1 de inscrição, isenção e prova. Rotina às 07:00 de Brasília, modelos de código, boas-vindas e resumo em HTML e texto. Boas-vindas após confirmar o e-mail; sem cota, prioridade na manhã seguinte. Resumo só com novidades, endereço verificado, preferência ligada e envio disponível.
- Cotas globais diárias: 200 códigos e 100 avisos; códigos usam a sobra dos avisos, nunca o contrário. Limpeza diária de Novidades lidas com mais de 6 meses (183 dias desde a criação); não lidas permanecem.
- Estimativa de custo de IA atualizada pelos preços atuais da DeepSeek, com correção da contagem de cache e sem recalcular o histórico. Ver [Stats](stats-do-administrador.md).
- Recursos gratuitos para todas as contas. Exportação e exclusão incluem os novos dados; Termos e Política passam para 1.2, ainda não publicados. Detalhes em [Funcionalidades](funcionalidades.md) e [Versão grátis](versao-gratis.md).

## Etapa 3 (ainda não publicado)

- Backend de [compatibilidade entre perfil e cargos](compatibilidade.md) implementado na versão principal, com regras conservadoras, IA só para explicar lacunas, cache por versão do perfil, cota e recuperação de falhas. A tela ainda depende de integração e revisão; nada desta etapa está em produção.
- A publicação inclui a migração v3_22 junto de v3_17 a v3_21, todas antes do reinício. Termos `gratis-1.2` e acentuação das mensagens já implementados, ainda não publicados. E-mail permanece desligado até a chave SMTP e a revisão correspondente. Veja [Preparação da publicação](pre-deploy.md).

## Rodada 2 (decidido, adiado)

- Saldo de buscas e planos com cobrança (com as regras de cobrança, cancelamento e reembolso publicadas antes).
- Itens salvos.

## Sugerido

- Rebranding do app desktop com o mesmo sistema de design.
- Fluxo de recuperação de senha.
