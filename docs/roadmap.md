# Roadmap

## Rodada 1 (no ar)

Rebranding do app web e da home, tela de login, páginas de privacidade e termos, pedido de acesso por chat, aba Solicitações na Administração, login enviado por WhatsApp e Configurações completas. Veja [Rebranding](rebranding-rodada-1.md), [Solicitações de acesso](solicitacoes-de-acesso.md) e [Configurações](configuracoes-do-usuario.md).

## Em seguida

- Validação das páginas de Privacidade e Termos por um advogado.

## Avisos e prazos publicados; e-mail pendente

- Novidades, alertas e acompanhamento publicados, conforme informado em 12/11/2026. Cadastro com e-mail ainda não publicado: obrigatório quando o envio estiver configurado, confirmação por código de 6 dígitos e preferência de avisos; sem cota no dia, conta com e-mail pendente para confirmar depois em Configurações. Endereço pendente não reserva o e-mail. Hoje o envio segue desligado, e o cadastro não pede e-mail.
- Até 10 alertas por perfil/termo/UFs, com linha de base ao criar/reativar e até 10 avisos por alerta por dia só para concursos futuros; até 50 concursos acompanhados, com lembretes D-3/D-1 de inscrição, isenção e prova. Rotina às 07:00 de Brasília, modelos de código, boas-vindas e resumo em HTML e texto. Boas-vindas após confirmar o e-mail; sem cota, prioridade na manhã seguinte. Resumo só com novidades, endereço verificado, preferência ligada e envio disponível.
- Cotas globais diárias: 200 códigos e 100 avisos; códigos usam a sobra dos avisos, nunca o contrário. Limpeza diária de Novidades lidas com mais de 6 meses (183 dias desde a criação); não lidas permanecem.
- Estimativa de custo de IA atualizada pelos preços atuais da DeepSeek, com correção da contagem de cache e sem recalcular o histórico. Ver [Stats](stats-do-administrador.md).
- Recursos gratuitos para todas as contas. Exportação e exclusão incluem os novos dados; Termos e Política passam para 1.2, ainda não publicados. Detalhes em [Funcionalidades](funcionalidades.md) e [Versão grátis](versao-gratis.md).

## Etapa 3 publicada

- [Compatibilidade entre perfil e cargos](compatibilidade.md) publicada em Alertas > Acompanhando, conforme informado em 12/11/2026, com regras conservadoras, IA só para explicar lacunas, cache por versão do perfil, cota e recuperação de falhas.
- O registro das dependências v3_17 a v3_22 e da conferência dos termos `gratis-1.2` permanece em [Preparação da publicação](pre-deploy.md). E-mail continua desligado até a chave SMTP e a revisão correspondente.

## IAprovale Empresas em produção

- [E1/E2](empresas.md): no ar desde **12/11/2026** (backend ef7dc58 ou posterior; site 0ccfa9d ou posterior). Currículo compactado com original opcional, perfil, compatibilidade 0–10 calculada em Python, explicação opcional e cota própria de 17 chamadas ou US$ 0,01 por conta/dia, o que vier primeiro. Exportação e exclusão abrangem os dados privados. Currículos longos usam `perfil-2`, com teto de resposta de 3.500 tokens.
- [E3/E4](empresas-e3-e4.md) publicados e **gratuitos no teste**, com **cobrança desligada**: currículo ATS em PDF/Word/copiar e roteiro de entrevista por vaga. Os **preços** e o **meio de pagamento** seguem **pendentes**; nenhuma tarifa é anunciada como aprovada.
- [E5](empresas-vagas.md) publicado: busca de vagas, panorama e prévia gratuita sem IA; índice atualizado às 06:00 de São Paulo, validade de 72 horas e cobertura pública restrita aos ATS suportados.
- [Carreira, Alertas e nova navegação](navegacao.md) publicados. O acesso à Carreira depende da resposta de `/empresas/cota`.
- Pendências: validação jurídica e conferência dos textos legais sobre armazenamento, remoção de contatos antes do perfil, DeepSeek e transferência internacional. Veja o registro de dependências em [Preparação da publicação](pre-deploy.md#empresas-em-produção).

## Rodada 2 (decidido, adiado)

- Saldo de buscas e planos com cobrança (com as regras de cobrança, cancelamento e reembolso publicadas antes).
- Itens salvos.

## Sugerido

- Rebranding do app desktop com o mesmo sistema de design.
- Fluxo de recuperação de senha.
