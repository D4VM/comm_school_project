#### Specific car URL

```https://api2.myauto.ge/ka/products/98222242```

```json
{
  "data": {
    "info": {
      "car_id": 98316902,
      "prod_year": 2015,
      "man_id": 42,
      "price_usd": 12800,
      "price_value": 34560,
      "fuel_type_id": 2,
      "gear_type_id": 3,
      "model_id": 1592
    }
  }
}
```

#### Contains found car numbers. Helpful with car count on page.Returns json with count number.
მაქსიმალური მანქანების რაოდენობა რის 30

```https://api2.myauto.ge/ka/products/count?TypeID=0&ForRent=0&Mans=25.569&CurrencyID=3&MileageType=1&Page=1&undefined=1```

#### Search page for specific model

```https://api2.myauto.ge/ka/products?TypeID=0&ForRent=0&Mans=25.569&CurrencyID=3&MileageType=1&Page=1```

```python
TypeID = 0  # 0 - მანქანები, 1 - წპეცტექნიკა, 2 - მოტო
ForRent = 0  # 0 - იყიდება, 1 - ქირავდება
Mans = 25.569  # 25 - მწარმოებელი, 569 მოდელი, ამ ფორმატაში არის გაერთიანებული
CurrencyID = 1  # 1 - USD, 3 - GEL
MileageType = 1  # ????
Customs = 1  # 0 - განუბაჟებული, 1 - განბაჟებული
Page = 1  # 1 - გვერდის ნომერი
```

```
        vehicleType: 'TypeID',
        bargainType: 'ForRent',
        period: 'Period',
        wheelType: 'WheelTypes',
        doorType: 'DoorTypes',
        currId: 'CurrencyID',
        mileageType: 'MileageType',
        cards: 'Cards',
        mansNModels: 'Mans',
        vehicleCats: 'Cats',
        gearTypes: 'GearTypes',
        fuelTypes: 'FuelTypes',
        locations: 'Locs',
        driveTypes: 'DriveTypes',
        vehicleColors: 'Colors',
        motorcycleColors: 'Colors',
        saloonColors: 'SaloonColors',
        saloonMaterials: 'SaloonMaterialID',
        stickers: 'StickerTypes',
        sellerTypes: 'UserTypes',
        yearFrom: 'ProdYearFrom',
        yearTo: 'ProdYearTo',
        priceFrom: 'PriceFrom',
        priceTo: 'PriceTo',
        engineFrom: 'EngineVolumeFrom',
        engineTo: 'EngineVolumeTo',
        mileageFrom: 'MileageFrom',
        mileageTo: 'MileageTo',
        customs: 'Customs',
        techInspect: 'TechInspection',
        hasCatalyst: 'HasCatalyst',
        swap: 'Changable',
        auction: 'Auction',
        vinCode: 'Vin',
        video: 'WithVideo',
        conditioner: 'Features',
        climateControl: 'ClimateType',
        wheels: 'Disks',
        electricWindows: 'ElWindows',
        hideDealPrice: 'HideDealPrice',
        rearViewCamera: 'BackCamera',
        onBoardComputer: 'BoardComp',
        armchairsHeating: 'ChairWarming',
        hydraulics: 'Hydraulics',
        turbo: 'HasTurbo',
        navigation: 'NavSystem',
        parkingControl: 'ObstacleIndicator',
        ssmpAdapted: 'SpecialPersons',
        elStarter: 'ElStarter',
        startStop: 'StartStop',
        trunk: 'Trunk',
        windShield: 'WindShield',
        hatch: 'Hatch',
        cruiseControl: 'CruiseControl',
        multiWheel: 'MultiWheel',
        alarm: 'Alarm',
        abs: 'abs',
        sort: 'SortOrder',
        page: 'Page',
        query: 'Keyword',
        userId: 'UserID',
        rentDaily: 'RentDaily',
        rentDriver: 'RentDriver',
        rentPurchase: 'RentPurchase',
        rentInsured: 'RentInsured',
        popularMans: 'PopularMans',
        hasStickers: 'HasStickers',
        vipTypeId: 'VipTypeId'
```