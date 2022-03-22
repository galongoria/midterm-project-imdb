from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Constants
BASE_URL = (
    "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres="
)
APP = "&sort=boxoffice_gross_us,desc"
APP2 = "&start="
APP3 = "&ref_=adv_nxt"
START_NUMS = [
    "51",
    "101",
    "151",
    "201",
]
OUT_DIR = os.path.join("data", "raw")
OUT_FILE = "imdb_scraped.csv"
OUT_PATH = os.path.join(OUT_DIR, OUT_FILE)

genres = [
    "comedy",
    "family",
    "talk-show",
    "romance",
    "fantasy",
    "action",
    "game-show",
    "musical",
    "horror",
    "documentary",
    "history",
    "western",
    "film-noir",
    "drama",
    "short",
    "animation",
    "adventure",
    "music",
    "sci-fi",
    "crime",
    "news",
    "mystery",
    "thriller",
    "sport",
    "biography",
    "war",
]

# Functions
def scrape_page(this_url: str):
    """Function accepts a url as a string and returns a pandas DataFrame containing one page of movie data"""

    r = requests.get(this_url).content
    s = BeautifulSoup(r, "html.parser")

    content_boxes = s.find_all("div", {"class": "lister-item-content"})

    titles_list = []
    years_list = []
    certificates_list = []
    runtimes_list = []
    genres_list = []
    desc_list = []
    imdb_ratings_list = []
    metascores_list = []
    votes_list = []
    gross_list = []

    for b in content_boxes:
        title = b.find("a").text
        year = b.find("span", {"class": "lister-item-year text-muted unbold"}).text
        certificate = b.find("span", {"class": "certificate"}).text
        runtime = b.find("span", {"class": "runtime"}).text
        genre = b.find("span", {"class": "genre"}).text
        desc = b.find_all("p", {"class": "text-muted"})[1].text
        imdb_rating = b.find("div", {"class": "inline-block ratings-imdb-rating"}).text
        metascore = b.find("div", {"class": "inline-block ratings-metascore"}).text
        votes = b.find_all("span", {"name": "nv"})[0].text
        gross = b.find_all("span", {"name": "nv"})[1].text

        titles_list.append(title)
        years_list.append(year)
        certificates_list.append(certificate)
        runtimes_list.append(runtime)
        genres_list.append(genre)
        desc_list.append(desc)
        imdb_ratings_list.append(imdb_rating)
        metascores_list.append(metascore)
        votes_list.append(votes)
        gross_list.append(gross)

    data = pd.DataFrame(
        {
            "Title": titles_list,
            "ReleaseYear": years_list,
            "Certificate": certificates_list,
            "Runtime": runtimes_list,
            "Genres": genres_list,
            "Description": desc_list,
            "IMDBRating": imdb_ratings_list,
            "Metascore": metascores_list,
            "Votes": votes_list,
            "GrossRevenue": gross_list,
        }
    )

    return data


def scrape_genre(this_genre):
    """Function accepts a genre from the Genres list and scrapes the top 250 grossing by US box office"""
    frames = []
    for page in range(5):
        # Generate URL to follow
        if page == 0:
            url = BASE_URL + this_genre + APP
        else:
            url = BASE_URL + this_genre + APP + APP2 + START_NUMS[page - 1] + APP3
        # Scrape that page and append - if it cannot scrape the page, skip
        try:
            page_data = scrape_page(url)
            frames.append(page_data)
        except:
            pass
    # Compile

    full = pd.concat(frames)
    full = full.assign(genre_pull=this_genre)
    return full


def scrape_across_genres(list_of_genres):
    """Function accepts a list of genres and scrapes the top 250 grossing by US box office for each"""
    frames = []
    for genre in list_of_genres:
        try:
            df = scrape_genre(genre)
            frames.append(df)
        except:
            pass

    return pd.concat(frames)


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    full_pull = scrape_across_genres(genres)
    full_pull.to_csv(OUT_PATH, index=False)
