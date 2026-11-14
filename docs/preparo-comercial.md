# Preparo para uso comercial (site 3.6.0, backend 2.6.0)

Estado: **Publicado**. As melhorias comerciais do site 3.6.0 e do backend 2.6.0 estão no ar. A ativação da página 404 não está confirmada; sua existência não garante a apresentação em todo endereço inexistente.

## Metadados e prévia de link
- Descrição da home (meta description, `og:description`, `twitter:description` e JSON-LD): "Busque concursos abertos em linguagem natural e receba o link direto da inscrição no site oficial. Grátis, sem cartão." (118 caracteres, sem prometer aprovação).
- Título: "IAprovale | Concursos abertos com o link da inscrição".
- Prévia no WhatsApp, X e Facebook: `og:type`, `og:site_name`, `og:locale`, `og:url`, `og:title`, `og:description`, `og:image` (com tipo, 1200x630 e texto alternativo) e `twitter:card=summary_large_image`. Imagem: `assets/og-iaprovale.png` (1200x630, menos de 100 KB), URL absoluta `https://augustusai.com.br/iaprovale/assets/og-iaprovale.png`.
- Os apps de mensagem guardam a prévia em cache: depois de publicar, use o depurador de compartilhamento do Facebook para renovar.

## SEO e PWA
- `canonical`, `lang="pt-BR"`, `theme-color` (#0e1e2e, igual ao manifest) na home, Termos e Privacidade.
- `robots.txt` e `sitemap.xml` referenciam home, Termos e Privacidade. Os rastreadores consultam as regras de indexação na raiz do domínio; a presença de um arquivo na pasta do produto não comprova sua aplicação. App e Login ficam fora do índice.
- JSON-LD `WebApplication` simples, sem notas, avaliações nem preços.
- Página 404 amigável prevista para orientar quem abre um endereço inexistente; ativação não confirmada.

## Aviso de fase de teste
Nota discreta, com filete dourado (mesmo padrão do checklist do app, sem vermelho nem azul): "Plataforma em fase de teste" (só isso, desde a v3.6.2; antes seguia "confirme sempre no edital e no site oficial") Aparece na home, abaixo do botão de criar conta, e no app, abaixo do título da Busca.

## Aviso no currículo
No Perfil, na seção Currículo, antes do botão de anexar: "Não inclua dados sensíveis (saúde, religião, origem, opinião política, filiação). Envie só o que ajuda a encontrar concursos." O currículo só é enviado pelo Perfil (anexo PDF/TXT, depois Salvar), então o aviso fica no ponto único de envio. Testado a 390 e 1280, claro e escuro.

## Acompanhamento comercial (só administradores)
- Exportação de feedbacks em Markdown com resumo (total, nota média, distribuição de 1 a 5 e período) e comentários. O usuário aparece pseudonimizado por padrão; a inclusão de sua identificação exige opção explícita. A contagem de buscas representa o total da conta até o dia do feedback e é omitida quando não há uso registrado. O arquivo exportado tem acesso restrito.
- `GET /admin/feedback.md?desde=&com_usuario=`: o mesmo conteúdo, só admin.
- Resumo diário do Telegram ganhou a segunda linha: "Buscas hoje: N (custo estimado US$ X). No mês: M buscas, US$ Y." (dia e mês em São Paulo), uma vez por dia.
