import pandas as pd


data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users.apply(
        lambda x: x["name"][0].upper() + x["name"][1:].lower(),
        axis=1
    )
    # users["name"] = users["name"].apply(
    #     lambda x: x[0].upper() + x[1:].lower()
    # )
    users.sort_values(
        by=["user_id"],
        axis=0, 
        ascending=True,
        inplace=True
    )
    return users