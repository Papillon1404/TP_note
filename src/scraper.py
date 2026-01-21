import requests
from bs4 import BeautifulSoup
import json

url = "https://api.openbrewerydb.org/v1/breweries/search?query=Montana"
params = {"per_page": 200}

response = requests.get(url, params)

html = json.loads(response.text)

if response.status_code != 200:
    print("Erreur :", response.status_code)


brasseries = [D["name"] for D in html]
villes = [D["city"] for D in html]
types = [D["brewery_type"] for D in html]

print(brasseries)

