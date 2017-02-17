import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import pandas_use


def missing_data():
    dates = pd.date_range('2005-12-31','2014-12-07')
    symbols = ['FAKE2']
    df = pandas_use.get_data(symbols, dates)
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)
    ax = df['FAKE2'].plot(title='SPY rolling mean and others', label='SPY')
    plt.show()