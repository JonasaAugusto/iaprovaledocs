"""Contrato público C12: calendário, alertas e requisitos antes da liberação."""
import json
import re
import unittest

from test_documentacao import ler, secao


class C12DocumentacaoTest(unittest.TestCase):
    def calendario(self):
        return secao(ler('docs/funcionalidades.md'), '## C12: calendário dos acompanhados')

    def test_calendario_datas_e_sincronizacao(self):
        texto = self.calendario()
        for regra in ('Ainda não publicado em produção', 'Google Agenda', 'Apple',
                      'Outlook', 'dia inteiro', 'inscrições', 'isenção', 'prova',
                      'datas ausentes não geram eventos', 'datas passadas',
                      'sem consulta externa', 'sem IA', 'sem consumir cota',
                      'títulos são tratados', 'não exporta nome nem e-mail',
                      'importação é uma fotografia', 'frequência de sincronização',
                      'botão de calendário ainda depende da interface'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_credencial_pessoal_e_revogacao(self):
        texto = secao(ler('docs/configuracoes-do-usuario.md'),
                      '## C12: link pessoal do calendário')
        for regra in ('Ainda não publicado em produção', 'credencial de leitura',
                      'quem tem o link', 'hash SHA-256', 'antigo deixa de valer imediatamente',
                      'revogar', 'não expira automaticamente', 'sair da sessão não revoga',
                      'não dá acesso às outras funções', 'conta inativa', 'senha provisória',
                      'controles nas Configurações ainda dependem da interface'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_limite_publico_e_limitacao_por_processo(self):
        texto = self.calendario()
        for regra in ('30 consultas', '60 segundos', 'endereço IPv4', 'rede IPv6 /64',
                      'HTTP 429', 'por processo e em memória',
                      'não é compartilhado entre instâncias', 'reinicia com o processo'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_contrato_alerta_e_exemplo_valido(self):
        texto = secao(ler('docs/funcionalidades.md'), '## C12: contrato de alerta por busca')
        exemplo = json.loads(re.search(r'```json\n(.*?)\n```', texto, re.S).group(1))
        self.assertEqual(exemplo, {'nome': 'Professor em SP', 'termo': 'professor',
                                   'ufs': ['SP'], 'usar_perfil': False})
        for regra in ('POST /me/alertas', 'sessão autenticada', '201', '1 a 60',
                      'até 200', 'até 27', 'remove duplicatas', 'inferência pelo termo',
                      'usar_perfil', 'falso', 'ativo', 'verdadeiro', '409',
                      'não deduplica', 'GET /me/alertas', 'PATCH /me/alertas/{id}',
                      'DELETE /me/alertas/{id}', '404', 'ultimo_envio_em',
                      'atalho visual para usar a busca atual ainda depende da interface'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_pre_deploy_sem_detalhes_operacionais(self):
        texto = secao(ler('docs/pre-deploy.md'), '## C12: calendário e proteção do link')
        for regra in ('Ainda não publicado em produção', 'v3.27', 'só cria a tabela',
                      'idempotente', 'antes do código novo', 'v3.25', 'hash de sessão',
                      'v3.26', 'servidor web', 'aplicação', 'ocultar o parâmetro',
                      'token', 'URL completa', 'reversão apaga as credenciais'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        self.assertNotRegex(texto, r'(?i)```|python -m|/srv/|Caddy|uvicorn|systemctl|\.service\b')

    def test_indice_changelog_e_estados_preservados(self):
        for pagina in ('README.md', 'CHANGELOG.md'):
            texto = ler(pagina)
            self.assertRegex(texto, r'C12[^\n]*ainda não publicado em produção')
            for ancora in ('funcionalidades.md#c12-calendário-dos-acompanhados',
                           'funcionalidades.md#c12-contrato-de-alerta-por-busca',
                           'pre-deploy.md#c12-calendário-e-proteção-do-link'):
                self.assertIn(ancora, texto)
        entrada = secao(ler('CHANGELOG.md'), '## [1.16.0] - Não publicado')
        self.assertIn('C12', entrada)
        abertura = ler('docs/configuracoes-do-usuario.md').split('\n## ', 1)[0]
        self.assertIn('No ar', abertura)
        self.assertIn('12/11/2026', abertura)


if __name__ == '__main__':
    unittest.main()
