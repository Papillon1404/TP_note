import requests
from bs4 import BeautifulSoup
import json
import sqlite3
from database import DatabaseManager

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
db = DatabaseManager("database.db")

url = "https://api.openbrewerydb.org/v1/breweries/search?query=Montana"
params = {"per_page": 200} # on fait en sorte d'avoir tous les résultats (sinon on ne récupère pas toutes les brasseries)

response = requests.get(url, params)

html = json.loads(response.text)

if response.status_code != 200:
    print("Erreur :", response.status_code)



noms = [D["name"] for D in html]
villes = [D["city"] for D in html]
types = [D["brewery_type"] for D in html]

db.creer_table(['Nom de la brasserie', 'Ville', 'Type'])

for i in range(len(noms)) :
    nom = noms[i]
    ville = villes[i]
    type = types[i]
    db.inserer_ligne(nom, ville, type)

