"""Contrato público C14: compartilhamento, privacidade e pré-requisitos."""
import unittest

from test_documentacao import ler, secao


class C14DocumentacaoTest(unittest.TestCase):
    def test_resultados_e_limites(self):
        texto = secao(ler('docs/funcionalidades.md'),
                      '## C14: link de compartilhamento de busca')
        for regra in ('Ainda não publicado em produção', 'até 100 resultados',
                      'somente títulos e links públicos', 'não revela o texto da busca',
                      'perfil nem dados da conta', 'não refaz a busca',
                      'http e https', 'sem endereço válido', '30 consultas por minuto',
                      'endereço IPv4 ou rede IPv6 /64', 'por processo e em memória',
                      'reinicia com o processo', 'não é compartilhado entre processos',
                      '429', '60 segundos', 'interface de apresentação'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_controle_validade_e_privacidade(self):
        texto = secao(ler('docs/configuracoes-do-usuario.md'),
                      '## C14: gerenciar links de busca')
        for regra in ('Ainda não publicado em produção', 'só o dono da conta',
                      'sessão autenticada', 'gerar, trocar e revogar',
                      'um link por busca', 'no máximo 10 buscas por conta',
                      '7 dias', 'aplicada no servidor', 'antigo deixa de valer',
                      'credencial de leitura', 'pode repassá-lo',
                      'revogar não remove cópias já feitas', 'sair da sessão não revoga',
                      'inexistente, expirado, revogado ou de conta inativa',
                      'mesma resposta 404', 'Link indisponível.',
                      'hash SHA-256', 'token não é recuperável',
                      'exportação não inclui os registros de compartilhamento',
                      'exclusão da conta apaga os links', 'apagar ou podar a busca',
                      'telas de gerar, trocar e revogar ainda dependem da interface'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_migracao_e_protecao_do_caminho(self):
        texto = secao(ler('docs/pre-deploy.md'),
                      '## C14: compartilhamento e proteção do link')
        for regra in ('Ainda não publicado em produção', 'v3.29',
                      'só cria a tabela', 'idempotente', 'antes do código novo',
                      'depois da v3.28 do C13', 'demais migrações pendentes',
                      'token vai no caminho da URL',
                      'registros de acesso do servidor web e da aplicação',
                      'ocultar o token', 'inclusive nas respostas de erro',
                      'contas e dados descartáveis', 'interface',
                      'reversão apaga os links', 'preserva o histórico'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        self.assertNotRegex(texto, r'```|python -m|/srv/|systemctl|\.service\b')

    def test_indice_e_changelog_sem_nova_versao(self):
        for pagina in ('README.md', 'CHANGELOG.md'):
            texto = ler(pagina)
            self.assertRegex(texto, r'C14[^\n]*ainda não publicado em produção')
            for ancora in ('funcionalidades.md#c14-link-de-compartilhamento-de-busca',
                           'configuracoes-do-usuario.md#c14-gerenciar-links-de-busca',
                           'pre-deploy.md#c14-compartilhamento-e-proteção-do-link'):
                self.assertIn(ancora, texto)
        self.assertIn('C14', secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado'))


if __name__ == '__main__':
    unittest.main()
