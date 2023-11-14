from flask import Flask
from tools.scrape import scrape_product

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, World!'


@app.post('/api/product/<path:url>')
def insert_to_database(url: str):
    return {'status': 'ok', 'data': scrape_product(url)}

