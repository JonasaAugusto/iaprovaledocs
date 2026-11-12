# Empresas: currículo ATS e pacote de entrevista

**Estado: ainda não publicado.** Backend implementado em branch, aguardando revisão e integração. Telas, textos legais e cobrança real continuam pendentes.

## Como usar

O currículo precisa estar enviado, com perfil pronto. Primeiro calcule a compatibilidade da vaga; depois escolha a geração para essa vaga. Os produtos usam o currículo da própria conta e os requisitos já processados.

| Produto | Preço previsto por geração |
|---|---|
| Currículo ATS em PDF ou DOCX | R$ 1,49 |
| Pacote de entrevista | R$ 2,99 |

Nesta entrega nenhum valor é debitado. O bloqueio por saldo/plano está desligado por padrão. O gancho de elegibilidade pode ser integrado pelo responsável; se for ligado sem integração disponível, a geração fica indisponível. Consulta de saldo não substitui a futura reserva e cobrança do pagamento.

## Currículo ATS

A adaptação prioriza tópicos originais conforme os requisitos da vaga, preservando contatos, contexto, cronologia e demais informações do currículo. Apresenta separadamente palavras presentes e ausentes, lacunas e dicas para o LinkedIn. Competências ausentes não são inseridas no arquivo como experiência adquirida.

O PDF usa uma coluna e texto selecionável, sem imagens ou tabelas. O DOCX preserva Unicode. Se o PDF não puder representar algum caractere, o download informa a limitação e sugere DOCX, sem substituir silenciosamente o texto.

A checagem é conservadora: só aceita citações comprovadas no texto original. Não faz paráfrases livres nem acrescenta empresa, cargo ou número. Um número existente em outro contexto não comprova uma nova conquista. A pessoa deve revisar o documento antes de enviá-lo. Não há garantia de aprovação em sistemas ATS ou de contratação.

## Pacote de entrevista

Inclui perguntas prováveis por requisitos da vaga, lacunas e rascunhos de histórias no método STAR: situação, tarefa, ação e resultado. As histórias usam somente conquistas comprovadas no currículo. Quando falta informação, o campo fica pendente e o pacote mostra perguntas para a pessoa completar com fatos reais. O pacote não inventa responsabilidades ou resultados e não garante que essas perguntas serão feitas na entrevista.

As perguntas por vaga são reaproveitáveis; as histórias e os arquivos de cada conta são privados. Esta entrega não inclui treino de entrevista em rodadas nem avaliação de respostas.

## IA, cota e reaproveitamento

A geração padrão é determinística, sem chamada de IA. A opção de IA usa apenas o DeepSeek para JSON curto, escolhendo ou organizando evidências completas. Contatos são removidos antes dessa chamada. Resultado não comprovado é recusado e não é guardado como geração válida.

A opção de IA compartilha a cota diária do Empresas. Não havendo evidências válidas para organizar, não faz chamada. Um resultado já guardado, para a mesma fonte, perfil, vaga e modo, é reaproveitado sem nova chamada. A geração determinística e o download de arquivos existentes continuam disponíveis quando a cota de IA acaba.

## Armazenamento e publicação

Os produtos ficam guardados de forma compactada na própria conta e entram na exportação de dados. A troca ou exclusão do currículo apaga as gerações anteriores; a exclusão da conta também as remove. Um resultado atrasado não restaura material apagado ou substituído.

Antes de disponibilizar o recurso ao público, precisam ser integradas as telas, a documentação geral do Empresas e os textos de privacidade sobre currículo armazenado e envio opcional ao DeepSeek. Cobrança real depende da integração do meio de pagamento. Nenhum desses estados significa publicação em produção.
