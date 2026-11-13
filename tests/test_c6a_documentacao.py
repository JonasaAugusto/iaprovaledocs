"""Contrato documental do C6a final, sem serviços externos."""

import unittest

from test_documentacao import ler, secao


class C6aDocumentacaoTest(unittest.TestCase):
    def test_alcance_e_limites(self):
        texto = secao(ler("docs/busca-por-perfil.md"), "## C6a: equivalentes de cargo")
        for regra in ("Ainda não publicado", "Direito encontra Advogado", "palavras inteiras",
                      "Superadvogado", "todos os termos", "até cinco", "até três formações",
                      "em paralelo", "seis segundos", "tempo total da busca", "já concluídas",
                      "não consomem", "sem retentativas", "C17", "não amplia a consulta",
                      "não se aplica", "edital"):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)
        self.assertIn("determinística e não chama a IA", ler("docs/busca-por-perfil.md"))

    def test_cache_privacidade_e_falhas(self):
        texto = secao(ler("docs/busca-por-perfil.md"), "### Reutilização, privacidade e falhas")
        for regra in ("30 dias", "24 horas", "SHA-256", "sem vínculo com usuário",
                      "somente o termo da formação normalizado", "nenhum dado do usuário",
                      "não é garantia de anonimato", "professor", "técnico", "analista",
                      "auxiliar", "assistente", "analista de sistemas", "não são guardados",
                      "sem chamar o modelo", "preservam os equivalentes recém-gerados",
                      "não derruba a busca", "não há limpeza periódica", "saldo",
                      "não há garantia de uma única chamada"):
            with self.subTest(regra=regra):
                self.assertIn(regra, texto)

    def test_custo_e_cancelamento(self):
        texto = secao(ler("docs/busca-por-perfil.md"), "### Estimativa de custo")
        for regra in ("zero tokens adicionais", "120 caracteres", "200 tokens de entrada",
                      "200 de saída", "US$ 0,0003", "US$ 0,30 por 1.000", "tarifas do código",
                      "renovações", "fatura", "JSON inválido", "sem informação de uso",
                      "não garante", "stats-do-administrador.md"):
            self.assertIn(regra, texto)

    def test_migracao_reversivel_e_cli(self):
        texto = secao(ler("docs/pre-deploy.md"), "## C6a: cache de equivalentes de cargo")
        for regra in ("Ainda não publicado", "v3.26", "idempotentes", "somente o cache",
                      "python -m scripts.migrate_v3_26_cargo_synonyms\n",
                      "python -m scripts.migrate_v3_26_cargo_synonyms --downgrade",
                      "v3_25_history_index", "C5", "posicionais", "retirar a versão",
                      "não interrompe a busca", "backup", "recursos descartáveis",
                      "não executa nem atesta", "operação autorizada"):
            self.assertIn(regra, texto)

    def test_referencias_e_estado(self):
        for pagina in ("README.md", "docs/funcionalidades.md", "CHANGELOG.md"):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn("busca-por-perfil.md#c6a-equivalentes-de-cargo", texto)
                self.assertIn("C6a", texto)
                self.assertIn("ainda não publicado", texto.lower())
        entrada = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for regra in ("24 horas", "seis segundos", "três", "pre-deploy.md#c6a-cache-de-equivalentes-de-cargo"):
            self.assertIn(regra, entrada)


if __name__ == "__main__":
    unittest.main()
