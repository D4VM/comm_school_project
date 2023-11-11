from fastapi import FastAPI
from tools.db import add_to_db

app = FastAPI(
    title="MyAuto Project API"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/api/product/{full_path:path}')
async def post_to_db(full_path: str):
    url = {'path': full_path}
    add_to_db(url['path'])
    return {"message": "Success"}



# @app.get('/api/product/1')
# async def get_product():
#     return {'message': 'product1'}
#
