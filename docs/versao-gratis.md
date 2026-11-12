# Versão grátis

Estado: **No ar**, servida na raiz do produto, https://augustusai.com.br/iaprovale/. É a versão publicada em produção. O endereço antigo `/iaprovale/gratis/` agora só redireciona para a raiz. A versão por convite deixou de ser a publicada e segue como modo de build alternativo.

## O que é
O site publicado, em que a pessoa cria a própria conta, sem esperar aprovação. É uma fase de teste: a plataforma ainda está sendo avaliada por grupos de concurseiros.

## Como a conta é criada

Este é o fluxo de criação da conta. O envio de e-mail está ligado via Brevo desde **12/11/2026**; o endereço é opcional e pode ser adicionado nas Configurações. Não é necessário receber um e-mail para acessar a conta.

- O cadastro acontece no mesmo chat da página inicial: o botão "Criar conta grátis" abre a janela de conversa. A pessoa conversa com um assistente que guia quatro passos: nome de usuário, celular com DDD, aceite dos Termos e da Política de Privacidade e senha.
- **Usuário.** Ao tocar em enviar, antes de ir ao servidor, abre um pop-up de vidro com "Quer confirmar esse usuário?" e os botões Sim e Não. Se o texto não segue as regras (de 3 a 30 letras, números, ponto, hífen ou sublinhado, sem espaços), não há confirmação: aparece um pop-up com as regras. Maiúsculas são aceitas e viram minúsculas. Usuário já usado também vira pop-up.
- **Celular.** Depois do usuário, o chat pede o celular e explica numa observação menor que ele serve para confirmar a conta e para o contato do suporte. Número inválido ou já usado aparece como pop-up, não como mensagem. Os alertas não têm botão: somem sozinhos depois de alguns segundos, ao tocar neles ou quando a pessoa volta a digitar.
- **Termos.** O chat pede a concordância com os Termos de Uso e a Política de Privacidade (com links) e mostra dois botões sob a mensagem: Aceito e Recuso. Quem recusa recebe uma resposta cordial e, na hora, uma mensagem curta lembrando que é preciso concordar para seguir, com os botões Sim (aceita e segue para a senha) e Sair (fecha o chat, apaga tudo o que foi digitado e o estado local da conversa, descarta a conversa no servidor e não cria conta). Escrever "sim", "aceito" ou "concordo" também vale. O aceite nunca vem da inteligência artificial.
- **Senha.** É digitada num campo próprio dentro da mesma janela, nunca como mensagem do chat, e não passa pela inteligência artificial. Se alguém escrever a senha na conversa, aparece um aviso em pop-up.
- **Conclusão.** O chat avisa que a conta foi criada e mostra um botão largo "Entrar", que leva ao login. A pessoa não entra logada sozinha.
- Quem decide se os dados são válidos é o sistema, não a inteligência artificial.

## Cadastro com e-mail

