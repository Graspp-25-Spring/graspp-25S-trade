import matplotlib.pyplot as plt
import numpy as np




# Plot histogram for percentage change in employment
# I use log for pct change in employment to reduce the effect of extreme values as the distribution without log was heavily right-skewed

def histogram_pct_change_employment_trade(df):
    
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(np.log1p(df['ILO_chpct1Y']), bins=50, color='skyblue')
    plt.title("Histogram of log(1 + Employment % Change)")
    plt.xlabel("log(1 + ILO_chpct1Y)")
    plt.ylabel("Frequency")

    # Plot histogram for percentage change in trade
    plt.subplot(1, 2, 2)
    plt.hist(df['Total_Trade_chpct1Y'], bins=50, color='salmon')
    plt.title("Histogram of Trade % Change")
    plt.xlabel("Total_Trade_chpct1Y")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()