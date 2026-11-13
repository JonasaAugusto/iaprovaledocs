"""Contrato público do C5 e limites da migração, sem serviços externos."""

import unittest

from test_documentacao import ler, secao


class C5DocumentacaoTest(unittest.TestCase):
    def test_sessao_hash_e_efeito_para_a_pessoa(self):
        texto = secao(ler("docs/configuracoes-do-usuario.md"), "## C5: proteção das sessões")
        for regra in ("Ainda não publicado", "SHA-256", "resumo irreversível",
                      "token", "apenas o hash", "não é aceito", "Bearer",
                      "entrar novamente uma vez", "Contas, senhas e perfis",
                      "30 dias sem uso", "Sair de todos os aparelhos",
                      "pre-deploy.md#c5-migração-e-reversão"):
            self.assertIn(regra, texto)

    def test_migracao_reversao_e_publicacao_controlada(self):
        texto = secao(ler("docs/pre-deploy.md"), "## C5: migração e reversão")
        for regra in ("Ainda não publicado", "migrate_v3_25_session_hash.py",
                      "backup consistente", "restauração validada",
                      "janela de indisponibilidade", "interromper os processos",
                      "não podem operar simultaneamente", "transação",
                      "login", "logout", "expiração", "token anterior",
                      "hash armazenado", "downgrade", "versão anterior",
                      "novo login", "não recupera os tokens apagados",
                      "Não restaurar sessões antigas", "não encerra sessões novas",
                      "revisão cruzada", "a operação", "encerra as sessões existentes",
                      "não executa nem atesta"):
            self.assertIn(regra, texto)

    def test_referencias_e_estado_preservado(self):
        for pagina in ("README.md", "CHANGELOG.md", "docs/funcionalidades.md"):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn("configuracoes-do-usuario.md#c5-proteção-das-sessões", texto)
                self.assertIn("ainda não publicado", texto.lower())
                self.assertIn("C5", texto)
        changelog = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for regra in ("SHA-256", "reversão", "novo login", "pre-deploy.md#c5-migração-e-reversão"):
            self.assertIn(regra, changelog)
        self.assertIn("O login expira depois de 30 dias sem uso", ler("docs/configuracoes-do-usuario.md"))


if __name__ == "__main__":
    unittest.main()
