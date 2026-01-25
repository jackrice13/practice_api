import requests
import CharacterData as char
import os

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

#creates new CSV
file_exists = os.path.exists("HouseData.csv")
print("with open")
with open("HouseData.csv","a",encoding="utf-8",newline="") as f:
  print("if not")
  if not file_exists:
    #writes headers if there is no file
    print("→ Writing header")
    f.write("House Name,House Words,House Region,House Coat Of Arms, House Lord Name\n")
    print("→ Writing header")
    #Writes new line each run
  print("→ Writing data row")
  f.write(f'{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms},{HouseLordName}\n')
  print("Write block finished")

# with open("HouseData.csv", "w") as f:
#   f.write("House Name,House Words,House Region,House Coat Of Arms, House Lord Name\n")
#   f.write(f"{HouseName},{HouseWords},{HouseRegion},{HouseCoatOfArms},{HouseLordName}\n")

