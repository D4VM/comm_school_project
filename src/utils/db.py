from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from scrape import scrape_product

# Change password
uri = "mongodb://mongo.d4vm.duckdns.org"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.myauto_database  # database name
cars = db.cars_collection  # collection name


def test_db_connection(uri: str) -> bool:
    """
    Testing if connection to free tier database is successful.
    :return:
    """
    # Create a new client and connect to the server
    # client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        # print("Pinged Successfully. Connected to MongoDB!")
        connection_status = True
    except Exception as e:
        print(e)
        connection_status = False

    return connection_status


# for [POST]/api/product ახალი პროდუქტის დამატება / შექმნა
def add_to_db(url: str):
    """
    Adding new ONE item to Database if connection is True
    :param url:
    :return:
    """
    if test_db_connection(uri):
        cars.insert_one(scrape_product(url))
        print("Added Item to DB")
        return True
    else:
        print('Problems with adding items to database')
        return False


# for [GET]/api/product/<product_id> პროდუქტის დეტალური ინფორმაცია
def get_product():
    pass


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