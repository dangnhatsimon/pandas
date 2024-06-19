import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat(
        [df1, df2],
        axis=0,
        join="outer",
        ignore_index=True,
    )
    return df