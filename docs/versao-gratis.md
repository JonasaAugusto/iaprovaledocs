# Versão grátis

Estado: **No ar** em `/iaprovale/gratis/`, ao lado do site por convite, que continua igual.

## O que é
Uma variante do site em que a pessoa cria a própria conta, sem esperar aprovação. É uma fase de teste: a plataforma ainda está sendo avaliada por grupos de concurseiros.

## Como a conta é criada
- O cadastro acontece no mesmo chat da página inicial: o botão "Criar conta grátis" abre a janela de conversa. A pessoa conversa com um assistente que guia quatro passos: nome de usuário, celular com DDD, aceite dos Termos e da Política de Privacidade e senha.
- **Usuário.** Ao tocar em enviar, antes de ir ao servidor, abre um pop-up de vidro com "Quer confirmar esse usuário?" e os botões Sim e Não. Se o texto não segue as regras (de 3 a 30 letras, números, ponto, hífen ou sublinhado, sem espaços), não há confirmação: aparece um pop-up com as regras. Maiúsculas são aceitas e viram minúsculas. Usuário já usado também vira pop-up.
- **Celular.** Depois do usuário, o chat pede o celular e explica numa observação menor que ele serve para confirmar a conta e para o contato do suporte. Número inválido ou já usado aparece como pop-up, não como mensagem. Os alertas não têm botão: somem sozinhos depois de alguns segundos, ao tocar neles ou quando a pessoa volta a digitar.
- **Termos.** O chat pede a concordância com os Termos de Uso e a Política de Privacidade (com links) e mostra dois botões sob a mensagem: Aceito e Recuso. Quem recusa recebe uma resposta cordial e, na hora, uma mensagem curta lembrando que é preciso concordar para seguir, com os botões Sim (aceita e segue para a senha) e Sair (fecha o chat, apaga tudo o que foi digitado e o estado local da conversa, descarta a conversa no servidor e não cria conta). Escrever "sim", "aceito" ou "concordo" também vale. O aceite nunca vem da inteligência artificial.
- **Senha.** É digitada num campo próprio dentro da mesma janela, nunca como mensagem do chat, e não passa pela inteligência artificial. Se alguém escrever a senha na conversa, aparece um aviso em pop-up.
- **Conclusão.** O chat avisa que a conta foi criada e mostra um botão largo "Entrar", que leva ao login. A pessoa não entra logada sozinha.
- Quem decide se os dados são válidos é o sistema, não a inteligência artificial.

## Dúvidas no chat
- A inteligência artificial responde dúvidas em linguagem simples e cordial, mas só com base numa ficha fixa de fatos (o que é o IAprovale, plano grátis e limite diário, dados de concursos podem estar desatualizados, para que serve o celular, que dados guardamos, senha protegida, apagar a conta, como entrar, suporte). O que não está na ficha ela não responde ("isso eu não sei te dizer por aqui"), e não promete prazos, preços ou canais.
- A mensagem da pessoa é tratada como dado, nunca como instrução.
- Depois da resposta o chat retoma o passo em que a pessoa estava. Se a inteligência artificial estiver fora do ar, o chat responde que só ajuda com cadastro e dúvidas sobre o IAprovale e retoma o passo, sem mostrar erro.
- O limite de 10 dúvidas por conversa conta só as mensagens fora do cadastro. Passando dele, o chat não encerra: avisa que a partir dali segue só com o cadastro. Com a conta já criada, convida a entrar.

## Plano grátis
- Limite de **17 buscas por dia**. No cabeçalho do app aparece uma etiqueta discreta com as buscas restantes e o total ("12/17"), atualizada depois de cada busca.
- A cada 5 buscas, aparece um pedido de avaliação (nota de 1 a 5 e comentário opcional). A busca fica pausada até a avaliação ser enviada. Não há limite de avaliações por dia.
- O responsável lê as avaliações pelo painel de administração.
- Limites de proteção: uma conta por dia por conexão; um teto total de **1000 cadastros grátis**, depois do qual o cadastro fecha com o aviso de que as vagas acabaram, e quem já tem conta continua entrando normalmente. Não existe limite diário de cadastros.

## Termos de Uso e Política de Privacidade
O plano grátis tem Termos de Uso e Política de Privacidade próprios (versão 1.0, em vigor desde 6 de novembro de 2026), com seções numeradas: quem somos e contato, dados coletados, finalidades e bases legais (LGPD, art. 7º), uso das avaliações, inteligência artificial e compartilhamento (o usuário e o telefone não vão à IA no fluxo normal; só a pergunta feita fora do fluxo), transferência internacional, retenção, direitos (art. 18), segurança e incidentes, crianças, armazenamento no navegador, limites do plano grátis (17 buscas por dia, avaliação a cada 5, teto de 1.000 cadastros, fase de teste), uso aceitável e foro. O texto do site por convite não muda.

## Organização técnica
A criação de usuário passou a ser um núcleo único, usado pelo fluxo por convite e pelo cadastro grátis. Os textos do assistente ficam num único arquivo, para ajuste fácil. A versão grátis é ligada por configuração e pode ser desligada sem alterar o site por convite.
