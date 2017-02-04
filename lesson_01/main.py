def plotting():
    pd.test()
    print("Executed")


def test_run():
    df = pd.read_csv("data/AAPL.csv")
#    print(df.head())
#    print(df)
    print(df.tail(5))


if __name__ == "__main__":
    import pandas as pd
    #plotting()
    test_run()