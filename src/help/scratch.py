import configparser
from pathlib import Path
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

config_path = Path.cwd().parent.parent / "var/config.ini"
config = configparser.ConfigParser()
config.read(config_path)
url = config.get("DB", "DB_url")

client = MongoClient(url, server_api=ServerApi('1'))
db = client['myauto_database']  # database name
cars = db['cars_collection']  # collection name

try:
    print(client.admin.command('ping'))
    query_db = {"car_id": 98420894}

    print(f"Query: {query_db}")
    products = cars.find(query_db, {'_id': 0})
    # products = cars.find({})

    # Iterate over the cursor to print the documents
    for product in products:
        print(product)


except Exception as e:
    print(f"An error occurred: {e}")

