import seaborn as sns


def scatterplot (df):
    g = sns.PairGrid(df)
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
 