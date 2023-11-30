from flask import Flask, request, jsonify
from tools.op import scrape_and_add, add_one_from_list, appraisal
from tools.db import query_product, update_database, founded_car
from tools.utils import extract_id
from redis import Redis
from rq import Queue

app = Flask(__name__)

redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route('/')
def hello_world():
    return '<p>Hello, World! <b>David!'


@app.post('/api/product/<path:url>/')
def insert_to_database(url: str):
    """
    Adding task for scrape data and insert to database
    :param url:
    :return:
    """

    q.enqueue(scrape_and_add, url)

    return {'task': 'task being added'}


@app.get('/api/product/<path:url>/')
def query_database(url: str):
    """
    Query database for specific car_id.
    extract_id func extracts car id from provided url.
    :param url:
    :return:
    """
    product_id = int(extract_id(url))  # converting to int, extracting id from myauto URL
    found_product = query_product(product_id)
    return {'data': found_product}


# [POST]/api/appraisal_request
@app.post('/api/appraisal_request/')
def send_appraisal_request():
    """
    Send request to query myauto for specific car ( man_id, model_id, prod_year).
    Founded cars then are added to mongodb.
    :return:
    """
    p = request.args.get('p', type=str)
    q.enqueue(add_one_from_list, p)
    return {'task': 'task for appraisal added'}


@app.get('/api/appraisal_request/')
def get_appraisal():
    p = request.args.get('p', type=str)
    price_average = round(appraisal(p))
    if price_average != 0:
        return {'average_price': f'{price_average}'}
    else:
        return {'message': 'you must first add car to database via POST request'}


# [PUT]/api/product/<product_id> პროდუქტის ცვლილება
@app.put('/api/product/<int:car_id>')
def update_db(car_id):
    update_data = request.get_json()
    if founded_car(car_id):
        update_database(car_id, update_data)
        return {"message": "data updated"}
    else:
        return {"message": "car not found, add first"}


if __name__ == '__main__':
    app.run(debug=True)
