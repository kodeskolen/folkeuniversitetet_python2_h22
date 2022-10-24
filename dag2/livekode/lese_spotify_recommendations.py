
import pandas as pd


dataframe = pd.read_csv("recommendations.csv")

print(dataframe)

print(dataframe.head(5))
print(dataframe.describe())
print(dataframe.mean())

print(dataframe["popularity"].mean())

#sortert_data = dataframe.sort_values(by="manhattan_dist", ascending=False)

#print(sortert_data["track_name"].head(1))

print(dataframe[dataframe["popularity"] == dataframe["popularity"].max()]["track_name"])

print(dataframe[dataframe["artist_name"] == "Taylor Swift"]["track_name"])

dataframe["popularity"].plot(kind="bar")

dataframe = dataframe[dataframe["popularity"] > 50]

dataframe.to_excel("recommendations.xls")