import pandas as pd

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        department,
        how="inner",
        left_on="departmentId",
        right_on="id",
        suffixes=('_employee', '_department')
    )
    highest_salary = df.groupby(
        by="departmentId",
        as_index=True
    )["salary"].transform("max")
    highest_salary_by_dep = df.loc[df["salary"] == highest_salary, :]
    highest_salary_by_dep.rename(
        columns={
            "salary": "Salary",
            "name_department": "Department",
            "name_employee": "Employee"
        },
        inplace=True,
        errors='ignore'
    )
    return highest_salary_by_dep[["Department", "Employee", "Salary"]]