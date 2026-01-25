import requests
import pprint

def get_char_name(character_id):
    if not character_id:
        return "No Lord Found"
    url = f"https://www.anapioficeandfire.com/api/characters/{character_id}"

    try:
        response = requests.get(url)
        data = response.json()
        charName = (data["name"])
        return charName
    except Exception as e:
       print(f"Error fetching character {character_id}: {e}")
       return "Error fetching name"

#print(type(data))
#print(characterName)
# print(HouseWords)
#pprint.pprint(data)

# with open("HouseData.csv", "w") as f:
#   f.write("House Name,House Words,House Region,House Coat Of Arms\n")
#   f.write(f"{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms}\n")

