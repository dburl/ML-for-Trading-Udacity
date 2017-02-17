import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import pandas_use


# 2) NumPy use
def test_run():
    #    print(np.array([(2,3,4),(5,6,7)]))
    #    print(np.zeros((4, 6), dtype=np.int_))
    #   print(np.random.normal(50,10,size=(2,3)))
    a = (np.random.randint(0,10,size=(2,3)))
    print(np.random.randint(0, 10, size=(6)))
    print(a.size)
    print(a.shape)
    print(a.sum())
    print(a.max(axis=1))


def time_check():
    t1= time.time()
    print("Time check")
    t2= time.time()
    print("Time spent:", t2-t1)
    # More complex operation
    nd1 = np.random.random((1000,1000))
    print(nd1.mean())
    t3=time.time()
    print("Time spent:", t3 - t2)


def rolling_mean():
    dates = pd.date_range('2012-01-01','2012-12-31')
    symbols = ['SPY']
    df = pandas_use.get_data(symbols, dates)
    ax = df['SPY'].plot(title='SPY rolling mean and others', label='SPY')
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    rm_SPY.plot(label='Rolling mean', ax=ax)
    rstd_SPY = pd.rolling_std(df['SPY'], window=20)

    bbmax_SPY = rm_SPY+2*rstd_SPY
    bbmax_SPY.plot(label='Bollinger Band max', ax=ax)
    bbmin_SPY = rm_SPY - 2*rstd_SPY
    bbmin_SPY.plot(label='Bollinger Band min', ax=ax)

    rmax_SPY = pd.rolling_max(df['SPY'], window=20)
    rmax_SPY.plot(label='Rolling max', ax=ax)
    rmin_SPY = pd.rolling_min(df['SPY'], window=20)
    rmin_SPY.plot(label='Rolling min', ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def daily_return():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM']
    df = pandas_use.get_data(symbols, dates)
    daily_return = (df / df.shift(1)) - 1
    daily_return.ix[0, :] = 0
    daily_return.plot(label='Daily return')
    print(daily_return)
    plt.show()
