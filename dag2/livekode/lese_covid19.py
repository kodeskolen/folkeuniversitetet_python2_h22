import pandas as pd
import statistics  as sts

df = pd.read_csv("covid-19.csv")
print(df.head())



print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.shape)

print(df[df["Deaths1Mpop"] == df["Deaths1Mpop"].max()])

print(df["TotalCases"].sum())

print(df["TotalCases"].median())

print(df["TotalCases"].mean())

population_first = df.sort_values(by="Population", ascending=False)
print(population_first.head(1))
population_first[["TotalCases", "TotalDeaths"]].head(1).plot(kind="bar")