from fastapi import FastAPI
from tools.db import add_to_db, query_product
from tools.utils import extract_id

app = FastAPI(
    title="MyAuto Project API"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# post api to add myauto.ge URL to database
@app.post('/api/product/{full_path:path}')
async def post_to_db(full_path: str):
    url = {'path': full_path}
    add_to_db(url['path'])
    return {"message": "Success"}


# query's database for specific car ID.
@app.get('/api/product/{full_path:path}')
async def query_db(full_path: str):
    url = {'path': full_path}
    # extracted id must be INT!
    ext_id = int(extract_id(url['path']))
    query = query_product(ext_id)
    return query



