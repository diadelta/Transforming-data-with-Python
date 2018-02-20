import read

df = read.load_data()

headlines = df["headline"]
s = ""
for hd in headlines:
    s += str(hd).lower() + " "
s = s.split()

from collections import Counter 
c = Counter()
for w in s:
    c[w] += 1
most_100 = c.most_common(100)
print(most_100)
