import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

# URL de la page contenant les avis
url = 'https://www.healthgrades.com/usearch?what=Cardiology&pt=40.71455%2C%20-74.007118'

# Envoi de la requête HTTP
response = requests.get(url)

response.raise_for_status()  # Vérifie si la requête a réussi


soup = BeautifulSoup(response.text, 'html.parser')

#liste = soup.find('li')



cad = soup.find_all('ul', class_= 'results__results-cards')

pprint (cad)

# # Extraction des informations (à adapter en fonction de la structure HTML)
# doctors = soup.find_all('div', class_='bAl8RXV_meQOV4mT UNhc2s2oeoUQ6YtF Z_rHgSF8ozQMxZC_')  
# data = []

# for doctor in doctors:
#     try:
#         name = doctor.find('a', class_='RML7ZoJM_T0OsSL0').text.strip()
#     except AttributeError:
#         name = None
#     try:
#         specialty = doctor.find('div', class_='ciXWR_F96QIbVTnf').text.strip()
#     except AttributeError:
#         specialty = None
#     try:
#         location = doctor.find('div', class_='efB6RomtY4gvWNmF').text.strip()
#     except AttributeError:
#         location = None
#     try:
#         rating = doctor.find('span', class_='star-rating__score').text.strip()
#     except AttributeError:
#         rating = None
#     # try:
#     #     comments = doctor.find('div', class_='review-count').text.strip()
#     # except AttributeError:
#     #     comments = None

#     data.append([name, specialty, location, rating])

# # Création d'un DataFrame pandas
# df = pd.DataFrame(data, columns=['Name', 'Specialty', 'Location', 'Rating'])

# # Sauvegarde des données dans un fichier CSV
# df.to_csv('healthgrades_reviews.csv', index=False, encoding='utf-8')

