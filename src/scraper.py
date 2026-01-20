import requests
from bs4 import BeautifulSoup


url = "https://www.openbrewerydb.org/breweries?query=Montana"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)

site = BeautifulSoup(html, "html.parser")
print (site) 

#brasseries = site.find_all()