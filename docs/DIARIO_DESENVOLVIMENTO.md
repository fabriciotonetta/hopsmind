# 📔 Diário de Desenvolvimento — hopsmind

Este arquivo documenta a evolução do projeto **hopsmind**, dia a dia, incluindo decisões técnicas, desafios e aprendizados. Serve tanto como registro pessoal quanto como material de apoio para explicar o projeto a recrutadores.

---

## Dia 1 — [30/06/2026] — Fundação do projeto e dados

### O que foi feito
- ✅ Ambiente de desenvolvimento configurado: Python 3.13.2, Git 2.54.0, VS Code
- ✅ Repositório `hopsmind` criado no GitHub (público, licença MIT, `.gitignore` para Python)
- ✅ Estrutura de pastas definida: `dados/`, `notebooks/`, `src/`, `rotulos_gerados/`, `docs/`, `prints/`
- ✅ Dataset real obtido: **Brewer's Friend Beer Recipes** (Kaggle, by jtrofe) — 73.861 receitas originais, 23 colunas
- ✅ Análise exploratória inicial (`src/01_explorar_dados.py`): identificação de valores ausentes por coluna
- ✅ Limpeza de dados (`src/02_limpar_dados.py`):
  - Selecionadas 13 colunas relevantes e completas (Name, Style, Size(L), OG, FG, ABV, IBU, Color, BoilSize, BoilTime, Efficiency, BrewMethod, SugarScale)
  - Descartadas colunas com alta taxa de valores ausentes (ex: PrimingMethod 91% vazio, PrimingAmount 93% vazio, PitchRate 53% vazio)
  - Removidas linhas sem `Name` ou `Style` (598 linhas, <1% do total)
  - Resultado: **73.263 linhas, 13 colunas, 0 valores ausentes**
- ✅ Criação de dataset enriquecido com sabores exóticos brasileiros (`src/03_criar_receitas_exoticas.py`):
  - 12 receitas inéditas criadas com curadoria orientada por dados reais (faixas de ABV/IBU/Color baseadas em estilos análogos do dataset original)
  - Sabores: Jabuticaba, Açaí com Guaraná, Pequi, Cupuaçu, Café com Pimenta Rosa, Maracujá com Mel, Cacau e Canela, Abacaxi com Hortelã, Goiaba Vermelha, Pimenta Biquinho, Mandioca Doce e Canela, Castanha do Pará
- ✅ União dos datasets (`src/04_juntar_datasets.py`): dataset final unificado com **73.275 receitas** (`dados/receitas_final.csv`)
- ✅ Dois commits realizados e enviados ao GitHub

### Decisões técnicas e por quê
- **Encoding `latin1`** usado na leitura do CSV original — necessário porque o dataset tem origem americana/antiga e apresenta problemas de acentuação com UTF-8 padrão.
- **Estratégia de limpeza:** ao invés de imputar (preencher artificialmente) valores ausentes em colunas com mais de 40% de dados faltantes, optei por descartar essas colunas inteiramente — evita introduzir ruído artificial no treinamento futuro do modelo.
- **Dataset exótico construído com mesmas colunas do dataset real** — decisão deliberada para permitir concatenação direta (`pd.concat`) sem necessidade de transformação adicional.

### Arquivos gerados até aqui
```
dados/recipeData.csv          (dataset original, bruto, do Kaggle)
dados/receitas_limpas.csv     (dataset real após limpeza)
dados/receitas_exoticas.csv   (12 receitas exóticas criadas manualmente)
dados/receitas_final.csv      (dataset final unificado — usado nas próximas etapas)

src/01_explorar_dados.py
src/02_limpar_dados.py
src/03_criar_receitas_exoticas.py
src/04_juntar_datasets.py
```

### Prints capturados
- `01-criacao-repositorio-github.png`
- `02-dataset-kaggle-baixado.png`
- `03-primeira-execucao-codigo.png`
- `04-limpeza-dados-concluida.png`
- `05-primeiro-commit-github.png`
- `06-dataset-final-unificado.png`

### Comando para retomar de onde paramos (usado no início do Dia 2)
```
cd "D:\Portfólio I.A\hopsmind"
git status
git pull origin main
```

---

## Dia 2 — [PREENCHER DATA] — Visualização de dados, ambiente virtual e início do Machine Learning

### O que foi feito
- ✅ Instaladas bibliotecas de visualização: `matplotlib` e `seaborn`
- ✅ Análise exploratória visual (`src/05_visualizar_dados.py`), gerando 3 gráficos:
  - Top 10 estilos de cerveja mais comuns no dataset (gráfico de barras)
  - Distribuição do teor alcoólico/ABV (histograma com curva de densidade)
  - Relação entre Cor (SRM) e Amargor/IBU (gráfico de dispersão, amostra de 3.000 receitas, `random_state=42` para reprodutibilidade)
