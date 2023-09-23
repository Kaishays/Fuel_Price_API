import requests 

import os
from config import API_KEY

baseurl = 'https://api.tomtom.com/search/2/fuelPrice.json?' + API_KEY + '&fuelPrice=1:2622f89a-6300-11ec-8d12-a0423f39b5a2'
endpoint = 'price'
data = {
    'baseurl': 'api.tomtom.com', 
    'versionNumber': '2',
    'ext': 'json',
    'key': API_KEY,
    'fuelPrice': '1:2622f89a-6300-11ec-8d12-a0423f39b5a2',
}

response = requests.get(baseurl, params=data,)
print(response)

