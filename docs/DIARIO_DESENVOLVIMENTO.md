# 📔 Diário de Desenvolvimento — hopsmind

Este arquivo documenta a evolução do projeto **hopsmind**, dia a dia, incluindo decisões técnicas, desafios e aprendizados. Serve tanto como registro pessoal quanto como material de apoio para explicar o projeto a recrutadores.

---

## Dia 1 — [PREENCHER DATA] — Fundação do projeto e dados

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

### Próximos passos (retomar aqui)
1. Análise exploratória do dataset final (estatísticas descritivas, distribuições de ABV/IBU/Color por estilo)
2. Possível visualização gráfica dos dados (gráficos de distribuição) — bom material visual para o portfólio
3. Preparação dos dados para Machine Learning (codificação de variáveis categóricas como `Style` e `BrewMethod`)
4. Escolha e treinamento do modelo de geração/recomendação de receitas
5. Avaliação do modelo
6. Integração com IA generativa de imagens para os rótulos
7. Documentação final (README, descrição do projeto, texto para recrutador)

### Comando para retomar de onde paramos
Ao voltar, abra o terminal na pasta do projeto e confirme que está tudo sincronizado:
```
cd "D:\Portfólio I.A\hopsmind"
git status
git pull origin main
```
