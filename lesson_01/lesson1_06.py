import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_use

def compute_daily_return(df):
    daily_returns=df.copy;
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns


def plot_histogram():
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY','XOM']
    df = pandas_use.get_data(symbols, dates)
    daily_returns=compute_daily_return(df)
    #   daily_returns.plot(label='Daily return')
    if False:
        daily_returns.hist(bins=20)
    else:
        daily_returns['SPY'].hist(bins=20, label='SPY')
        daily_returns['XOM'].hist(bins=20, label='XOM')

    mean = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    plt.axvline(mean, color='w', linestyle='dashed',linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    print(daily_returns.kurtosis())
    plt.show()


def plot_scatter():
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = pandas_use.get_data(symbols, dates)
    daily_returns = compute_daily_return(df)
    daily_returns.plot(kind='scatter',x='SPY',y='XOM')
    beta_XOM, alpha_XOM= np.polyfit(daily_returns['SPY'],daily_returns['XOM'],1)
    plt.plot(daily_returns['SPY'],beta_XOM*daily_returns['SPY']+alpha_XOM,'-',color='r')
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    plt.show()
    print( daily_returns.corr(method='pearson'))

