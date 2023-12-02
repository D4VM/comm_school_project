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
---

## For Windows

---

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

---

### Option 2

#### Inside Docker

Create an app image for docker container, and create docker-compose yaml config file.  
Run everything inside docker(app, rq worker, redis, mongo)
---

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

Run worker from src folder

```bash
rq worker
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

---

# API usage examples

## API endpoints

---

### [POST]  `/api/product/`

**Data must be posted in request body as `raw` `JSON`**  
Example:

```json
{
  "car_id": 1,
  "man_id": 2,
  "model_id": 3,
  "prod_year": 2003,
  "price_usd": 3000,
  "price_value": 9000,
  "fuel_type_id": 1,
  "gear_type_id": 2
}
```

Output:

```JSON
1. {
  "message": "data added to database"
}



2. {
  "message": "item exist in database"
}



3. {
  "message": e
}
```

---

### [GET] `/api/product/`

**Data must be posted in request body as `raw` `JSON`**  
Example:

```JSON
{
  "car_id": 1
}
```

Output:

```json
{
  "car_id": 1,
  "man_id": 2,
  "model_id": 3,
  "prod_year": 2003,
  "price_usd": 3000,
  "price_value": 9000,
  "fuel_type_id": 1,
  "gear_type_id": 2
}
```

---

### [POST] `/api/appraisal_request/`

**Data must be posted in request body as `raw` `JSON`**  
Example:

```JSON
{
  "car_id": 1
}
```

Output:

```JSON
{
  "task": "task for appraisal added"
}
```

---

### [GET] `/api/appraisal_request/`

**Data must be posted in request body as `raw` `JSON`**  
Example:

```JSON
{
  "car_id": 99062659
}
```

Output:

```JSON
{
  "avg_price": 5074,
  "max_price": 6200,
  "min_price": 1850.07,
  "sum_price": 142080.07,
  "total_products": 28
}
```

---

### [PUT] `/api/product/`

**Data must be posted in request body as `raw` `JSON`**  
Example: `car_id` must be valid.  
Data: `price_usd`,`price_value` is `int` or `float`.  
Rest of the data must be `int`

```JSON
{
  "car_id": 99062659,
  "man_id": 222222,
  "model_id": 2222222,
  "prod_year": 2003222,
  "price_usd": 3000222,
  "price_value": 9000222,
  "fuel_type_id": 1222,
  "gear_type_id": 22222
}
```

Output:

```JSON
1. {
  "message": "data updated"
}



2. {
  "message": "item not found"
}
```
