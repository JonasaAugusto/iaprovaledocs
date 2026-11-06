# Preparo para uso comercial (proposta: site 3.6.0, backend 2.6.0)

Branches `comercial-site` (site e docs) e `comercial-backend`. Nada foi publicado.

## Metadados e prévia de link
- Descrição da home (meta description, `og:description`, `twitter:description` e JSON-LD): "Busque concursos abertos em linguagem natural e receba o link direto da inscrição no site oficial. Grátis, sem cartão." (118 caracteres, sem prometer aprovação). O `index.html` guarda a versão neutra (sem "grátis"); `scripts/build-gratis.py` acrescenta "Grátis, sem cartão." e falha se não achar os 4 trechos.
- Título: "IAprovale | Concursos abertos com o link da inscrição".
- Prévia no WhatsApp, X e Facebook: `og:type`, `og:site_name`, `og:locale`, `og:url`, `og:title`, `og:description`, `og:image` (com tipo, 1200x630 e texto alternativo) e `twitter:card=summary_large_image`. Imagem: `assets/og-iaprovale.png` (1200x630, menos de 100 KB), URL absoluta `https://augustusai.com.br/iaprovale/assets/og-iaprovale.png`. O Caddy já serve `/iaprovale/assets/*` de `/srv/iaprovale-web/assets` com cache de 1 dia, então a imagem sai pelo mesmo caminho dos outros assets. A fonte da imagem é `scripts/og/og.html` (renderizada com Playwright em 1200x630).
- Os apps de mensagem guardam a prévia em cache: depois de publicar, use o depurador de compartilhamento do Facebook para renovar.

## SEO e PWA
- `canonical`, `lang="pt-BR"`, `theme-color` (#0e1e2e, igual ao manifest) na home, Termos e Privacidade.
- `robots.txt` e `sitemap.xml` (home, Termos, Privacidade) em `web-app/homepage/`. Atenção: os rastreadores só leem `/robots.txt` na raiz do domínio, que é servida de `/srv/augustusai`. O arquivo do IAprovale vale como referência; para valer, acrescente as linhas dele (e `Sitemap: https://augustusai.com.br/iaprovale/sitemap.xml`) ao robots da raiz. App e Login ficam fora do índice.
- JSON-LD `WebApplication` simples, sem notas, avaliações nem preços.
- `404.html` amigável (usa caminhos absolutos `/iaprovale/...`). O Caddy não a usa sozinho; para ativar, no bloco `handle @iaprovale` do site, dentro do mesmo bloco: `handle_errors { @e404 expression {err.status_code} == 404 ... }` com `rewrite * /404.html` e `file_server`, mantendo o `root * /srv/iaprovale-web` (o `strip_prefix` é recriado no handle_errors; teste com `caddy validate`). Não aplicado.

## Aviso de fase de teste
Nota discreta, com filete dourado (mesmo padrão do checklist do app, sem vermelho nem azul): "Plataforma em fase de teste: confirme sempre no edital e no site oficial." Aparece na home, abaixo do botão de criar conta, e no app, abaixo do título da Busca. Classe `.nota-aviso` em `shared/css/base.css`.

## Aviso no currículo
No Perfil, na seção Currículo, antes do botão de anexar: "Não inclua dados sensíveis (saúde, religião, origem, opinião política, filiação). Envie só o que ajuda a encontrar concursos." O currículo só é enviado pelo Perfil (anexo PDF/TXT, depois Salvar), então o aviso fica no ponto único de envio. Testado a 390 e 1280, claro e escuro.

## Backend
- `python -m scripts.exportar_feedbacks [--saida arq.md] [--desde AAAA-MM-DD] [--com-usuario]`: markdown com resumo (total, nota média, distribuição de 1 a 5, período) e cada feedback (data, nota, comentário, usuário, buscas). Usuário pseudonimizado (`u-` + 8 caracteres de hash do id) a menos que `--com-usuario`; o arquivo sai com permissão 600. "Buscas" é o total da conta em `search_usage` até o dia do feedback; omitido quando não há uso registrado.
- `GET /admin/feedback.md?desde=&com_usuario=`: o mesmo conteúdo, só admin (mesma dependência de `/admin/feedback`).
- Resumo diário do Telegram ganhou a segunda linha: "Buscas hoje: N (custo estimado US$ X). No mês: M buscas, US$ Y." (soma de `search_usage.token_cost_usd`, dia e mês em São Paulo). Continua com uma execução por dia e `--dry-run`.