- ✅ Commit e push do progresso de visualização
- ✅ Criado **ambiente virtual** (`.venv`) para isolar as dependências do projeto — boa prática profissional para evitar conflitos entre bibliotecas de diferentes projetos
- ✅ Reinstaladas as bibliotecas dentro do ambiente virtual: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`
- ✅ Decisão de abordagem de IA definida: **Clustering (K-Means, 8 grupos) + geração de receitas** baseada nos padrões aprendidos pelos clusters
- 🔄 Em andamento: `src/06_treinar_clustering.py` — preparação dos dados para o modelo de clustering

### Decisões técnicas e por quê
- **Ambiente virtual (`.venv`):** isola as dependências deste projeto do Python global do computador, evitando conflitos de versão com outros projetos futuros. Prática padrão de mercado.
- **Abordagem de IA escolhida — Clustering + Geração (em vez de só regressão ou só geração simples):** permite demonstrar dois conceitos de Machine Learning no mesmo projeto (aprendizado não-supervisionado via K-Means, e lógica de geração de dados sintéticos a partir dos clusters aprendidos), além de viabilizar a geração de receitas "exóticas" de forma mais sofisticada futuramente.
- **K=8 clusters:** número escolhido como equilíbrio entre granularidade (grupos suficientemente específicos) e simplicidade (não fragmentar demais os dados).
- **`random_state=42` na amostragem do gráfico de dispersão:** garante reprodutibilidade — rodar o código novamente sempre gera a mesma amostra, facilitando comparações e depuração.

### Insights obtidos com os gráficos
- **American IPA** é disparadamente o estilo mais comum no dataset (quase 12.000 receitas), seguido por American Pale Ale (~7.500).
- A maioria das receitas tem ABV concentrado entre 4,5% e 7%, com pico por volta de 5-5,5% — distribuição com formato de sino, consistente com cervejas comerciais/caseiras típicas.
- Não foi identificada correlação forte entre Cor (SRM) e Amargor (IBU) — cervejas escuras não são necessariamente mais ou menos amargas que as claras neste dataset.

### Obstáculos encontrados e como foram resolvidos
- **IndentationError** no arquivo `05_visualizar_dados.py`: uma linha de código tinha espaço extra no início, sem pertencer a nenhum bloco — corrigido alinhando a indentação com as linhas vizinhas.
- **Confusão entre terminal e editor de código:** comandos Python foram digitados por engano diretamente no terminal (PowerShell) em vez de dentro do arquivo `.py` — resolvido reforçando a diferença entre "escrever a receita" (arquivo `.py`) e "mandar executar a receita" (comando `python arquivo.py` no terminal).
- **Falha no processo de documentação:** alguns prints deixaram de ser solicitados nas etapas de visualização e configuração do ambiente virtual. Recuperados retroativamente nesta atualização do diário (ver lista abaixo). Reforçado o processo: a cada etapa grande concluída, fazer uma checagem de "prints/commits pendentes" antes de seguir adiante.

### Arquivos gerados no Dia 2
```
src/05_visualizar_dados.py
src/06_treinar_clustering.py        (em andamento)

prints/grafico_top_estilos.png
prints/grafico_distribuicao_abv.png
prints/grafico_cor_vs_ibu.png

.venv/                               (ambiente virtual — não vai para o GitHub, listado no .gitignore)
```

### Prints capturados (Dia 2)
- `07-ambiente-virtual-criado.png` — terminal mostrando `(.venv)` ativo e instalação das bibliotecas concluída *(recuperado retroativamente)*
- Gráficos gerados automaticamente pelo código (já contam como material visual, sem necessidade de captura manual):
  - `grafico_top_estilos.png`
  - `grafico_distribuicao_abv.png`
  - `grafico_cor_vs_ibu.png`

### Próximos passos (retomar aqui)
1. Finalizar preparação dos dados para o clustering (padronização com `StandardScaler` — entender por que é necessária)
2. Treinar o modelo K-Means com 8 clusters
3. Analisar e interpretar os clusters formados (que características definem cada grupo)
4. **📸 Tirar print do resultado do treinamento** → `08-clustering-treinado.png`
5. Construir a lógica de geração de receitas novas a partir dos clusters
6. Avaliação/validação do modelo
7. Integração com IA generativa de imagens para os rótulos
8. Documentação final (README, descrição do projeto, texto para recrutador)

### Comando para retomar de onde paramos
Ao voltar, abra o terminal na pasta do projeto, ative o ambiente virtual (caso não ative sozinho) e confirme que está tudo sincronizado:
```
cd "D:\Portfólio I.A\hopsmind"
.venv\Scripts\activate
git status
git pull origin main
```