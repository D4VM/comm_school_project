from pymongo.mongo_client import MongoClient

# client = MongoClient(host='10.10.1.153', port=27017)  # Windows Host
client = MongoClient()
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


def query_database(car_dict: dict):
    query_fields = {
        'man_id': car_dict['man_id'],
        'model_id': car_dict['model_id'],
        'prod_year': car_dict['prod_year']
    }
    result = cars.find(query_fields)
    car_price = []
    for item in result:
        car_price.append(item['price_usd'])

    return car_price


def query_id(car_id: int) -> bool:
    query_field = {'car_id': car_id}
    result = cars.find_one(query_field)
    if result:
        return True
    else:
        return False


def founded_car(car_id: int):
    if query_id(car_id):
        query_field = {'car_id': car_id}
        result = cars.find_one(query_field, {'_id': 0})
        return result
    else:
        return False


def update_database(car_id: int, data: dict):
    db_filter = {'car_id': car_id}
    db_new_values = {"$set": data}
    cars.update_one(db_filter, db_new_values)
