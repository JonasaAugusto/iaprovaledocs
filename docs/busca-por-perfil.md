# Busca pelo perfil, filtro por nível e regra de cota

Estado: **no ar** (backend 2.10.0, publicado em 06/11/2026). A migração `migrate_v3_16_feedbacks_fk` já foi aplicada antes do backend.

## Por que mudou

Quem tinha só a escolaridade no perfil (por exemplo Fundamental e Médio, em Rio de Janeiro/RJ) recebia zero resultados em "Buscar com meu perfil". A IA de interpretação transformava a escolaridade em termo de busca ("fundamental médio") e o filtro procurava essas palavras no nome do cargo. O campo de nível do concurso (Ensino Médio, Fundamental / Médio, Superior...) vem da fonte e não era usado. A mensagem de zero resultados ainda sugeria "tente em alguns dias", e a busca vazia gastava uma das buscas do dia e contava para a avaliação.

## Buscar com meu perfil

- Frases reconhecidas (sem diferenciar maiúsculas, acentos nem pontuação): "Buscar com meu perfil", "buscar pelo meu perfil", "usar meu perfil", "meu perfil", "concursos para mim" e variações próximas.
- A consulta é **determinística e não chama a IA**: custo zero e o mesmo resultado a cada vez. Usa a UF e a cidade do perfil:
  - mobilidade **local** com cidade: só os concursos da cidade (mais os nacionais, desde a 2.11.0);
  - mobilidade **estado** (ou local sem cidade): cidade mais a lista da região, mantendo só a UF do perfil (mais os nacionais, desde a 2.11.0);
  - **qualquer** ou sem mobilidade: cidade mais a região, ordenados por proximidade (mesma UF, mesma região, resto);
  - sem UF no perfil: lista geral.
- Em seguida entra o filtro por nível.

## C9: cache da PCI

Estado: **Ainda não publicado**. As consultas à fonte pública PCI Concursos passam a reutilizar respostas em memória. Esse cache é uma cópia temporária da resposta da fonte, compartilhada entre buscas atendidas pelo mesmo processo do serviço, antes dos filtros e das anotações de cada pessoa.

A entrada é identificada pela ferramenta e argumentos enviados à fonte; mudar a ordem das chaves dos argumentos não cria outra entrada. A validade é de **5 minutos** após guardar a resposta; reutilizar a entrada não renova o prazo. Ao vencer, a próxima consulta volta à fonte. Há até **500 entradas por processo**; ao ultrapassar o limite, as mais antigas são removidas. Cada processo tem sua própria cópia, perdida ao reiniciar, sem persistência no banco.

Uma lista vazia válida também pode ser reutilizada. Respostas com avisos e falhas não alimentam o cache, permitindo nova consulta à fonte na próxima tentativa. Consultas simultâneas sem entrada válida podem fazer mais de uma chamada para os mesmos critérios; este lote não reúne essas chamadas em uma só.

A chave usa SHA-256, um resumo da ferramenta e dos argumentos: não guarda os termos em claro na chave e não acrescenta identificação da conta, perfil completo ou currículo. Os critérios de consulta podem derivar da busca ou do perfil; o resumo não garante anonimato desses critérios. Só a resposta pública da fonte é reutilizada. Cada busca recebe uma cópia independente antes dos filtros e das anotações, como `is_new` e cargos compatíveis, evitando compartilhar marcas pessoais entre buscas.

Esse cache não torna a busca gratuita nem altera cotas, avaliação, histórico ou custos das demais etapas de IA. Ele é diferente do cache de equivalentes de cargo, do cache de compatibilidade por pessoa e do cache de tokens do provedor. Pode apresentar dados da fonte ainda não renovados dentro da validade: confirme no edital e no portal oficial os requisitos e os prazos antes da inscrição.

## C6a: equivalentes de cargo

Estado: **Ainda não publicado**. Nas buscas em linguagem natural, o filtro local passa a aceitar os termos originais da formação ou todos os termos de um cargo equivalente sugerido pelo DeepSeek. Exemplo: Direito encontra Advogado entre os cargos já retornados pela fonte. A comparação usa palavras inteiras, sem diferença de acentos ou maiúsculas: Advogado não corresponde a Superadvogado; TI não corresponde a infantil ou dentista só por conterem essas letras. Cada formação admite até cinco equivalentes.

