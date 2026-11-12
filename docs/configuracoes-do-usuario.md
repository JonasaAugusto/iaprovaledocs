# Configurações do usuário

Vale para administrador e usuário comum. Estado: **No ar**, incluindo o pedido de exclusão pelo Telegram e a tela de nova senha no primeiro acesso. As adições de e-mail e dos dados de avisos abaixo estão **ainda não publicadas**.

## Estrutura

- Perfil e Configurações são telas separadas, cada uma com seu item na barra.
- O administrador tem as mesmas configurações. A Administração continua na própria aba.
- A tela é uma coluna só, em seções: Conta, Aparência, Busca, Histórico de buscas, Dados e privacidade, Uso e plano e Ajuda. Cada ajuste é uma linha com o valor atual e a ação; o formulário abre na própria linha, sem janela por cima.

## Conta

- **Usuário:** o próprio usuário pode alterar, informando a senha atual. O perfil e os dados permanecem, porque o vínculo é pelo identificador interno. Aceita de 3 a 30 caracteres: letras sem acento, números, ponto, hífen ou sublinhado, e não pode repetir o de outra pessoa.
- **Estado atual:** a confirmação por código está desligada enquanto o WhatsApp da empresa está fora do ar. Nesse período o número troca direto, informando a senha atual, continua valendo o intervalo de 15 dias, a etiqueta "verificado" e a ação "Verificar" não aparecem, e a exclusão da conta é pedida ao responsável pelo Telegram (veja Dados e privacidade). O texto abaixo descreve o fluxo completo, que volta quando a confirmação for religada.
- **WhatsApp (telefone):** editável, informando a senha atual, e só vale depois de confirmado por código. A pessoa digita o número (com formatação automática no padrão brasileiro com DDD, aceitando número colado com o código do país) e toca em "Enviar código". Um código de 6 dígitos chega por WhatsApp nesse número e vale por 10 minutos. Na mesma linha, a tela mostra "Enviamos um código de 6 dígitos para o WhatsApp final XXXX" e um campo só para dígitos, com "Confirmar", "Reenviar código" (liberado depois de uma contagem regressiva visível) e "Cancelar". Código errado mostra quantas tentativas restam; o código é de uso único, e ao esgotar as tentativas ou vencer é preciso pedir outro. Enquanto não confirma, vale o número antigo. Se a página for recarregada com um código pendente, a tela volta direto para a etapa do código. Ao confirmar, o responsável recebe um aviso (só com o final do número) e o número novo fica fora da lista de prospecção. Existem limites de envio para proteger quem recebe as mensagens. O WhatsApp só pode ser trocado uma vez a cada 15 dias, contados da confirmação da troca anterior; antes disso a tela avisa em quantos dias dá para trocar de novo, sem enviar código. O primeiro cadastro e a verificação do número que já está na conta não têm essa espera. Ao lado do número aparece a etiqueta discreta "verificado"; número cadastrado e ainda não verificado mostra "não verificado" e a ação "Verificar", que manda o código para o número que já está na conta.
- **Senha:** troca direta, pedindo a senha atual, com regras mínimas. Ao trocar, os outros aparelhos saem da conta.
- **Nova senha obrigatória:** quem entra com senha provisória (conta nova ou senha gerada pelo administrador) vê primeiro uma tela de nova senha. Ela pede a senha provisória e a nova senha, explica as regras e só libera o aplicativo depois da troca. Não fecha por Esc nem por clique fora; dá para sair da conta.
- **E-mail (ainda não publicado):** em produção, ainda não é coletado. Quando o envio estiver configurado, será possível cadastrar, confirmar o endereço pendente do cadastro ou trocar o e-mail, com código de 6 dígitos válido por 10 minutos. Até confirmar uma troca, continua valendo o endereço anterior, se houver. Um e-mail não confirmado não reserva o endereço; outra pessoa que prove a titularidade pode confirmá-lo, e a pendência anterior é removida. A verificação pendente mostra o endereço mascarado; código vencido ou tentativas esgotadas exigem um novo pedido. Há espera para reenviar e limites de proteção, informados pelo serviço; sem cota global, só é possível pedir um novo código no dia seguinte. É possível remover o e-mail, o que também cancela a verificação pendente. Hoje o envio está desligado, e não é possível pedir códigos.
- **Avisos por e-mail (ainda não publicado):** preferência ativada por padrão, mas o resumo só é enviado com e-mail verificado, preferência ligada e envio disponível. A pessoa pode desligar os avisos por e-mail sem perder a caixa de Novidades dentro do site. Boas-vindas só sai após confirmar o endereço; sem cota, fica para a rotina da manhã seguinte, antes dos resumos. Veja [Funcionalidades](funcionalidades.md) para as cotas globais, alertas e lembretes.
- **Segurança:** "Sair de todos os aparelhos" encerra a conta em todos os lugares, inclusive no aparelho atual. Errar a senha atual várias vezes bloqueia essa troca por um tempo, sem impedir o login. O login expira depois de 30 dias sem uso: quem passa esse tempo sem abrir o IAprovale precisa entrar de novo. Usar o serviço renova o prazo.

