import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(
        by="salary",
        ascending=False,
        inplace=True,
        ignore_index=False
    )
    df = employee.iloc[:, :]
    df.drop_duplicates(
        subset="salary",
        keep="first",
        inplace=True,
        ignore_index=False
    )
    if len(df) >= 2:
        df = df.iloc[1:2, :]
        df.rename(
            columns={"salary": "SecondHighestSalary"},
            index=None,
            inplace=True
        )
        return df[["SecondHighestSalary"]]
    else:
        return pd.DataFrame(
            data={"SecondHighestSalary": [None]},
            index=None
        )