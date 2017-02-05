import pandas as pd
import matplotlib.pyplot as plt
import os

# 1) Pandas use
def unit_test():
    pd.test()
    print("Unit test executed")


def test_plot():
    df = pd.read_csv("data/AAPL.csv")
    print(df.head())
    df[['Close','Adj Close']].plot()
    plt.show()


def get_max_close(symbol):
        df=pd.read_csv("data/{}.csv".format(symbol))
        return df['Close'].max()


def get_mean_volume(symbol):
    df= pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()


def stat_data():
    for symbol in ['AAPL', 'ABC']:
        print("Max close for " + symbol)
        print(symbol, get_max_close(symbol))
        print("Mean Vol for " + symbol)
        print(symbol, get_mean_volume(symbol))


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir,'{}.csv'.format(str(symbol)))


def get_data(symbols, dates):
    df1 = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                               parse_dates=True, usecols=['Date', 'Adj Close'],
                               na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)
        if symbol == 'SPY':
            df1=df1.dropna(subset=["SPY"])
    return df1


def df_join():
    dates = pd.date_range('2010-01-01', '2010-12-31')
    symbols = ['SPY', 'GOOG', 'IBM', 'GLD']
    df = get_data(symbols, dates)
#    df2=df.ix['2010-01-01':'2010-01-31']
#    print(df2)
#    print(df2[['GOOG','GLD']])
#    print(df.ix['2010-01-01':'2010-01-31', ['SPY', 'IBM']])
    return df


def plot_data(df, title="Stock prices"):
    df= df/df.ix[0]
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel("Data")
    ax.set_ylabel("Price")
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    df2=df.ix[start_index:end_index,columns]
    df2.plot()
    plt.show()
