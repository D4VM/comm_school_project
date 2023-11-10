from fastapi import FastAPI, Request
from project_scraper import scrape_product
from project_database import add_to_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/api/product/{full_path:path}')
async def scrape_data(full_path: str):
    url = {'path': full_path}
    return scrape_product(url['path'])


@app.post('/api/product/{full_path:path}')
async def insert_into_db(full_path: str):
    url = {'path': full_path}
    return add_to_db(url['path'])