O C6a não amplia a consulta à fonte: amplia somente o filtro dos cargos já retornados. UFs, inscrições abertas, escolaridade e datas mantêm suas regras. A geração não ocorre na busca só por nível nem quando a fonte retorna uma lista vazia. Esta etapa não se aplica à consulta determinística “Buscar com meu perfil”, que continua sem IA. A tabela curta de siglas como alternativa fica para C17; não integra esta entrega.

Cada busca admite geração para até três formações sem cache válido, em paralelo, com teto conjunto de seis segundos de espera pelo modelo. Acertos do cache não consomem esse limite. As demais formações seguem com os termos originais e podem tentar gerar equivalentes em outra busca. A chamada de equivalentes é feita sem retentativas automáticas, inclusive nos alertas. Se o provedor falhar ou o teto for atingido, a busca segue com os termos originais para as formações sem resposta, sem erro por essa etapa; respostas já concluídas e seu uso são preservados. Chamadas pendentes são canceladas e não geram uma entrada vazia no cache. O teto limita a espera pelo modelo, não o tempo total da busca: não interrompe operações síncronas do banco que estejam bloqueadas.

Os equivalentes são sugestões conservadoras; o modelo pode errar e não comprova habilitação para o cargo. Confira sempre os requisitos no edital. A validação limita formato, tamanho e quantidade, sem garantir o significado de toda sugestão.

### Reutilização, privacidade e falhas

Cache significa guardar uma resposta para reutilizá-la. Aqui ele é global, compartilhado por formação, sem vínculo com usuário: formações iguais após uniformizar acentos, maiúsculas e espaços usam a mesma entrada. Ela contém uma chave SHA-256 (resumo da formação normalizada), os equivalentes normalizados e a expiração. Não guarda o texto original da formação, busca, currículo, e-mail ou localização. O resumo não é garantia de anonimato, sobretudo para formações raras.

Nesta geração, o DeepSeek recebe somente o termo da formação normalizado, além da instrução fixa; nenhum dado do usuário, perfil completo, currículo ou identificação da conta é enviado nesta chamada. Isso descreve apenas a geração de equivalentes, não as demais etapas da busca. Os registros técnicos mostram estado do cache e quantidade de equivalentes, sem formação nem cargos, SQL, parâmetros ou texto das exceções. A validação descarta e-mails, telefones e URLs na saída e equivalentes isolados genéricos: professor, técnico, analista, auxiliar e assistente. Cargos específicos como “analista de sistemas” continuam aceitos.

Respostas com equivalentes valem 30 dias; uma lista vazia válida vale 24 horas. Após vencer, a entrada é renovada na próxima consulta. Entradas vencidas são substituídas sob demanda; não há limpeza periódica neste lote. Erros de comunicação, JSON inválido e chamadas canceladas não são guardados: o filtro mantém os termos originais e pode tentar gerar equivalentes em outra consulta.

A transação do cache é independente da busca. Uma falha no cache não derruba a busca: falhas de leitura, inclusive tabela ausente ou conteúdo inválido, mantêm os termos originais sem chamar o modelo. Falhas de escrita preservam os equivalentes recém-gerados para aquela busca, mas não os guardam para reutilização.

Nos alertas, a geração opcional respeita o saldo de chamadas compartilhado com as demais etapas. Sem saldo, ainda pode usar um cache válido; sem ele, segue com os termos originais. Consultas simultâneas sem cache podem gerar mais de uma chamada para a mesma formação; não há garantia de uma única chamada nem teto global de custo neste lote.

### Estimativa de custo

Uma resposta válida no cache usa zero tokens adicionais nesta etapa. Cada geração admite entrada de até 120 caracteres de formação mais a instrução fixa e saída de até 200 tokens (unidades de texto cobradas pelo provedor).

