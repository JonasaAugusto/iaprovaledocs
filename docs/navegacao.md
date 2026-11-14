# Navegação do site e Carreira

Estado: **No ar** desde **12/11/2026**. Esta página descreve as telas publicadas e identifica separadamente os ajustes do front 3.13.0 (publicado em 13/11/2026), sem alterar a interface.

## Barra e topo

A barra de navegação apresenta **Concursos, Carreira, Perfil, Administração e Estatísticas**, conforme a disponibilidade do serviço e as permissões da conta. Administração e Estatísticas são exclusivas de administradores. A barra fica na lateral no computador e embaixo no celular.

No topo, **Alertas** fica junto do **sino**, e **Configurações** ocupa o lugar do atalho de tema. Tema claro, escuro ou automático continua disponível nas Configurações. A home ganhou uma seção do **Empresas** e um **menu no celular** para acessar suas seções.

## Busca fora da URL

Estado: **Publicado em 13/11/2026**, front **3.13.0**. O texto da busca fica fora da URL da página: texto, modo de busca, uso do currículo e UFs ficam no histórico do navegador (`history.state`). Os botões voltar e avançar e a ação de recarregar preservam o estado da busca, sem depender de `?q=` ou `uf=` na URL.

Um link antigo com `?q=` abre a busca uma vez e a URL é limpa. Copiar o endereço da página não compartilha a busca; quem recebe o link precisa informar os critérios. Esse histórico de navegação é diferente do [histórico de buscas da conta](configuracoes-do-usuario.md#c4-histórico-enxuto), que tem retenção própria no serviço. A mudança na URL da página não significa que o texto deixou de ser enviado à API para executar a busca.

## Login

No front 3.13.0, publicado em 13/11/2026, a gravação compartilhada da sessão acontece só no navegador; isso não impõe uma única sessão no backend, e vários aparelhos continuam permitidos.

## C8: início agregado

Estado: **Ainda não publicado**. O backend implementa `GET /me/inicio` para reunir em uma chamada as quatro leituras usadas no início do aplicativo. “Agregado” significa que a resposta junta informações antes consultadas separadamente. A adaptação do front segue separada; esta entrega não confirma uso pela interface nem publicação.

A consulta exige a mesma sessão Bearer (a credencial de acesso enviada pelo aplicativo) e senha definitiva das rotas individuais. Retorna HTTP 200, isto é, leitura bem-sucedida, com quatro campos obrigatórios, todos restritos à conta autenticada:

| Campo | Origem equivalente | Conteúdo |
|---|---|---|
| `cota` | `GET /empresas/cota` | Mesmo objeto da cota diária do Empresas; não é a cota de buscas de concursos. Inclui `dia`, `chamadas`, `limite_chamadas`, `custo_usd`, `limite_usd`, `chamadas_restantes` e `esgotada`. |
| `acompanhados` | `GET /me/acompanhando` | Mesma lista de concursos, com datas e metadados, ordenada por próxima data futura, criação e identificador. Sem acompanhados, retorna lista vazia. |
| `perfil` | `GET /profile` | Mesmo objeto completo do Perfil de concursos, incluindo `updated_at` (data da atualização). Se nunca foi salvo, retorna objeto com campos nulos e `updated_at` gerado no instante da leitura, em vez de `null` no lugar do objeto. |
| `nao_lidas` | `GET /me/novidades` | Mesmo contador: inteiro não negativo com todas as novidades não lidas da conta, sem limite de página, sem textos nem lista de novidades. |

Sem uso prévio, a cota tem consumo zero. Mesmo esgotada, a consulta retorna HTTP 200 com `esgotada: true`. A leitura não consome nem reserva chamadas de IA, não cria perfil, não marca novidades como lidas e não consulta provedores externos. A autenticação mantém a renovação usual da sessão.

Sessão ausente, inválida, expirada ou revogada, ou conta inativa, resulta em 401 (acesso não autorizado). Senha provisória resulta em 403 (acesso impedido), com `detail: "senha_provisoria"`; é necessário definir a senha definitiva. Não há resposta parcial: falha em uma leitura falha a requisição inteira. As consultas usam uma mesma sessão de banco, mas isso não garante que todos os campos retratem o mesmo instante se outra requisição alterar dados durante a leitura.

As quatro rotas individuais permanecem disponíveis com contratos intactos por uma versão, como alternativa de recuperação (fallback). O aplicativo pode substituir as quatro chamadas pela agregada; isso depende da adaptação do front. O lote é entregue sem migração de banco e preserva as regras de [cota do Empresas](empresas.md#cota-diária-de-ia) e de [Novidades e acompanhamento](funcionalidades.md#avisos-e-prazos-publicados-e-mail-ligado).

## Carreira

A aba Carreira **só aparece** quando **`GET /empresas/cota` responde** e confirma a disponibilidade do backend Empresas. Oferece duas opções:

- **Currículo e vaga:** envio de **PDF/DOCX/TXT até 5 MB**, acompanhamento do perfil extraído e comparação com uma vaga. O resultado apresenta nota de **0 a 10 com régua**, pontos fortes, lacunas e a ação **“Por que essa nota?”**. Os limites de extração e as situações de perfil pendente estão em [Empresas E1/E2](empresas.md).
- **Buscar vagas:** consulta ao índice e prévia gratuita por regras, com cobertura e validade descritas em [Busca de vagas (E5)](empresas-vagas.md).

O C11, **ainda não publicado**, prevê [coleta incremental SmartRecruiters](empresas-vagas.md#c11-coleta-incremental-smartrecruiters): a primeira coleta é lenta; as seguintes ficam mais rápidas ao reaproveitar os detalhes de vagas sem alteração. Uma coleta parcial preserva vagas já conhecidas ainda não revisitadas como desatualizadas, respeitando a validade do índice. Isso não garante cobertura completa nem confirma mudança na interface publicada.

Quem já tem currículo salvo no Perfil pode **usar o currículo do Perfil** em vez de enviar o arquivo de novo, e o botão **Preencher com currículo**, no começo do Perfil, completa só os campos vazios com o que o currículo tiver, avisando o que preencheu.

Os materiais são **por vaga**: currículo ATS em **PDF**, **Word** (DOCX) ou texto para **copiar**, e **roteiro de entrevista**. Consulte as regras conservadoras de geração, a cota e o teste gratuito em [E3/E4](empresas-e3-e4.md). A nota não representa chance de contratação e os materiais precisam ser revisados pela pessoa antes do uso.

## Envio de currículo: aviso de tamanho

Estado: **Publicado em 13/11/2026**, front **3.13.0**. Na Carreira e no Perfil, o navegador confere o limite de **5 MB** antes de enviar o currículo. Acima do limite, o envio é recusado e o aviso mostra o tamanho real do arquivo, por exemplo: “O arquivo tem 7,3 MB. O limite é 5 MB…”. Reduza o arquivo e tente novamente.

Se o envio for recusado pelo servidor com **413**, a tela mostra a mesma orientação sobre o limite de 5 MB, sem o tamanho real do arquivo. A conferência no navegador não substitui a validação do servidor.

## Detalhe do histórico

Após a liberação do C4 do backend, as novas buscas em Configurações mostram título e link, sem local e prazo no detalhe; registros antigos não são reescritos e podem continuar completos até a retenção removê-los. O front 3.13.0 não ativa o C4. Veja o [contrato e os prazos do histórico](configuracoes-do-usuario.md#c4-histórico-enxuto).

## Acessibilidade dos avisos

Os avisos de erro e de confirmação (`role="alert"` no App e no Login) ficam sempre na página e só o texto muda, para o leitor de tela anunciá-los; sem texto, não ocupam espaço. O visual não mudou. O app não carrega mais scripts de CDN: Alpine e leitor de PDF são servidos pelo próprio site.

## Alertas

Em **Alertas > Acompanhando**, cada concurso acompanhado permite consultar a compatibilidade **por cargo**, com motivo e lacunas. É a [compatibilidade educacional de concursos](compatibilidade.md), que usa o Perfil de concursos e a cota de buscas desse produto; é diferente da comparação com currículo e vagas de empresas na aba Carreira.

O sino dá acesso às Novidades. O envio de e-mail está ligado via Brevo desde 12/11/2026; o endereço é opcional nas Configurações, e o resumo das 07:00 de São Paulo exige e-mail verificado e preferência ativa. Novidades permanece disponível no site, inclusive sem cota ou entrega por e-mail. Veja [Avisos e acompanhamento](funcionalidades.md#alertas-e-concursos-acompanhados).

## Endereços das abas

As abas têm endereço por fragmento, após a URL do aplicativo:

| Fragmento | Destino |
|---|---|
| `#alertas` | Alertas e acompanhamento de concursos. |
| `#carreira` | Currículo, comparação e busca de vagas de empresas. |
| `#admin` | Administração. |
| `#stats` | Estatísticas de uso para administradores (aba **Estatísticas**). |
| `#config/<secao>` | Seção de Configurações; por exemplo, `#config/privacidade`. |

Um endereço direto respeita as permissões da conta e a disponibilidade do recurso. O fragmento não concede acesso administrativo nem torna a aba Carreira disponível sem o backend. Veja também [Configurações do usuário](configuracoes-do-usuario.md#estrutura).
