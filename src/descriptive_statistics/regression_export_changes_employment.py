# Differ from Wanno's regression, it analyzes the relationship between year-to-year changes in employment
# and total trade volume (Export + Import, as Trade_diff), rather than using absolute values.
# Unlike the previous analysis that examined whether high employment correlates with high exports,
# this approach focuses on whether increases in trade are associated with increases in employment over time.

import seaborn as sns
import matplotlib.pyplot as plt
from src.features.generate_features import GenerateFeatures

def regression_changes_employment(df):
    df['Total_Trade'] = df['Export'] + df['Import']
    df_merge = df.sort_index()

    # Percentage changes

    features_generator = GenerateFeatures(time_period="Y")
    df_features = features_generator.transform(df_merge)
    df_clean = df_features.dropna(subset=['ILO_chpct1Y', 'Total_Trade_chpct1Y'])

    correlation = df_clean['ILO_chpct1Y'].corr(df_clean['Total_Trade_chpct1Y'])
    print("Correlation between percentage change in employment and trade volume:", correlation)

    sns.lmplot(x='Total_Trade_chpct1Y', y='ILO_chpct1Y', data=df_clean, height=6, aspect=1.5)
    plt.title("Regression Analysis of Employment and Trade Volume Changes")
    # Interpretation: When a country's total trade volume increases, its employment tends to increase, on average.
