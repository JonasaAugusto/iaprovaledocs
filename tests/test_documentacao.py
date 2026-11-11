"""Regressões do contrato público; somente arquivos locais, sem serviços externos."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


RAIZ = Path(__file__).resolve().parents[1]


def ler(nome):
    return (RAIZ / nome).read_text(encoding="utf-8")


def secao(texto, titulo):
    posicao = texto.find(titulo)
    if posicao < 0:
        raise AssertionError(f"Seção obrigatória ausente: {titulo}")
    inicio = posicao + len(titulo)
    nivel = len(titulo) - len(titulo.lstrip("#"))
    fim = re.search(rf"^#{{1,{nivel}}} ", texto[inicio:], re.MULTILINE)
    return texto[inicio:inicio + fim.start()] if fim else texto[inicio:]


class DocumentacaoTest(unittest.TestCase):
    def test_estado_changelog_e_links_locais(self):
        pacote = secao(ler("docs/funcionalidades.md"), "## Avisos, prazos e e-mail")
        self.assertIn("Estado: **Ainda não publicado**", pacote)
        changelog = ler("CHANGELOG.md")
        versoes = re.findall(r"^## \[(\d+\.\d+\.\d+)\] - (.+)$", changelog, re.MULTILINE)
        self.assertEqual(versoes[0], ("1.13.0", "Não publicado"))
        self.assertEqual(len(versoes), len({v for v, _ in versoes}))
        self.assertIn("[1.12.2] - Não publicado", changelog)
        self.assertIn("ainda não publicado", ler("README.md"))
        self.assertIn("ainda não publicado", ler("docs/roadmap.md"))
        documentos = [RAIZ / "README.md", RAIZ / "CHANGELOG.md", *sorted((RAIZ / "docs").glob("*.md"))]
        for documento in documentos:
            for destino in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", documento.read_text(encoding="utf-8")):
                url = urlsplit(destino)
                if url.scheme or url.netloc:
                    continue
                alvo = (documento.parent / unquote(url.path)).resolve() if url.path else documento
                with self.subTest(documento=documento.name, destino=destino):
                    self.assertTrue(alvo.is_file(), f"Link local inexistente: {destino}")
                    if url.fragment:
                        titulos = re.findall(r"^#+ (.+)$", alvo.read_text(encoding="utf-8"), re.MULTILINE)
                        ancoras = [re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-") for t in titulos]
                        self.assertIn(unquote(url.fragment), ancoras, f"Âncora inexistente: {destino}")

    def test_cadastro_e_confirmacao_posterior(self):
        cadastro = secao(ler("docs/versao-gratis.md"), "## Cadastro com e-mail")
        self.assertIn("ainda não publicado", cadastro)
        self.assertRegex(cadastro, r"e-mail é \*\*obrigatório\*\*")
        self.assertIn("código de 6 dígitos", cadastro)
        self.assertIn("conta é criada com e-mail pendente", cadastro)
        self.assertIn("Configurações", cadastro)
        self.assertIn("não reserva o endereço", cadastro)
        self.assertIn("envio está desligado", cadastro)
        self.assertIn("fluxo atual, sem pedir e-mail", cadastro)
        configuracoes = ler("docs/configuracoes-do-usuario.md")
        self.assertIn("não reserva o endereço", configuracoes)
        self.assertIn("gratis-1.2", ler("docs/versao-gratis.md"))

    def test_cotas_e_sentido_do_compartilhamento(self):
        cotas = secao(ler("docs/funcionalidades.md"), "### Cotas de e-mail")
        self.assertIn("**200 envios de códigos**", cotas)
        self.assertIn("**100 envios de avisos**", cotas)
        self.assertIn("globais por dia", cotas)
        self.assertIn("Brasília", cotas)
        self.assertIn("Códigos podem usar a sobra da cota de avisos", cotas)
        self.assertIn("avisos nunca usam a cota de códigos", cotas)
        self.assertIn("boas-vindas usa a categoria de códigos", cotas)

    def test_alertas_futuros_prazos_e_retencao(self):
        texto = ler("docs/funcionalidades.md")
        alertas = secao(texto, "### Alertas e concursos acompanhados")
        self.assertIn("primeira busca bem-sucedida", alertas)
        self.assertIn("linha de base", alertas)
        self.assertIn("criar ou reativar", alertas)
        self.assertIn("**10 avisos por alerta por dia**", alertas)
        self.assertIn("excedentes ficam pendentes", alertas)
        self.assertIn("**50 concursos por conta**", alertas)
        self.assertIn("**D-3 e D-1**", alertas)
        novidades = secao(texto, "### Caixa de Novidades")
        self.assertRegex(novidades, r"lidas.*6 meses.*183 dias.*criação")
        self.assertIn("não lidas são mantidas", novidades)

    def test_boas_vindas_rotina_e_modelos(self):
        rotina = secao(ler("docs/funcionalidades.md"), "### Rotina diária e modelos de e-mail")
        self.assertIn("**07:00, horário de Brasília**", rotina)
        self.assertIn("depois de confirmar o e-mail", rotina)
        self.assertIn("manhã seguinte", rotina)
        self.assertIn("antes dos resumos", rotina)
        self.assertIn("HTML e texto", rotina)
        self.assertIn("e-mail verificado", rotina)
        self.assertIn("preferência de avisos ativada", rotina)
        self.assertIn("sem novidades, não há resumo", rotina)
        self.assertIn("adiados por falta de cota", rotina)
        self.assertIn("não é reenviado automaticamente", rotina)

    def test_estimativa_de_custo_e_historico_preservado(self):
        custo = secao(ler("docs/stats-do-administrador.md"), "## Estimativa de custo")
        self.assertIn("Ainda não publicado", custo)
        self.assertIn("tarifa de pico", custo)
        self.assertIn("não equivale à fatura", custo)
        self.assertIn("Histórico já registrado não é recalculado", custo)
        self.assertIn("cache", custo)
        self.assertIn("https://api-docs.deepseek.com/quick_start/pricing/", custo)


if __name__ == "__main__":
    unittest.main()
