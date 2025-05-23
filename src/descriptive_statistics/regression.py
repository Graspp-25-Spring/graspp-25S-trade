import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf


def regression(df):
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
    plt.show()