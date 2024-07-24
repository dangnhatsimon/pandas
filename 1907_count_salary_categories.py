import pandas as pd

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts["income"]<20000])
    average = len(accounts[(accounts["income"]>=20000) & (accounts["income"]<=50000)])
    high = len(accounts[accounts["income"]>50000])
    return pd.DataFrame(
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [low, average, high]
        }
    )