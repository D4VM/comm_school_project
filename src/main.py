from flask import Flask, request
from tools.scrape import scrape_and_add
from tools.db import query_product
from tools.utils import extract_id
from redis import Redis
from rq import Queue

# import rq_dashboard

app = Flask(__name__)
# app.config["RQ_DASHBOARD_REDIS_URL"] = 'redis://10.10.1.153:6379'
# app.config.from_object(rq_dashboard.default_settings)
# rq_dashboard.web.setup_rq_connection(app)
# app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

redis_conn = Redis(host='10.10.1.153')
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

    return {'status': 'task being added'}


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
    p = extract_id(request.args.get('p', type=str))

    return {'message': p}


if __name__ == '__main__':
    app.run(debug=True)
