import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

VISUALIZATION_DIR = BASE_DIR / "report" / "visualization"
VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

def scatterplot (df):
    g = sns.PairGrid(df)
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
 

    # Save figure
    plt.savefig(VISUALIZATION_DIR / "scatterplot.png", dpi=300, bbox_inches='tight')
    
    plt.show()