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

Need to include here a quick summary of:
* Goal of analysis -
The goal of our analysis is to understand consumer perference of cinematic genres over the timeserie of data avilable. Almost since the inception of the moving picture, the best-selling movies have commanded a passage straight into our hearts, and through time, our cultural lingo. By understanding the characteristics that make a top-selling movie, we aim to investigate what makes the audience tick, fundementally.
* Methodology - 
By scraping data from IMBD, we collected data points with features important to our analysis and have been validated by a high volume of user. We then cleaned the data by removing entries with missing data field. We then created dummie variables and conduct exploratry data analysis with Python. 
* Findings - Through

## Data

The features used in our analysis are summarized in the [Data Dictionary](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/data_dictionary.csv), which includes the feature name, definition, type, and example values.

### Scraping

When we decided to make our topic best-selling movies for our project, we turned to the best website for raw movie data: IMdb. Elliot scraped the data from IMdb using "Beautiful Soup" and "requests" as his python packages. Both of these packages allowed for seamless extraction of data from a URL. From the IMdb website we set our schema as title, release year, certificates (rating), run time, genres, IMdb rating, Metascore rating, # of votes for IMdb rating, and gross revenue. We then took a deeper look at genre and noticed that most movies were categorized to more than one genre. We knew that this could become an issue and decided to fix this problem when cleaning the data.

We note that one of the important limitations of our analysis is with our methodology for scraping the raw data from imdb's site. We only scraped movies for which we were able to retrieve all data fields desired from the analysis. Thus, in instances where movies were missing a data field, we excluded these from the scraping process. However, this could skew our analysis away from less popular or older movies. A potential extension of our analysis would be to attempt to scrape these movies and interpolate or estimate missing values where possible, though this process would take more time and consideration than available to us for this project.

Another limitation of our data is that IMdb ratings and to a lesser extent, Metascore rating do not reflect a consistent rubric. During the time scope of our study, it is unclear to us whether IMdb or Metascore changed their internal rubric. It is also unclear if the same evaluator are used for movies falling into different genres. Furthermore, the number of votes for IMdb rating may reflect whether the demographics for a certain movie is more prone to be IMdb users (and therefore more likely to leave a rating).

Lastly, the gross revenue may be a poor measure of popularity due to the confounding effect of inflation and the unknown spending on marketing. An additional route of analysis would be to control for inflation and combine another dataset for marketing spendings.  


### Cleaning

From the scraped data we needed to have more palatable data from processing and analyzing, so then Austin cleaned the data using "pandas" and "os" as his packages. The raw data collected from IMdb needed mainly to be cleaned as most of the entries in the raw data are written as text and not integers or floats. As well the scraper picked up a lot of extraneous values and words when scraping the pages. In order to get rid of most of this unnecessary information Austin stripped most of the data. For example, the Gross Revenue column of our raw data set had both "$" and "M" attached to the earnings, stripping this and then formatting to a float allowed for a singular number of revenue based in the millions of earnings.

As well we needed to create dummy variables for the differnet genres, so that each could be accessed when processing the data. To do this Austin created variables for each genre by separating the strings at the comma in between each genre listing. Then he concatenated the genres back into the data set. This basically allowed for categorical variables that were separated and easier to use in regressions and data analysis.

## Exploratory Data Analysis
After scraping and cleaning the data we were finally able to manipulate and analyze the dataframe we had created. With Kashaf in charge of the analysis, she chose to use "pandas" as well as "statsmodel.api" for her analysis. First we thought it would be a good idea to look at the different summary statistics for each decade that movies were released in. This was done by creating a "Decade" variable that took every "ReleaseYear" and divided by 10 with no decimals then remultiplied by ten to normalize to each decade. Then we grouped all movies by the decade of their release, and proceeded to run summary statistics of the variables by each decade by the pandas function `.describe`.

We found from our summary statistics that the average IMdb rating was at its highest during the 1960's. As well we found that ever since the 1960's IMdb ratings on average decade to decade have steadily decreased. Metascore ratings also see this trend as well decade to decade a steady drop in average ratings, but not starting in the 1960's but actually earlier. The problem though could be from the fewer amount of films produced in these earlier decades, as we see counts of movies on the rise decade by decade. If there were more movies rated from the 1930's-1960's there would be easier comparisions to be made through the decades, but this list isnt as comprehensive on the earlier decades. A possible extension of this analysis could be to find a database that has more movies from the earlier decades of cinema so that we could have better analysis across decades, rather than having so few title from the 1930's-1960's.

