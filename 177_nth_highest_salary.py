import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee_sorted = employee.sort_values(
        by="salary",
        ascending=False, 
        inplace=False,
        ignore_index=False,
        na_position="last"
    )
    employee_sorted.drop_duplicates(
            subset="salary",
            keep="first",
            inplace=True,
            ignore_index=False
        )
    if N <= len(employee_sorted) and N>0:
        df = employee_sorted.iloc[N-1:N,:]
        df.rename(
            columns={"salary": f"getNthHighestSalary({N})"},
            index=None,
            inplace=True
        )
        return df[[f"getNthHighestSalary({N})"]]
    else:
        return pd.DataFrame(
            {f"getNthHighestSalary({N})": [None]}
        )