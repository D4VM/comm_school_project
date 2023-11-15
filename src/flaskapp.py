from flask import Flask
from tools.scrape import scrape_product
from tools.db import insert_to_db, query_product
from tools.utils import extract_id
from redis import Redis
from rq import Queue
from time import sleep
import rq_dashboard

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
rq_dashboard.web.setup_rq_connection(app)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

# Explicitly provide Redis configuration
redis_conn = Redis()
q = Queue(connection=redis_conn)




@app.route('/')
def hello_world():
    return '<p>Hello, World! <b>David!'


@app.post('/api/product/<path:url>/')
def insert_to_database(url: str):
    job_scrape = q.enqueue(scrape_product, url)
    while not job_scrape.is_finished:
        sleep(1)
    car_data = job_scrape.return_value()

    job_database_insert = q.enqueue(insert_to_db, car_data)
    while not job_database_insert.is_finished:
        sleep(1)
    returned_status = job_database_insert.return_value()
    return {'status': returned_status}


@app.get('/api/product/<path:url>')
def query_database(url: str):
    product_id = int(extract_id(url))  # converting to int, extracting id from myauto URL
    found_product = query_product(product_id)
    return {'status': 'ok', 'data': found_product}


if __name__ == '__main__':
    app.run(debug=True)