import pandas as pd
import re

data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[a-zA-Z][\w\d\_\.\-]*(@leetcode\.com)$"
    df = users.loc[
        users["mail"].apply(
            lambda x: True if re.search(pattern, x) else False
        ),
        :
    ]
    return df