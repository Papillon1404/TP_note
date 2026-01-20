import requests

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)