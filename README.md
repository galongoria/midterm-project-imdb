# midterm-project-imbd

Team Good-2-Great Midterm Project for Python, Data, and Databases

Team Members: 
* [Elliott Metzler](https://github.com/ElliottMetzler) - Data Scraping and Cleaning, Git/Project Management
* [Pedro Rodrigues](https://github.com/PedroNBRodrigues) - Figure Production
* [Colin McNally](https://github.com/cmcnally23) - Project Management, Report Writing
* [Austin Longoria](https://github.com/galongoria) - Data Cleaning, Report Writing, Presentation
* [Arpan Chatterji](https://github.com/achatterji1) - Quantitative Analysis
* [Kashaf Oneeb](https://github.com/koneeb) - Quantitative Analysis, Data Dictionary, Report Writing

Due: 3/22/2022 

## Introduction

Need to include here a quick summary of:
* Goal of analysis
* Methodology
* Findings

## Data

The features used in our analysis are summarized in the [Data Dictionary](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/data/clean/data_dictionary.csv), which includes the feature name, definition, type, and example values.

### Scraping



We note that one of the important limitations of our analysis is with our methodology for scraping the raw data from imdb's site. We only scraped movies for which we were able to retrieve all data fields desired from the analysis. Thus, in instances where movies were missing a data field, we excluded these from the scraping process. A potential extension of our analysis would be to attempt to scrape these movies and interpolate or estimate missing values where possible, though this process would take more time and consideration than available to us for this project.

### Cleaning



## Exploratory Data Analysis

## Modeling Analysis

## Conclusions

Need to include here a summary of:
* Goal of analysis and conclusions
* limitations of the project
* Areas where we would have improved or expanded the project if we had more time

## Instructions to Reproduce Analysis:

1) Set-up Instructions:
	* Run `pip install -r requirements.txt`

2) Data Scrape and Clean Instructions:
	* Run `python3 code/imdb_scraper.py` to scrape the data from the imdb website. This script will navigate to the imdb pages and scrape the data, generating a csv file of raw data in the raw data folder. The output is `data/raw/imdb_scraped.csv`
	* Run `python3 code/imdb_cleaner.py` to clean the raw imdb data. This file takes in the csv generated by the prior script and cleans it using pandas. The output is `data/clean/imdb_clean.csv`
	* Run `python3 code/data_dictionary.py` to generate the data dictionary. This script uses the clean imdb data to produce the data dictionary here: `data/clean/data_dictionary.csv`

3) Instructions to Produce Figures:
	* [[TO BE CONTINUED]]

4) Instructions to Produce Quantitative Analysis:
	* Run `python3 code/quant_analysis.py` to perform a decade analysis of features and OLS regression of Gross Revenue on IMDB Rating, Metascore, and Release Year. 
	 	* The decade analysis divides data into decades based on Release Year and generates a csv of summary statistics for all features except Release Year for each decade. The output is [decade_analysis.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/decade_analysis.csv)
	 	* The OLS regression results are summarized into a csv. The output is [ols_regression.csv](https://github.com/ElliottMetzler/midterm-project-imdb/blob/document/quantitative%20analysis/ols_regression.csv)
