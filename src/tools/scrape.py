import requests
from time import sleep
from random import randrange as rr
from tools.utils import validate_url, extract_id

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}


def scrape_one(provided_url: str) -> dict:
    """
    Scrapes product from myauto.ge
    Inserts to database
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


# https://api2.myauto.ge/ka/products?
# TypeID=0&
# ForRent=0&
# Mans=41.1077&
# ProdYearFrom=2020&
# ProdYearTo=2023&
# CurrencyID=3&
# MileageType=1&
# Page=1

def search_scrape(url: str):
    """
    Returns a list with dicts with data for searched car.
    Must provide url.
    :param url:
    :return:
    """

    def get_search_url(page_num=1) -> str:  # In case we need to cycle through pages...
        """
        Creating a Valid Searchable URL for specific car
        :return:
        """
        car_data = scrape_one(url)
        car_man = car_data['man_id']
        car_mod = car_data['model_id']
        c_Mans = f'{car_man}.{car_mod}'  # Done
        c_ProdYearFrom = car_data['prod_year']
        c_ProdYearTo = car_data['prod_year']
        start_url = 'https://api2.myauto.ge/ka/products?TypeID=0&ForRent=0&'
        end_url = 'CurrencyID=3&MileageType=1&Page='  # page_num instead of 1

        search_url = f'{start_url}Mans={c_Mans}&ProdYearFrom={c_ProdYearFrom}&ProdYearTo={c_ProdYearTo}&{end_url}{page_num}'
        return search_url

    cars_list = []
    searched_cars = requests.get(get_search_url(), headers=headers)
    if searched_cars.status_code == 200:
        json_data = searched_cars.json().get('data').get('items')
        for item in json_data:
            car_dict = {
                'car_id': item['car_id'],
                'man_id': item['man_id'],
                'model_id': item['model_id'],
                'prod_year': item['prod_year'],
                'price_usd': item['price_usd'],
                'price_value': item['price_value'],
                'fuel_type_id': item['fuel_type_id'],
                'gear_type_id': item['gear_type_id']
            }
            cars_list.append(car_dict)
        return cars_list
    else:
        return 'Bad Status Code'
