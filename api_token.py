from dotenv import load_dotenv
from os import getenv
from requests import post
from typing import Any

load_dotenv()

URL = 'https://id.twitch.tv/oauth2/token'
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')


def fetch_api() -> Any:
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    response_data = post(URL, data=data).json()
    
    return response_data


if __name__ == '__main__':
    access_token = fetch_api()['access_token']

    print(access_token)
