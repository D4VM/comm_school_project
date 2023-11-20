from tools.db import add_one, query_database
from tools.scrape import scrape_one, search_scrape
from tools.utils import calculate_average


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
    """
    Adds one by one cars to database from search URL
    :param url:
    :return:
    """
    car_list = search_scrape(url)
    for car in car_list:
        add_one(car)


def appraisal(url: str):
    """
    Queries Database for specific year and model, calculates averages price
    :param url:
    :return:
    """
    data = scrape_one(url)
    query = query_database(data)
    average_price = calculate_average(query)
    return average_price
