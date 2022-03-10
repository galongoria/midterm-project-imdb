import pandas as pd
import os

# Constants
IN_FILE_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUT_FILE = "imdb_one_genre.csv"
OUT_DIR = os.path.join("data", "clean")
OUT_PATH = os.path.join(OUT_DIR, OUT_FILE)


def one_genre(path):
    df = pd.read_csv(path)
    df[["Genre", "rest"]] = df["Genres"].str.split(",", n=1, expand=True)
    df = df.drop(["Genres", "rest"], axis=1)
    return df


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    cleaned_genre = one_genre(IN_FILE_PATH)
    cleaned_genre.to_csv(OUT_PATH, index=False)
