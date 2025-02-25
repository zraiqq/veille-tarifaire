import requests
from bs4 import BeautifulSoup

def get_price_from_agrizone(ref):
    url = f"https://www.agrizone.net/search?q={ref}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price = soup.select_one(".price")  # À adapter selon la structure réelle du site
    return price.text.strip() if price else "Prix non trouvé"

def get_price_from_prodealcenter(ref):
    url = f"https://www.prodealcenter.fr/catalogsearch/result/?q={ref}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price = soup.select_one(".price")  # À adapter selon la structure réelle du site
    return price.text.strip() if price else "Prix non trouvé"

def get_price_from_agrifournitures(ref):
    url = f"https://www.agrifournitures.fr/catalogsearch/result/?q={ref}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price = soup.select_one(".price")  # À adapter selon la structure réelle du site
    return price.text.strip() if price else "Prix non trouvé"

def get_prices(references):
    results = []
    for ref in references:
        agrizone_price = get_price_from_agrizone(ref)
        prodeal_price = get_price_from_prodealcenter(ref)
        agrifournitures_price = get_price_from_agrifournitures(ref)
        results.append([ref, agrizone_price, prodeal_price, agrifournitures_price])
    
    return results
