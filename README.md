# midterm-project-imdb

Team Good-2-Great Midterm Project for Python, Data, and Databases

Team Members: 
* [Elliott Metzler](https://github.com/ElliottMetzler) - Data Scraping and Cleaning, Git/Project Management
* [Pedro Rodrigues](https://github.com/PedroNBRodrigues) - Figure Production
* [Colin McNally](https://github.com/cmcnally23) - Project Management, Report Writing
* [Austin Longoria](https://github.com/galongoria) - Data Cleaning, Report Writing, Presentation
* [Arpan Chatterji](https://github.com/achatterji1) - Quantitative Analysis
* [Kashaf Oneeb](https://github.com/koneeb) - Quantitative Analysis, Data Dictionary, Report Writing
* [Jack Hill](https://github.com/ts1989mu) -  Figure Production, Report Writing, Vetting

Due: 3/22/2022 

## Introduction

For this project, we set out to use [IMDb](https://www.imdb.com/) data on the top United States grossing movies to gain a better understanding of consumer preferences for different genres. Almost since the inception of the moving picture, the best-selling movies have commanded a passage straight into our hearts, and through time, our cultural lingo. By understanding the characteristics that make a top-selling movie, we aim to investigate what makes the audience tick, fundamentally. To achieve this aim, we created a webscraping tool to retrieve data from IMDb's website before cleaning it and performing various linear regression analyses. As we had hoped, we found that certain genres listed on each movie's IMDb page are associated with higher ratings, though sometimes these results differed by whether or not we attempted to predict a crowd-based rating or a critics score. We also analyzed revenue as predicted by ratings, finding that in some, but not all, cases, the genres predicting higher ratings also predicted higher revenue.

## Data

We document all of the features used in our analysis in the [Data Dictionary](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/data_dictionary.csv). This includes the feature name, definition, type, and a few example values.

### Scraping

#### Process

When we decided to make our topic best-selling movies, we turned to the best website for raw movie data: IMDb. We scraped the data from IMDb using the `Beautiful Soup` and `requests` packages. Both of these packages allowed for seamless extraction of data from a URL. From the IMDb website we set our schema as title, release year, certificates (rating), run time, genres, IMDb rating, Metascore rating, number of votes for IMDb rating, and gross revenue. We then took a deeper look at genre and noticed that most movies were categorized to more than one genre. We knew that this was a potential issue and address our fix to this problem below in the cleaning section.

#### Limitations

One important limitation of our analysis is with our methodology for scraping the raw data from IMDb's site. We only scraped movies for which we were able to retrieve all data fields desired from the analysis. Thus, in instances where movies were missing a data field, we excluded these from the scraping process. Importantly, this could skew our analysis away from less popular or older movies. A potential extension of our analysis would be to attempt to scrape these movies and interpolate or estimate missing values where possible, though this process would take more time and consideration than available to us for this project.

A second limitation of our data is that IMDb ratings, and, to a lesser extent, Metascore ratings do not reflect a consistent rubric. During the time scope of our analysis, it is unclear to us whether IMDb or Metascore changed their internal rubric. It is also unclear if the same evaluator is used for movies falling into different genres. Furthermore, the number of votes for IMDb rating may reflect whether the demographics for a certain movie are more prone to be IMDb users (and therefore more likely to leave a rating).

Third, the gross revenue may be a poor measure of popularity due to the confounding effect of inflation and the unknown spending on marketing. Another extension of our analysis would be to control for inflation and combine another dataset for marketing expenditure.  


### Cleaning

With our raw data from IMDb, we needed to clean some fields so we could use them in our analysis. We cleaned the data using the `pandas` package. The key cleaning issue with the raw data was to convert some fields appearing as text to integers or floats. Additionally, the scraper picked up some extraneous values and words when scraping the pages. In order to get rid of extraneous values and convert types, we stripped most of the data. For example, the Gross Revenue column of our raw data set had both "$" and "M" attached to the earnings, stripping this and then formatting to a float allowed for a singular number of revenue in millions USD.

We also needed to create dummy variables for the different genres so that we could run our regression analyses. The complicating factor in this step was that the genres were listed together in the raw data, so we needed to first split them into individual columns before using tools from `pandas` to dummy code the genres.


## Exploratory Data Analysis

After scraping and cleaning the data, our first analytical step was to perform some exploratory analysis to gain a better understanding of our data. We used the `pandas` and `statsmodels` packages. Our most notable results and charts are reported here, while underlying statistical output can be found under [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/decade_analysis.csv) and additional figures can be found in the [figures](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/figures) sub-directory.

### Decades Analysis

First, we calculated summary statistics by the decade in which the movie was released. These included the mean, maximium, minimum, and certain quantile values of runtime, IMDb rating, Metascore, votes, and gross revenue.  The analysis showed that audience engagement increased within the IMDb community over time. For instance, movies since the 1990's have received relatively more IMDb votes, which may have resulted in lower average ratings. This analysis also reveals some important limitations in our data. For example, average gross revenue increased sharply since the 1990's which can be partially attributed to the lack of inflation-adjusted figures. Furthermore, we can see this data is biased because it has fewer observations earlier in the century as shown in the figure below.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Movies_per_decade.png)

We also found that since the 1960's the average IMDb ratings by decade have steadily declined. We saw a similar trend in Metascores, though the Metascores decline started earlier. As mentioned above, a good extension of this analysis would be to find a database that has more movies from the earlier decades of cinema so that we could have better analysis across decades, rather than having so few titles from the 1930's to 1960's.

### Genres Analysis

Since we were most interested in better understanding various genres' impact on movie performance, we also explored this in our first review of the data. In the next figure, we display the share of movies in our sample that list each possible genre on their IMDb page.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Percentage_of_movies_genre.png)

As shown by the figure, in our sample of the highest grossing movies on IMDb, they tend to be Adventure, Action, Comedy, and Drama movies.

### Rating and Grossing Analysis

We also wanted to visually assess the relationship between the rating (IMDb and Metascore) and movie gross revenue. We figured that this would help us see if we had a strong correlation between the movie being achieving either a high IMDb rating or Metascore and a high gross revenue figure. We display the results first of IMDb rating on gross revenue then of Metascore on gross revenue.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/IMDBRating_by_Grossing.png)

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Metascore_by_Grossing.png)

As shown by the figures, we see that the majority of the movies in our sample center around the mean of both axes (identified by red lines separating the figures into quadrants). Notably, we do not see movies that have a high grossing revenue (y-axis) and a low rating (x-axis). Thus, we find that the movies in our sample that had high gross revenue were also well received movies. 

Finally, we assessed the relationship between IMDb rating and Metascore to see the strength of the correlation between these two variables.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Scatter_IMDB_by_metascore.png)

As expected, we find a strong correlation between these two metrics.


## Quantitative Analysis

From the cleaned data, we analyzed four regression models using the `statsmodels` package.

The first two OLS regression models show the effect of IMDb rating or Metascore and genres on gross revenue. Since we noticed the strong correlation between IMDb rating and Metascore, we ran separate regressions. We noticed a difference in constants due to Metascore being assigned by critics and IMDb rating being a result of fan votes along with the difference in scale of the variables. The model yielded statistically significant coefficients for IMDb rating and Metascore. We present the results of these regressions below.

#### Revenue ~ IMDb Rating + Genres Regression Results
![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_imdb_ols_regression.png)

#### Revenue ~ Metascore + Genres Regression Results
![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_meta_ols_regression.png)

The second two OLS regression models evaluated the effect of different genres on IMDb rating and Metascore, respectively. In the IMDb rating regression, a total of 11 out of the 20 genres were statistically significant, whereas in the Metascore regression, a total of 12 genres were statistically significant. The differing variable in terms of statistical significance between the two models was the Sport genre. Interestingly, the coefficients with the largest order of magnitude differed slightly between the two models. In the IMDb rating regression, the Horror, Comedy, and Family genres had the highest magnitude among the statistically significant variables, while in the Metascore regression, the Horror, Musical, and Comedy genres had the highest magnitude. In addition, the sign of each significant coefficient aligns. We present the results of these regressions below.

#### IMDb Rating ~ Genres OLS Regression Results
![IMDb OLS Regression](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/imdb_ols_regression.png)

#### Metascore ~ Genres OLS Regression Results
![Metascore OLS Regression](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/metascore_ols_regression.png)


## Conclusions

In our analysis, we were able to review and analyze how different genres impact ratings and gross revenue for the movies in our sample. We found that the Animation and Musical genres had the largest positive impact on IMDb ratings and Metascore, while the Comedy and Horror genres had the largest negative impact on both ratings. Additionally, we found that when estimating gross revenue, IMDb rating and genres like Adventure and Fantasy had a positive impact, while genres like Biography and War had a negative impact. We found similar results in our regression predicting gross revenue using Metascore.

To overcome some of the limitations that exist with our data scraping methodology and with the actual data available through IMDb's website, we propose some interesting expansions for this project. For instance, a relatively simple expansion would be to add an inflation factor to the gross revenue data. A more complex one may be to pull data on production budget, advertising budget, and awards to make our regressions more robust. Another potentially useful extension could be to expand the scraping mechanism to pull significantly more movies, both historically and with lower gross revenue figures, in order to have a broader sample.

 
## Instructions to Reproduce Analysis:

__NOTE__: These reproduction instructions expect that the user is running everything through Vertex AI on Google Cloud Platform. All instructions run through terminal.

1) Set-up Instructions:
	* Run `pip install -r requirements.txt`. This file includes the additional packages necessary to run our code: `requests`, `bs4`, `black`, `matplotlib`, `seaborn`, and `statsmodels`
	* Run `cd midterm-project-imdb`

2) Instructions to scrape and clean data:
	* Run `python3 code/imdb_scraper.py` to scrape the data from the IMDb website. The script [imdb_scraper.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/code/imdb_scraper.py) will navigate to [IMDb pages](https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=), scrape the data, and store it as a csv file. The output is stored in the [raw](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/data/raw) data folder as [imdb_scraped.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/raw/imdb_scraped.csv)
	* Run `python3 code/imdb_cleaner.py` to clean the raw IMDb data. The script [imdb_cleaner.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/code/imdb_cleaner.py) takes in [imdb_scraped.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/raw/imdb_scraped.csv) generated by the prior script and cleans it. The output is stored in the [clean](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/data/clean) data folder as [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/imdb_clean.csv)
	* Run `python3 code/data_dictionary.py` to generate the data dictionary. The script [data_dictionary.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/code/data_dictionary.py) uses the clean IMDb data [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/imdb_clean.csv) generated by the prior script to produce the data dictionary. The output is stored in the [clean](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/data/clean) data folder as [data_dictionary.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/data_dictionary.csv)

3) Instructions to produce Figures:
	* Run `python3 code/graphs.py` to produce figures from the clean IMDb data. The script [graphs.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/code/graphs.py) takes in [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/imdb_clean.csv) and creates a variety of plots highlighting various patterns in the data. The output figures are stored in the [figures](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/figures) folder as .png files

4) Instructions to produce Quantitative Analysis:
	* Run `python3 code/quant_analysis.py` to perform a decade analysis of the features and conduct four different OLS regressions. The script [quant_analysis.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/code/quant_analysis.py) takes in [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/imdb_clean.csv) and creates a csv for the decade analysis and png's for the four OLS regressions in the [quantitative analysis](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/quantitative%20analysis) folder
	 	* Note: For the OLS regressions, all genre dummies are included except for "Western" to account for multicollinearity
	 	* The decade analysis divides data into decades based on Release Year and generates a csv of summary statistics for all features except Release Year for each decade. The output is stored in [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/decade_analysis.csv)
	 	* The first OLS regression regresses Gross Revenue on IMDb Rating and genre dummies. The regression results are summarized in [revenue_imdb_ols_regression.png](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_imdb_ols_regression.png)
	 	* The second OLS regression regresses Gross Revenue on Metascore and genre dummies. The regression results are summarized in [revenue_meta_ols_regression.png](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_meta_ols_regression.png)
	 	* The third OLS regression regresses IMDb Rating on genre dummies. The regression results are summarized in [imdb_ols_regression.png](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/imdb_ols_regression.png)
	 	* The fourth OLS regression regresses Metascore on genre dummies. The regression results are summarized in [metascore_ols_regression.png](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/metascore_ols_regression.png)
