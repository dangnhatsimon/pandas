import pandas as pd

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = tweets["content"].apply(
        lambda x: len(x) > 15
    )
    return tweets.loc[invalid, :][["tweet_id"]]