- O e-mail é **opcional** na conta, com envio ligado desde **12/11/2026**. A pessoa pode adicioná-lo nas **Configurações** e confirma a posse com um código de 6 dígitos, válido por 10 minutos; há opção de reenviar ou trocar o endereço. Endereço e código não passam pela inteligência artificial.
- Se a cota global de envios do dia estiver esgotada, a conta é criada com e-mail pendente, sem impedir o acesso. A pessoa confirma depois em **Configurações**, quando puder pedir um novo código. Um e-mail não confirmado não reserva o endereço: quem comprovar a titularidade pode confirmá-lo, removendo pendências anteriores em outras contas.
- A confirmação habilita o envio de boas-vindas depois de a conta existir; sem cota, fica para a manhã seguinte, com prioridade antes dos resumos. Resumos exigem também a preferência de avisos ligada. Veja as [cotas e condições de envio](funcionalidades.md#cotas-de-e-mail).
- Novidades permanece disponível no site sem e-mail, com avisos por e-mail desativados ou quando não houver cota ou entrega. O resumo diário das 07:00 de São Paulo só sai para conta ativa, endereço verificado e preferência de avisos ligada, quando houver novidades.

## Dúvidas no chat
- A inteligência artificial responde dúvidas em linguagem simples e cordial, mas só com base numa ficha fixa de fatos (o que é o IAprovale, plano grátis e limite diário, dados de concursos podem estar desatualizados, para que serve o celular, que dados guardamos, senha protegida, apagar a conta, como entrar, suporte). O que não está na ficha ela não responde ("isso eu não sei te dizer por aqui"), e não promete prazos, preços ou canais.
- A mensagem da pessoa é tratada como dado, nunca como instrução.
- Depois da resposta o chat retoma o passo em que a pessoa estava. Se a inteligência artificial estiver fora do ar, o chat responde que só ajuda com cadastro e dúvidas sobre o IAprovale e retoma o passo, sem mostrar erro.
- O limite de 10 dúvidas por conversa conta só as mensagens fora do cadastro. Passando dele, o chat não encerra: avisa que a partir dali segue só com o cadastro. Com a conta já criada, convida a entrar.

## Plano grátis
- Limite de **17 buscas por dia**. No cabeçalho do app aparece uma etiqueta discreta com as buscas restantes e o total ("12/17"), atualizada depois de cada busca.
- A cada 5 buscas, aparece um pedido de avaliação (nota de 1 a 5 e comentário opcional). A busca fica pausada até a avaliação ser enviada. Não há limite de avaliações por dia.
- O responsável lê as avaliações pelo painel de administração.
- **Etapa 3 publicada:** uma avaliação nova de [compatibilidade com cargos](compatibilidade.md) com cargos na resposta compartilha a cota de 17 buscas por dia e o contador de avaliação a cada 5 buscas, mesmo quando só usa regras. Acerto do cache de compatibilidade e resposta `sem_perfil` não consomem nova busca ou feedback.
- **Empresas, no ar desde 12/11/2026:** a cota de [IA do Empresas](empresas.md#cota-diária-de-ia) é separada das buscas de concursos e do feedback: 17 chamadas ou US$ 0,01 por conta/dia, o que vier primeiro; tentativas e repetições contam, acertos de cache não consomem. Não representa cobrança à pessoa. E3/E4 são gratuitos no teste, com cobrança desligada; preços e meio de pagamento pendentes. A busca e a prévia de E5 não chamam IA.
- Limites de proteção: uma conta por dia por conexão; um teto total de **1000 cadastros grátis**, depois do qual o cadastro fecha com o aviso de que as vagas acabaram, e quem já tem conta continua entrando normalmente. Não existe limite diário de cadastros.

## Termos de Uso e Política de Privacidade
O plano grátis tem Termos de Uso e Política de Privacidade próprios. O registro histórico desta documentação identifica a versão 1.1 desde 6 de novembro de 2026 e a implementação do aceite `gratis-1.2`, ainda sem confirmação de publicação desse aceite. A ativação do e-mail não comprova qual versão do plano grátis foi apresentada e aceita.

**Modo por convite: textos legais 1.3 vigentes desde 12/11/2026.** Incluem **e-mail opcional**, verificação por código, avisos e a seção **Carreira**, além da **Brevo (Sendinblue SAS, França)** como **operador** de envio de códigos, boas-vindas e resumos, com **transferência internacional** de dados. O remetente público é **IAprovale <avisos@augustusai.com.br>**. A pessoa pode desligar os avisos por e-mail mantendo Novidades no site. Isso não altera a disponibilidade do modo por convite como build alternativo nem troca o site publicado para esse modo.

**Plano grátis: variante 1.3 ainda não ativada**, mantida no site em `scripts/legal-gratis/v1_3.py`. Sua existência não comprova publicação nem aceite `gratis-1.3`. A ativação e o alinhamento entre o texto apresentado e o registro do aceite ficam com o responsável; a validação por advogado continua pendente.

Preservam-se os temas já documentados dos textos do plano grátis: quem somos e contato, dados coletados, finalidades e bases legais (LGPD, art. 7º), uso das avaliações, inteligência artificial e compartilhamento (usuário e telefone não vão à IA no fluxo normal do cadastro; só a pergunta feita fora do fluxo), transferência internacional, retenção, direitos (art. 18), segurança e incidentes, crianças, armazenamento no navegador, limites do plano grátis (17 buscas por dia, avaliação a cada 5, teto de 1.000 cadastros e fase de teste), uso aceitável e foro, além do [registro de eventos de busca e retenção](eventos-de-busca.md). O e-mail serve para confirmar o endereço e entregar os avisos escolhidos.

E-mail e verificação, preferência, Novidades, alertas, acompanhados e controles de resumos e boas-vindas entram na exportação e exclusão. No site já publicado, Novidades lidas são apagadas após 6 meses (mais de 183 dias desde a criação); não lidas ficam até serem lidas e atingirem esse prazo, ou até a exclusão da conta. Há confirmação posterior quando faltar cota e boas-vindas após confirmar o endereço. Os limites e condições de entrega estão em [Funcionalidades](funcionalidades.md).

**Empresas, publicado em 12/11/2026:** a seção Carreira dos textos 1.3 do convite deve ser considerada na conferência do [tratamento de currículo no Empresas](empresas.md#privacidade-e-textos-legais): texto e perfil somente compactados, original opcional também compactado, retenção até apagar, exportação e exclusão (incluindo materiais de E3/E4), cota própria de IA e envio somente ao DeepSeek, com contatos reconhecidos removidos antes do perfil, sem garantia de anonimização, além da transferência internacional. Esta documentação não ativa a variante grátis nem anuncia novo aceite; o alinhamento dos textos apresentados precisa ser conferido pelo responsável e a validação por advogado continua pendente.

## Registro do aceite (prova de consentimento)
Quando a conta grátis é criada, o sistema guarda na própria linha do usuário, como prova do consentimento (LGPD, art. 8º, §2º) e por segurança do cadastro:

| Campo | O que guarda |
|---|---|
| `aceite_termos_em` | data e hora do "aceito" no chat (se a conversa não tiver o instante, o da criação da conta) |
| `aceite_termos_ip` | endereço IP do cliente em texto (não só o código irreversível), lido como o resto do cadastro: primeiro IP do `X-Forwarded-For` atrás do proxy |
| `aceite_termos_versao` | versão dos Termos e da Política aceita, no formato `gratis-<versão>`; por exemplo, `gratis-1.1` |

- **Retenção:** enquanto a conta existir. Excluir a conta apaga a linha do usuário e, com ela, esses três campos; a exportação de dados da própria pessoa os inclui.
- **Quem não tem:** contas antigas e contas por convite ficam com os campos vazios (não passaram pelo chat de cadastro grátis).
- **Texto legal:** os Termos e a Política do plano grátis avisam o registro, a finalidade e a retenção. A versão dos textos (`VERSAO` no site) e `ACEITE_TERMOS_VERSAO` no backend devem mudar juntas, conforme a variante efetivamente apresentada.
- **Implementação anterior (publicação ainda não confirmada):** já implementado no backend, `ACEITE_TERMOS_VERSAO = "gratis-1.2"` registra 1.2 nos novos cadastros quando alinhado aos textos apresentados. A informação de vigência 1.3 do convite não comprova a publicação desse aceite no plano grátis. Os aceites anteriores preservam a versão que a pessoa aceitou, inclusive `gratis-1.1`; não são reescritos. A persistência e a exportação incluem a versão registrada. A variante grátis 1.3 ainda não foi ativada e não autoriza registrar `gratis-1.3`. Veja a [ordem da publicação](pre-deploy.md).
- Decisão do responsável (6 de novembro de 2026): guardar o IP em claro, necessário como prova.

## Mensagens revisadas

Estado: **No ar**, com o envio ligado desde 12/11/2026. As mensagens de e-mail do cadastro e de Configurações tiveram a acentuação corrigida, incluindo “dígitos”, “código”, “amanhã” e “Configurações”. A revisão abrange código inválido, envio indisponível (503) e cota diária esgotada (429), sem mudar nomes de campos, identificadores de botões ou os demais valores do contrato.

## Organização técnica
A criação de usuário passou a ser um núcleo único, usado pelo fluxo por convite e pelo cadastro grátis. Os textos do assistente ficam num único arquivo, para ajuste fácil. O site publicado é o build grátis (publicado com base `/iaprovale/`, na raiz). O build em modo convite continua disponível como alternativa e pode ser usado se o responsável decidir voltar ao acesso só por convite. O processo de publicação gera o build a partir da versão principal do código do site e copia o resultado para a raiz.
