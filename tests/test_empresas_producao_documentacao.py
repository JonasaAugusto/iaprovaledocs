"""Regressões da publicação de 12/11/2026, E5 e navegação; só arquivos locais."""

import re
import unittest

from test_documentacao import ler, secao


class EmpresasProducaoDocumentacaoTest(unittest.TestCase):
    def test_publicacao_e_referencias_atuais(self):
        for pagina in ("docs/empresas.md", "docs/empresas-e3-e4.md",
                       "docs/compatibilidade.md"):
            with self.subTest(pagina=pagina):
                abertura = ler(pagina).split("\n## ", 1)[0]
                self.assertIn("Estado: **No ar**", abertura)
                self.assertIn("12/11/2026", abertura)
                self.assertNotIn("ainda não publicado", abertura.lower())
        for pagina in ("README.md", "docs/funcionalidades.md", "docs/roadmap.md",
                       "docs/decisoes.md", "docs/versao-gratis.md",
                       "docs/configuracoes-do-usuario.md", "docs/pre-deploy.md"):
            with self.subTest(pagina=pagina):
                linhas = [linha for linha in ler(pagina).splitlines()
                          if "empresas.md" in linha]
                self.assertTrue(linhas, f"Falta referência ao Empresas: {pagina}")
                self.assertTrue(any("12/11/2026" in linha for linha in linhas))
                for linha in linhas:
                    self.assertNotIn("ainda não publicado", linha.lower())
                    self.assertNotIn("fora de produção", linha.lower())
        changelog = secao(ler("CHANGELOG.md"), "## [1.15.0] - Não publicado")
        for referencia in ("12/11/2026", "empresas.md", "empresas-vagas.md",
                           "navegacao.md", "perfil-2"):
            self.assertIn(referencia, changelog)
        self.assertNotIn("## [Não publicado — Empresas E3/E4]", ler("CHANGELOG.md"))

    def test_e5_rotas_e_parametros(self):
        consulta = secao(ler("docs/empresas-vagas.md"), "## Consulta")
        rotas = re.findall(r"^\| `(GET /empresas/[^`]+)` \|", consulta, re.MULTILINE)
        self.assertEqual(set(rotas), {
            "GET /empresas/vagas", "GET /empresas/panorama",
            "GET /empresas/vagas/{id}/compatibilidade",
        })
        self.assertEqual(len(rotas), 3)
        parametros = re.findall(r"^\| `([a-z_]+)` \|", consulta, re.MULTILINE)
        self.assertEqual(set(parametros), {"termo", "uf", "remoto", "empresa", "ats",
                                           "limite", "offset"})
        self.assertIn("autenticadas", consulta)
        self.assertIn("503", consulta)
        self.assertIn("não há índice", consulta)

    def test_e5_coleta_cobertura_e_validade(self):
        indice = secao(ler("docs/empresas-vagas.md"), "## Índice e cobertura")
        for regra in ("iaprovale-empresas-vagas", "06:00", "America/Sao_Paulo",
                      "saída 2", "coleta parcial aceita", "EMPRESAS_INDICE_PATH",
                      "72 horas", "176 empresas", "data/empresas", "robots.txt",
                      "Greenhouse", "Lever", "Ashby", "Workable", "SmartRecruiters",
                      "Gupy", "não garante"):
            with self.subTest(regra=regra):
                self.assertIn(regra, indice)

    def test_previa_gratuita_nao_se_confunde_com_e2(self):
        previa = secao(ler("docs/empresas-vagas.md"), "## Prévia de compatibilidade")
        for regra in ("gratuita", "sem IA", "por regras", "requisitos", "prévia",
                      "E2", "não é chance de contratação", "empresas.md"):
            self.assertIn(regra, previa)

    def test_c2_busca_por_palavra_e_ordenacao(self):
        busca = secao(ler("docs/empresas-vagas.md"), "## Busca por palavra e ordenação — C2")
        for regra in ("Ainda não publicado", "todos os termos", "palavras completas",
                      "título, descrição, empresa e área", "análise", "analise",
                      "JavaScript", "Java", "C++", "Go", "golang",
                      "siglas curtas", "maiúsculas", "cada termo encontrado no título",
                      "empresa, título e identificador", "antes da paginação",
                      "Sem termo", "não é uma nota de compatibilidade"):
            with self.subTest(regra=regra):
                self.assertIn(regra, busca)

    def test_c2_cache_nao_prolonga_validade_nem_oculta_falha(self):
        cache = secao(ler("docs/empresas-vagas.md"), "## Reutilização do índice — C2")
        for regra in ("Ainda não publicado", "cache", "memória", "data de modificação",
                      "recarregado", "consultas simultâneas", "durante a coleta",
                      "Índices antigos", "sem migração", "a cada consulta",
                      "mais de 24 horas", "72 horas", "503", "ausente ou inválido",
                      "não usa a cópia anterior", "identificador", "404"):
            with self.subTest(regra=regra):
                self.assertIn(regra, cache)

    def test_c2_estado_e_referencias_sem_anunciar_publicacao(self):
        abertura = ler("docs/empresas-vagas.md").split("\n## ", 1)[0]
        self.assertIn("No ar", abertura)
        self.assertIn("12/11/2026", abertura)
        funcionalidades = secao(ler("docs/funcionalidades.md"), "## IAprovale Empresas — E1–E5")
        self.assertIn("C2", funcionalidades)
        self.assertIn("Ainda não publicado", funcionalidades)
        self.assertIn("empresas-vagas.md#busca-por-palavra-e-ordenação--c2", funcionalidades)
        changelog = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for regra in ("C2", "palavras completas", "título", "cache", "72 horas",
                      "ainda não publicado", "docs/empresas-vagas.md"):
            self.assertIn(regra, changelog)

    def test_tela_carreira_e_materiais(self):
        tela = secao(ler("docs/navegacao.md"), "## Carreira")
        for regra in ("GET /empresas/cota", "só aparece", "Currículo e vaga", "Buscar vagas",
                      "PDF/DOCX/TXT", "5 MB", "perfil", "0 a 10", "régua",
                      "Por que essa nota?", "PDF", "Word", "copiar", "roteiro de entrevista",
                      "por vaga", "empresas-e3-e4.md", "empresas-vagas.md"):
            self.assertIn(regra, tela)

    def test_navegacao_alertas_home_e_enderecos(self):
        texto = ler("docs/navegacao.md")
        barra = secao(texto, "## Barra e topo")
        self.assertIn("Concursos, Carreira, Perfil, Administração e Estatísticas", barra)
        for regra in ("administradores", "Alertas", "sino", "Configurações",
                      "tema", "menu no celular", "home", "Empresas"):
            self.assertIn(regra, barra)
        alertas = secao(texto, "## Alertas")
        self.assertIn("Alertas > Acompanhando", alertas)
        self.assertIn("por cargo", alertas)
        self.assertIn("compatibilidade.md", alertas)
        enderecos = secao(texto, "## Endereços das abas")
        fragmentos = re.findall(r"^\| `([^`]+)` \|", enderecos, re.MULTILINE)
        self.assertEqual(set(fragmentos), {"#alertas", "#carreira", "#admin", "#stats",
                                           "#config/<secao>"})
        self.assertIn("permissões", enderecos)
        configuracoes = secao(ler("docs/configuracoes-do-usuario.md"), "## Estrutura")
        self.assertIn("topo", configuracoes)
        self.assertIn("#config/<secao>", configuracoes)
        self.assertNotIn("cada uma com seu item na barra", configuracoes)

    def test_curriculo_longo_mantem_limites_e_privacidade(self):
        curriculo = secao(ler("docs/empresas.md"), "## E1")
        for regra in ("3.500 tokens", "perfil-2", "teto de resposta", "12.000 caracteres",
                      "`perfil_parcial`", "`pendente`", "40.000 caracteres"):
            self.assertIn(regra, curriculo)

    def test_precos_pendentes_e_teste_gratuito(self):
        produtos = ler("docs/empresas-e3-e4.md")
        self.assertNotIn("R$ 1,49", produtos)
        self.assertNotIn("R$ 2,99", produtos)
        for pagina in ("docs/empresas-e3-e4.md", "docs/roadmap.md", "docs/decisoes.md"):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                for regra in ("preços", "meio de pagamento", "pendentes", "cobrança desligada",
                              "E3/E4", "gratuitos no teste", "17 chamadas", "US$ 0,01",
                              "o que vier primeiro"):
                    self.assertIn(regra, texto)


if __name__ == "__main__":
    unittest.main()
