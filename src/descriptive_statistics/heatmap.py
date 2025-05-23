import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def heatmap(df):
    df_heatmap = df['ILO'].unstack(level=0)
    df_heatmap = df_heatmap.sort_index(ascending=False)

    # Sort countries (columns) by average employment (low → high)
    avg_employment = df_heatmap.mean(axis=0)
    df_heatmap = df_heatmap[avg_employment.sort_values().index]

    # Plot
    plt.figure(figsize=(20, 10))
    sns.heatmap(np.log1p(df_heatmap), cmap='viridis', linewidths=0.1)
    plt.title("ILO Employment Heatmap (Countries Sorted by Avg Employment)")
    plt.xlabel("Country (Sorted by Avg Employment)")
    plt.ylabel("Year (Recent at Top)")
    plt.show()