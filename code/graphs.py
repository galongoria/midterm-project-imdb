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

    # Top 50 highest domestic grossing movies plot 
    plot1 = (
    df.groupby("Title")["GrossRevenue"]
    .mean()
    .sort_values(ascending=False)[:50]
    .plot.bar(figsize=(25, 8), title="Top 50 highest domestic grossing movies")
    )
    plot1.set(xlabel="Title", ylabel="Domestic Gross Revenue (in Millions of $)")
    plot1.set_ylim([300, 1000])
    save_plot(plot1.figure, OUT_DIR, "Top_50_Grossing.png")

    # Relation between release year and domestic revenue plot 
    plot2 = plt.figure(figsize=(20, 10))
    plot2 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue")
    plot2 = sns.regplot(data=df, x="ReleaseYear", y="GrossRevenue", order=3)
    plot2.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue")
    save_plot(plot2.figure, OUT_DIR, "Release_Year_by_Grossing.png")

    # Relation between metascore and domestic revenue plot 
    plot3 = plt.figure(figsize=(20, 10))
    plot3 = sns.scatterplot(data=df, x="Metascore", y="GrossRevenue")
    plot3.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot3.axvline(np.mean(df["Metascore"]), color="red")
    plot3.set(xlabel="Metascore", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between metascore and domestic revenue")
    save_plot(plot3.figure, OUT_DIR, "Metascore_by_Grossing.png")


    # Relation between IMDB rating and domestic revenue plot
    plot4 = plt.figure(figsize=(20, 10))
    plot4 = sns.scatterplot(data=df, x="IMDBRating", y="GrossRevenue")
    plot4.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot4.axvline(np.mean(df["IMDBRating"]), color="red")
    plot4.set(xlabel="IMDB Rating", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between IMDB rating and domestic revenue")
    save_plot(plot4.figure, OUT_DIR, "IMDBRating_by_Grossing.png")

    # Relation between IMDB rating and metascore plot
    plot5 = plt.figure(figsize=(20, 10))
    plot5 = sns.scatterplot(data=df, x="IMDBRating", y="Metascore")
    plot5.set(xlabel="IMDB Rating", ylabel="Metascore",
         title="Relation between IMDB rating and metascore")
    save_plot(plot5.figure, OUT_DIR, "Scatter_IMDB_by_metascore.png")
    
    # Code for probability distribution graph   
    genre_props = (
    df[['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical',
       'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']]
    .mean()
    .reset_index()
    .rename(columns = {"index": "Genre", 0: "Proportion"})
    .sort_values("Proportion", ascending = False)
    )
    
    # Plot of percentage of Top 1000 US Grossing Movies by Genre
    plot6 = plt.figure(figsize=(18,6))
    plot6 = sns.barplot(data=genre_props,
            x = "Proportion",
            y = "Genre",
           orient = "h",
           palette = "Blues_r")
    plot6.set(title="Percentage of Top 1000 US Grossing Movies by Genre")
    save_plot(plot6.figure, OUT_DIR, "Percentage_of_movies_genre.png")
    
    
    # Plot of relation between release year and domestic revenue with Action movies highlighted
    plot7 = plt.figure(figsize=(20, 10))
    plot7 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue", hue="Action")
    plot7.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue with Action movies highlighted")
    save_plot(plot7.figure, OUT_DIR, "Release_year_by_grossing_action.png")
    
    
    # Plot of relation between release year and domestic revenue with Adventure movies highlighted
    plot8 = plt.figure(figsize=(20, 10))
    plot8 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue", hue="Adventure")
    plot8.set(xlabel="Release Year", ylabel="Domestic Gross Revenue (in Millions of $)",
         title="Relation between release year and domestic revenue with Adventure movies highlighted")
    save_plot(plot8.figure, OUT_DIR, "Release_year_by_grossing_adventure.png")
    
    # Plot of relation between genres and average domestic revenue
    plot9 = (
    df.groupby("Genres")["GrossRevenue"]
    .mean()
    .sort_values(ascending=False)[:50]
    .plot.bar(figsize=(25, 8))
    )
    plot9.set(xlabel="Genre Combination", ylabel="Average Domestic Gross Revenue (in Millions of $)",
         title="Relation between genres and average domestic revenue")
    plot9.set_ylim([100, 500])
    save_plot(plot9.figure, OUT_DIR, "Grossing_by_genre_group.png")