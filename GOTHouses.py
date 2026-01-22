import requests
import pprint
import CharacterData as char

houseID=378
url = f"https://www.anapioficeandfire.com/api/houses/{houseID}"


response = requests.get(url)
data = response.json()
HouseName = (data["name"])
HouseWords = (data["words"])
HouseRegion = (data["region"])
HouseCoatOfArms = (data["coatOfArms"])
HouseLordURL = (data["currentLord"])
HLID = HouseLordURL.split("/")[-1]
HouseLordName = char.get_char_name(HLID)

#print(type(data))
print(HouseName)
print(HouseWords)
print(HLID)
print(HouseLordName)
#pprint.pprint(data)

with open("HouseData.csv", "w") as f:
  f.write("House Name,House Words,House Region,House Coat Of Arms, House Lord Name\n")
  f.write(f"{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms},{HouseLordName}\n")

