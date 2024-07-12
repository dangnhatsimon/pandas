import pandas as pd
import re

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r"\w*\b(DIAB1)[\w\b]*"
    df = patients.loc[
        patients["conditions"].apply(
            lambda x: True if re.search(pattern, x) else False
        ),
        :
    ]
    return df