import pandas as pd
df=pd.read_json('https://gist.githubusercontent.com/josephbhardwaj301/baa37fa6100fbcb8f10779cb77d1be6d/raw/cd8a7f113273feef71c52544e25f4ad4e69be0de/data.json')
print(df.head(100))
print(df.tail())
print(df.info())
