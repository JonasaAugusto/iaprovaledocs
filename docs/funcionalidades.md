# Funcionalidades

## O que já existia

Estado: **No ar**.

| Área | Funcionalidade |
|---|---|
| Busca | Busca por texto com interpretação por IA (siglas expandidas, cargo e local) |
| Busca | Busca usando o perfil salvo |
| Busca | Opção de usar o currículo salvo como pista extra |
| Resultado | Cartão com cargos compatíveis com a formação, prazo de inscrição e localização |
| Resultado | Aviso de "formação futura" para quem ainda vai se formar |
| Resultado | Selo "Novo" para concursos que não apareceram em buscas anteriores |
| Resultado | Link da matéria do concurso e, quando a IA o encontra, link direto da inscrição |
| Informações | Painel por concurso: vagas, remuneração, taxa, datas importantes, cargos e links oficiais, com aviso de que os dados são extraídos automaticamente |
| PDF | Geração e visualização do PDF dos resultados |
| Perfil | Formação, cidade, estado e currículo |
| Administração | Criar usuário, gerar nova senha, renomear, desativar, reativar, excluir e ver informações de uso |
| Administração | O administrador não exclui nem desativa a própria conta |
| Ajuda | Guia "Como pesquisar" em abas (Começar, Onde buscar, Dicas e Entender o resultado), com exemplo ilustrado do cartão de resultado; cada aba, e cada abertura do guia, começa do alto |
| Aparência | Tema claro e escuro |
| Plataformas | App web e app desktop, ambos com o painel Informações |

Regra de produto: não há pesquisas de exemplo clicáveis, porque cada busca tem custo.

## Acrescentado na Rodada 1 (novembro de 2026)

Estado: **No ar**, em https://augustusai.com.br/iaprovale/.

| Funcionalidade | Estado |
|---|---|
| Novo sistema visual (paleta, fontes, forma e espaçamento) | **No ar** |
| Navegação lateral no computador e barra inferior no celular | **No ar** |
| Barra lateral recolhível no computador, com a escolha lembrada | **No ar** |
| Busca com rótulo visível, validação e estados claros (inicial, carregando, resultados, vazio, erro) | **No ar** |
| Estado da busca na URL e recarregar sem nova busca | **No ar** |
| Área de cursos patrocinados, visível só antes de uma pesquisa e sempre marcada como "Patrocinado" | **No ar** |
| Cartão de resultado com prazo em evidência e um botão principal ("Ir para a inscrição" ou "Ver o concurso") | **No ar** |
| Checklist para completar o perfil | **No ar** |
| Administração com abas (Usuários e Solicitações), blocos, rótulos visíveis e ações sensíveis separadas | **No ar** |
| Tela de login no novo visual, com suporte ao gerenciador de senhas do aparelho (veja [Decisões](decisoes.md)) | **No ar** |
| Home pública nova com demonstração do produto e movimento ao rolar a página | **No ar** |
| Chamada principal da home com Pedir acesso e Ver como funciona, e Login no cabeçalho | **No ar** |
| Marca "IAprovale by Augustus" em duas linhas, igual em todas as telas | **No ar** |
| Ícone do IAprovale (ramo com o nome embaixo) ao adicionar o site à tela de início do celular | **No ar** |
| Pedido de acesso por chat, com verificação do nome de usuário em tempo real (veja [Pedido de acesso](pedido-de-acesso.md)) | **No ar** |
| Janela de 5 minutos de dúvidas com IA depois do pedido, contada no servidor | **No ar** |
| Aviso ao responsável, no Telegram, quando chega um pedido novo | **No ar** |
| Aprovar ou recusar o pedido pelos botões do Telegram, com botão que abre o WhatsApp com o login pronto | **No ar** |
| Aprovar sem enviar: o sistema devolve usuário, senha provisória e mensagem prontos; caixa com "Copiar mensagem" e "Abrir no WhatsApp" | No ar |
| Troca obrigatória da senha provisória no primeiro acesso, com tela própria | No ar |
| Limite de 8 perguntas ou 5 minutos de dúvidas depois do pedido, o que vier primeiro | **No ar** |
| Aba Solicitações na Administração: aprovar ou recusar pedidos (veja [Solicitações de acesso](solicitacoes-de-acesso.md)) | **No ar** |
| Login mostrado uma única vez ao aprovar, com botão de copiar, para o responsável enviar à pessoa | **No ar** |
| Páginas de privacidade e termos de uso | **No ar** |
| Testes automatizados de interface e de acessibilidade: home, chat de pedido de acesso, app, administração, solicitações, configurações e login | **No ar** (todos passando) |
| Melhorias de acessibilidade: bordas dos campos com contraste maior, foco visível e nunca coberto por cabeçalho ou menu, diálogos que deixam o resto da tela inerte, nomes específicos para botões e links, links externos que avisam "abre em nova aba", Perfil com rótulos, preenchimento automático e erros anunciados, título da página por seção, suporte a cores forçadas e aviso de 1 minuto restante no chat de dúvidas | **No ar** |
| Acessibilidade ainda não confirmada: falta auditoria com leitor de tela e tecnologia assistiva reais (2 critérios) e há 1 critério pendente por decisão de produto. Não declaramos conformidade nem certificação (veja [Decisões](decisoes.md)) | Pendente |

