import os
print("PID du script :", os.getpid())
print("Dossier courant :", os.getcwd())
print("Fichiers présents :", os.listdir("."))
import sys
print("Python version:", sys.version)
print("Script en cours d'exécution...")
sys.stdout.flush()  # Force l'affichage immédiat

import time
for i in range(5):
    print(f"Étape {i+1}...")
    sys.stdout.flush()
    time.sleep(1)

print("Fin du script.")
import requests
from bs4 import BeautifulSoup
from rapidfuzz import process, fuzz

def get_products_from_agrizone():
    url = "https://www.agrizone.net/pieces-d-usure/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    products = []
    for item in soup.select(".product-item"):  # Ajuste selon le site
        name = item.select_one(".product-title").text.strip()
        price = item.select_one(".price").text.strip()
        link = item.select_one("a")['href']
        products.append({"name": name, "price": price, "link": link})
    return products

def search_best_match(products, query):
    names = [p["name"] for p in products]
    best_match = process.extractOne(query, names, scorer=fuzz.token_sort_ratio)
    if best_match:
        match_name = best_match[0]
        for product in products:
            if product["name"] == match_name:
                return product
    return None

def get_price_comparison(query):
    agrizone_products = get_products_from_agrizone()
    best_match = search_best_match(agrizone_products, query)
    if best_match:
        return best_match
    return {"error": "Produit non trouvé"}

if __name__ == "__main__":
    query = input("Entrez un mot-clé produit : ")
    result = get_price_comparison(query)
    print(result)
