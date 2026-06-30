import requests
import logging


def search_artist(token, execution_results,artist_name,limit,offset):
    execution_results.append(f"Searching artist : {artist_name}")
    logging.info(f"Artist Searching Started")
    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = "https://api.spotify.com/v1/search"

    params = {
        "q": artist_name,
        "type": "artist",
        "limit": limit,
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    # print(response.json())
    # print(response.text)
    logging.info("Artist data retrieved successfully.")
    if response.status_code != 200:
        error_msg = "Search failed and Failed to retrieve artist data from Spotify"
        logging.info(error_msg)
        raise Exception(error_msg)
    return response.json()
