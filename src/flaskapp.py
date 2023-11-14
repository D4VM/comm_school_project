from flask import Flask
from tools.scrape import scrape_product
from tools.db import insert_to_db, query_product
from tools.utils import extract_id

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, World! <b>David!'


@app.post('/api/product/<path:url>/')
def insert_to_database(url: str):
    car_dict: dict = scrape_product(url)
    print(car_dict)
    db_status = insert_to_db(car_dict)
    return {'status': db_status, 'data': car_dict}  # car_dictT ypeError: Object of type ObjectId is not JSON serializable



@app.get('/api/product/<path:url>')
def query_database(url: str):
    product_id = int(extract_id(url))  # converting to int, extracting id from myauto URL
    found_product = query_product(product_id)
    return {'status': 'ok', 'data': found_product}