Exemplo de orçamento: com 200 tokens de entrada sem cache e 200 de saída, a estimativa pelas tarifas do código é US$ 0,0003 por geração, ou US$ 0,30 por 1.000 formações distintas em 30 dias, antes de renovações e chamadas simultâneas. Não é cotação atual nem fatura; conferir as tarifas antes de orçar. O cache de formações é diferente do desconto de cache de tokens do provedor descrito em [Estatísticas](stats-do-administrador.md#estimativa-de-custo-ainda-não-publicado).

Os tokens informados pelo provedor entram no custo registrado da busca, inclusive quando a resposta tem JSON inválido. Falhas e cancelamentos sem informação de uso não permitem estimar o número exato de tokens. Cancelar a espera não garante que o processamento no provedor tenha parado. A [preparação da publicação](pre-deploy.md#c6a-cache-de-equivalentes-de-cargo) descreve a dependência do banco e a reversão.

## C7: ranking por relevância

Estado: **Ainda não publicado**. Ranking é a ordem de relevância dos resultados. O C7 ordena localmente as buscas por texto e pelo perfil, sem IA nesta etapa. “Buscar com meu perfil” continua sem IA em todo o caminho. Os filtros de inscrições abertas, UF, formação e formação futura continuam anteriores à ordenação, sem novo limite de resultados.

A localização tem prioridade sobre cargo e prazo. Com UFs selecionadas, vale a ordem escolhida, com nacionais depois. Sem seleção e sem local explícito, a preferência é mesma UF do perfil, mesma região e demais locais. Local explícito não recebe preferência regional do perfil; sem UF válida, contam apenas cargo e prazo.

Dentro de cada grupo geográfico, cargo exato vale 200 pontos; correspondência parcial por palavras inteiras vale 100; seleção apenas por nível vale zero. A comparação ignora maiúsculas, acentos e pontuação. Conta o melhor cargo do concurso, considerando a formação em uso, o cargo ou termo extraído da busca e os equivalentes já obtidos. A formação futura só pontua nos resultados admitidos pelas regras de prazo já existentes.

O prazo de inscrição completo e válido acrescenta `max(1, 30 - dias)` pontos: quanto menos dias faltam, maior a prioridade; dias negativos são tratados como zero no cálculo, sem dispensar o filtro de inscrições abertas. São aceitas datas ISO (`AAAA-MM-DD`) e `DD/MM/AAAA`. Data ausente ou inválida vale zero, sem inventar prazo. Em empate de pontos, vem a data mais próxima; em empate completo, fica a ordem recebida, inclusive a preferência da cidade já aplicada na busca pelo perfil.

Cada grupo geográfico soma múltiplos de 1.000 pontos. Na seleção de UFs, a primeira recebe a quantidade de UFs vezes 1.000, a seguinte recebe 1.000 a menos, até a última com 1.000; nacionais recebem zero. Na preferência regional, mesma UF soma 2.000, mesma região soma 1.000 e demais locais zero. Cargo e prazo não ultrapassam essa prioridade.

### Campos da resposta

Em `POST /search`, cada item de `results` recebe os campos adicionais abaixo. A pontuação não é probabilidade de aprovação e não deve ser comparada entre buscas.

| Campo | Tipo | Significado |
|---|---|---|
| `pontuacao` | Inteiro | Soma relativa de localização, cargo e prazo nesta busca. |
| `motivo` | Texto | Explica cargo, localização quando aplicável, prazo confirmado ou não e formação futura quando houver. |
| `compatibilidade_cargos` | Lista | Avaliação por cargo na ordem da fonte, com `nome`, `nivel`, `motivo` e `falta` (lacunas a confirmar). |

O motivo da ordenação é diferente do motivo de compatibilidade de cada cargo. `cargos_compativeis` continua indicando correspondência textual e não comprova habilitação. Veja os [limites do selo por cargo](compatibilidade.md#c7-selo-na-resposta-da-busca). A apresentação visual do selo e do motivo depende da integração de quem usa a resposta; esta entrega não anuncia uma nova tela.

A marca `is_new`, a contagem, o histórico e as condições de formação futura mantêm seus contratos. O PDF recebe a ordem da busca e ainda aplica sua preferência por novos.

## Filtro por nível

- O nível do perfil vem da escolaridade marcada (fundamental, médio, técnico, superior; "pós" conta como superior). Se há graduação ou pós preenchida, o perfil também conta como superior. Valem exatamente os níveis marcados: quem marcou só Médio não recebe concurso só de Superior.
- O concurso entra se o campo de nível dele citar **qualquer** nível do perfil ("Fundamental / Médio / Técnico / Superior" serve para quem marcou Médio).
- Quem tem graduação, técnico, pós ou áreas continua com o casamento por cargo; os dois somam-se, e os concursos que casam por cargo aparecem primeiro, com os cargos compatíveis. Concursos que entram só pelo nível mostram os primeiros cargos.
- Só concursos com inscrição aberta.

## Escolaridade nunca vira termo

- A instrução da IA proíbe colocar escolaridade em termo, cargo ou formação mencionada. O código também descarta qualquer termo que seja só nível ("fundamental médio", "nível superior", "ensino médio").
- Busca com nível citado ("concurso de nível superior no RJ") usa o nível citado no lugar do perfil e a UF da própria busca.
- Antes de responder "defina sua formação", o sistema tenta o nível da escolaridade. A mensagem só aparece se o perfil não tem nem formação nem nível.

## Zero resultados

- Mensagem nova e curta: "Não encontrei vagas abertas para essa busca. Tente um cargo (ex.: Administrativo) ou veja os concursos da sua cidade por nível." Sem UF no perfil, o fim vira "ou informe sua cidade no perfil."
- Busca com zero resultados **não conta** na cota diária do plano grátis, no contador de avaliação (a cada N buscas) nem no histórico de buscas.
- Se a busca vazia gastou a IA, o custo real continua somado no dia (painel e Stats), sem somar busca nem resultados. Para não virar laço de chamadas pagas, essas buscas entram num teto técnico de 20 por hora por usuário (resposta 429). O anti-rajada de 10 buscas por minuto continua valendo para todas. A consulta por perfil não gasta IA e não entra nesse teto.
- O limite diário do plano grátis segue valendo para qualquer busca com resultado.

**Etapa 3 publicada, conforme informado em 12/11/2026:** a [compatibilidade detalhada por cargo](compatibilidade.md), em Alertas > Acompanhando, é uma consulta própria sobre concursos acompanhados. Uma avaliação nova com cargos compartilha a cota de buscas e o contador de avaliação, mesmo com comparação só por regras; acerto do cache de compatibilidade e `sem_perfil` não consomem de novo. Isso não altera a busca determinística pelo perfil descrita acima.

## Exclusão de conta e avaliações

- A exclusão feita pelo administrador agora apaga também as avaliações, o histórico de buscas, as verificações de telefone, os avisos ao responsável e o pedido de acesso da conta, igualando a exclusão pela própria pessoa. Antes ficavam avaliações órfãs.
- A migração `migrate_v3_16_feedbacks_fk` apaga as avaliações de contas que não existem mais e cria a chave estrangeira de `feedbacks.user_id` para `users.id` com exclusão em cascata. É idempotente, não mexe em avaliações de contas existentes e, se a criação da chave falhar, mostra o erro sem desfazer nada.

## Riscos e ideias

- Quem tem graduação passa a receber também concursos de nível superior de qualquer área pela busca por perfil (depois dos que casam por cargo). Mais resultados, menos precisão.
- Mobilidade vazia ou "qualquer" não restringe a UF: concursos de outros estados aparecem depois dos locais. O filtro rígido de UF foi feito à parte, na 2.11.0 (ver `docs/filtro-de-uf.md`).
- Concurso sem nível informado pela fonte só entra se casar por cargo.

## Testes

Backend: `tests/test_search_perfil.py` (frases, nível, mobilidade, IA que falha se chamada, termo de nível, cota, avaliação, histórico e teto), `tests/test_exclusao_avaliacoes.py` (exclusão pelo administrador e migração em SQLite e Postgres), com amostra real da fonte em `tests/fixtures/mcp_perfil_rj.json`.
