import json
from flask import Flask, request, redirect, url_for
from tools.db import update_database, founded_car, add_one, search_database
from tools.worker import task_add_to_database
from tools.models import Car
from redis import Redis
from rq import Queue

app = Flask(__name__)

redis_conn = Redis()
q = Queue(connection=redis_conn)


@app.route('/')
def hello_world():
    return '<p>Hello, World! <b>D4VM!'


@app.post('/api/product/')
def post_to_database():
    """
    Validating Data and Adding to database
    :return:
    """

    try:
        data = Car(**request.json)
        if not founded_car(data.car_id):
            add_one(data.__dict__)
            return {"message": "data added to database"}
        return {"message": "item exist in database"}
    except Exception as e:
        return {"message": e}


@app.get('/api/product/')
def get_from_database():
    """
    Getting data from Database
    """
    try:
        data = Car(**request.json)
        if not founded_car(data.car_id):
            return {"message": "item not found"}
        return {"message": founded_car(data.car_id)}
    except Exception as e:
        return {"message": e}


@app.post('/api/appraisal_request/')
def send_appraisal_request():
    """
    Adding data to Database
    """
    try:
        body = request.json
        data = Car(**body)
        car_id = data.car_id
        q.enqueue(task_add_to_database, car_id)
        return {'task': 'task for appraisal added'}
    except Exception as e:
        return {"message": e}


@app.get('/api/appraisal_request/')
def get_appraisal_request():
    try:
        data = Car(**request.json)
        car_id = data.car_id
        car_data = founded_car(car_id)
        if car_data:
            price_data = search_database(car_data)

            total_products = len(price_data)
            max_price = max(price_data)
            min_price = min(price_data)
            sum_price = sum(price_data)
            avg_price = round(sum_price / total_products)

            return {
                "total_products": total_products,
                "max_price": max_price,
                "min_price": min_price,
                "sum_price": sum_price,
                "avg_price": avg_price
            }
        else:
            return {"message": "item not found"}

    except Exception as e:
        return {"message": e}


@app.put('/api/product/')
def update_db():
    data = Car(**request.json)
    car_id = data.car_id
    if founded_car(car_id):
        update_database(car_id, data.__dict__)
        return {"message": "data updated"}
    else:
        return {"message": "item not found"}


if __name__ == '__main__':
    app.run(debug=True)
