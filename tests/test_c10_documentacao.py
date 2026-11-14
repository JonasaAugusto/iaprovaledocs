"""Contrato previsto do C10, sem chamadas de rede ou dados de usuários."""

import re
import unittest

from test_documentacao import ler, secao


class C10DocumentacaoTest(unittest.TestCase):
    def test_verificacao_de_links_preserva_destino_e_identidade(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C10: verificação de links e cidade')
        for regra in ('Ainda não publicado', 'contrato previsto', 'SSRF',
                      'IP público validado', 'cada IP em ordem',
                      'IPv4 mapeado em IPv6', 'Endereços privados',
                      'cliente dedicado', 'variáveis de ambiente de proxy',
                      'Host', 'SNI', 'certificado', 'cada redirecionamento',
                      'não comprova', 'confirme no edital'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_cidade_original_fallback_condicional_e_cache(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C10: verificação de links e cidade')
        for regra in ('grafia original', 'somente se a resposta vier vazia',
                      'forma normalizada', 'no máximo duas chamadas',
                      'não faz a segunda consulta', 'Salvador - BA',
                      'Salvador/BA', 'Salvador', 'Ilhéus', 'Ilheus',
                      'nos dois sentidos', 'cache da PCI',
                      '#c9-cache-da-pci', 'UF', 'não garante resultados'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_indice_resumo_changelog_e_estado(self):
        for pagina in ('README.md', 'docs/funcionalidades.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn('busca-por-perfil.md#c10-verificação-de-links-e-cidade', texto)
                self.assertIn('pre-deploy.md#c10-links-e-consulta-por-cidade', texto)
                self.assertRegex(texto, r'C10[^\n]*[Aa]inda não publicado')
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('C10', entrada)

    def test_validacao_antes_da_publicacao(self):
        texto = secao(ler('docs/pre-deploy.md'), '## C10: links e consulta por cidade')
        for regra in ('Ainda não publicado', 'recursos descartáveis',
                      'rede simulada', 'sem dados reais', 'conferência do código e da documentação',
                      'IP público validado', 'IPv4 mapeado em IPv6',
                      'Host/SNI', 'certificado', 'proxy', 'redirecionamento',
                      'no máximo duas chamadas', 'sem segunda consulta',
                      'Ilhéus', 'Ilheus', 'cache da PCI',
                      'não exige migração de banco', 'operação autorizada',
                      'não atesta'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_c10_nao_reintroduz_escopo_descartado(self):
        contrato = secao(ler('docs/pre-deploy.md'), '## C10: links e consulta por cidade')
        self.assertIn('não exige migração de banco', contrato)
        paginas = ('README.md', 'CHANGELOG.md', 'docs/funcionalidades.md',
                   'docs/busca-por-perfil.md', 'docs/pre-deploy.md')
        for pagina in paginas:
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                # Outros lotes podem ter migração e regras próprias de duplicação.
                if pagina == 'docs/pre-deploy.md':
                    texto = contrato
                elif pagina == 'docs/busca-por-perfil.md':
                    texto = secao(texto, '## C10: verificação de links e cidade')
                else:
                    texto = '\n'.join(linha for linha in texto.splitlines()
                                      if re.search(r'\bC10\b', linha))
                self.assertIsNone(re.search(
                    r'dedup|[óo]rg[ãa]o\s*\+\s*edital|v?3[._]27', texto, re.I))


if __name__ == '__main__':
    unittest.main()
