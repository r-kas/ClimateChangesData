#INSTRUCTIONS
#1.0 DOWNLOAD THE LIBRARIES IN COMMAND PROMPT
#1.1 TYPE: pip install pandas
#1.2 TYPE: pip install geopy
#1.3 TYPE: pip install folium

#2.0 DOWNLOAD VSCODE/JUPYTER
#2.1 COPY 
#2.2 PASTE
#2.3 RUN IN VSCODE/JUPYTER
#ENJOY

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#UMA LISTA QUALQUER, PODEM SER OUTROS ENDEREÇOS ESPECÍFICOS 
lista ={"name":["Sergipe", "Tocantins", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão","Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Acre", "Roraima", "Alagoas", "Santa Catarina", "Amapá", "São Paulo", "Amazonas", "Bahia"]};

#TO A SPECIFIC ADDRESS:
#1. from geopy.geocoders import Nominatim#

#2. end = "1.número', 2.rua', 3.cidade";#

#3. geolocator = Nominatim(user_agent="MyGeocoder")#

#4. location = geolocator.geocode(end)#

#5. print(location.address)#

df = pd.DataFrame(lista)

from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="MyGeocoder")

from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="MyGeocoder")

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df["location"] = df["name"].apply(geocode)

df

#CRIANDO UM MAPA

import folium

m = folium.Map(location=[0, 0], zoom_start=11) #INSIRA AS COORDENADAS DESEJADAS ENTRE AS CHAVES

m

