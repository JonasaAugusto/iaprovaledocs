"""Consistência pública dos estados, dependências e conteúdo comercial."""
import re
import unittest

from test_documentacao import RAIZ, ler, secao


class AuditoriaDocumentacaoTest(unittest.TestCase):
    def test_uf_disponivel_sem_pendencia_antiga(self):
        texto = ler('docs/filtro-de-uf.md')
        self.assertIn('disponíveis desde o backend 2.12.0', texto)
        self.assertNotRegex(texto, r'(?i)aguardando publicação|até a publicação|pronto, não publicado')
        linha = next(l for l in ler('README.md').splitlines() if '[Filtro de UF]' in l)
        self.assertIn('disponíveis', linha)
        self.assertNotIn('aguardando', linha)

    def test_comercial_publicado_sem_infraestrutura(self):
        texto = ler('docs/preparo-comercial.md')
        self.assertIn('Estado: **Publicado**', texto)
        self.assertIn('site 3.6.0, backend 2.6.0', texto)
        self.assertNotRegex(texto, r'(?i)branches?|/srv/|Caddy|handle_errors|strip_prefix|file_server|scripts/|web-app/|Nada foi publicado')
        for conteudo in ('Grátis, sem cartão', '1200x630', 'robots.txt', '404',
                         'fase de teste', 'dados sensíveis', 'pseudonimiz', 'só admin'):
            self.assertIn(conteudo, texto)
        self.assertIn('ativação da página 404 não está confirmada', texto)

    def test_paginas_sem_linguagem_de_execucao_interna(self):
        for caminho in [RAIZ / 'README.md', RAIZ / 'CHANGELOG.md', *sorted((RAIZ / 'docs').glob('*.md'))]:
            with self.subTest(pagina=caminho.name):
                self.assertNotRegex(caminho.read_text(encoding='utf-8'),
                                    r'(?i)\b(?:Claude|Codex|agentes?)\b|\[Publicar\]|\b(?:esta|nesta) tarefa\b|revisão cruzada|fluxo interno de desenvolvimento')

    def test_migracoes_empresas_na_tabela_e_na_ordem(self):
        texto = ler('docs/pre-deploy.md')
        tabela = secao(texto, '## Migrações necessárias')
        arquivos = re.findall(r'^\| `([^`]+\.py)` \|', tabela, re.MULTILINE)
        self.assertEqual(arquivos[-2:], ['scripts/migrate_v3_23_empresas.py',
                                       'scripts/migrate_v3_24_empresas_produtos.py'])
        empresas = secao(texto, '## Empresas em produção')
        for termo in ('v3_24', 'E3/E4', 'após a v3_23', 'idempotente'):
            self.assertIn(termo, empresas)
        ordem = secao(texto, '## Ordem da publicação')
        self.assertRegex(ordem, r'2\.[^\n]*v3_23[^\n]*v3_24[^\n]*antes do reinício')

    def test_custo_publicado_sem_confundir_lotes_pendentes(self):
        custo = secao(ler('docs/stats-do-administrador.md'), '## Estimativa de custo')
        self.assertIn('**No ar** desde **12/11/2026**', custo)
        self.assertNotIn('Ainda não publicado', custo)
        for pagina in ('README.md', 'docs/roadmap.md', 'docs/funcionalidades.md'):
            linha = next(l for l in ler(pagina).splitlines() if 'estimativa de custo de ia' in l.lower())
            self.assertIn('12/11/2026', linha)
            self.assertNotIn('ainda não publicado', linha)
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('estimativa de custo', entrada)
        for lote in ('C1', 'C2', 'C4', 'C5', 'C6a', 'C7', 'C8', 'C9', 'C10', 'C11'):
            self.assertRegex(entrada, rf'{lote}\b[^\n]*ainda não publicad')
