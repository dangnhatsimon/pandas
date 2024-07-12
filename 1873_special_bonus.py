import pandas as pd

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees.loc[(employees["employee_id"] % 2 != 0) & (~employees["name"].str.startswith("M")), :]["salary"]  
    employees.fillna(
        value={"bonus": 0},
        axis=0,
        inplace=True
    )
    employees.sort_values(
        by="employee_id", 
        axis=0, 
        ascending=True, 
        inplace=True,
        ignore_index=False
    )
    return employees[["employee_id", "bonus"]]