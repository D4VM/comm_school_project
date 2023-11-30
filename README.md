# Setup project on local

```bash
mkdir app
# NOTE: move project to app folder
# NOTE: activate your virtual env
# NOTE: install requirements
pip install -r src/requirements.txt
```

# Run the application

## For Windows

```bash
# NOTE: open terminal and `cd` to `app/src` folder
python flask --app main run 
```

```bash
# NOTE: to debug app run with `--debug` flag
python flask --app main run --debug
```

# Setup services

## For Windows

### Option 1

#### Install OracleVirtualBox

Download Alpine linux , install and run in virtual box.  
Get ip address of VM with `ip addr` command.  
Install docker on alpine.

Comment out in main.py `redis_conn = Redis()`  
Uncomment in main.py `# redis_conn = Redis(host='10.10.1.153')  # Windows Host` and change ip addr with your VM's IP
addr.

Comment out in db.py `client = MongoClient()`  
Uncomment in db.py `# client = MongoClient(host='10.10.1.153', port=27017)  # Windows Host` and change ip addr with your
VM's IP addr.

Run mongo container.

```bash
docker run -d --name mongo --hostname host -p 27017:27017 -v /home/mongodb:/data/db mongo
```

Run redis container.

```bash
docker run -d --name redis --hostname host -p 6379:6379 -v /home/redis:/data redis
```

RQ workers will only run on systems that implement fork(). Most notably,  
this means it is not possible to run the workers on Windows without using  
the Windows Subsystem for Linux and running in a bash shell.

From Windows Store download Alpine.    
After, run install all required dependencies.  
CD to app/src/ folder in WSL and run `rq worker`  
Then run the app.

### Option 2

#### Inside Docker

Create an app image for docker container, and create docker-compose yaml config file.  
Run everything inside docker(app, rq worker, redis, mongo)

## For Linux

### Install Docker

For linux run Redis & Mongo in a container.  
Then run the app from app folder

Run mongo container.

```bash
docker run -d --name mongo --hostname host -p 27017:27017 -v /home/mongodb:/data/db mongo
```

Run redis container.

```bash
docker run -d --name redis --hostname host -p 6379:6379 -v /home/redis:/data redis
```

Run app

```bash
# NOTE: open terminal and `cd` to app/src/ folder
python3 flask --app main run 
```

Run app with debug

```bash
# NOTE: to debug app run with `--debug` flag
python3 flask --app main run --debug
```

# API usage examples

## [POST] /api/product/<URL><MYAUTO.GE_URL>

Scraping one product & adding it to database.
Also adds this function as task to Redis RQ  
Request example:

```
/api/product/https://www.myauto.ge/ka/pr/97264590/iyideba-manqanebi-sedani-audi-s7-2017-benzini-tbilisi?offerType=superVip
```

Database data example:

```json
{
  "_id": {
    "$oid": "6557826019be238645d9a9d1"
  },
  "car_id": 97172766,
  "man_id": 41,
  "model_id": 1124,
  "prod_year": 2010,
  "price_usd": 4500,
  "price_value": 12155,
  "fuel_type_id": 2,
  "gear_type_id": 2
}
```

## [GET] /api/product/<URL><MYAUTO.GE_URL>

Queries database for specific car_id   
Request example:

```
/api/product/https://www.myauto.ge/ka/pr/98620870/iyideba-manqanebi-hechbeqi-toyota-prius-2010-hibridi-tbilisi?offerType=superVip
```

API response:

```json
{
  "data": {
    "car_id": 98620870,
    "fuel_type_id": 6,
    "gear_type_id": 4,
    "man_id": 41,
    "model_id": 1124,
    "price_usd": 6300,
    "price_value": 17016,
    "prod_year": 2010
  }
}
```

## [POST] /api/appraisal_request/<MYAUTO.GE_URL>

Searches for cars on myauto, adds cars to dict then appends to list.  
Returns a list with dicts with data for searched car, then adds one by one data to database from a returned list.

Also adds this function as task to Redis RQ  
Request example:

```
/api/appraisal_request/?p=https://www.myauto.ge/ka/pr/98620870/iyideba-manqanebi-hechbeqi-toyota-prius-2010-hibridi-tbilisi?offerType=superVip
```

Note: `?p=` is used here as a post parameter

## [GET] /api/appraisal_request/<MYAUTO.GE_URL>

Queries mongodb for cars.Returns Average Price(price_usd)  
Request example:

```
/api/appraisal_request/?p=https://www.myauto.ge/ka/pr/98620870/iyideba-manqanebi-hechbeqi-toyota-prius-2010-hibridi-tbilisi?offerType=superVip
```

Note: `?p=` is used here as a post parameter

Query example:

```python
query_fields = {
    'man_id': car_dict['man_id'],
    'model_id': car_dict['model_id'],
    'prod_year': car_dict['prod_year']
}
```

## [PUT] /api/product/<PRODUCT_ID>

Updates Database for specific product ID.

```
/api/appraisal_request/99017431
```

Note: `request body` must be in `json`

Request Body Example in `POSTMAN`:

```JSON
{
  "prod_year": 1800,
  "price_usd": 1000
}
```