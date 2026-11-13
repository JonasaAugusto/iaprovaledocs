"""Contrato documentado do front 3.13.0, somente arquivos locais."""

import unittest

from test_documentacao import ler, secao


class Front313DocumentacaoTest(unittest.TestCase):
    def test_busca_no_navegador_e_compatibilidade_de_links(self):
        for pagina in ("docs/navegacao.md", "docs/funcionalidades.md"):
            texto = secao(ler(pagina), "## Busca fora da URL")
            for regra in ("Publicado em 13/11/2026", "3.13.0", "history.state", "voltar",
                          "avançar", "recarregar", "?q=", "uma vez", "URL é limpa",
                          "não compartilha", "UFs", "currículo"):
                with self.subTest(pagina=pagina, regra=regra):
                    self.assertIn(regra, texto)
        self.assertNotIn("| Estado da busca na URL", ler("docs/funcionalidades.md"))
        filtro = ler("docs/filtro-de-uf.md")
        self.assertIn("history.state", filtro)
        self.assertIn("Publicado em 13/11/2026", filtro)
        self.assertIn("3.13.0", ler("docs/rebranding-rodada-1.md"))

    def test_prechecagem_e_erro_do_servidor(self):
        for pagina, titulo in (("docs/navegacao.md", "## Envio de currículo: aviso de tamanho"),
                               ("docs/empresas.md", "### Front 3.13.0: aviso de tamanho")):
            texto = secao(ler(pagina), titulo)
            for regra in ("Publicado em 13/11/2026", "5 MB", "antes de enviar", "7,3 MB",
                          "413", "sem o tamanho", "Carreira", "Perfil"):
                with self.subTest(pagina=pagina, regra=regra):
                    self.assertIn(regra, texto)

    def test_historico_e_login_sem_prometer_sessao_unica(self):
        historico = secao(ler("docs/configuracoes-do-usuario.md"), "### C4: histórico enxuto")
        for regra in ("`linkOficial`", "alias de `link`", "título e link",
                      "sem local e prazo", "não são reescritos", "após sua liberação"):
            self.assertIn(regra, historico)
        login = secao(ler("docs/navegacao.md"), "## Login")
        for regra in ("sessão", "navegador", "vários aparelhos", "não impõe"):
            self.assertIn(regra, login)

    def test_estado_da_publicacao_e_validacoes(self):
        for pagina, titulo in (("CHANGELOG.md", "## [1.16.0] - Não publicado"),
                               ("docs/pre-deploy.md", "## Front 3.13.0"),
                               ("docs/roadmap.md", "## Front 3.13.0")):
            texto = secao(ler(pagina), titulo)
            self.assertIn("3.13.0", titulo + texto)
            with self.subTest(pagina=pagina):
                self.assertIn("Publicado em 13/11/2026", texto)
        preparo = secao(ler("docs/pre-deploy.md"), "## Front 3.13.0")
        for regra in ("voltar/avançar", "recarregar", "413", "5 MB", "chave",
                      "C4", "títulos repetidos"):
            self.assertIn(regra, preparo)

    def test_publicacao_consistente_sem_estado_anterior(self):
        paginas = ("CHANGELOG.md", "docs/pre-deploy.md", "docs/roadmap.md",
                   "docs/navegacao.md", "docs/funcionalidades.md",
                   "docs/empresas.md", "docs/filtro-de-uf.md",
                   "docs/rebranding-rodada-1.md")
        for pagina in paginas:
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertRegex(texto, r"(?i)publicado em 13/11/2026")
                self.assertNotRegex(texto, r"(?i)\bem publicação\b")
                for linha in texto.splitlines():
                    if "3.13.0" in linha or "Estado:" in linha:
                        self.assertNotIn("sem confirmação de deploy", linha)
