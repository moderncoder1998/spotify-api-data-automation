import requests
import base64
import logging
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data_api(execution_results):
    execution_results.append("Starting Spotify Authentication")
    logging.info("Spotify Authentication Started")
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    if not client_id or not client_secret:
        error_msg=("CLIENT_ID or CLIENT_SECRET not found in .env")
        logging.info (error_msg)
        execution_results.append(error_msg)
        raise Exception (error_msg)
    credentials = f"{client_id}:{client_secret}"
    encoded = base64.b64encode(credentials.encode()).decode()
    logging.info("Encoding credentials")
    headers = {
        "Authorization": f"Basic {encoded}"
    }

    data = {
        "grant_type": "client_credentials"
    }
    url="https://accounts.spotify.com/api/token"
    logging.info(f"POST {url}")
    response = requests.post(url, headers=headers, data=data)
    logging.info(f"status_code {response.status_code}")
    if response.status_code != 200:
        error_msg = "Failed to generate access token"
        logging.info(error_msg)
        raise Exception(error_msg)
    token = response.json()["access_token"]
    logging.info("Token generated")
    execution_results.append("Access token generated successfully")
    return token
