import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.loc[animals["weight"]>100, :]
    df.sort_values(
        by=["weight"],
        axis=0,
        ascending=False,
        inplace=True
    )
    return df[["name"]]