# midterm-project-imbd

Team Good-2-Great Midterm Project for Python, Data, and Databases

Team Members: 
* [Elliott Metzler](https://github.com/ElliottMetzler) - Data Scraping and Cleaning, Git/Project Management
* [Pedro Rodrigues](https://github.com/PedroNBRodrigues) - Figure Production
* [Colin McNally](https://github.com/cmcnally23) - Project Management, Report Writing
* [Austin Longoria](https://github.com/galongoria) - Data Cleaning, Report Writing, Presentation
* [Arpan Chatterji](https://github.com/achatterji1) - Quantitative Analysis
* [Kashaf Oneeb](https://github.com/koneeb) - Quantitative Analysis, Data Dictionary, Report Writing
* [Jack Hill](https://github.com/ts1989mu) -  Report Writing, Vetting
Due: 3/22/2022 

## Introduction

Need to include here a quick summary of:
* Goal of analysis
The goal of our analysis is to understand consumer perference of cinematic genres over the timeserie of data avilable. Almost since the inception of the moving picture, the best-selling movies have commanded a passage straight into our hearts, and through time, our cultural lingo. By understanding the characteristics that make a top-selling movie, we aim to investigate what makes the audience tick, fundementally.
* Methodology
By scraping data from IMBD, we collected data points with features important to our analysis and have bee validated by a high volume of user.
* Findings

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

## Modeling Analysis

## Conclusions

Need to include here a summary of:
* Goal of analysis and conclusions
* limitations of the project
* Areas where we would have improved or expanded the project if we had more time

## Instructions to Reproduce Analysis:

1) Set-up Instructions:
	* Run `pip install -r requirements.txt` in terminal

2) Data Scrape and Clean Instructions:
	* Run `python3 code/imdb_scraper.py` to scrape the data from the imdb website. This script will navigate to the imdb pages and scrape the data, generating a csv file of raw data in the raw data folder. The output is `data/raw/imdb_scraped.csv`
	* Run `python3 code/imdb_cleaner.py` to clean the raw imdb data. This file takes in the csv generated by the prior script and cleans it using pandas. The output is `data/clean/imdb_clean.csv`
	* Run `python3 code/data_dictionary.py` to generate the data dictionary. This script uses the clean imdb data to produce the data dictionary here: `data/clean/data_dictionary.csv`

3) Instructions to Produce Figures:
	* Run `python3 code/graphs.py` to produce the charts used in the analysis, it will create nine charts showing the relation between or variables of interest.
		*The figures will be created and saved in folder [figures](https://github.com/ElliottMetzler/midterm-project-imdb/tree/main/figures)

4) Instructions to Produce Quantitative Analysis:
	* Run `python3 code/quant_analysis.py` to perform a decade analysis of features and OLS regression of Gross Revenue on IMDB Rating, Metascore, and Release Year. 
	 	* The decade analysis divides data into decades based on Release Year and generates a csv of summary statistics for all features except Release Year for each decade. The output is [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/decade_analysis.csv)
	 	* The OLS regression results are summarized into a csv. The output is [ols_regression.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/ols_regression.csv)
