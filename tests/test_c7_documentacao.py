"""Regressões do contrato público do ranking C7, sem serviços externos."""

import re
import unittest

from test_documentacao import ler, secao


class C7DocumentacaoTest(unittest.TestCase):
    def test_ordem_e_pontuacao(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C7: ranking por relevância')
        for regra in ('Ainda não publicado', 'ordem escolhida', 'nacionais depois',
                      'UF do perfil, mesma região e demais locais', 'local explícito',
                      '200', '100', 'palavras inteiras', 'acentos', 'pontuação',
                      'max(1, 30 - dias)', '1.000', '2.000', 'DD/MM/AAAA',
                      'ausente ou inválida', 'ordem recebida', 'sem IA',
                      'formação futura', 'PDF', 'preferência por novos'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_campos_da_resposta(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C7: ranking por relevância')
        campos = re.findall(r'^\| `([^`]+)` \| ([^|]+) \|', texto, re.MULTILINE)
        self.assertEqual({nome: tipo.strip() for nome, tipo in campos}, {
            'pontuacao': 'Inteiro', 'motivo': 'Texto', 'compatibilidade_cargos': 'Lista'})
        for regra in ('POST /search', '`results`', 'não é probabilidade',
                      'entre buscas', '`nome`, `nivel`, `motivo` e `falta`',
                      '`cargos_compativeis`', 'apresentação visual'):
            self.assertIn(regra, texto)

    def test_selo_conservador_separado_da_consulta_detalhada(self):
        texto = secao(ler('docs/compatibilidade.md'), '## C7: selo na resposta da busca')
        for regra in ('Ainda não publicado', '`combina`', '`parcial`', '`nao_combina`',
                      'sem requisitos individuais', 'selos atuais permanecem `parcial`',
                      'nível global', 'formação concluída',
                      'sem chamadas adicionais', 'sem cobrança adicional',
                      'não garante elegibilidade', 'confirme no edital',
                      'Alertas > Acompanhando', 'cota e cache próprios',
                      'não comprova habilitação', 'busca-por-perfil.md#c7-ranking-por-relevância'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_referencias_e_changelog_sem_anuncio_de_publicacao(self):
        for pagina in ('README.md', 'docs/funcionalidades.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn('busca-por-perfil.md#c7-ranking-por-relevância', texto)
                self.assertRegex(texto, r'C7[^\n]*[Aa]inda não publicado')
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('compatibilidade.md#c7-selo-na-resposta-da-busca', entrada)


if __name__ == '__main__':
    unittest.main()
