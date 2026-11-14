"""Contrato público C13, verificado apenas em documentos locais."""
import json
import re
import unittest

from test_documentacao import ler, secao


class C13DocumentacaoTest(unittest.TestCase):
    def versoes(self):
        return secao(ler('docs/configuracoes-do-usuario.md'), '## C13: versões do perfil')

    def test_curriculo_sem_texto_nas_versoes(self):
        texto = self.versoes()
        for regra in ('não guardam o texto do currículo', 'hash SHA-256',
                      'tamanho em bytes UTF-8', 'até 20 versões', 'sem prazo em dias',
                      'não é um backup', 'sem texto nem hash no diff'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        exemplo = json.loads(re.search(r'```json\n(.*?)\n```', texto, re.S).group(1))
        self.assertEqual(exemplo, {'de': 1, 'para': 2, 'alteracoes': [
            {'campo': 'graduacao', 'antes': 'Direito', 'depois': None},
            {'campo': 'curriculo', 'antes': 'currículo alterado', 'depois': 'currículo alterado'}]})

    def test_limpeza_exportacao_e_isolamento(self):
        texto = self.versoes()
        for regra in ('PUT /profile', 'curriculo: null', 'DELETE /me/curriculo',
                      'todas as versões da conta', 'texto legado, hash e tamanho',
                      'mesmo se o currículo atual já estiver vazio',
                      'demais campos são preservados', 'GET /me/exportar',
                      '`checklist` e `versoes_perfil`', 'exclusão da conta',
                      'resíduos físicos', 'backups', 'validação jurídica',
                      'somente da própria conta', '422', '2147483647', '404'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_gravacao_e_consulta(self):
        texto = self.versoes()
        for regra in ('GET /profile/versoes', 'GET /profile/versoes/diff?de=1&para=2',
                      '`numero` e `criado_em`', 'mais recente', 'conteúdo idêntico',
                      'estado anterior', 'não reconstrói', 'vazia',
                      '`campo`, `antes` e `depois`', 'null e texto vazio',
                      'mesma versão', 'inverter a ordem', 'independente do hash'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_checklist(self):
        texto = secao(ler('docs/funcionalidades.md'), '## C13: checklist de inscrição')
        for regra in ('Ainda não publicado em produção', 'senha definitiva',
                      '/me/acompanhando/{concurso_id}/checklist', 'GET', 'POST',
                      'PATCH', 'DELETE', '201', '204', '30 itens', '409', '404',
                      '1 a 2147483647', '422', 'UUID', '1 a 200',
                      'booleano estrito', 'não aceita null', 'independentes',
                      'começa vazio', 'não são criados automaticamente'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_migracao_e_reversao(self):
        texto = secao(ler('docs/pre-deploy.md'), '## C13: checklist e versões do perfil')
        for regra in ('Ainda não publicado em produção', 'v3.28', 'antes do código novo',
                      'PUT /profile', 'exportação', 'exclusão de conta',
                      'DELETE /me/curriculo', 'idempotente', 'código anterior',
                      'não geram versões', 'base defasada', 'apaga checklist e versões',
                      '--confirmar', 'perfil e acompanhados', 'resíduos físicos',
                      'backups', 'validação jurídica'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        self.assertNotRegex(texto, r'```|python -m|/srv/|systemctl')

    def test_indice_changelog_e_links(self):
        for pagina in ('README.md', 'CHANGELOG.md'):
            texto = ler(pagina)
            self.assertRegex(texto, r'C13[^\n]*ainda não publicado em produção')
            for ancora in ('funcionalidades.md#c13-checklist-de-inscrição',
                           'configuracoes-do-usuario.md#c13-versões-do-perfil',
                           'pre-deploy.md#c13-checklist-e-versões-do-perfil'):
                self.assertIn(ancora, texto)
        self.assertIn('C13', secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado'))


if __name__ == '__main__':
    unittest.main()
