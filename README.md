## comm school project


### [POST] /api/product/<URL>
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

### [GET] /api/product/<URL>
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

### [POST] /api/appraisal_request/
Searches for cars on myauto, adds cars to dict then appends to list.  
Returns a list with dicts with data for searched car, then adds one by one data to database from a returned list. 

Also adds this function as task to Redis RQ  
Request example:
```
/api/appraisal_request/?p=https://www.myauto.ge/ka/pr/98620870/iyideba-manqanebi-hechbeqi-toyota-prius-2010-hibridi-tbilisi?offerType=superVip
```
Note: `?p=` is used here as a post parameter

### [GET] /api/appraisal_request/
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


