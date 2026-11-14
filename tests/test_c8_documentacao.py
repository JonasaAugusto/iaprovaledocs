"""Regressões do contrato público do início agregado, só com arquivos locais."""

import re
import unittest

from test_documentacao import ler, secao


class C8DocumentacaoTest(unittest.TestCase):
    def test_campos_e_origens(self):
        texto = secao(ler('docs/navegacao.md'), '## C8: início agregado')
        campos = re.findall(r'^\| `([^`]+)` \| `([^`]+)` \|', texto, re.MULTILINE)
        self.assertEqual(dict(campos), {
            'cota': 'GET /empresas/cota',
            'acompanhados': 'GET /me/acompanhando',
            'perfil': 'GET /profile',
            'nao_lidas': 'GET /me/novidades',
        })
        for regra in ('GET /me/inicio', 'quatro campos obrigatórios',
                      'cota diária do Empresas', 'não é a cota de buscas',
                      '`dia`, `chamadas`, `limite_chamadas`, `custo_usd`, `limite_usd`, `chamadas_restantes` e `esgotada`',
                      'próxima data futura, criação e identificador',
                      'lista vazia', 'campos nulos', '`updated_at`',
                      'instante da leitura', 'inteiro não negativo',
                      'sem limite de página', 'sem textos nem lista de novidades'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_acesso_efeitos_falhas_e_compatibilidade(self):
        texto = secao(ler('docs/navegacao.md'), '## C8: início agregado')
        for regra in ('Ainda não publicado', 'conta autenticada', 'Bearer',
                      'senha definitiva', '401', 'expirada', 'revogada',
                      'inativa', '403', 'senha_provisoria',
                      'consumo zero', 'HTTP 200', '`esgotada: true`',
                      'não consome nem reserva chamadas de IA',
                      'não cria perfil', 'não marca novidades como lidas',
                      'não consulta provedores externos', 'renovação usual da sessão',
                      'Não há resposta parcial', 'falha a requisição inteira',
                      'não garante que todos os campos retratem o mesmo instante',
                      'contratos intactos por uma versão', 'alternativa de recuperação',
                      'adaptação do front', 'sem migração de banco'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_referencias_e_estado(self):
        for pagina in ('README.md', 'docs/funcionalidades.md', 'CHANGELOG.md'):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn('navegacao.md#c8-início-agregado', texto)
                self.assertRegex(texto, r'C8[^\n]*[Aa]inda não publicado')
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('GET /me/inicio', entrada)


if __name__ == '__main__':
    unittest.main()
