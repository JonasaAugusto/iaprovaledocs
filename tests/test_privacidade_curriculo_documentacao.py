"""Contrato público do tratamento do currículo enviado pela busca à IA."""

import unittest

from test_documentacao import ler, secao


class PrivacidadeCurriculoDocumentacaoTest(unittest.TestCase):
    def test_busca_descreve_envio_ordem_repeticoes_e_limites(self):
        texto = secao(ler('docs/busca-por-perfil.md'),
                      '## Privacidade do currículo na busca')
        for regra in ('Ainda não publicado em produção', 'usar currículo',
                      'DeepSeek', 'e-mails, telefones, links e CPF',
                      'substituídos por marcadores', 'mesma função da Carreira',
                      'antes do corte de 6.000 caracteres',
                      'inclusive nas repetições da chamada',
                      'texto salvo no Perfil não muda',
                      'Nome e endereço continuam no texto',
                      'não anonimiza o currículo',
                      'formatos não reconhecidos podem permanecer',
                      'demais campos do perfil',
                      'Buscar com meu perfil', 'continua sem IA'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_funcionalidades_e_preferencia_informam_privacidade(self):
        paginas = (('docs/funcionalidades.md', '## Privacidade do currículo na busca'),
                   ('docs/configuracoes-do-usuario.md', '## Busca'))
        for pagina, titulo in paginas:
            with self.subTest(pagina=pagina):
                texto = secao(ler(pagina), titulo)
                for regra in ('Ainda não publicado em produção', 'DeepSeek',
                              'e-mails, telefones, links e CPF',
                              '6.000 caracteres', 'texto salvo no Perfil não muda',
                              'Nome e endereço continuam no texto',
                              'não anonimiza o currículo',
                              'busca-por-perfil.md#privacidade-do-currículo-na-busca'):
                    self.assertIn(regra, texto)

    def test_carreira_nao_e_apresentada_como_unica_remocao(self):
        texto = secao(ler('docs/empresas.md'), '## Privacidade e textos legais')
        self.assertIn('A busca de concursos com currículo', texto)
        self.assertIn('ainda não publicado em produção', texto)
        self.assertIn('busca-por-perfil.md#privacidade-do-currículo-na-busca', texto)
        self.assertIn('Nome e endereço continuam no texto', texto)

    def test_indice_e_changelog_preservam_estado_sem_nova_versao(self):
        for pagina in ('README.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = (secao(ler(pagina), '## [1.16.0] - Não publicado')
                         if pagina == 'CHANGELOG.md' else secao(ler(pagina), '## Índice'))
                for regra in ('Privacidade do currículo na busca',
                              'ainda não publicado em produção',
                              'busca-por-perfil.md#privacidade-do-currículo-na-busca',
                              'nome e endereço', 'não anonimiza'):
                    self.assertIn(regra, texto)


if __name__ == '__main__':
    unittest.main()
