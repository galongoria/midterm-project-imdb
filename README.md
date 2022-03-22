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

For this project, we set out to use [IMDb](https://www.imdb.com/) data on the top United States grossing movies to gain a better understanding of consumer preferences for different genres. Almost since the inception of the moving picture, the best-selling movies have commanded a passage straight into our hearts, and through time, our cultural lingo. By understanding the characteristics that make a top-selling movie, we aim to investigate what makes the audience tick, fundementally. To achieve this aim, we created a webscraping tool to retrieve data from IMDb's website before cleaning it and performing various linear regression analyses. As we had hoped, we found that certain genres listed on each movie's IMDb page are associated with higher ratings (popularity or critical), though sometimes these results differed by whether or not we attempted to predict a crowd based rating or a critics score. We also analyzed revenue as predicted by ratings, finding that in some, but not all, cases, the genres predicting higher ratings also predicted higher revenue.

## Data

We document all of the features used in our analysis in the [Data Dictionary](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/data/clean/data_dictionary.csv). This includes the feature name, definition, type, and a few example values.

### Scraping

#### Process

When we decided to make our topic best-selling movies for our project, we turned to the best website for raw movie data: IMDb. We scraped the data from IMDb using "Beautiful Soup" and "requests" packages. Both of these packages allowed for seamless extraction of data from a URL. From the IMDb website we set our schema as title, release year, certificates (rating), run time, genres, IMDb rating, Metascore rating, # of votes for IMDb rating, and gross revenue. We then took a deeper look at genre and noticed that most movies were categorized to more than one genre. We knew that this was a potential issue and address our fix to this problem below in the cleaning section.

#### Limitations

One important limitation of our analysis is with our methodology for scraping the raw data from IMDb's site. We only scraped movies for which we were able to retrieve all data fields desired from the analysis. Thus, in instances where movies were missing a data field, we excluded these from the scraping process. Importantly, this could skew our analysis away from less popular or older movies. A potential extension of our analysis would be to attempt to scrape these movies and interpolate or estimate missing values where possible, though this process would take more time and consideration than available to us for this project.

A second limitation of our data is that IMDb ratings, and, to a lesser extent, Metascore rating do not reflect a consistent rubric. During the time scope of our analysis, it is unclear to us whether IMDb or Metascore changed their internal rubric. It is also unclear if the same evaluator are used for movies falling into different genres. Furthermore, the number of votes for IMDb rating may reflect whether the demographics for a certain movie is more prone to be IMDb users (and therefore more likely to leave a rating).

Third, the gross revenue may be a poor measure of popularity due to the confounding effect of inflation and the unknown spending on marketing. Another extension of our analysis would be to control for inflation and combine another dataset for marketing expenditure.  


### Cleaning

With our raw data from IMDb, we needed to clean some fields so we could use them in our analysis. We cleaned the data using the `pandas` package. The key cleaning issue with the raw data was to convert some fields appearing as text to integers or floats. Additionally, the scraper picked up some extraneous values and words when scraping the pages. In order to get rid of extraneous values and convert types, we stripped most of the data. For example, the Gross Revenue column of our raw data set had both "$" and "M" attached to the earnings, stripping this and then formatting to a float allowed for a singular number of revenue in millions USD.

We also needed to create dummy variables for the different genres so that we could run our regression analyses. The complicating factor in this step was that the genres were listed together in the raw data, so we needed to first split them into individual columns before using tools from `pandas` to dummy code the genres.


## Exploratory Data Analysis

After scraping and cleaning the data, our first analytical step was to perform some exploratory analysis to gain a better understanding of our data. We used the `pandas` and `statsmodels` packages. Our most notable results and charts are reported here, while underlying statistical output can be found under [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/decade_analysis.csv) and additional figures can be found in the [figures](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/figures) sub-directory.

### Decades Analysis

First, we calculated summary statistics by release decade. These included the mean, maximium, minimum, and certain quantile values of runtime, IMDb score, Metascore, votes, and gross revenue.  This analysis shows the effects increased audience engagement within the IMDb community. For instance, movies since the 90s have received relatively more votes on IMDb and Metascore, which may have resulted in lower average ratings. This analysis also reveals some important limitations in our data. For example, average gross revenue has increased sharply since the 90s; however, this is mostly due to lack of inlfation-adjusted figures. Similarly, we can see this data is biased because it has less observations earlier in the century (see the figure below displaying the distribution of movies in our sample by decade). As a result, more attention is given to recent films.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Movies_per_decade.png)

We also found that since the 1960's, the IMDb ratings on average by decade have steadily declined. We see a similar trend in Metascore ratings, though the Metascore ratings decline starts earlier. As mentioned above, a good extension of this analysis would be to find a database that has more movies from the earlier decades of cinema so that we could have better analysis across decades, rather than having so few title from the 1930's-1960's.

### Genres Analysis

