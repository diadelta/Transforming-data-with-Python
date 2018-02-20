from dateutil.parser import parse
import datetime
import read

df = read.load_data()

def trans(st):
    date = parse(str(st))
    return date.hour

df["submission_hours"] = df["submission_time"].apply(trans)

counts = df["submission_hours"].value_counts()

print(counts)
