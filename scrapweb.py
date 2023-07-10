import requests
from bs4 import BeautifulSoup

# URL della pagina di Wikipedia di Fabrizio Ravanelli
url = "https://it.wikipedia.org/wiki/Vasco_Rossi"

# Effettua la richiesta GET alla pagina web
response = requests.get(url)

# Parsing dell'HTML della pagina utilizzando BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Trova il div con l'ID "mw-content-text"
content_div = soup.find("div", id="mw-content-text")

# Estrai il testo all'interno del div
content = content_div.get_text()

# Stampa il contenuto del div
print(content)