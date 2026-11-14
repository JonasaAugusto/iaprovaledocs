"""Contrato documentado da coleta incremental, sem rede ou dados reais."""

import unittest

from test_documentacao import ler, secao


class C11DocumentacaoTest(unittest.TestCase):
    def coleta(self):
        return secao(ler('docs/empresas-vagas.md'),
                     '## C11: coleta incremental SmartRecruiters')

    def test_primeira_coleta_e_reutilizacao_condicional(self):
        texto = self.coleta()
        for regra in ('Ainda não publicado', 'primeira coleta é lenta',
                      'listagem não traz texto nem link', 'detalhe de cada vaga',
                      'mesmo identificador e mesma data de revisão',
                      'texto e o link da coleta anterior', 'novas ou alteradas',
                      'cerca de 7 dias', 'escalonada', 'edições de texto'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_orcamento_parcial_preserva_indice_e_restricoes(self):
        texto = self.coleta()
        for regra in ('120 segundos por board', 'coleta fica parcial',
                      'já conhecidas e ainda não revisitadas permanecem no índice',
                      'marcadas como desatualizadas', 'código de saída 2',
                      'falha temporária tolerada pelo timer', 'robots.txt',
                      '1 segundo por host', '72 horas',
                      'não garante cobertura completa'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_referencias_e_publicacao_separadas_do_e5(self):
        ancora = 'empresas-vagas.md#c11-coleta-incremental-smartrecruiters'
        for pagina in ('README.md', 'docs/navegacao.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn(ancora, texto)
                self.assertRegex(texto, r'C11[^\n]*[Aa]inda não publicado')
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('C11', entrada)
        for pagina in ('docs/empresas-vagas.md', 'docs/navegacao.md'):
            abertura = ler(pagina).split('\n## ', 1)[0]
            self.assertIn('No ar', abertura)
            self.assertIn('12/11/2026', abertura)


if __name__ == '__main__':
    unittest.main()
