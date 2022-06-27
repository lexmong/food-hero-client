# foodHeroClient


A Food Hero API client in python

## Installation
Install requests
```
pip install requests
```

## Usage
### Register
```
from foodhero import FoodHero
token = FoodHero.register()
```
A file containing the token will be created (fh_token.json)

### Get departments

```
from foodhero import FoodHero
fh = FoodHero(token)
fh.get_product_departments()
```

```
[
  {
    'logoUrl': 'https://s3.amazonaws.com/foodhero-dev/department_meat_poultry.jpg',
    'id': '5b96b5a6c11a3803e4e672fb',
    'name': 'Meat & Poultry'
  },
  ...
]
```

### Get schedule

```
from foodhero import FoodHero
fh = FoodHero(token)
fh.get_schedule()
```
```
{
  'intervals': [
    {'label': 'Morning Release', 'time': 1656424800},
    {'label': 'Afternoon Release', 'time': 1656444600}
  ],
  'nextRelease': 1656424800,
  'nextReleaseRemainingTime': 64153
 }
```

### Get stores
```
from foodhero import FoodHero
fh = FoodHero(token)
fh.get_stores(
    lat = '45.501026591246394',
    lng = '-73.61578431084538',
    limit=3,
    offset=0
)
```
```
[
  {
    'bannerId': '5da5f07833834b03e9cc12e4',
    'chainId': '5da5f011d3bf355deac38597',
    'name': 'Metro Côte-des-Neiges',
    'locationTypeId': '5cd42ac883af3b050deb3a4d',
    'typeId': '5cd42ac883af3b050deb3a4b',
    'activeInStoreNotification': True,
    'timezone': 'America/New_York',
    'productCount': 82,
    'logoUrl': 'https://foodhero-dev.s3.amazonaws.com/stores/JpyqGiAR-_1591383730.png',
    'distance': 748.5702434891007,
    'isFavorite': False,
    'id': '5eda95d4b7d8967a70c4669a',
    'location': {
      'lat': 45.49494109999998, 
      'lng': -73.61986630000001
    },
    'address': {
      'googlePlaceId': 'ChIJ1ckQj_AZyUwR3RudZOx90qg',
      'street': '5150 Chemin de la Côte-des-Neiges',
      'city': 'Montréal',
      'country': 'CA',
      'state': 'QC',
      'postalCode': 'H3T1X8',
      'location': {
        'lat': 45.49494109999998, 
        'lng': -73.61986630000001
      }
    },
    'eatIn': False,
    'pickUp': True,
    'delivery': False,
    'type': {
      'id': '5cd42ac883af3b050deb3a4b',
      'name': 'Grocery store',
      'logoUrl': 'https://s3.amazonaws.com/foodhero-dev/store-type-grocery.png'},
      'locationType': {
        'id': '5cd42ac883af3b050deb3a4d', 
        'name': 'Urban'
      },
    'offerCount': 77,
    'lastCallOfferCount': 0
  },
  ...
]
```

### Get offers

```
from foodhero import FoodHero
fh = FoodHero(token)
fh.get_offers(
    store_id = '5eda95d4b7d8967a70c4669a',
    department_id = '5b96b5a6c11a3803e4e672fb'
)
```

```
{
  'offers': [
    {
      'product': {
        'id': '5da88549ac63f888c1a0de79',
        'uniqueId': '0020311100000',
        'name': 'Boneless Center-Cut Pork Loin Roast',
        'desc': '',
        'brand': '',
        'isByWeight': True,
        'logoUrl': 'https://product-images.metro.ca/images/h35/h61/9279438815262.jpg',
        'departmentId': '5b96b5a6c11a3803e4e672fb',
        'department': {
          'id': '5b96b5a6c11a3803e4e672fb',
          'name': 'Meat & Poultry',
          'logoUrl': 'https://s3.amazonaws.com/foodhero-dev/department_meat_poultry.jpg'
        },
        'size': '1.0 kg',
        'weight': 1242,
        'quantity': {
          'value': 750, 
          'unit': 'g'
        }
      },
      'id': '62b8a372cc0d540b98318f36',
      'isNew': False,
      'price': 17.77,
      'discount': 40,
      'discountPrice': 10.66,
      'itemLeft': 1,
      'bestBefore': None,
      'isFrozen': True,
      'co2Volume': 0.24,
      'size': '1.242kg',
      'releaseStartDate': 1656271800,
      'releaseEndDate': 1656703800,
      'isLastCall': False,
      'storeId': '5eda95d4b7d8967a70c4669a',
      'creationDate': 1656267634.882,
      'savings': 7.109999999999999
    },
    ...
  ],
  'productCount': 64,
  'lastCallOfferCount': 0,
  'id': '5b96b5a6c11a3803e4e672fb',
  'name': 'Meat & Poultry',
  'offerCount': 64
}
```

