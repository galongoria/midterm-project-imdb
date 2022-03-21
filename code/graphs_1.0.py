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
    df = pd.read_csv(IN_FILE_PATH).sort_values("GrossRevenue", ascending=False)[:1000]

    # First Plot 
    plot1 = (
    df.groupby("Title")["GrossRevenue"]
    .mean()
    .sort_values(ascending=False)[:50]
    .plot.bar(figsize=(25, 8), title="Top 50 highest domestic grossing movies")
    )
    plot1.set(xlabel="Title", ylabel="Domestic Gross Revenue (in Millions of $)")
    plot1.set_ylim([300, 1000])
    save_plot(plot1.figure, OUT_DIR, "Figure1.png")

    # Second Plot 
    plot2 = plt.figure(figsize=(20, 10))
    plot2 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue")
    plot2 = sns.regplot(data=df, x="ReleaseYear", y="GrossRevenue", order=3)
    plot2.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot2.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue")
    save_plot(plot2.figure, OUT_DIR, "Figure2.png")

    # Third Plot 
    plot3 = plt.figure(figsize=(20, 10))
    plot3 = sns.scatterplot(data=df, x="Metascore", y="GrossRevenue")
    plot3.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot3.axvline(np.mean(df["Metascore"]), color="red")
    plot3.set(xlabel="Metascore", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between metascore and domestic revenue")
    save_plot(plot3.figure, OUT_DIR, "Figure3.png")


    # Fourth Plot
    plot4 = plt.figure(figsize=(20, 10))
    plot4 = sns.scatterplot(data=df, x="IMDBRating", y="GrossRevenue")
    plot4.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot4.axvline(np.mean(df["IMDBRating"]), color="red")
    plot4.set(xlabel="IMDB Rating", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between IMDB rating and domestic revenue")
    save_plot(plot4.figure, OUT_DIR, "Figure4.png")

    # Fifth Plot
    plot5 = plt.figure(figsize=(20, 10))
    plot5 = sns.scatterplot(data=df, x="IMDBRating", y="Metascore")
    plot5 = sns.regplot(data=df, x="IMDBRating", y="Metascore")
    plot5.set(xlabel="IMDB Rating", ylabel="Metascore",
         title="Relation between IMDB rating and metascore")
    save_plot(plot5.figure, OUT_DIR, "Figure5.png")
    
    # Sixth Code   
    genre_props = (
    df[['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical',
       'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']]
    .mean()
    .reset_index()
    .rename(columns = {"index": "Genre", 0: "Proportion"})
    .sort_values("Proportion", ascending = False)
    )
    
    # Plot
    plot6 = plt.figure(figsize=(18,6))
    plot6 = sns.barplot(data=genre_props,
            x = "Proportion",
            y = "Genre",
           orient = "h",
           palette = "Blues_r")
    plot6.set(title="Percentage of Top 1000 US Grossing Movies by Genre")
    save_plot(plot6.figure, OUT_DIR, "Figure6.png")
    
    
    # Seventh Plot   
    plot7 = plt.figure(figsize=(20, 10))
    plot7 = sns.regplot(data=df, x="ReleaseYear", y="GrossRevenue", order =2)
    plot7 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue", hue="Action")

    plot7.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue with Action movies highlighted")
    save_plot(plot7.figure, OUT_DIR, "Figure7.png")
    
    
    # Eighth Plot   
    plot8 = plt.figure(figsize=(20, 10))
    plot8 = sns.regplot(data=df, x="ReleaseYear", y="GrossRevenue", order = 2)
    plot8 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue", hue="Adventure")
    plot8.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue with Adventure movies highlighted")
    save_plot(plot8.figure, OUT_DIR, "Figure8.png")
    
    # Ninth Plot
    plot9 = (
    df.groupby("Genres")["GrossRevenue"]
    .mean()
    .sort_values(ascending=False)[:50]
    .plot.bar(figsize=(25, 8))
    )
    plot9.set(xlabel="Genre Combination", ylabel="Average Domestic Gross Revenue (in Millions of $)",
         title="Relation between genres and average domestic revenue")
    plot9.set_ylim([100, 500])
    save_plot(plot9.figure, OUT_DIR, "Figure9.png")
    
    
    ## Extra Plots
    # Tenth Plot
    plot10 = plt.figure(figsize=(20, 10))
    plot10 = sns.lineplot(data=df, x="ReleaseYear", y="Runtime")
    save_plot(plot10.figure, OUT_DIR, "Figure10.png")
    
    # Eleventh Plot
    plot11 = plt.figure(figsize=(20, 10))
    plot11 = sns.lineplot(data=df, x="IMDBRating", y="Runtime")
    save_plot(plot11.figure, OUT_DIR, "Figure11.png")
    
    # Twelfth Plot
    plot12 = plt.figure(figsize=(20, 10))
    plot12 = sns.lineplot(data=df, x="Metascore", y="Runtime")
    save_plot(plot12.figure, OUT_DIR, "Figure12.png")
