import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    dedup_customers = customers.drop_duplicates(
        subset=['email'], 
        keep='first', 
        inplace=False, 
        ignore_index=False
    )
    return dedup_customers
    