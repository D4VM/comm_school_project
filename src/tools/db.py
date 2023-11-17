from pymongo.mongo_client import MongoClient

client = MongoClient(host='10.10.1.153', port=27017)
db = client.myauto_database  # database name
cars = db.cars_collection  # collection name


def test_db_connection() -> bool:
    """
    Testing if connection to free tier database is successful.
    :return:
    """
    # Create a new client and connect to the server
    # client = MongoClient(url, server_api=ServerApi('1'))
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
def add_one(data):
    """
    Adding new ONE item to Database if connection is True
    :param data:
    :return:
    """
    if test_db_connection():
        cars.insert_one(data)
        print("---> Added Item to DB")
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
    if test_db_connection():
        try:
            query_db = {"car_id": int(product_id)}
            # {'_id': 0} added because ValueError: [TypeError("'ObjectId' object is not iterable") (stackoverflow)
            products = cars.find(query_db, {'_id': 0})
            if products:
                for product in products:
                    return product
            return {"message": f"{query_db['car_id']} ID not found in database"}

        except Exception as e:
            return f"An error occurred: {e}"
    else:
        print('---> Problem with getting item from database')


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
