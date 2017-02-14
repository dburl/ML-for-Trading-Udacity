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
    ax= df['SPY'].plot(title='SPY rolling mean', label='SPY')
    rm_SPY=pd.rolling_mean(df['SPY'],window=20)
    rm_SPY.plot(label='Rolling mean',ax=ax)
    plt.show()