## Modeling Analysis
From the cleaned data, four models were created by Kashaf using the “statsmodels" package. These include 1 summary statistics model and 3 regression models.

For the first model, we calculated summary statistics per the release decade and they were evaluated across genres to see their average IMDb score, Metascore, and Gross Revenue they collected.  This model gives a clear picture of the increased engagement of the audience in terms of critiquing films. For instance, movies since the 90s have received relatively more votes on IMDb and Metascore, which has resulted in lower average ratings on these platforms for movies in that decade. This prelimianry analysis also shows some limitations, including usage over the past decades and inflation adjustments. For instance, the average gross revenue has increased sharply since the 90s, but the average gross revenue generated is not inflation-adjusted. Finally, this analysis is also biased since the top movies on IMDb and Metascore are partial towards recent releases; therefore, more attention is given to recent films.

The second and third OLS regression models evaluate the effect of different genres on either either IMDb score or Metascore. In the IMDb model, a total of 11 genres out of the 20 genres we have accounted for are statistically significant, whereas for the Metascore model, a total of 12 genres are statistically significant. The “sport” variable is the difference between these two models in terms of statistical significance. In both models, horror, comedy, and have the highest magnitude among statistically significant variables. This finding agrees with the fact that IMDb and Metascore are correlated.

The fourth OLS regression model shows effect of genres on revenue, which yields a statistically significant coefficient with respect to IMDb, Metascore and the Release Year. This shows the accuracy of this model and consistency with our previous findings. However, it is hard to evaluate the statistical significance of gross revenue on one movie, since one movie can encompass several genres that might/might not be statistically significant in this model. 

## Conclusions

Need to include here a summary of:
* Goal of analysis and conclusions
* limitations of the project
The focual point for the expansion of our current project should focuse on the use of additional data sets and estimation techniques to reduce the effect of cofounders on our analysis. 
Clear data on how genre influences the kind of audience a movie gets and whether they are likely to be a IMdb user would help us calibrate the value of IMdb ratings. On the other hand, we could utilize inflation data to do a present value translation for our revenue figures.

## Instructions to Reproduce Analysis:

1) Set-up Instructions:
	* Run `pip install -r requirements.txt` in terminal.

2) Data Scrape and Clean Instructions:
	* Run `python3 code/imdb_scraper.py` to scrape the data from the IMDb website. The script [imdb_scraper.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/code/imdb_scraper.py) will navigate to [IMDb pages](https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=), scrape the data, and store it as a csv file. The output is stored in the [raw](https://github.com/ElliottMetzler/midterm-project-imdb/tree/document/data/raw) data folder as [imdb_scraped.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/raw/imdb_scraped.csv).
	* Run `python3 code/imdb_cleaner.py` to clean the raw IMDb data. The script [imdb_cleaner.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/code/imdb_cleaner.py) takes in [imdb_scraped.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/raw/imdb_scraped.csv) generated by the prior script and cleans it. The output is stored in the [clean](https://github.com/ElliottMetzler/midterm-project-imdb/tree/document/data/clean) data folder as [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/imdb_clean.csv).
	* Run `python3 code/data_dictionary.py` to generate the data dictionary. The script [data_dictionary.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/code/data_dictionary.py) uses the clean IMDb data [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/imdb_clean.csv) generated by the prior script to produce the data dictionary. The output is stored in the [clean](https://github.com/ElliottMetzler/midterm-project-imdb/tree/document/data/clean) data folder as [data_dictionary.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/data_dictionary.csv).

3) Instructions to Produce Figures:
	* Run `python3 code/graphs.py` to produce figures from the clean IMDb data. The script [graphs.py](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/code/graphs.py) takes in [imdb_clean.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/imdb_clean.csv) and creates a variety of plots highlighting various patterns in the data. The output figures are stored in the [figures](https://github.com/ElliottMetzler/midterm-project-imdb/tree/document/figures) folder as .png files.

4) Instructions to Produce Quantitative Analysis:
	* Run `python3 code/quant_analysis.py` to perform a decade analysis of features and OLS regression of Gross Revenue on IMDB Rating, Metascore, and Release Year. 
	 	* The decade analysis divides data into decades based on Release Year and generates a csv of summary statistics for all features except Release Year for each decade. The output is [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/decade_analysis.csv)
	 	* The OLS regression results are summarized into a csv. The output is [ols_regression.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/ols_regression.csv)
