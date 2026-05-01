import pandas as pd
df=pd.read_csv("gender_submission.csv")
print(df.head())#it prints 1sr top 5 data
print(df.tail())#it prints last  5 data
print(df.shape)