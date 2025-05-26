import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

VISUALIZATION_DIR = BASE_DIR / "report" / "visualization"
VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)


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

    # Save figure
    plt.savefig(VISUALIZATION_DIR / "ilo_employment_heatmap.png", dpi=300, bbox_inches='tight')
    
    plt.show()