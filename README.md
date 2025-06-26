### Binder for the first milestone
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Gericko/graspp-25S-trade/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fmilestone_1.ipynb)


### Collaborators
- Gerwin He 
- Hanako Nakamura
- Wanonno Iqtyider
- Natsuki Konishi

(Quentin Hillebrand, Tue Lan Le, Yijing Lian, Angie Henon) 

### Research Question
- Does an increase in trade openness, measured by total trade volume, lead to a decline in secondary sector employment (manufacturing and construction)?
- How does this relationship vary with a country’s level of economic development?

### Thesis Statement/Results
Time series analyses and scatter plots reveal that the relationship between trade and employment is highly context-dependent. In developed economies such as the United States and Japan, employment in industrial sectors shows little to no consistent correlation with trade growth. In some cases, employment even declines as trade expands, pointing to structural changes such as automation, demographic shifts, and capital-intensive industrial transitions. Germany, in contrast, demonstrates a more aligned pattern, with employment broadly tracking trade trends, likely reflecting stronger labor protections and manufacturing resilience.

In contrast, emerging economies such as India and Vietnam show a more positive association between trade expansion and employment growth. Vietnam, in particular, illustrates a tightly coupled relationship across exports, imports, and job creation, consistent with its export-led industrialization strategy. India exhibits more volatility but still displays an overall upward trend in both trade and employment.
Regression analysis confirms that there is a moderate positive relationship between trade growth and employment growth across the panel, though it is far from uniform or deterministic. While higher trade volumes and year-over-year increases are associated with employment gains, the effects are neither linear nor universally strong. This indicates that trade is a contributing factor, but not the sole driver, of employment outcomes.

### Hypothesis
Based on existing research, we hypothesize that greater trade openness, characterized by higher total trade volumes and lower tariff rates, is associated with a decline in industrial employment. Specifically, we expect that during trade-friendly periods (with lower tariffs and higher trade flows), industrial sectors experience more employment reduction compared to trade-unfriendly periods (with higher tariffs and restricted trade flows). Furthermore, we anticipate that this effect will be more pronounced in developing countries than in OECD countries, reflecting differences in industrial resilience and economic structures.

### Analysis Methods 
This study investigates whether greater trade openness, reflected by rising total trade volumes, contributes to a decline in industrial employment. By conducting separate regression analyses for OECD and developing countries, the research aims to identify differences in how trade dynamics influence industrial sectors across different economic contexts. Using cross-country panel data and variations in tariff levels over time, the study focuses on a few case studies:
    
    1. Comparison between developed and developing countries
    2. Change in shock periods like US-China trade war

We visualized trends over time and examined the relationship between employment levels and export values through regression analysis. In addition, time series analyses are performed separately for each country, including correlation analysis, rolling correlation windows, stationarity tests (ADF test), and simple regressions of exports on employment.

### Data Source
- To conduct our research and to examine our hypothesis, we chose three datasets from the OECD, the ILO, and from COMTRADE.

OECD: https://data-explorer.oecd.org/vis?fs%5b0%5d=T%2Co&pg=0&fc=Topic&bp=true&snb=68&df%5bds%5d=dsDisseminateFinalDMZ&df%5bid%5d=DSD_ALFS%2540DF_SUMTAB&df%5bag%5d=OECD.SDD.TPS&df%5bvs%5d=1.0&dq=........A&pd=%2C&to%5bTIME_PERIOD%5d=false&vw=ov

ILO: https://rshiny.ilo.org/dataexplorer16/?id=EMP_TEMP_ECO_OCU_NB_A&timefrom=2014&timeto=2024

COMTRADE: https://comtradeplus.un.org/TradeFlow

We chose to work with the OECD ALFS summary tables dataset, which is a subset of the Annual Labor Force Statistics database and shows annual labor statistics for OECD member states. This longitudinal dataset tracks employment data over nearly 70 years, from which we have additionally singled out employment rate and type of employment to explore manufacturing-specific employment rates over time.
From the ILO, we used the ILOSTAT data explorer to download employment data specific to the industrial sector. This dataset provides annual employment numbers from 2014 to 2020 by industry classification and occupational group, allowing for a more detailed breakdown of recent developments than the OECD dataset.

By combining both datasets, we attempted to build a broad view on manufacturing employment trends. The OECD data offered a historical baseline from 1955 onward, whereas the ILO provided insights into sector-specific employment rates with more current data.
Regarding trade openness, we used a dataset from the UN Comtrade Database to reflect annual trade data from 1988 to 2025. We specifically extracted both export and import trade volumes in commodities for all available reporting countries. Combining this with the previous employment datasets, we seek to analyze whether greater trade openness, reflected by rising total trade volumes and falling tariff rates, contributes to a decline in industrial employment.

### Task Table
[Main Members]       

[Gerwin He]  
Establishing the research question, giving an overview of the literature to explain how we got interested in our research question, deriving our hypotheses from the research question.                                 

[Hanako Nakamura]
Designed and produced additional visualizations to support our analysis, including time series plots and histograms. These plots were used to explore trends over time and the distribution of key variables, enriching the empirical grounding of our findings.

[Wanonno Iqtyider]
Estimated the main regression models to test our hypotheses, using statistical methods suited to our data structure. Additionally contributed optional case study insights and prepared a robustness check using supplementary text analysis, adding qualitative depth to our otherwise quantitative approach.

[Natsuki Konishi] 
Conducted the descriptive statistical analysis by summarizing key characteristics of the dataset, including the number of countries and years observed, as well as the minimum, maximum, and mean values of core variables. Created scatter plots to visualize key relationships of interest, helping to identify potential correlations and patterns relevant to our hypotheses

[Sub Members]  
| Tue Lan Le         |                             
| Yijing Lian        |                      
| Angie Henon        |                                  
| Quentin Hillebrand |                                 