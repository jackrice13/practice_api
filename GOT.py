import requests
import pprint

url = ("https://www.anapioficeandfire.com/api/houses")

params = {
  "page": 1,
  "pageSize": 10
}

response = requests.get(url)

pprint.pprint(response.json())

