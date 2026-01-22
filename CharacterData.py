import requests
import pprint

def get_char_name(character_id):
    characterID=1303
    url = f"https://www.anapioficeandfire.com/api/characters/{character_id}"


    response = requests.get(url)
    data = response.json()
    charName = (data["name"])
    return charName

#print(type(data))
#print(characterName)
# print(HouseWords)
#pprint.pprint(data)

# with open("HouseData.csv", "w") as f:
#   f.write("House Name,House Words,House Region,House Coat Of Arms\n")
#   f.write(f"{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms}\n")

