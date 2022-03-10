IMdb Data and Analysis
---
Data Scraping
---
When we decided to make our topic best-selling movies for our project, we turned to the best website for raw movie data: IMdb. Elliot scraped the data from IMdb using "Beautiful Soup" and "requests" as his python packages. Both of these packages allowed for seamless extraction of data from a URL. From the IMdb website we set our schema as title, release year, certificates (rating), run time, genres, IMdb rating, Metascore rating, # of votes for IMdb rating, and gross revenue. We then took a deeper look at genre and noticed that most movies were categorized to more than one genre. We decided to then include any genre listed for a specific movie in our data set. 
