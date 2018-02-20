import pandas as pd

df = pd.read_csv("hn_stories.csv")

df.columns = ["submission_time", "upvotes", "url", "headline"]
print(df.columns)

def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ["submission_time", "upvotes", "url", "headline"]
    return df

