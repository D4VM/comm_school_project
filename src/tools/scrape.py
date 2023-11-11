import requests
from time import sleep
from random import randrange as rr
from tools.utils import validate_url, extract_id

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
    if validate_url(provided_url):
        sleep(rr(5, 20))  # faking user with sleep & randrange functions
        extracted_id = extract_id(provided_url)  # extracting id from url
        requested_data = requests.get(f"{base_url}{extracted_id}", headers=headers)
        # checking if status code is ok
        if requested_data.status_code == 200:
            json_data = requested_data.json().get('data').get('info')
            car_dict = {
                'car_id': json_data['car_id'],
                'man_id': json_data['man_id'],
                'model_id': json_data['model_id'],
                'prod_year': json_data['prod_year'],
                'price_usd': json_data['price_usd'],
                'price_value': json_data['price_value'],
                'fuel_type_id': json_data['fuel_type_id'],
                'gear_type_id': json_data['gear_type_id']
            }

            return car_dict



