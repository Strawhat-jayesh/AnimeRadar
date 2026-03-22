import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import requests
import json
import time


from config.settings import BASE_URL, START_YEAR, END_YEAR, SEASONS


# Dynamically point to the root data/raw folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")


def fetch_season(year, season):
    """
    Fetch seasonal anime data from Jikan API
    """
    url = f"{BASE_URL}/seasons/{year}/{season}"

    # ask the API: "give me seasonal anime data for this year and season"
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Error fetching {season} {year}: {response.status_code}")
            return None
            
        return response.json()
    except requests.RequestException as e:
        print(f"Network error fetching {season} {year}: {e}")
        return None

# This function will extract only the required fields from the API response
def extract_fields(data, year, season):
    """
    Extract only required fields from API response
    """

    anime_list = []

    for anime in data["data"]:
        anime_info = {
            "title": anime.get("title"),
            "score": anime.get("score"),
            "members": anime.get("members"),
            "favorites": anime.get("favorites"),
            "episodes": anime.get("episodes"),
            "status": anime.get("status"),
            "genres": [g["name"] for g in anime.get("genres", [])],
            "season": season,
            "year": year
        }

        anime_list.append(anime_info)

    return anime_list

# This function will save the raw JSON data to a file
def save_raw_data(data, year, season):
    """
    Save raw JSON data to data/raw folder
    """

    filename = os.path.join(RAW_DATA_PATH, f"{season}_{year}.json")

    # Ensure the directory exists
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4) #This writes the API data into a JSON file inside the data/raw folder

    print(f"Saved data: {filename}")

# This function will collect data for all seasons from START_YEAR to END_YEAR
def collect_all_seasons():
    """
    Collect anime data for multiple years and seasons
    """

    for year in range(START_YEAR, END_YEAR + 1):

        for season in SEASONS:

            print(f"Fetching {season} {year}...")

            data = fetch_season(year, season)

            if data is None:
                continue

            # Extract only the useful fields so we don't store unnecessary API data
            extracted_data = extract_fields(data, year, season)
            save_raw_data(extracted_data, year, season)

            time.sleep(1)  # prevent API rate limit


if __name__ == "__main__":
    collect_all_seasons()