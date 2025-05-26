### Binder for the first milestone

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Gericko/graspp-25S-trade/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fmilestone_1.ipynb)


### Collaborators
- Quentin Hillebrand
- Gerwin He
- Hanako Nakamura
- Wanonno Iqtyider
- Tue Lan Le
- Yijing Lian
- Angie Henon
- Natsuki Konishi

### Research Question
Does an increase in trade openness, measured by total trade volume and tariff levels, lead to a decline in secondary sector (manufacturing and construction) employment? 

### Thesis Statement
This study investigates whether greater trade openness, reflected by rising total trade volumes and falling tariff rates, contributes to a decline in industrial employment. By conducting separate regression analyses for OECD and developing countries, the research aims to identify differences in how trade dynamics influence industrial sectors across different economic contexts. Using cross-country panel data and variations in tariff levels over time, the study focuses on a few case studies:
1. comparison between developed and developing countries
2. change in shock periods like US-China trade war

### Hypothesis
We hypothesize that greater trade openness, characterized by higher total trade volumes and lower tariff rates, is associated with a decline in industrial employment. Specifically, we expect that during trade-friendly periods (with lower tariffs and higher trade flows), industrial sectors experience more employment reduction compared to trade-unfriendly periods (with higher tariffs and restricted trade flows). Furthermore, we anticipate that this effect will be more pronounced in developing countries than in OECD countries, reflecting differences in industrial resilience and economic structures.

### Analysis Methods 
We visualized trends over time and examined the relationship between employment levels and export values through regression analysis. In addition, time series analyses are performed separately for each country, including correlation analysis, rolling correlation windows, stationarity tests (ADF test), and simple regressions of exports on employment.

### Data Source
- ILO Data: https://rshiny.ilo.org/dataexplorer16/?id=EMP_TEMP_ECO_OCU_NB_A&timefrom=2014&timeto=2024
- OECD Data on annual labor force: https://data-explorer.oecd.org/vis?fs[0]=T%2Co&pg=0&fc=Topic&bp=true&snb=68&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_ALFS%2540DF_SUMTAB&df[ag]=OECD.SDD.TPS&df[vs]=1.0&dq=........A&pd=%2C&to[TIME_PERIOD]=false&vw=ov

### Task Table
| Name               | Work Under Progress              | Work Done           |
|:------------------|:------------------|:---------------|
| Quentin Hillebrand |                                  |                     |
| Gerwin He          | Cleaning up the milestone folder: taking the code for descriptive statistics into separate py files and importing them back into the milestone folder  | cleaning up and importing, created in src a new folder with py code for descriptive statistics |
| Hanako Nakamura    |                                  |                     |
| Wanonno Iqtyider   |                                  |                     |
| Tue Lan Le         |                                  |      identifying outliers in industry employment to find potential case study candidates               |
| Yijing Lian        | Case study on US-China trade war | 1. Mapping employment by country and year,<br>2. Regression and Histogram on pct. change of employment and trade|
| Angie Henon        |                                  |                     |
| Natsuki Konishi    |                                  |                     |