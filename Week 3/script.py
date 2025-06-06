import pandas as pd

df_in = pd.read_csv("innie.csv")
print(df_in.head())

df_out = pd.read_csv("../outtie.csv")
print(df_out.head())

df_in = pd.read_csv("../Week_2/innie2.csv")