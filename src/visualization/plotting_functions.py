import numpy as np
import pandas as pd
import scipy 
import scipy.optimize as opt
import matplotlib.pyplot as plt
import textwrap # Do we really need this? maybe just make a sub title?
import seaborn as sns
import sys
import ipywidgets as widgets
from IPython.display import display

#Importing utility functions from src\features\utility_functions.py

import concurrent.futures
sys.path.append('../src')
import features.utility_functions as util

def plot_ef(er, cov, er2, cov2, xlim=None, ylim=None):
    """
    Plots two multi-asset efficient frontiers on the same graph with optional axis limits.
    """
    # First efficient frontier
    weights = util.optimal_weights(200, er, cov)  # Assuming optimal_weights is implemented
    rets = [util.portfolio_return(w, er) for w in weights]
    vols = [util.portfolio_vol(w, cov) for w in weights]
    ef1 = pd.DataFrame({
        "Returns": rets,
        "Volatility": vols
    })

    # Second efficient frontier
    weights2 = util.optimal_weights(200, er2, cov2)  # Assuming optimal_weights is implemented
    rets2 = [util.portfolio_return(w, er2) for w in weights2]
    vols2 = [util.portfolio_vol(w, cov2) for w in weights2]
    ef2 = pd.DataFrame({
        "Returns": rets2,
        "Volatility": vols2
    })

    # Plotting both efficient frontiers on the same graph
    ax = ef1.plot.line(x="Volatility", y="Returns", style='.-', label='Industry portfolio without cryptocurrencies', color='b', marker='o', markersize=3)
    ef2.plot.line(x="Volatility", y="Returns", style='.-', ax=ax, label='Industry portfolio with cryptocurrencies', color='r', marker='s', markersize=3)

    # Set axis limits if provided
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Customize the plot as needed
    title_text = "Efficient Frontier Comparison"
    plt.title("\n".join(textwrap.wrap(title_text, width=30)), fontsize=15)
    plt.xlabel("Volatility", fontsize=12)
    plt.ylabel("Returns", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.35)

def plot_efficient_frontier_widget(start_date, end_date, ind_crypto):

    from data.config import TICKERS_CRYPTO
    industry_and_crypto = ind_crypto.columns.values.tolist()
    industry = [item for item in industry_and_crypto if item not in TICKERS_CRYPTO]

    ind_crypto_spliced = ind_crypto[start_date:end_date]
    periods_per_year=260
    er = util.annualize_rets(ind_crypto_spliced, periods_per_year)
    cov = ind_crypto_spliced.cov()

    plot = plot_ef(
        er[industry], cov.loc[industry, industry], 
        er[industry_and_crypto], 
        cov.loc[industry_and_crypto, industry_and_crypto],
        #Adjust the plot limits accordingly
        #xlim=(0.0114, 0.015),
        #ylim=(0.055, 0.12)
    )

    plt.show()

