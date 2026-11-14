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
        pacote = secao(ler("docs/funcionalidades.md"), "## Avisos e prazos publicados")
        self.assertIn("Estado: **No ar**", pacote)
        self.assertIn("envio de e-mail ligado", pacote)
        self.assertIn("12/11/2026", pacote)
        changelog = ler("CHANGELOG.md")
        versoes = re.findall(r"^## \[(\d+\.\d+\.\d+)\] - (.+)$", changelog, re.MULTILINE)
        self.assertEqual(versoes[0], ("1.16.0", "Não publicado"))
        self.assertEqual(len(versoes), len({v for v, _ in versoes}))
        self.assertIn("[1.12.2] - Não publicado", changelog)
        self.assertIn("ainda não publicado", ler("README.md"))
        self.assertIn("após a liberação separada do C4", ler("docs/roadmap.md"))
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

    def test_paginas_publicas_sem_fluxo_interno_de_desenvolvimento(self):
        documentos = [RAIZ / "README.md", RAIZ / "CHANGELOG.md",
                      *sorted((RAIZ / "docs").glob("*.md"))]
        proibidos = (r"\b(?:Claude|Codex)\b", r"\[Publicar\]",
                     r"botão do dono", r"\b(?:agentes?|IA)\b[^.\n]*"
                     r"\b(?:desenvolvimento|revisão do código|deploy)\b")
        for documento in documentos:
            with self.subTest(documento=documento.name):
                texto = documento.read_text(encoding="utf-8")
                for padrao in proibidos:
                    self.assertIsNone(re.search(padrao, texto, re.IGNORECASE),
                                      f"Referência interna em {documento.name}: {padrao}")

    def test_cadastro_e_confirmacao_posterior(self):
        cadastro = secao(ler("docs/versao-gratis.md"), "## Cadastro com e-mail")
        self.assertIn("e-mail é **opcional**", cadastro)
        self.assertNotIn("obrigatório", cadastro)
        self.assertIn("código de 6 dígitos", cadastro)
        self.assertIn("10 minutos", cadastro)
        self.assertIn("conta é criada com e-mail pendente", cadastro)
        self.assertIn("Configurações", cadastro)
        self.assertIn("não reserva o endereço", cadastro)
        self.assertIn("12/11/2026", cadastro)
        configuracoes = ler("docs/configuracoes-do-usuario.md")
        self.assertIn("não reserva o endereço", configuracoes)
        conta = secao(configuracoes, "## Conta")
        for regra in ("opcional", "código de 6 dígitos", "10 minutos", "remover",
                      "endereço anterior", "dia seguinte"):
            self.assertIn(regra, conta)
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
        self.assertIn("**No ar** desde **12/11/2026**", custo)
        self.assertIn("tarifa de pico", custo)
        self.assertIn("não equivale à fatura", custo)
        self.assertIn("Histórico já registrado não é recalculado", custo)
        self.assertIn("cache", custo)
        self.assertIn("https://api-docs.deepseek.com/quick_start/pricing/", custo)

    def test_compatibilidade_contrato_e_limites_da_ia(self):
        texto = ler("docs/compatibilidade.md")
        self.assertIn("Estado: **No ar**", texto)
        contrato = secao(texto, "## Consulta e resposta")
        self.assertIn("GET /concursos/{id}/compatibilidade", contrato)
        self.assertIn("autenticada", contrato)
        self.assertIn("link salvo na própria lista de acompanhados", contrato)
        self.assertIn("cache de Informações", contrato)
        linhas = re.findall(r"^\| `([^`]+)` \| ([^|]+) \|", contrato, re.MULTILINE)
        self.assertEqual({codigo: escopo.strip() for codigo, escopo in linhas}, {
            "combina": "Cargo e geral", "parcial": "Cargo e geral",
            "nao_combina": "Cargo e geral", "sem_perfil": "Somente geral",
        })
        self.assertIn("`nome`, `nivel`, `motivo` e `falta`", contrato)
        self.assertIn("`geral`, `cargos` e `gerado_em`", contrato)
        regras = secao(texto, "## Regras e papel da IA")
        self.assertIn("IA nunca decide o nível", regras)
        self.assertIn("formação concluída", regras)
        self.assertIn("não são herdados por todos os cargos", regras)
        self.assertIn("confirme sempre no edital", regras)

    def test_compatibilidade_cota_cache_falha_e_privacidade(self):
        texto = ler("docs/compatibilidade.md")
        cota = secao(texto, "## Cota, cache e falhas")
        for regra in ("reserva durável antes de qualquer chamada externa",
                      "usuário, concurso e versão do perfil", "uma busca normal",
                      "contador da avaliação", "acerto do cache de compatibilidade não consome",
                      "cache de Informações não dispensa", "sem_perfil",
                      "sem chamadas externas e sem consumir cota", "409", "502",
                      "qualquer exceção encerra a tentativa como falha",
                      "sem repetir custos já registrados", "custo permanece desconhecido"):
            with self.subTest(regra=regra):
                self.assertIn(regra, cota)
        self.assertRegex(cota, r"falha.*não consome busca nem feedback")
        dados = secao(texto, "## Dados e privacidade")
        self.assertIn("`compatibilidades`", dados)
        self.assertIn("apagado com a conta", dados)
        self.assertIn("campos educacionais", dados)
        for pagina in ("docs/configuracoes-do-usuario.md", "docs/eventos-de-busca.md",
                       "docs/busca-por-perfil.md", "docs/decisoes.md"):
            self.assertIn("compatibilidade.md", ler(pagina))

    def test_tarifas_numericas_e_cache_sem_dupla_contagem(self):
        custo = secao(ler("docs/stats-do-administrador.md"), "## Estimativa de custo")
        self.assertIn("11/11/2026", custo)
        self.assertIn("1 milhão de tokens", custo)
        linhas = re.findall(r"^\| (Fora de pico|Pico) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|$", custo, re.MULTILINE)
        tarifas = {nome: tuple(float(v.replace(',', '.')) for v in valores)
                   for nome, *valores in linhas}
        self.assertEqual(tarifas, {"Fora de pico": (0.003, 0.15, 0.60),
                                  "Pico": (0.006, 0.30, 1.20)})
        for regra in ("zero explícito", "ausente ou nulo", "limitado a zero",
                      "uma única vez", "não distingue horários ou feriados"):
            self.assertIn(regra, custo)

    def test_pre_deploy_migracoes_antes_do_reinicio(self):
        texto = ler("docs/pre-deploy.md")
        self.assertIn("Estado: **Publicado com envio de e-mail**", texto)
        migracoes = re.findall(r"^\| `([^`]+\.py)` \|", texto, re.MULTILINE)
        self.assertEqual(migracoes, [
            "scripts/migrate_v3_17_email_novidades.py",
            "scripts/migrate_v3_18_alertas_acompanhamento.py",
            "scripts/migrate_v3_19_email_cadastro_cotas.py",
            "scripts/migrate_v3_20_email_pendente.py",
            "scripts/migrate_v3_21_boas_vindas.py",
            "scripts/migrate_v3_22_compatibilidade.py",
            "scripts/migrate_v3_23_empresas.py",
            "scripts/migrate_v3_24_empresas_produtos.py",
        ])
        ordem = secao(texto, "## Ordem da publicação")
        passos = re.findall(r"^\d+\. (.+)$", ordem, re.MULTILINE)
        self.assertEqual(len(passos), 5)
        self.assertIn("v3_17 a v3_22 antes de reiniciar", passos[1])
        self.assertIn("Reiniciar", passos[2])
        self.assertIn("site", passos[4])
        for regra in ("reexecutar a v3_18", "mesmo com a rotina diária desligada",
                      "Brevo", "não executa migrações automaticamente",
                      "backup antes de alterar a base", "autorização explícita"):
            self.assertIn(regra, texto)
        self.assertIn("e-mail pendente", passos[2])
        self.assertIn("e-mail ligado", passos[3])
        self.assertIn("variante grátis 1.3 ainda não ativada", passos[4])

    def test_termos_implementados_e_estado_consistente(self):
        aceite = secao(ler("docs/versao-gratis.md"), "## Registro do aceite")
        self.assertIn('`ACEITE_TERMOS_VERSAO = "gratis-1.2"`', aceite)
        self.assertIn("já implementado", aceite)
        self.assertIn("publicação ainda não confirmada", aceite)
        self.assertIn("aceites anteriores preservam", aceite)
        mensagens = secao(ler("docs/versao-gratis.md"), "## Mensagens revisadas")
        self.assertIn("No ar", mensagens)
        for termo in ("dígitos", "código", "amanhã", "Configurações", "campos", "botões"):
            self.assertIn(termo, mensagens)
        for pagina in ("README.md", "docs/funcionalidades.md", "docs/roadmap.md", "CHANGELOG.md"):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn("compatibilidade.md", texto)
                self.assertIn("pre-deploy.md", texto)
                self.assertNotIn("Etapa 3 (a desenvolver)", texto)

    def test_email_publicado_sem_estados_antigos_nas_paginas_atuais(self):
        paginas = ("README.md", "docs/funcionalidades.md", "docs/versao-gratis.md",
                   "docs/configuracoes-do-usuario.md", "docs/navegacao.md",
                   "docs/pre-deploy.md", "docs/roadmap.md", "docs/decisoes.md")
        for pagina in paginas:
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn("12/11/2026", texto)
                self.assertRegex(texto, r"(?i)(?:envio de e-mail|e-mail|envio) (?:está )?ligado")
                self.assertNotRegex(texto, r"(?i)(?:hoje (?:o )?envio|envio de e-mail|e-mail|envio) "
                                          r"(?:continua |permanece |segue |está )?desligado")
                self.assertNotIn("e-mail (ainda não publicado)", texto)
        entrada = secao(ler("CHANGELOG.md"), "## [1.16.0] - Não publicado")
        for regra in ("12/11/2026", "Brevo", "1.3", "não ativada", "funcionalidades.md",
                      "pre-deploy.md"):
            self.assertIn(regra, entrada)

    def test_brevo_remetente_operador_e_transferencia(self):
        rotina = secao(ler("docs/funcionalidades.md"), "### Rotina diária e modelos de e-mail")
        self.assertIn("Brevo SMTP", rotina)
        self.assertIn("IAprovale <avisos@augustusai.com.br>", rotina)
        self.assertIn("America/Sao_Paulo", rotina)
        legais = secao(ler("docs/versao-gratis.md"), "## Termos de Uso e Política de Privacidade")
        for regra in ("Brevo", "Sendinblue SAS", "França", "operador",
                      "transferência internacional", "códigos", "boas-vindas", "resumos",
                      "Novidades", "validação por advogado continua pendente"):
            self.assertIn(regra, legais)

    def test_legais_13_convite_e_gratis_sem_ativacao(self):
        legais = secao(ler("docs/versao-gratis.md"), "## Termos de Uso e Política de Privacidade")
        for regra in ("1.3", "12/11/2026", "convite", "e-mail opcional", "Brevo", "Carreira",
                      "scripts/legal-gratis/v1_3.py", "ainda não ativada"):
            self.assertIn(regra, legais)
        self.assertNotIn("Próxima atualização: versão 1.2", legais)
        aceite = secao(ler("docs/versao-gratis.md"), "## Registro do aceite")
        self.assertIn("não comprova", aceite)
        self.assertIn("aceites anteriores preservam", aceite)
        for pagina in ("docs/pre-deploy.md", "docs/roadmap.md", "docs/decisoes.md"):
            with self.subTest(pagina=pagina):
                texto = ler(pagina)
                self.assertIn("scripts/legal-gratis/v1_3.py", texto)
                self.assertIn("ainda não ativada", texto)


if __name__ == "__main__":
    unittest.main()
