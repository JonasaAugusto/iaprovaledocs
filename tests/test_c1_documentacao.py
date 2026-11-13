"""Contrato público C1, conferido apenas em documentos locais."""

import json
import re
import unittest

from test_documentacao import ler, secao


class C1DocumentacaoTest(unittest.TestCase):
    def test_upload_limite_inclusivo_e_erro_estruturado(self):
        texto = secao(ler("docs/empresas.md"), "### C1: erro de tamanho")
        for regra in ("Ainda não publicado", "5 MiB", "5.242.880 bytes",
                      "exatamente", "413", "Content-Length", "durante a leitura"):
            self.assertIn(regra, texto)
        exemplo = re.search(r"```json\n(.*?)\n```", texto, re.DOTALL)
        self.assertIsNotNone(exemplo, "Falta exemplo da resposta de tamanho excedido")
        self.assertEqual(json.loads(exemplo.group(1)), {
            "detail": "O arquivo passa de 5 MB. Envie um arquivo de até 5 MB.",
            "codigo": "arquivo_muito_grande",
        })

    def test_pdf_limites_por_campo_e_listas(self):
        texto = secao(ler("docs/funcionalidades.md"), "## C1: limites do PDF de concursos")
        self.assertIn("Ainda não publicado", texto)
        self.assertIn("POST /pdf", texto)
        limites = re.findall(r"^\| `([^`]+)` \| (\d+) \|", texto, re.MULTILINE)
        self.assertEqual(dict(limites), {
            "results": "100", "query": "500", "extracted_summary": "2000",
            "titulo": "500", "cargos": "100", "cargos_compativeis": "100",
            "cargos[]": "200", "cargos_compativeis[]": "200", "uf": "32",
            "regiao": "100", "datas.fim": "100", "data_formacao_futura": "7",
            "noticia.link": "2048",
        })
        for regra in ("100 links", "um por resultado", "HTTP ou HTTPS", "422",
                      "chamadas diretas", "metadados", "descartados",
                      "não altera", "15 páginas"):
            self.assertIn(regra, texto)

    def test_ip_novo_sem_perder_retencao_do_aceite(self):
        texto = secao(ler("docs/versao-gratis.md"), "## C1: identificação da conexão")
        for regra in ("Ainda não publicado", "IP da conexão", "proxy confiável",
                      "último endereço não confiável", "cadeia inválida",
                      "cabeçalho enviado diretamente", "login", "cadastro"):
            self.assertIn(regra, texto)
        aceite = secao(ler("docs/versao-gratis.md"), "## Registro do aceite")
        self.assertNotIn("primeiro IP", aceite)
        for regra in ("enquanto a conta existir", "exportação", "IP em claro",
                      "aceites anteriores preservam", "identificação da conexão"):
            self.assertIn(regra, aceite)

    def test_worker_unico_e_pendencia_operacional(self):
        texto = secao(ler("docs/pre-deploy.md"), "## C1: validação antes da publicação")
        for regra in ("Ainda não publicado", "--workers 1", "um processo",
                      "memória", "não são compartilhados", "não foi instalada",
                      "configuração ativa", "solução compartilhada", "decisão do dono",
                      "a operação", "recursos descartáveis", "revisão cruzada"):
            self.assertIn(regra, texto)

    def test_indice_changelog_e_estado_sem_versao_inventada(self):
        indice = ler("README.md")
        self.assertIn("C1", indice)
        self.assertIn("funcionalidades.md#c1-limites-do-pdf-de-concursos", indice)
        changelog = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for regra in ("C1", "5 MiB", "413", "IP", "PDF", "--workers 1",
                      "empresas.md", "versao-gratis.md", "pre-deploy.md",
                      "ainda não publicado"):
            self.assertIn(regra, changelog)


if __name__ == "__main__":
    unittest.main()
