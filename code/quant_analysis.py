import pandas as pd
import os
import statsmodels.api as sm

IN_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUTPUT_DIR = "quantitative analysis"
OLS_PATH = os.path.join(OUTPUT_DIR, "ols_regression.csv")
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "decade_analysis.csv")

df = pd.read_csv(IN_PATH)

def decade_summary(out_path):
    '''Convert summary statistics for each decade to csv'''

    '''Find the minimum and maximum release years to divide data into decades'''
    
    year = df["ReleaseYear"]
    print(year.min())
    print(year.max())

    '''Divide data into decades'''

    df_1930 = df[(year//10)*10 == 1930]
    df_1940 = df[(year//10)*10 == 1940]
    df_1950 = df[(year//10)*10 == 1950]
    df_1960 = df[(year//10)*10 == 1960]
    df_1970 = df[(year//10)*10 == 1970]
    df_1980 = df[(year//10)*10 == 1980]
    df_1990 = df[(year//10)*10 == 1990]
    df_2000 = df[(year//10)*10 == 2000]
    df_2010 = df[(year//10)*10 == 2010]
    df_2020 = df[(year//10)*10 == 2020]

    '''Create csv for summary statistics by decade'''
    
    df_1930.describe().to_csv(out_path)
    df_1940.describe().to_csv(out_path, mode ="a")
    df_1950.describe().to_csv(out_path, mode ="a")
    df_1960.describe().to_csv(out_path, mode ="a")
    df_1970.describe().to_csv(out_path, mode ="a")
    df_1980.describe().to_csv(out_path, mode ="a")
    df_1990.describe().to_csv(out_path, mode ="a")
    df_2000.describe().to_csv(out_path, mode ="a")
    df_2010.describe().to_csv(out_path, mode ="a")
    df_2020.describe().to_csv(out_path, mode ="a")

def ols_regression(out_path):
    '''Perform OLS regression of movie revenue by IMBD score and create csv of results'''

    revenue = df["GrossRevenue"]
    imdb_score = df["IMDBRating"]
    imdb_score_model = sm.OLS(revenue, sm.add_constant(imdb_score))
    imdb_score_fit = imdb_score_model.fit()
    imdb_score_summary = imdb_score_fit.summary()


    imdb_score_as_html = imdb_score_summary.tables[1].as_html()
    pd.read_html(imdb_score_as_html, header=0, index_col=0)[0].to_csv(out_path)

    '''Perform OLS regression of movie revenue by Metascore score and create csv of results'''
    metascore= df["Metascore"]
    metascore_model = sm.OLS(revenue, sm.add_constant(metascore))
    metascore_fit = metascore_model.fit()
    metascore_summary = metascore_fit.summary()

    metascore_as_html = metascore_summary.tables[1].as_html()
    pd.read_html(metascore_as_html, header=0, index_col=0)[0].to_csv(out_path, mode="a", header=False)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    decade_summary(SUMMARY_PATH)
    ols_regression(OLS_PATH)