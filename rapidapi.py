import requests
from config import API_KEY_rapidapi

url = "https://gas-price.p.rapidapi.com/allUsaPrice"

headers = {
	"X-RapidAPI-Key": API_KEY_rapidapi,
	"X-RapidAPI-Host": "gas-price.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())