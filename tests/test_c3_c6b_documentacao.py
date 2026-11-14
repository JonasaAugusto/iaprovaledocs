"""Regressões dos filtros e da renovação de detalhes, sem serviços externos."""

import unittest

from test_documentacao import ler, secao


class CorrecoesDocumentacaoTest(unittest.TestCase):
    def test_c3_uf_textual_e_dia_de_brasilia(self):
        texto = secao(ler('docs/filtro-de-uf.md'), '## C3: inferência textual e prazo')
        for regra in ('Ainda não publicado em produção', 'título ou órgão',
                      'Salvador/ba', 'Salvador - BA', 'Salvador – BA',
                      'Salvador — ba', 'Salvador (BA)', 'siglas soltas',
                      'Palmas', 'Vitória', 'Belém', 'Campo Grande', 'Boa Vista',
                      'Rio Branco', 'São Luís', 'Salvador', 'Natal', 'Fortaleza',
                      'do, da ou de', 'Pará', 'preposição',
                      'anterior ao dia de Brasília', 'YYYY-MM-DD', 'DD/MM/AAAA',
                      'igual ao dia atual', 'ausente ou inválido', 'flag da fonte',
                      'Sul da Bahia', 'não promete suporte'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        for pagina in ('README.md', 'CHANGELOG.md'):
            self.assertIn('filtro-de-uf.md#c3-inferência-textual-e-prazo', ler(pagina))

    def test_c6b_terceiros_e_nivel_individual(self):
        texto = secao(ler('docs/busca-por-perfil.md'), '## C6b: terceiros e nível dos cargos')
        for regra in ('Ainda não publicado em produção', 'para o meu sobrinho',
                      'pra a minha neta', 'pro meu afilhado', 'vizinhos',
                      'ambos os gêneros', 'pedido de reformulação',
                      'menção narrativa não bloqueia', 'do/da', 'pedido de busca',
                      'antes do limite de oito', 'sem nível individual anotado',
                      'nível explícito incompatível', 'não deduz escolaridade',
                      '- Médio', '- Nível Superior em TI', 'Professor - Ensino Médio',
                      'etapa em que leciona', 'requisito desconhecido',
                      'lista compatível vazia', 'lista original de cargos', 'edital'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        for pagina in ('README.md', 'CHANGELOG.md'):
            self.assertIn('busca-por-perfil.md#c6b-terceiros-e-nível-dos-cargos', ler(pagina))

    def test_c11_intervalo_real_e_data_propria(self):
        texto = secao(ler('docs/empresas-vagas.md'), '## C11: coleta incremental SmartRecruiters')
        for regra in ('entre 4 e 7 dias', 'identificador da vaga',
                      'data própria do detalhe', 'não renova',
                      'índices antigos sem essa data', 'não garante atualização imediata'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('entre 4 e 7 dias', entrada)
        for pagina in ('docs/empresas-vagas.md', 'CHANGELOG.md'):
            self.assertNotRegex(ler(pagina), r'cerca de (?:sete|7) dias')


if __name__ == '__main__':
    unittest.main()
