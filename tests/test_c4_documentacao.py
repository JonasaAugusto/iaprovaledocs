"""Contrato público do C4, sem serviços externos ou dados de usuários."""

import unittest

from test_documentacao import ler, secao


class C4DocumentacaoTest(unittest.TestCase):
    def test_historico_minimo_e_contagem_total(self):
        texto = secao(ler("docs/configuracoes-do-usuario.md"), "### C4: histórico enxuto")
        for regra in ("Ainda não publicado", "até 100 resultados", "`id`", "`titulo`",
                      "`link`", "`noticia.link`", "contagem total", "resumo",
                      "local, prazo e demais detalhes", "não são guardados",
                      "exportação", "não limita os resultados da busca"):
            self.assertIn(regra, texto)

    def test_registros_anteriores_e_prazos_preservados(self):
        texto = secao(ler("docs/configuracoes-do-usuario.md"), "### C4: histórico enxuto")
        for regra in ("não são reescritos", "10 buscas", "90 dias", "apagar uma busca",
                      "exclusão da conta"):
            self.assertIn(regra, texto)
        conta = secao(ler("docs/configuracoes-do-usuario.md"), "## Conta")
        self.assertIn("30 dias sem uso", conta)

    def test_sql_sessoes_e_estados_protegidos(self):
        texto = secao(ler("docs/pre-deploy.md"), "## C4: histórico e retenção")
        for regra in ("Ainda não publicado", "DELETE", "SQL", "10 buscas", "90 dias",
                      "pedidos aprovados", "exclusões e verificações pendentes",
                      "30 dias da revogação", "30 dias de inatividade", "mais 30 dias",
                      "data de criação", "contagens", "sem carregar"):
            self.assertIn(regra, texto)

    def test_migracao_reversivel_sem_reescrever_dados(self):
        texto = secao(ler("docs/pre-deploy.md"), "## C4: histórico e retenção")
        for regra in ("scripts/migrate_v3_25_history_index.py", "v3_24", "idempotente",
                      "reversível", "`search_history(user_id, created_at)`",
                      "`--downgrade`", "preservam os registros", "antes do reinício",
                      "não usa Alembic", "recursos descartáveis", "Claude/serviço",
                      "[Publicar]", "não comprova"):
            self.assertIn(regra, texto)

    def test_referencias_e_eventos_separados(self):
        eventos = secao(ler("docs/eventos-de-busca.md"), "## Retenção e privacidade")
        for regra in ("C4", "ainda não publicado", "90 dias", "registro separado",
                      "configuracoes-do-usuario.md#c4-histórico-enxuto"):
            self.assertIn(regra, eventos)
        entrada = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for texto in (entrada, ler("README.md")):
            for regra in ("C4", "ainda não publicado",
                          "configuracoes-do-usuario.md#c4-histórico-enxuto",
                          "pre-deploy.md#c4-histórico-e-retenção"):
                self.assertIn(regra, texto)


if __name__ == "__main__":
    unittest.main()
