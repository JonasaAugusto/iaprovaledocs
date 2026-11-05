# Pedido de acesso pelo chat

O acesso ao IAprovale é por convite. Quem quer entrar pede pelo chat da página inicial; o login só é criado depois da análise do pedido.

Estado: front e backend **no ar**. A aprovação do pedido, a criação do login e a confirmação por WhatsApp continuam manuais.

## Como a conversa funciona

1. O chat abre e o agente diz, com o campo bloqueado: "Oi! Para analisar e liberar o seu acesso à plataforma, preciso guardar o seu nome, o seu telefone e o usuário que você quer, ok?" Não há pergunta de sim ou não.
2. O campo só destrava quando há uma pergunta para responder. Ordem: nome completo, telefone (com máscara e DDD) e nome de usuário.
3. Enquanto o agente fala, o campo fica bloqueado e a cor do botão e do campo escurece de forma gradual (no tema escuro, o dourado). Ao destravar, clareia de forma gradual. Com "reduzir movimento" ligado, a troca é instantânea.
4. O nome de usuário é verificado em tempo real, a cada caractere digitado (a partir do terceiro). O botão de enviar fica apagado e só acende quando o servidor confirma que o nome está livre; nesse caso aparece um "V" discreto dentro do campo. Se o nome já existir, aparece um aviso flutuante em vidro translúcido ("Tente outro usuário."), sem empurrar a conversa, e a pessoa apaga e escreve outro. O servidor responde apenas livre ou em uso, sem dizer o motivo e sem devolver listas, e limita a quantidade de consultas por conexão. Se mesmo assim o servidor recusar no envio, o campo reabre com o mesmo usuário marcado como em uso, sem repetir a pergunta.
5. Depois do envio, o agente confirma que o usuário receberá a confirmação no WhatsApp, com login e senha, e convida: "Enquanto você não recebe o seu acesso, pode tirar algumas dúvidas comigo!"
6. Começa uma janela de **5 minutos** de dúvidas, com um cronômetro no topo do chat, ao lado do botão de fechar. Ao zerar, o chat é bloqueado.

## Janela de dúvidas

- O tempo é contado no servidor. O navegador só exibe o relógio, então fechar e reabrir o chat não renova a janela.
- Cada janela tem um número máximo de perguntas.
- Quem já usou uma janela recentemente pode ainda enviar o pedido, mas não ganha nova janela de dúvidas.
- As respostas são geradas por IA com instruções fixas: só falam do IAprovale como descrito nesta documentação, não inventam preços, prazos nem funcionalidades, e não pedem dados pessoais. Quando não sabem, indicam que a equipe responde pelo WhatsApp.

## Outros assuntos

Os botões "Quero anunciar" e "Falar sobre a API" usam o mesmo chat, com nome, telefone e uma frase. Não pedem nome de usuário.

## Dados guardados

Nome, telefone, nome de usuário desejado e, nos pedidos comerciais, a mensagem. O endereço de rede (IP) não é guardado em claro. Não há coleta de e-mail.

## Para a equipe (administradores)

Uma lista de pedidos recebidos fica disponível para administradores. A criação do login e o envio da confirmação pelo WhatsApp continuam manuais; a automação está no roadmap (Rodada 2).
