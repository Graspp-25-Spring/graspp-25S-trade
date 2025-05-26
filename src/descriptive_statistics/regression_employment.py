import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

VISUALIZATION_DIR = BASE_DIR / "report" / "visualization"
VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

def regression_employment(df):
    df_regression = df.dropna(subset=["Export", "ILO"]).reset_index()
    model = smf.ols(formula='Q("Export") ~ ILO', data=df_regression).fit()
    print(model.summary())
    plt.figure(figsize=(10,6))
    sns.regplot(
        data=df_regression,
        x="ILO",
        y="Export",
        scatter_kws={"s":50, "alpha":0.7},
        line_kws={"linewidth":2}
    )
    plt.title('Regression of Export on Employment')
    plt.xlabel('Employment')
    plt.ylabel('Export (USD)')
    plt.grid(True)

    # Save figure
    plt.savefig(VISUALIZATION_DIR / "regression_employment.png", dpi=300, bbox_inches='tight')
    
    plt.show()