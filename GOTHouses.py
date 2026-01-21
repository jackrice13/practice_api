import requests
import pprint

houseID=378
url = f"https://www.anapioficeandfire.com/api/houses/{houseID}"


response = requests.get(url)
data = response.json()
HouseName = (data["name"])
HouseWords = (data["words"])
HouseRegion = (data["region"])
HouseCoatOfArms = (data["coatOfArms"])

#print(type(data))
print(HouseName)
print(HouseWords)
#pprint.pprint(data)

with open("HouseData.csv", "w") as f:
  f.write("House Name,House Words,House Region,House Coat Of Arms\n")
  f.write(f"{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms}\n")

