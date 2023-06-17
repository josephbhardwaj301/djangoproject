import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)  # load data into a Dataframe object
print(df)
print(df.loc(0))  # refer to the row index:
print(df.loc[[1, 1]])
