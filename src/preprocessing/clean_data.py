import ast
import pandas as pd

df = pd.read_csv("data/combined_raw.csv")

#removing rows with missing scores
df = df.dropna(subset=["score"])

#removing invalid scores
df = df[df["score"] > 0]

#removing animes that haven't aired yet
df = df[df["status"] != "Not yet aired"]

#removing duplicate titles
df = df.drop_duplicates(subset=["title"])

#removing whitespace
df["title"] = df["title"].str.strip()
df["status"] = df["status"].str.strip()
df["season"] = df["season"].str.strip()

df["genres"] = df["genres"].apply(ast.literal_eval)

#reset index
df = df.reset_index(drop=True)

df.to_csv("data/combined_clean.csv", index=False)

