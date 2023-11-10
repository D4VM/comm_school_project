import requests
from time import sleep
from random import randrange as rr
import project_utils

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}


def scrape_product(provided_url: str) -> dict:
    """
    Returns JSON data requested from myauto.ge as dict.

    :param provided_url:
    :return:
    """
    base_url = 'https://api2.myauto.ge/ka/products/'
    # checking if user provided url is correct
    if project_utils.validate_url(provided_url):
        sleep(rr(5, 20))  # faking user with sleep & randrange functions
        extracted_id = project_utils.extract_url_id(provided_url)  # extracting id from url
        requested_data = requests.get(f"{base_url}{extracted_id}", headers=headers)
        # checking if status code is ok
        if requested_data.status_code == 200:
            json_data = requested_data.json().get('data')
            return json_data.get('info')


