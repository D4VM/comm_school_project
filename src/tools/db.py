import configparser
from pathlib import Path
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from tools.scrape import scrape_product
from tools.utils import extract_id

config_path = Path.cwd().parent / "var/config.ini"
config = configparser.ConfigParser()
config.read(config_path)
url = config.get("DB", "DB_url")

client = MongoClient(url, server_api=ServerApi('1'))
db = client.myauto_database  # database name
cars = db.cars_collection  # collection name


def test_db_connection() -> bool:
    """
    Testing if connection to free tier database is successful.
    :return:
    """
    # Create a new client and connect to the server
    # client = MongoClient(ur;, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    # reading database url from config.ini

    try:
        client.admin.command('ping')
        # print("Pinged Successfully. Connected to MongoDB!")
        connection_status = True
    except Exception as e:
        print(e)
        connection_status = False

    return connection_status


# for [POST]/api/product ახალი პროდუქტის დამატება / შექმნა
def add_to_db(provided_url: str):
    """
    Adding new ONE item to Database if connection is True
    :param provided_url:
    :return:
    """
    if test_db_connection():
        cars.insert_one(scrape_product(provided_url))
        print("Added Item to DB")
        return True
    else:
        print('Problems with adding items to database')
        return False


# for [GET]/api/product/<product_id> პროდუქტის დეტალური ინფორმაცია
def query_product(product_id: int):
    """
    query database for specific car_id
    :param product_id:
    :return:
    """
    try:
        print(client.admin.command('ping'))
        query_db = {"car_id": int(product_id)}
        print(f"Query: {query_db}")
        # {'_id': 0} added because ValueError: [TypeError("'ObjectId' object is not iterable") (stackoverflow)

        products = cars.find(query_db, {'_id': 0})
        if products:
            for product in products:
                return product
        return {"message": f"{query_db['car_id']} ID not found in database"}

    except Exception as e:
        return f"An error occurred: {e}"


# for [PUT]/api/product/<product_id> პროდუქტის ცვლილება
def update_product():
    pass


# for [POST]/api/appraisal_request შეფასების მოთხოვნის შექმნა
# მოთხოვნის გამგზავნი დამატებით აგზავნის შემდეგ ინფორმაციას:
# პროდუქტის ბმული - რომლის გაანალიზებაც არის საჭირო
def appraisal_request():
    pass


# for [GET]/api/appraisal_request/<appraisal_request_id> შეფასების მოთხოვნის დეტალური ინფორმაცია
# ???
def appraisal_request_return():
    pass


debug = True
