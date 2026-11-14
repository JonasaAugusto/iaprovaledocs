"""Contrato público do C9, validado somente em documentos locais."""

import unittest

from test_documentacao import ler, secao


class C9DocumentacaoTest(unittest.TestCase):
    def test_cache_publico_validade_e_limites(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C9: cache da PCI')
        for regra in ('Ainda não publicado', 'PCI Concursos', '5 minutos',
                      '500 entradas por processo', 'ferramenta e argumentos',
                      'ordem das chaves', 'próxima consulta', 'mais antigas',
                      'reiniciar', 'lista vazia válida', 'avisos', 'falhas',
                      'mais de uma chamada', 'não renova o prazo'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_isolamento_privacidade_e_cota(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C9: cache da PCI')
        for regra in ('SHA-256', 'não guarda os termos em claro na chave',
                      'não garante anonimato', 'identificação da conta',
                      'cópia independente', '`is_new`', 'filtros',
                      'não torna a busca gratuita', 'cotas',
                      'cache de equivalentes', 'cache de compatibilidade',
                      'confirme no edital'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_pool_preserva_trava_e_limita_promessa(self):
        texto = secao(ler('docs/compatibilidade.md'), '## C9: conexões durante a avaliação')
        for regra in ('Ainda não publicado', 'pool', 'conexões reutilizáveis',
                      '12 conexões persistentes', '12 extras por processo',
                      'transação de leitura', 'antes da chamada de IA',
                      'mantém uma conexão', 'trava', '409',
                      '12 avaliações simultâneas', 'provedor fictício',
                      'não é garantia de capacidade ilimitada',
                      'cota, cache por perfil e contabilização de custos'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_referencias_e_estado_sem_nova_versao(self):
        for pagina in ('README.md', 'docs/funcionalidades.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn('busca-por-perfil.md#c9-cache-da-pci', texto)
                self.assertIn('compatibilidade.md#c9-conexões-durante-a-avaliação', texto)
                self.assertRegex(texto, r'C9[^\n]*[Aa]inda não publicado')
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('C9', entrada)


if __name__ == '__main__':
    unittest.main()
