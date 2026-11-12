"""Contrato público de E1/E2; sem dados pessoais nem chamadas externas."""

import re
import unittest

from test_documentacao import ler, secao


class EmpresasDocumentacaoTest(unittest.TestCase):
    def test_rotas_autenticadas_e_contratos(self):
        texto = ler("docs/empresas.md")
        rotas = secao(texto, "## Endpoints")
        self.assertIn("autenticadas", rotas)
        encontradas = re.findall(r"^\| `(GET|POST|DELETE) (/empresas/[^`]+)` \|", rotas, re.MULTILINE)
        self.assertEqual(set(encontradas), {
            ("POST", "/empresas/curriculo"), ("GET", "/empresas/curriculo"),
            ("GET", "/empresas/curriculo/original"), ("POST", "/empresas/curriculo/perfil"),
            ("DELETE", "/empresas/curriculo"), ("POST", "/empresas/compatibilidade"),
            ("POST", "/empresas/compatibilidade/explicacao"), ("GET", "/empresas/cota"),
        })
        self.assertEqual(len(encontradas), 8)
        for contrato in ("Content-Type", "multipart", "guardar_original=true", "X-Nome-Arquivo",
                         "`texto` ou `url`", "`vaga_id`", "204", "`perfil_status`", "`aviso`"):
            self.assertIn(contrato, rotas)

    def test_curriculo_e_compatibilidade_com_limites(self):
        texto = ler("docs/empresas.md")
        curriculo = secao(texto, "## E1")
        for regra in ("PDF, DOCX ou TXT", "5 MB", "15 páginas", "sem OCR", "extração local",
                      "`pendente`", "40.000", "12.000", "`perfil_parcial`", "`texto_truncado`"):
            self.assertIn(regra, curriculo)
        compatibilidade = secao(texto, "## E2")
        for regra in ("Greenhouse, Lever, Ashby, Workable e SmartRecruiters", "Gupy",
                      "calculados em Python", "0 a 10", "não é chance de contratação",
                      "`nota: null`", "`dados_insuficientes: true`", "`nao_avaliados`",
                      "cache global", "sem o texto completo da vaga", "versão do currículo",
                      "9.000 caracteres", "sob demanda", "sem enviar o currículo"):
            self.assertIn(regra, compatibilidade)

    def test_cota_numerica_e_reserva(self):
        cota = secao(ler("docs/empresas.md"), "## Cota diária")
        limites = re.findall(r"^\| (Chamadas de IA|Custo estimado em US\$) \| ([\d,]+) \|$", cota, re.MULTILINE)
        self.assertEqual(dict(limites), {"Chamadas de IA": "17", "Custo estimado em US$": "0,01"})
        for regra in ("o que vier primeiro", "Brasília", "separada da cota de buscas de concursos",
                      "cada tentativa", "JSON inválido", "acertos de cache não consomem",
                      "reserva pelo custo máximo antes", "429", "mesmo sem atingir os dois limites",
                      "não é cobrança", "`chamadas_restantes`", "`esgotada`"):
            self.assertIn(regra, cota)

    def test_armazenamento_exportacao_e_exclusao(self):
        texto = ler("docs/empresas.md")
        armazenamento = secao(texto, "## Armazenamento")
        for regra in ("texto extraído e o perfil", "somente compactados", "zstd ou gzip",
                      "original não é guardado por padrão", "`guardar_original=true`",
                      "também compactado", "não é criptografia", "até a pessoa apagar"):
            self.assertIn(regra, armazenamento)
        dados = secao(texto, "## Exportação e exclusão")
        for regra in ("GET /me/exportar", "`empresas`", "`curriculo`", "`explicacoes`", "`uso_ia`",
                      "descompactados", "base64", "não zera a cota", "ambos os fluxos",
                      "cache global de requisitos de vagas permanece"):
            self.assertIn(regra, dados)

    def test_privacidade_sem_promessas_de_anonimizacao(self):
        privacidade = secao(ler("docs/empresas.md"), "## Privacidade")
        for regra in ("somente ao DeepSeek", "e-mail, telefone, links e CPF",
                      "antes de gerar o perfil", "não garante anonimização",
                      "não são enviados aos ATS", "transferência internacional",
                      "não inclua dados sensíveis", "textos legais", "ainda não publicado"):
            self.assertIn(regra, privacidade)

    def test_estado_indices_e_dependencias(self):
        texto = ler("docs/empresas.md")
        self.assertIn("Estado: **Ainda não publicado**", texto)
        self.assertIn("backend 2.15.0", texto)
        self.assertIn("E3", texto)
        self.assertIn("E4", texto)
        self.assertIn("E5", texto)
        for pagina in ("README.md", "docs/funcionalidades.md", "docs/roadmap.md", "docs/decisoes.md",
                       "docs/configuracoes-do-usuario.md", "docs/versao-gratis.md", "CHANGELOG.md"):
            with self.subTest(pagina=pagina):
                linhas = [linha for linha in ler(pagina).splitlines() if "empresas.md" in linha]
                self.assertTrue(linhas, f"Falta referência ao Empresas: {pagina}")
                self.assertTrue(any("ainda não publicado" in linha.lower() for linha in linhas),
                                f"Estado do Empresas ausente: {pagina}")
        changelog = secao(ler("CHANGELOG.md"), "## [1.14.0] - Não publicado")
        self.assertIn("empresas.md", changelog)
        preparacao = secao(ler("docs/pre-deploy.md"), "## Empresas E1/E2")
        for regra in ("Ainda não publicado", "v3_23", "pypdf==6.21.4", "antes do reinício", "textos legais"):
            self.assertIn(regra, preparacao)


if __name__ == "__main__":
    unittest.main()