## Aparência

- Tema claro, escuro ou automático (segue o aparelho).
- Tamanho do texto em 3 níveis: normal, grande e maior.
- As duas escolhas ficam salvas no aparelho.

## Busca

**Usar o meu currículo:** quando ligado e com currículo salvo no Perfil, a busca já começa com ele como pista extra. Vale só neste aparelho e muda na hora, sem recarregar a página.

## Histórico de buscas

Lista das últimas 10 buscas, com a data e a quantidade de concursos encontrados. Cada busca abre ali mesmo e mostra os resultados da época (título, local, prazo e o link do concurso), com o aviso de que os prazos podem ter mudado. Há botões para apagar uma busca ou todas. Cada busca é guardada por 90 dias e tudo é apagado junto com a conta.

## Dados e privacidade

- **Baixar meus dados:** um arquivo com o que o IAprovale guarda sobre a pessoa: perfil, currículo, histórico de buscas, o registro de uso de buscas por dia, a data de criação da conta, o telefone cadastrado (e se foi verificado) e a data do último acesso. Não inclui senha nem dados de outras pessoas.
  - **Ainda não publicado (etapas 1 e 2):** a exportação passa a incluir e-mail, estado e data de verificação, preferência de avisos e itens de Novidades; na etapa 2, inclui também os alertas e os concursos acompanhados com suas datas. Não inclui os códigos de confirmação.
  - O pacote ainda não publicado inclui também os registros de controle de avisos repetidos, resumos e boas-vindas da própria conta. Novidades lidas com mais de 6 meses (183 dias desde a criação) são apagadas na limpeza diária; não lidas permanecem. Esses prazos são próprios de Novidades, sem alterar os 90 dias do histórico de buscas.
  - **Ainda não publicado (etapa 3):** inclui o cache de [compatibilidade](compatibilidade.md) da própria conta em `compatibilidades`, com versão do perfil, estado, data e resposta quando disponível. O prazo de 90 dias do histórico não se aplica automaticamente a esse cache.
- **Currículo salvo:** apaga o texto do currículo enviado, com confirmação na própria linha.
- **Sair de todos os aparelhos:** com confirmação na própria linha.
- **Excluir minha conta:** ação separada, em tom neutro, no fim da seção. Só está disponível com o WhatsApp verificado; se o número ainda não foi confirmado, a seção explica que é preciso verificá-lo antes e oferece o atalho. Funciona em duas etapas: (1) a pessoa informa a senha atual na tela e o sistema manda uma mensagem ao WhatsApp cadastrado, repetindo o nome do usuário; (2) a conta só é excluída se a pessoa responder "SIM". Qualquer outra resposta cancela, e o pedido vale por 24 horas. Trocar o telefone cancela o pedido pendente, e a tela mostra o pedido em andamento com a opção de cancelar. Excluir apaga a conta, o perfil, o histórico e o pedido de acesso que a originou, mesmo que o usuário ou o telefone tenham sido trocados depois da aprovação. Contas de administrador não são excluídas por aqui.
  - **Sem confirmação por código (situação atual):** o botão volta a funcionar. A pessoa informa a senha atual e o pedido vai ao responsável pelo Telegram, que confirma em dois passos (primeiro pede para continuar, depois confirma a exclusão). **Cancelar** no segundo passo encerra o pedido. A tela mostra "pedido enviado ao responsável" e o pedido vale por 24 horas. Nada é excluído sem a confirmação do responsável.
  - **Ainda não publicado (etapas 1 e 2):** a exclusão da conta, tanto pelo fluxo da pessoa quanto pelo administrador, apaga também o e-mail, os registros de verificação, a preferência de avisos e os itens de Novidades; na etapa 2, apaga também os alertas, os concursos acompanhados e os registros usados para evitar avisos repetidos, além dos controles de resumos e boas-vindas.
  - **Ainda não publicado (etapa 3):** ambas as formas de excluir a conta apagam também o cache de compatibilidade por cascata.

## Uso e plano

Aviso de que o saldo e o uso de buscas chegam em breve, até haver planos com cobrança.

## Ajuda

Texto e botão "Falar com a equipe no WhatsApp", que abre uma conversa com o número da empresa.

## O que não entra

- Política de privacidade e termos não aparecem nas configurações; ficam no rodapé da home.
- Lista de sessões e aparelhos conectados.
- Configurações extras para administradores.
