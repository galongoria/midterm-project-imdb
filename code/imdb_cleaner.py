import pandas as pd
import os

# Constants
IN_FILE_PATH = os.path.join("data", "raw", "imdb_scraped.csv")
OUT_FILE = "imdb_clean.csv"
OUT_DIR = os.path.join("data", "clean")
OUT_PATH = os.path.join(OUT_DIR, OUT_FILE)

# Function
def read_and_clean_imdb(path):
    """Function accepts the raw, scraped IMDB data file and cleans it up for use in analysis"""

    data = (
        pd.read_csv(IN_FILE_PATH)
        .assign(
            ReleaseYear=lambda df_: df_["ReleaseYear"]
            .str.extract("(\d+)", expand=False)
            .astype(int),
            Runtime=lambda df_: df_["Runtime"]
            .str.extract("(\d+)", expand=False)
            .astype(int),
            GrossRevenue=lambda df_: df_["GrossRevenue"]
            .str.lstrip("$")
            .str.rstrip("M")
            .astype(float),
            Metascore=lambda df_: df_["Metascore"]
            .str.strip()
            .str.rstrip("Metascore")
            .str.strip()
            .astype(int),
            Genres=lambda df_: df_["Genres"].str.strip(),
            Description=lambda df_: df_["Description"].str.strip(),
            Votes=lambda df_: df_["Votes"].str.replace(",", "").astype(int),
        )
        .drop_duplicates(subset=["Title", "ReleaseYear", "Runtime"])
        .sort_values(by="GrossRevenue", ascending=False)
        .drop(columns=["genre_pull"])
    )

    return data



def dummy_cols(data):
        dummies = data["Genres"].str.get_dummies(sep=', ')
        data = pd.concat([data, dummies], axis = 1) 
        return data


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    clean_data = read_and_clean_imdb(IN_FILE_PATH)
    clean_data_dummies = dummy_cols(clean_data)
    clean_data_dummies.to_csv(OUT_PATH, index=False)
