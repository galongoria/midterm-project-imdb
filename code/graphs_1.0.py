import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
IN_FILE_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUT_DIR = "figures"


# Functions
def save_plot(figure_obj, output_directory, output_file_name):
    """Function takes in a figure, the output directory and file name and saves the figure"""
    path = os.path.join(output_directory, output_file_name)
    figure_obj.savefig(path)


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    df = pd.read_csv(IN_FILE_PATH)

    # First Plot
    plot1 = (
        df.groupby("Title")["GrossRevenue"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot1.figure, OUT_DIR, "Figure1.png")

    # Second Plot
    plot2 = (
        df.groupby("Title")["IMDBRating"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot2.figure, OUT_DIR, "Figure2.png")

    # Third Plot
    plot3 = (
        df.groupby("Title")["Metascore"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot3.figure, OUT_DIR, "Figure3.png")

    # Fourth Plot
    plot4 = plt.figure(figsize=(20, 10))
    plot4 = sns.scatterplot(data=df, x="IMDBRating", y="GrossRevenue")
    save_plot(plot4.figure, OUT_DIR, "Figure4.png")

    # Fifth Plot
    plot5 = plt.figure(figsize=(20, 10))
    plot5 = sns.scatterplot(data=df, x="Runtime", y="GrossRevenue")
    plot5.axhline(np.mean(df["GrossRevenue"]), color="green")
    plot5.axvline(np.mean(df["Runtime"]), color="green")
    save_plot(plot5.figure, OUT_DIR, "Figure5.png")

    # Sixth Plot
    plot6 = plt.figure(figsize=(20, 10))
    plot6 = graph2 = sns.scatterplot(data=df, x="Metascore", y="GrossRevenue")
    plot6.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot6.axvline(np.mean(df["Metascore"]), color="red")
    save_plot(plot6.figure, OUT_DIR, "Figure6.png")

    # Seventh plot
    plot7 = plt.figure(figsize=(15, 8))
    plot7 = sns.lineplot(data=df, x="ReleaseYear", y="GrossRevenue")
    save_plot(plot7.figure, OUT_DIR, "Figure7.png")

    # Eighth plot
    plot8 = plt.figure(figsize=(15, 8))
    plot8 = sns.lineplot(data=df, x="ReleaseYear", y="Runtime")
    save_plot(plot8.figure, OUT_DIR, "Figure8.png")
