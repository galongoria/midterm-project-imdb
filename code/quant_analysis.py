import pandas as pd
import os
import statsmodels.api as sm

IN_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUTPUT_DIR = "quantitative analysis"
OLS_PATH = os.path.join(OUTPUT_DIR, "ols_regression.csv")
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "decade_analysis.csv")

df = pd.read_csv(IN_PATH)

def decade_summary(out_path):
    '''Group data by decade and convert summary statistics to csv'''   
    
    (
    df.assign(Decade=lambda df: (df["ReleaseYear"]//10)*10)
    .drop("ReleaseYear", axis=1)
    .groupby("Decade")
    .describe()
    .round(decimals=2)
    .to_csv(SUMMARY_PATH)
    )


def ols_regression(out_path):
    '''Perform OLS regression of movie revenue by IMBD score, Metascore, and Release Year and create csv'''

    x = df[["IMDBRating", "Metascore", "ReleaseYear"]]
    y = df["GrossRevenue"]
    model = sm.OLS(y, sm.add_constant(x))
    model_fit = model.fit()
    model_fit_summary = model_fit.summary()

    model_as_html = model_fit_summary.tables[1].as_html()
    pd.read_html(model_as_html, header=0, index_col=0)[0].to_csv(OLS_PATH)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    decade_summary(SUMMARY_PATH)
    ols_regression(OLS_PATH)