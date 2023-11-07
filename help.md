## Key:value Types for parsed JSON Data for specific car(product)

```json
"data": {
  "info": {
    "car_id": 98222242,
    "prod_year": 1993,
    "man_id": 25,
    "price": 0,
    "price_usd": 0,
    "model_id": 569
  }
}
```

## Types of URL in myauto.ge API

#### Specific car URL
```https://api2.myauto.ge/ka/products/98222242```


#### Contains found car numbers. Helpful with car count on page.Returns json with count number.
  ```https://api2.myauto.ge/ka/products/count?TypeID=0&ForRent=0&Mans=25.569&CurrencyID=3&MileageType=1&Page=1&undefined=1```


## Search page for specific model
#### Helpful Parameters 
#### Mans = Manufacture Variable
#### Mans Value Before . (dot) = Manufacturer ID
#### Mans Value After . (dot) = Model ID
#### Page, Indicates on what page are we now. Helpful with car count on page.
```https://api2.myauto.ge/ka/products?TypeID=0&ForRent=0&Mans=25.569&CurrencyID=3&MileageType=1&Page=1```