Since we were most interested in better understanding various genres impact on movie performance by either rating or income metrics, we also explored this in our first review of the data. In the next figure, we display the share of movies in our sample that list each possible genre on their IMDb page.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Percentage_of_movies_genre.png)

As shown by the figure, in our sample of the highest grossing movies on IMDb, they tent to be Adventure, Action, Comedy, and Drama movies.

### Rating and Grossing Analysis

We also wanted to visually assess the relationship between the rating (IMDb and Metascore) and movie gross income. We figured that this would help us see if we had a strong correlation between the movie being "good" and making lots of money. We display the results first of IMDb on gross then of Metascore on gross.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/IMDBRating_by_Grossing.png)

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Metascore_by_Grossing.png)

As shown by the figures, we see that the majority of the movies in our sample center around the mean of both axes (identified by red lines separating into quadrants). Notably, we do not see movies that have a high grossing income (y-axis) and a low rating score (x-axis). Thus, we find that the movies in our sample that made a lot of money also were well received movies. 

Finally, we assessed the relationship between IMDb score and Metascore to see how strong the correlation between this two variables was.

![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/figures/Scatter_IMDB_by_metascore.png)

As expected, we find a strong correlation between these two scoring metrics.


## Quantitative Analysis

From the cleaned data, we analyzed four regression models using the `statsmodels` package.

The first two OLS regression models evaluate the effect of different genres on either IMDb score or Metascore. We saw these 2 variables are correlated and see how Metascore and IMDb were affected by them. In the IMDb model, a total of 11 genres out of the 20 genres we have accounted for are statistically significant, whereas for the Metascore model, a total of 12 genres are statistically significant. The “sport” variable is the difference between these two models in terms of statistical significance. The ranking of magnitudes were slightly different in these models. In the IMDb model, horror, comedy, and family have the highest magnitude among statistically significant variables, while in the Metascore model, those ranks are held by horror, musical and comedy. In addition, the sign of every significant coefficient is the same, which coincides with our assumption that IMDb and Metascore are correlated. We present the results of these regressions below.

#### IMDb OLS Regression Results
![IMDb OLS Regression](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/imdb_ols_regression.png)

#### Metascore OLS Regression Results
![Metascore OLS Regression](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/metascore_ols_regression.png)

The second two OLS regression models show the effect of IMDb score or Metascore and genres on gross revenue. Since we notice the strong correlation between IMDb score and Metascore, they have been put in separate regressions. We notice a difference in constants due to Metascore being assigned by critics and IMDb score being a result of fan votes. The model yields a statistically significant coefficient with respect to IMDb and the Metascore, which shows the accuracy of this model and consistency with our previous findings. However, it is hard to evaluate the statistical significance of gross revenue on one movie, since one movie can encompass several genres that might/might not be statistically significant in this model. We present the results of these regressions below.

#### Revenue ~ IMDb Regression Results
![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_imdb_ols_regression.png)

#### Revenue ~ Metascore Regression Results
![](https://github.com/ElliottMetzler/midterm-project-imdb/blob/main/quantitative%20analysis/revenue_meta_ols_regression.png)

## Conclusions

The goal of our analysis is to find the fundemntal genre drivers of film ratings and revenue. We discovered that the genre of horror and comedey had the largest effect on ratings. On the other hand, adventure and sci-fi had the largest positive effect on reveune, while biography, horror and war had the largest negative effects. We can immediately sense that it is perhaps some aspects of the genre's production, rather than the mere presence of genre itself, that drives the difference in revenue. Adventure and sci-fi films, espically in recent years, are usually big budget productions that begin franchises and are heavily promoted with big stars. On the other hand, biographies and horror movies are know to be lower budget, indie productions. 

The focal point for the expansion of our current project should focus on the use of additional data sets and estimation techniques to reduce the effect of confounders on our analysis. 

Clear data on how genre influences the kind of audience a movie gets and whether they are likely to be a IMDb user would help us calibrate the value of IMDb ratings. On the other hand, we could utilize inflation data to do a present value translation for our revenue figures. This process of calibration could be further extended to give each more an era score, or how they scored relative to movies produced in the same decade. This would further reduce the biases that result from the trend in IMDb ratings. A final data set that would be helpful is the total production budget and total advertising budget of a movie, which will help us control for the effect of genre on revneue.

But our analysis could also benefit through the use of interaction variables. Specifically, we could investigate how different genre's interact with each other and how different genres interact with the release year variable.

Finally, we had to eliminate entries due to missing data values. In further analysis, we could partition some of the data into a training set and train an alogrithm to automatically fill in some of the missing data values. This estimation will introduce more varience to our regression, but may be worthwhile for the data entries they were able to recover. As a finishing touch, we could use the number of peer movies, or how dense are the data around an entry, to give a confidence rating that vary on the different percentiles of the variable of interest.

## Instructions to Reproduce Analysis:

NOTE: These reproduction instructions expect that the user is running everything through Vertex AI. All instructions run through terminal.

1) Set-up Instructions:
	* Run `pip install -r requirements.txt`
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
