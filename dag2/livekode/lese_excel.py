
import pandas as pd

df = pd.read_excel("netflix.xls")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().mean())
print(df.dtypes)
print(df.shape)
print(df.head(11))
print(df.sort_values(by="release_year",ascending=False))
print(df["date_added"].head(3))
print(df["type"].value_counts().plot(kind="bar",color="pink"))
print(df["release_year"].median())
print(len(df[df["director"] == "Steven Spielberg"]))

movies = df[df["type"] == "Movie"]
shows = df[df["type"] == "TV Show"]
movies.to_excel("netflix_movies.xls")
shows.to_excel("netflix_shows.xls")

