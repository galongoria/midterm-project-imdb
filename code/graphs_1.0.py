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

    # First Plot - top 50 movies ranked by gross revenue
    plot1 = (
        df.groupby("Title")["GrossRevenue"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot1.figure, OUT_DIR, "Figure1.png")

    # Second Plot - top 50 movies ranked by IMDB Rating
    plot2 = (
        df.groupby("Title")["IMDBRating"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot2.figure, OUT_DIR, "Figure2.png")

    # Third Plot - - top 50 movies ranked by Metascore
    plot3 = (
        df.groupby("Title")["Metascore"]
        .mean()
        .sort_values(ascending=False)[:50]
        .plot.bar(figsize=(25, 8))
    )
    save_plot(plot3.figure, OUT_DIR, "Figure3.png")

    # Fourth Plot - scatterplot with all movies from dataset showing relation between revenue and IMDB Rating
    plot4 = plt.figure(figsize=(20, 10))
    plot4 = sns.scatterplot(data=df, x="IMDBRating", y="GrossRevenue")
    save_plot(plot4.figure, OUT_DIR, "Figure4.png")

    # Fifth Plot - scatterplot with all movies showing relation between runtime and revenue, with mean lines to separate in quadrants
    plot5 = plt.figure(figsize=(20, 10))
    plot5 = sns.scatterplot(data=df, x="Runtime", y="GrossRevenue")
    plot5.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot5.axvline(np.mean(df["Runtime"]), color="red")
    save_plot(plot5.figure, OUT_DIR, "Figure5.png")

    # Sixth Plot - scatterplot with all movies showing relation between Metascore and revenue, with mean lines to separate in quadrants
    plot6 = plt.figure(figsize=(20, 10))
    plot6 = sns.scatterplot(data=df, x="Metascore", y="GrossRevenue")
    plot6.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot6.axvline(np.mean(df["Metascore"]), color="red")
    save_plot(plot6.figure, OUT_DIR, "Figure6.png")

    # Seventh plot - average grossing per year, with confidence interval
    plot7 = plt.figure(figsize=(15, 8))
    plot7 = sns.lineplot(data=df, x="ReleaseYear", y="GrossRevenue")
    save_plot(plot7.figure, OUT_DIR, "Figure7.png")

    # Eighth plot - average runtime per year, with confidence interval
    plot8 = plt.figure(figsize=(15, 8))
    plot8 = sns.lineplot(data=df, x="ReleaseYear", y="Runtime")
    save_plot(plot8.figure, OUT_DIR, "Figure8.png")

    # Ninth plot - average runtime per classification, without confidence interval
    plot9 = plt.figure(figsize=(15, 8))
    plot9 = sns.lineplot(data=df, x="Certificate", y="Runtime", ci=False)
    save_plot(plot9.figure, OUT_DIR, "Figure9.png")
    
    # Tenth plot - average grossing per classification, without confidence interval
    plot10 = plt.figure(figsize=(15, 8))
    plot10 = sns.lineplot(data=df, x="Certificate", y="GrossRevenue", ci=False)
    save_plot(plot10.figure, OUT_DIR, "Figure10.png")
    
    # Eleventh plot - scatterplot with all movies showing relation between release year and revenue, with mean lines to separate in quadrants
    plot11 = plt.figure(figsize=(20, 10))
    plot11 = graph2 = sns.scatterplot(data=df, x="ReleaseYear", y="GrossRevenue")
    plot11.axhline(np.mean(df["GrossRevenue"]), color="red")
    plot11.axvline(np.mean(df["ReleaseYear"]), color="red")
    save_plot(plot11.figure, OUT_DIR, "Figure11.png")
    
    # created a group with all the genres dummies to refer to it easily in following graphs
    genres = [
    'Action',
    'Adventure',
    'Animation',
    'Biography', 
    'Comedy',
    'Crime',
    'Drama',
    'Family', 
    'Fantasy', 
    'History', 
    'Horror', 
    'Music', 
    'Musical',
    'Mystery', 
    'Romance', 
    'Sci-Fi', 
    'Sport', 
    'Thriller', 
    'War', 
    'Western'
    ]
    
    # Twelfth plot - bar plot with the number of movies released in each metascore with different columns for genres
    plot12 = (
    df.groupby("Metascore")[genres]
    .sum()
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot12.figure, OUT_DIR, "Figure12.png")
    
    # Thirteenth plot - bar plot with the number of movies released each year with different columns for genres
    plot13 = (
    df.groupby("ReleaseYear")[genres]
    .sum()
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot13.figure, OUT_DIR, "Figure13.png")
    
    # Fourteenth plot - same as 13, but with lines instead
    plot14 = (
    df.groupby("ReleaseYear")[genres]
    .sum()
    .sort_values("ReleaseYear", ascending=False)
    .plot.line(figsize=(25, 8))
    )
    save_plot(plot14.figure, OUT_DIR, "Figure14.png")
    
    # Fifteenth plot - line plot with number of movies released in past 10 years with different lines by genres
    plot15 = (
    df.groupby("ReleaseYear")[genres]
    .sum()
    .sort_values("ReleaseYear", ascending=False)[:10]
    .plot.line(figsize=(25, 8))
    )
    save_plot(plot15.figure, OUT_DIR, "Figure15.png")
    
    # Sixteenth plot - same as 15, but with bar plots instead - I think it looks better than in a line
    plot16 = (
    df.groupby("ReleaseYear")[genres]
    .sum()
    .sort_values("ReleaseYear", ascending=False)[:10]
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot16.figure, OUT_DIR, "Figure16.png")
    
    # Seventeenth plot - same as 16, but with the first 10 years of the dataset
    plot17 = (
    df.groupby("ReleaseYear")[genres]
    .sum()
    .sort_values("ReleaseYear", ascending=True)[:10]
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot17.figure, OUT_DIR, "Figure17.png")
    
    # Eighteenth plot - bar plot with number of movies by each genres that are in the top 30 Metascore ratings
    plot18 = (
    df.groupby("Metascore")[genres]
    .sum()
    .sort_values("Metascore", ascending=False)[:30]
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot18.figure, OUT_DIR, "Figure18.png")
    
    # Nineteenth plot - bar plot with number of movies by each genres that are in the lowest 30 Metascore ratings
    plot19 = (
    df.groupby("Metascore")[genres]
    .sum()
    .sort_values("Metascore", ascending=True)[:30]
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot19.figure, OUT_DIR, "Figure19.png")
    
    # Twentieth plot - bar plot with number of movies by each genres that are in the average Metascore ratings
    plot20 = (
    df.groupby("Metascore")[genres]
    .sum()
    .sort_values("Metascore", ascending=True)[30:70]
    .plot.bar(figsize=(25, 8))
    )
    save_plot(plot20.figure, OUT_DIR, "Figure20.png")