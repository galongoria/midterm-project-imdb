import pandas as pd
import os
import statsmodels.api as sm
from stargazer.stargazer import Stargazer

IN_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUTPUT_DIR = "quantitative analysis"
REVENUE_OLS_PATH = os.path.join(OUTPUT_DIR, "revenue_ols_regression.csv")
IMDB_OLS_PATH = os.path.join(OUTPUT_DIR, "imdb_ols_regression.csv")
METASCORE_OLS_PATH = os.path.join(OUTPUT_DIR, "metascore_ols_regression.csv")
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "decade_analysis.csv")

df = pd.read_csv(IN_PATH)
dummy_cols = df.columns[10:-1]

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


def revenue_ols_regression(out_path):
    '''Perform two OLS regressions of movie Revenue. First on IMBD Rating, Release Year, and genre dummies and then on
    Metascore, Release Year, and genre dummies create csv'''
    
    x_cols1 = ["IMDBRating", "ReleaseYear"]
    for col in dummy_cols:
        x_cols1.append(col)
    
    x_cols2 = ["Metascore", "ReleaseYear"]
    for col in dummy_cols:
        x_cols2.append(col)
        
    x1 = df[x_cols1]
    x2 = df[x_cols2]
    y = df["GrossRevenue"]
    
    model1 = sm.OLS(y, sm.add_constant(x1)).fit()
    model2 = sm.OLS(y, sm.add_constant(x2)).fit()
    
    stargazer = Stargazer([model1, model2])
    open(out_path, 'w').write(stargazer.render_latex())
    
def imdb_ols_regression(out_path):
    '''Perform OLS regression of IMBD Rating on genre dummies and create csv'''
    
    x = df[dummy_cols]
    y = df["IMDBRating"]
    
    model = sm.OLS(y, sm.add_constant(x)).fit()

    stargazer = Stargazer([model])
    open(out_path, 'w').write(stargazer.render_latex())
    
def metascore_ols_regression(out_path):
    '''Perform OLS regression of Metascore on genre dummies and create csv'''
    
    x = df[dummy_cols]
    y = df["Metascore"]
    
    model = sm.OLS(y, sm.add_constant(x)).fit()

    stargazer = Stargazer([model])
    open(out_path, 'w').write(stargazer.render_latex())

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    decade_summary(SUMMARY_PATH)
    revenue_ols_regression(REVENUE_OLS_PATH)
    imdb_ols_regression(IMDB_OLS_PATH)
    metascore_ols_regression(METASCORE_OLS_PATH)