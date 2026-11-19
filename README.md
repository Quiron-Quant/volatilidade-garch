<p align="center">
  <img src="assets/quiron-logo-preto.svg#gh-light-mode-only" alt="Quiron" height="100">
  <img src="assets/quiron-logo-branco.svg#gh-dark-mode-only" alt="Quiron" height="100">
</p>

# Uso de modelos ARMA-GARCH para previsão de risco no Ibovespa

Prever diariamente o risco de perdas do Ibovespa e de ações da B3 com modelos GARCH sob diferentes distribuições, compará-los com métodos tradicionais e testar fora da amostra, inclusive em crises como 2020, qual deles mede o risco de forma mais confiável.

## Perguntas de pesquisa

- Assumir que os retornos são normais subestima o risco das ações brasileiras?
- Qual modelo da família ARMA-GARCH prevê melhor o VaR e o Expected Shortfall, quando avaliado só com informação disponível em cada dia?

## Escopo

- **Ativos:** Ibovespa e cerca de 10 ações líquidas da B3 
- **Período:** dados diários de 2010 até a data de corte *(a definir)*
- **Modelos de variância:** GARCH(1,1), GJR-GARCH e EGARCH
- **Distribuições dos erros:** normal, t de Student e t assimétrica
- **Média condicional:** constante ou AR(1), escolhida por AIC/BIC
- **Benchmarks:** VaR histórico (janela de 250 dias) e VaR normal com volatilidade constante
- **Medidas de risco:** VaR e Expected Shortfall a 1% e 5%, horizonte de 1 dia
- **Avaliação:** previsão fora da amostra com janela móvel de 1.000 dias; testes de Kupiec e Christoffersen; subperíodos 2015-16 e Covid (fev. a jun. de 2020)

## Princípios

- **Fora da amostra:** a previsão de cada dia usa apenas dados anteriores a ele.
- **Sem look-ahead:** nenhuma informação do futuro entra no modelo.
- **Código reutilizável:** funções em `src/`, análises em `notebooks/`.
- **Escopo fechado:** ideias novas vão para a lista de próximos passos.

## Ativos
| Ativo| Setor da economia| Obs|
|---|---|---|
| BVSP| Índice |Referẽncia do projeto|
|PETR4 | Petróleo |Choques políticos e do petróleo |
| VALE3 | Mineração | Commodities e China  |
| ITUB4 | Banco privado | Maior banco, vol. baixa  |
| BBDC4 | Banco privado | Par de comparação com o Itaú  |
| BBAS3 | Banco estatal | Risco político  |
|  WEGE3|  Bens de capital| Crescimento estável, defensiva   |
| LREN3 | Varejo | Consumos domésticos, Covid  |
| AXIA3 | Energia e Elétrica | Privatização em 2022, saltos  |
| GGBR4 | Siderurgia | Cíclica, aço e açúcar  |
| EMBR3 | Aeronáutica | Exportadora, quedas em 2020  |


## Estrutura do repositório

```
volatilidade-garch/
├── assets/            # logos e imagens do README
├── data/              # dados baixados (fora do Git)
├── src/
│   ├── data.py        # coleta e limpeza
│   ├── models.py      # ARMA-GARCH
│   ├── rolling.py     # janela móvel
│   ├── risk.py        # VaR e ES
│   └── backtest.py    # Kupiec, Christoffersen
├── notebooks/         # 01_eda, 02_modelos, 03_backtest
├── reports/           # figuras, relatório e slides
├── requirements.txt
└── README.md
```

## Como reproduzir


```bash
git clone https://github.com/Quiron-Quant/volatilidade-garch.git
cd volatilidade-garch
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python teste_download.py
```

## Cronograma

| Fase | Semanas | Entregável |
|---|---|---|
| 0 – Preparação | 0 | Repositório criado, ambiente testado, ativos e período definidos |
| 1 – Dados e EDA | 1–2 | `notebooks/01_eda.ipynb` com figuras e tabela de fatos estilizados |
| 2 – Modelagem ARMA-GARCH | 3–4 | `notebooks/02_modelos.ipynb` e especificações escolhidas |
| 3 – VaR, ES e janela móvel | 5–6 | Previsões fora da amostra de todos os modelos e benchmarks |
| 4 – Backtesting | 7–8 | `notebooks/03_backtest.ipynb` com tabela final e conclusão |
| 5 – Relatório e apresentação | 9–10 | Relatório, repositório público, apresentação e post |


## Equipe

| Nome | Frente | GitHub |
|---|---|---|
| | A – Dados e modelagem | |
| | B – Risco e avaliação | |

<p align="center">
  <img src="assets/logo-usp.webp" alt="Brasão da USP" height="150">
</p>

<p align="center">
  Quiron · Análise Quantitativa de Finanças · ICMC-USP
</p>
