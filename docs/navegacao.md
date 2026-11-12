# Navegação do site e Carreira

Estado: **No ar** desde **12/11/2026**. Esta página descreve as telas publicadas, sem alterar a interface.

## Barra e topo

A barra de navegação apresenta **Concursos, Carreira, Perfil, Administração e Stats**, conforme a disponibilidade do serviço e as permissões da conta. Administração e Stats são exclusivas de administradores. A barra fica na lateral no computador e embaixo no celular.

No topo, **Alertas** fica junto do **sino**, e **Configurações** ocupa o lugar do atalho de tema. Tema claro, escuro ou automático continua disponível nas Configurações. A home ganhou uma seção do **Empresas** e um **menu no celular** para acessar suas seções.

## Carreira

A aba Carreira **só aparece** quando **`GET /empresas/cota` responde** e confirma a disponibilidade do backend Empresas. Oferece duas opções:

- **Currículo e vaga:** envio de **PDF/DOCX/TXT até 5 MB**, acompanhamento do perfil extraído e comparação com uma vaga. O resultado apresenta nota de **0 a 10 com régua**, pontos fortes, lacunas e a ação **“Por que essa nota?”**. Os limites de extração e as situações de perfil pendente estão em [Empresas E1/E2](empresas.md).
- **Buscar vagas:** consulta ao índice e prévia gratuita por regras, com cobertura e validade descritas em [Busca de vagas (E5)](empresas-vagas.md).

Os materiais são **por vaga**: currículo ATS em **PDF**, **Word** (DOCX) ou texto para **copiar**, e **roteiro de entrevista**. Consulte as regras conservadoras de geração, a cota e o teste gratuito em [E3/E4](empresas-e3-e4.md). A nota não representa chance de contratação e os materiais precisam ser revisados pela pessoa antes do uso.

## Alertas

Em **Alertas > Acompanhando**, cada concurso acompanhado permite consultar a compatibilidade **por cargo**, com motivo e lacunas. É a [compatibilidade educacional de concursos](compatibilidade.md), que usa o Perfil de concursos e a cota de buscas desse produto; é diferente da comparação com currículo e vagas de empresas na aba Carreira.

O sino dá acesso às Novidades. O envio de e-mail está ligado via Brevo desde 12/11/2026; o endereço é opcional nas Configurações, e o resumo das 07:00 de São Paulo exige e-mail verificado e preferência ativa. Novidades permanece disponível no site, inclusive sem cota ou entrega por e-mail. Veja [Avisos e acompanhamento](funcionalidades.md#alertas-e-concursos-acompanhados).

## Endereços das abas

As abas têm endereço por fragmento, após a URL do aplicativo:

| Fragmento | Destino |
|---|---|
| `#alertas` | Alertas e acompanhamento de concursos. |
| `#carreira` | Currículo, comparação e busca de vagas de empresas. |
| `#admin` | Administração. |
| `#stats` | Estatísticas de uso para administradores. |
| `#config/<secao>` | Seção de Configurações; por exemplo, `#config/privacidade`. |

Um endereço direto respeita as permissões da conta e a disponibilidade do recurso. O fragmento não concede acesso administrativo nem torna a aba Carreira disponível sem o backend. Veja também [Configurações do usuário](configuracoes-do-usuario.md#estrutura).
