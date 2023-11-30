from tools.db import add_one, query_database, founded_car
from tools.scrape import scrape_one, search_scrape
from tools.utils import calculate_average, extract_id


# Workaround with RQ
def scrape_and_add(url: str):
    """
    Scraping one product & adding one to database.
    :param url:
    :return:
    """
    car_dict = scrape_one(url)
    if car_dict is not None:
        add_one(car_dict)
        return True
    return False


def add_one_from_list(url):
    car_list = search_scrape(url)
    for car in car_list:
        add_one(car)


def appraisal(url: str):
    # checks if car is already in database.
    car_id = int(extract_id(url))
    car_found = founded_car(car_id)
    if car_found:
        query = query_database(car_found)
        average_price = calculate_average(query)
        return average_price
    else:
        return 0
