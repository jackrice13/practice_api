import requests
import pprint
from data import data

# url= "https://sandbox.zestfuldata.com/parseIngredients"
#
# payload = {}
# headers = {
#     "Content-Type": "application/json"
# }
# data = {
#     "ingredients": ["bacon"]
# }
# response = requests.post(url, json=data, headers=headers)
#
# #print(response.json())


pprint.pprint(data ['results'][0])

print('Hello World')
print(data['results'][0]['ingredientRaw'])