## Configurações do usuário

Estado: **No ar**. Detalhes em [Configurações do usuário](configuracoes-do-usuario.md).

| Funcionalidade | Estado |
|---|---|
| Tela de Configurações, separada do Perfil, igual para administrador e usuário | **No ar** |
| Troca de senha, de usuário e de telefone, sempre pedindo a senha atual | **No ar** |
| Telefone com formatação automática enquanto se digita | **No ar** |
| Tema claro, escuro ou automático e tamanho do texto em 3 níveis | **No ar** |
| Preferência "usar o meu currículo" por padrão na busca (vale neste aparelho) | **No ar** |
| Histórico das últimas 10 buscas, com os resultados de cada uma e botão de apagar | **No ar** |
| Baixar os próprios dados, apagar o currículo e "Sair de todos os aparelhos" | **No ar** |
| Excluir a própria conta em duas etapas: senha na tela e resposta "SIM" no WhatsApp | Temporariamente indisponível: o WhatsApp da empresa está fora do ar |
| Excluir a própria conta com o WhatsApp desligado: pedido enviado ao responsável pelo Telegram, que confirma em dois passos | No ar |
| Aviso ao responsável quando o usuário troca o telefone | **No ar** |
| Contato com a equipe pelo WhatsApp, em Ajuda | **No ar** |
| Bloco de saldo e uso de buscas ("em breve") | **No ar** (aviso de que chega em breve) |

## Privacidade e retenção (novembro de 2026)

| Funcionalidade | Estado |
|---|---|
| Páginas de Privacidade e Termos revisadas contra o que o serviço faz hoje (LGPD), com controlador, encarregado, direitos, retenção e transferência internacional | **No ar** (a validação por advogado segue pendente) |
| Limpeza automática diária: pedidos de acesso pendentes ou recusados, avisos ao responsável, exclusões já decididas e buscas do histórico com mais de 90 dias | **No ar** |
| Quem é usuário do IAprovale nunca recebe prospecção da empresa | **No ar** |
| Redefinir a senha de alguém, na Administração, encerra as sessões dela | **No ar** |
| Proteção contra tentativas repetidas de senha também com tentativas simultâneas | **No ar** |
| Bloqueio de login por origem e por usuário: quem erra muito é barrado sem tirar o dono da conta do ar | No ar |
| Proteções contra uso abusivo do pedido de acesso e do pedido de exclusão de conta | **No ar** |

## Ainda por construir

| Funcionalidade | Estado |
|---|---|
| Verificação do telefone por código enviado por WhatsApp, para provar que o número é da própria pessoa | Pronto, desligado por enquanto: depende do WhatsApp da empresa. Até lá, o número troca direto com a senha atual |
| Login expira após 30 dias sem uso | **No ar** |
| WhatsApp só pode ser trocado uma vez a cada 15 dias | **No ar** |
| Cobrança, planos e regras de reembolso | **Decidido** (adiado) |
