import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    drop_missing_students = students.dropna(
        axis=0, 
        how='any', 
        subset=['name'], 
        inplace=False, 
        ignore_index=False
    )
    return drop_missing_students