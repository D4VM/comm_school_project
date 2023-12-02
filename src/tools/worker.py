from tools.scrape import search_scrape
from tools.db import add_one, founded_car
from tools.models import Car


def task_add_to_database(car_id: int):
    car_list = search_scrape(car_id)
    for item in car_list:
        item_data = Car(**item)
        if not founded_car(item_data.car_id):
            print(item_data)
            add_one(item_data.__dict__)
        else:
            print('item exist in database')
