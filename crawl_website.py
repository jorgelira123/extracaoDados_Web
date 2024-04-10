import requests
from requests.exceptions import HTTPError

def crawl_website(url, headers: dict) -> str:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except HTTPError as exc:
        print(f'Error HTTP: {exc.response}')
    else:
        return response.text
