#es interesante trabajar en proyecto con entornos virtuales -> env 
import requests
response = requests.get ("https://api.coingecko.com/api/v3/ping")
print (response.json())
