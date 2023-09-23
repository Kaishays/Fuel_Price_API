import requests 

baseurl = 'https://api.tomtom.com/search/2/fuelPrice.json?key={API_KEY}'
endpoint = 'price'

def main_requests(baseurl):
    r = requests.get(baseurl)
    return r.json()

def get_fuel_price(response):
    # Modify this function to correctly extract the fuel price from the API response
    # For example, if the JSON structure is like: {"fuelPrices": [{"price": 2.5}]}
    # You can access the price with: response['fuelPrices'][0]['price']
    return response['fuelPrices'][0]['price']

if __name__ == '__main__':
    response = main_requests(baseurl)
    fuel_price = get_fuel_price(response)
    print("Fuel Price:", fuel_price)