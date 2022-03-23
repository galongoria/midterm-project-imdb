import pandas as pd
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt

IN_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUTPUT_DIR = "quantitative analysis"
REVENUE_IMDB_OLS_PATH = os.path.join(OUTPUT_DIR, "revenue_imdb_ols_regression.png")
REVENUE_META_OLS_PATH = os.path.join(OUTPUT_DIR, "revenue_meta_ols_regression.png")
IMDB_OLS_PATH = os.path.join(OUTPUT_DIR, "imdb_ols_regression.png")
METASCORE_OLS_PATH = os.path.join(OUTPUT_DIR, "metascore_ols_regression.png")
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "decade_analysis.csv")

df = pd.read_csv(IN_PATH)
dummy_cols = df.columns[10:-1]


def decade_summary(out_path):
    """Group data by decade and convert summary statistics to csv"""

    (
        df.assign(Decade=lambda df: (df["ReleaseYear"] // 10) * 10)
        .drop("ReleaseYear", axis=1)
        .groupby("Decade")
        .describe()
        .round(decimals=2)
        .to_csv(SUMMARY_PATH)
    )


def revenue_imdb_ols_regression(out_path):
    """Perform OLS regression of movie Revenue on IMBD Rating and genre dummies, and create png"""

    x_cols = ["IMDBRating"]
    for col in dummy_cols:
        x_cols.append(col)

    x = df[x_cols]
    y = df["GrossRevenue"]

    model = sm.OLS(y, sm.add_constant(x)).fit()
    model_summary = model.summary()

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.text(
        0.01, 0.05, str(model_summary), {"fontsize": 10}, fontproperties="monospace"
    )
    ax.axis("off")
    plt.tight_layout()
    fig.savefig(out_path)


def revenue_meta_ols_regression(out_path):
    """Perform OLS regression of movie Revenue on Metascore and genre dummies, and create png"""

    x_cols = ["Metascore"]
    for col in dummy_cols:
        x_cols.append(col)

    x = df[x_cols]
    y = df["GrossRevenue"]

    model = sm.OLS(y, sm.add_constant(x)).fit()
    model_summary = model.summary()

    fig1, ax1 = plt.subplots(figsize=(12, 7))

    ax1.text(
        0.01, 0.05, str(model_summary), {"fontsize": 10}, fontproperties="monospace"
    )
    ax1.axis("off")
    plt.tight_layout()
    fig1.savefig(out_path)


def imdb_ols_regression(out_path):
    """Perform OLS regression of IMBD Rating on genre dummies and create png"""

    x = df[dummy_cols]
    y = df["IMDBRating"]

    model = sm.OLS(y, sm.add_constant(x)).fit()
    model_summary = model.summary()

    fig2, ax2 = plt.subplots(figsize=(12, 7))

    ax2.text(
        0.01, 0.05, str(model_summary), {"fontsize": 10}, fontproperties="monospace"
    )
    ax2.axis("off")
    plt.tight_layout()
    fig2.savefig(out_path)


def metascore_ols_regression(out_path):
    """Perform OLS regression of Metascore on genre dummies and create png"""

    x = df[dummy_cols]
    y = df["Metascore"]

    model = sm.OLS(y, sm.add_constant(x)).fit()
    model_summary = model.summary()

    fig3, ax3 = plt.subplots(figsize=(12, 7))

    ax3.text(
        0.01, 0.05, str(model_summary), {"fontsize": 10}, fontproperties="monospace"
    )
    ax3.axis("off")
    plt.tight_layout()
    fig3.savefig(out_path)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    decade_summary(SUMMARY_PATH)
    revenue_imdb_ols_regression(REVENUE_IMDB_OLS_PATH)
    revenue_meta_ols_regression(REVENUE_META_OLS_PATH)
    imdb_ols_regression(IMDB_OLS_PATH)
    metascore_ols_regression(METASCORE_OLS_PATH)
