"""Contrato público de acesso administrativo, erros e retenção de dados."""

import re
import unittest

from test_documentacao import ler, secao


class SegurancaRetencaoDocumentacaoTest(unittest.TestCase):
    def test_admin_oculto_inclui_metodo_errado_sem_mudar_admin_valido(self):
        texto = secao(ler('docs/referencia-api.md'), '## Acesso administrativo')
        for regra in ('Ainda não publicado em produção', '/admin/', '/auth/users',
                      'sem credencial', 'inválida', 'expirada', 'revogada',
                      'usuário comum', 'método incorreto', '404',
                      '{"detail":"Not Found"}', 'sem cabeçalho `Allow`',
                      'administrador autenticado', '405', 'senha provisória', '403',
                      'senha_provisoria',
                      'contrato de sucesso permanece'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        linhas = re.findall(r'^\| ([^|]+) \| ([^|]+) \|$', texto, re.MULTILINE)
        respostas = {situacao.strip(): resposta.strip() for situacao, resposta in linhas}
        for situacao, resposta in (
            ('Sem credencial, credencial inválida ou sessão de usuário comum, inclusive com método incorreto',
             '404, sem cabeçalho `Allow`'),
            ('Administrador com sessão válida e senha definitiva, método incorreto',
             '405, com cabeçalho `Allow`'),
            ('Administrador com senha provisória, método aceito',
             '403, com `detail`: `senha_provisoria`'),
            ('Administrador com senha provisória, método incorreto',
             '404, sem cabeçalho `Allow`'),
        ):
            with self.subTest(situacao=situacao):
                self.assertEqual(respostas.get(situacao), resposta)

    def test_erros_delimitam_rotas_mensagens_e_logs_sem_promessa_global(self):
        texto = secao(ler('docs/referencia-api.md'), '## Erros de serviços externos')
        for regra in ('Ainda não publicado em produção', 'POST /search', 'POST /v1/search',
                      'POST /v1/partner/wallet/topup', '502',
                      'A fonte de concursos está indisponível no momento, tente novamente em instantes.',
                      'Não foi possível iniciar a recarga agora. Tente novamente mais tarde.',
                      'corpo bruto', 'contratos de sucesso', 'privacidade-e-seguranca.md'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        logs = secao(ler('docs/privacidade-e-seguranca.md'), '## Respostas e registros de diagnóstico')
        for regra in ('Ainda não publicado em produção', 'webhook de pagamento',
                      'cliente da busca', 'tipo do erro', 'código HTTP',
                      'sem o corpo de terceiros', 'todos os logs', 'infraestrutura'):
            self.assertIn(regra, logs)

    def test_retencao_tabela_tem_prazos_e_limita_garantia_de_remocao(self):
        texto = secao(ler('docs/privacidade-e-seguranca.md'), '## Retenção e exclusão')
        linhas = re.findall(r'^\| ([^|]+) \| ([^|]+) \|$', texto, re.MULTILINE)
        prazos = {nome.strip(): prazo.strip() for nome, prazo in linhas}
        self.assertEqual(prazos['Hash de IP dos pedidos, inclusive aprovados'],
                         '7 dias desde a criação; remove só o hash, preservando o pedido aprovado')
        for nome, prazo in (
            ('Falhas de login', '1 dia'),
            ('Eventos do cadastro', '2 dias'),
            ('Sessões do cadastro', 'Vencidas há mais de 1 dia ou criadas há 30 dias'),
            ('Registros de envio de e-mail do cadastro', '24 horas'),
            ('IP, data e versão do aceite dos termos', 'Enquanto a conta existir; os três são apagados com a conta'),
        ):
            with self.subTest(nome=nome):
                self.assertEqual(prazos[nome], prazo)
        for regra in ('Ainda não publicado em produção', 'diária', '03:30',
                      '**03:30, horário de Brasília**', '7 dias',
                      'execuções seguintes', '90 dias'):
            self.assertIn(regra, texto)

    def test_textos_publicos_sem_ressalvas_editoriais_da_revisao(self):
        paginas = ('README.md', 'CHANGELOG.md', 'docs/privacidade-e-seguranca.md',
                   'docs/solicitacoes-de-acesso.md', 'docs/versao-gratis.md')
        for pagina in paginas:
            texto = ler(pagina)
            with self.subTest(pagina=pagina):
                for trecho in ('código consultado', 'previstos para conferência',
                               'referência de 7 dias', 'referência inicial mencionava 7 dias',
                               'conferência do agendamento', 'Conferir o agendamento',
                               'não está comprovado pelo código versionado consultado'):
                    self.assertNotIn(trecho, texto)
        retencao = secao(ler('docs/privacidade-e-seguranca.md'), '## Retenção e exclusão')
        self.assertIn('7 dias', retencao)

    def test_armazenamento_distingue_sessao_preferencias_e_rastreio(self):
        texto = secao(ler('docs/privacidade-e-seguranca.md'), '## Armazenamento no navegador')
        for regra in ('sessionStorage', 'token', 'usuário', 'última atividade',
                      'localStorage', 'tema', 'tamanho', 'menu', 'usar currículo',
                      'não define cookies', 'sem rastreio', 'não significa ausência',
                      'configuracoes-do-usuario.md'):
            self.assertIn(regra, texto)

    def test_paginas_existentes_e_indice_remetem_ao_contrato(self):
        for pagina in ('docs/versao-gratis.md', 'docs/configuracoes-do-usuario.md',
                       'docs/solicitacoes-de-acesso.md'):
            with self.subTest(pagina=pagina):
                self.assertIn('privacidade-e-seguranca.md', ler(pagina))
        for pagina in ('README.md', 'CHANGELOG.md'):
            texto = ler(pagina)
            if pagina == 'CHANGELOG.md':
                texto = secao(texto, '## [1.16.0] - Não publicado')
            for regra in ('T4', 'T3', 'T6', 'ainda não publicado em produção',
                          'docs/privacidade-e-seguranca.md', 'docs/referencia-api.md'):
                with self.subTest(pagina=pagina, regra=regra):
                    self.assertIn(regra, texto)


class FiscalEPrazoIPDocumentacaoTest(unittest.TestCase):
    def test_hash_ip_sete_dias_em_todas_as_mencoes(self):
        paginas = ('README.md', 'CHANGELOG.md', 'docs/privacidade-e-seguranca.md',
                   'docs/solicitacoes-de-acesso.md', 'docs/versao-gratis.md',
                   'docs/pre-deploy.md')
        total = 0
        for pagina in paginas:
            for linha in ler(pagina).splitlines():
                if re.search(r'hash de IP', linha, re.IGNORECASE):
                    total += 1
                    with self.subTest(pagina=pagina, linha=linha):
                        self.assertIn('7 dias', linha)
                        self.assertNotIn('30 dias', linha)
        self.assertGreaterEqual(total, 4)

    def test_fiscal_retencao_e_excecoes_da_exclusao(self):
        texto = secao(ler('docs/privacidade-e-seguranca.md'), '## T5: registros fiscais')
        for regra in ('Ainda não publicado em produção', 'recurso desligado',
                      'quando houver cobrança', 'separado da conta', 'número', 'valor',
                      'data', 'nome e documento do pagador', 'referência',
                      '5 anos após a emissão', 'obrigação legal', 'depois apagado',
                      'mesmo após a exclusão da conta', 'apaga os demais dados',
                      'apenas identificador, datas e estado, sem dados pessoais',
                      'até 90 dias', 'exportação', 'backups', 'validação jurídica'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_exportacao_fiscal_isolada_e_desligada_sem_bloco(self):
        texto = secao(ler('docs/referencia-api.md'), '## T5: exportação de registros fiscais')
        for regra in ('Ainda não publicado em produção', 'recurso desligado',
                      'GET /me/exportar', 'autenticada', '`registros_fiscais`',
                      '`aviso`', '`notas`', 'somente os registros da própria conta',
                      'não inclui o bloco', 'lista vazia', '`numero_nota`',
                      '`valor_centavos`', '`emitida_em`', '`documento_pagador`',
                      '`nome_pagador`', '`pedido_ref`', '`reter_ate`',
                      'sem identificadores internos', 'privacidade-e-seguranca.md#t5-registros-fiscais'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_preparacao_fiscal_e_indice_sem_anunciar_publicacao(self):
        texto = secao(ler('docs/pre-deploy.md'), '## T5: registros fiscais')
        for regra in ('Ainda não publicado em produção', 'recurso desligado',
                      'v3.30', 'scripts/migrate_v3_30_registros_fiscais.py',
                      'antes do código novo', 'antes de ligar o recurso',
                      'idempotente', 'código anterior', 'descartáveis',
                      '5 anos', '7 dias', 'quando houver cobrança'):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        for pagina in ('README.md', 'CHANGELOG.md'):
            texto = ler(pagina)
            if pagina == 'CHANGELOG.md':
                texto = secao(texto, '## [1.16.0] - Não publicado')
            linhas = [linha for linha in texto.splitlines() if 'T5' in linha]
            self.assertTrue(linhas, pagina)
            for regra in ('ainda não publicado em produção', 'recurso desligado',
                          '5 anos', 'docs/privacidade-e-seguranca.md#t5-registros-fiscais',
                          'docs/referencia-api.md#t5-exportação-de-registros-fiscais',
                          'docs/pre-deploy.md#t5-registros-fiscais'):
                with self.subTest(pagina=pagina, regra=regra):
                    self.assertIn(regra, '\n'.join(linhas))
