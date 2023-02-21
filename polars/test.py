import time
import pandas as pd
import polars as pl
import numpy as np

# Python decorator that times functions running them multiple times
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        for i in range(10):
            output = func(*args, **kwargs)
        average_time = (time.time() - start) / 10
        print(func.__name__, ":", average_time)
        return output
    return wrapper

@timeit
def read_csv_pandas():
    df = pd.read_csv("https://j.mp/iriscsv")
    df.sample(3)
    return df

@timeit
def read_csv_polars():
    df = pl.read_csv("https://j.mp/iriscsv")
    df.sample(3)
    return df

@timeit
def filter_pandas(df):
    df[df["sepal_length"] > 5].groupby("species", sort=False, as_index=False).agg(lambda x: x.all().sum())

@timeit
def filter_polars(df):
    df.filter(pl.col("sepal_length") > 5).groupby("species", maintain_order=True).agg(pl.all().sum())

@timeit
def filter_polars_lazy(df):
    df.lazy().filter(pl.col("sepal_length") > 5).groupby("species", maintain_order=True).agg(pl.all().sum()).collect()


@timeit
def filter_big_pandas(df):
    df[df["col1"] > 50].groupby("col3", sort=False, as_index=False).agg(lambda x: x.all().sum())

@timeit
def filter_big_polars(df):
    df.filter(pl.col("col1") > 0).groupby("col3", maintain_order=True).agg(pl.all().sum())

@timeit
def filter_big_polars_lazy(df):
    df.lazy().filter(pl.col("col1") > 50).groupby("col3", maintain_order=True).agg(pl.all().sum()).collect()


@timeit
def join_pandas(df, df2):
    df.join(df2.set_index("x"), on="a")

@timeit
def join_polars(df, df2):
    df.join(df2, left_on="a", right_on="x")

@timeit
def join_polars_lazy(df, df2):
    df.lazy().join(df2.lazy(), left_on="a", right_on="x").collect()

if __name__ == "__main__":

    # print('\n\nReading a CSV file:')
    # df_pd = read_csv_pandas()
    # df_pl = read_csv_polars()

    # print('\n\nFiltering a (smol) DataFrame:')
    # filter_pandas(df_pd)
    # filter_polars(df_pl)
    # filter_polars_lazy(df_pl)

    # print('\n\nFiltering a (big) DataFrame:')
    # BIGNESS: int = 100000000
    # data = {
    #     'col1': np.random.randint(0, 100, size=BIGNESS),
    #     'col2': np.random.randn(BIGNESS),
    #     'col3': np.random.choice(['a', 'b', 'c', 'd', 'e', 'f'], size=BIGNESS),
    #     'col4': np.random.choice([True, False], size=BIGNESS),
    # }

    # df = pd.DataFrame(data)
    # filter_big_pandas(df)

    # df = pl.DataFrame(data)
    # filter_big_polars(df)
    # filter_big_polars_lazy(df)


    print('\n\nJoining two DataFrames:')
    BIGNESS: int = 10000
    raw_1 = {
                'a': np.random.choice(['a', 'b'], size=BIGNESS),
                'col1': np.random.randint(0, 100, size=BIGNESS),
                'col2': np.random.randn(BIGNESS),
            }
    raw_2 = {
                'x': np.random.choice(['a', 'b'], size=BIGNESS),
                'col4': np.random.choice([True, False], size=BIGNESS),
            }

    df_1 = pd.DataFrame(raw_1)
    df_2 = pd.DataFrame(raw_2)
    join_pandas(df_1, df_2)

    df_1 = pl.DataFrame(raw_1)
    df_2 = pl.DataFrame(raw_2)
    join_polars(df_1, df_2)
    join_polars_lazy(df_1, df_2)


